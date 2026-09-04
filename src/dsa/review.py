import json
from dataclasses import dataclass
from datetime import date, timedelta

from dsa.paths import ATTEMPTS

INITIAL_EASE = 2.3
MIN_EASE = 1.3
MAX_EASE = 2.8

EASE_DELTA = {0: -0.20, 1: -0.15, 2: 0.0, 3: 0.10}

FIRST_INTERVAL = 1
SECOND_INTERVAL = 3

LEECH_THRESHOLD = 3


@dataclass(frozen=True)
class Attempt:
    id: str
    date: date
    grade: int
    minutes: int | None
    hint: bool
    note: str


def _parse(line: str) -> Attempt:
    data = json.loads(line)

    return Attempt(
        id=data["id"],
        date=date.fromisoformat(data["date"]),
        grade=int(data["grade"]),
        minutes=data.get("minutes"),
        hint=bool(data.get("hint", False)),
        note=str(data.get("note") or ""),
    )


def load_attempts() -> list[Attempt]:
    if not ATTEMPTS.exists():
        return []

    attempts = [
        _parse(line) for line in ATTEMPTS.read_text().splitlines() if line.strip()
    ]

    return sorted(attempts, key=lambda attempt: attempt.date)


def append_attempt(attempt: Attempt) -> None:
    record = {
        "id": attempt.id,
        "date": attempt.date.isoformat(),
        "grade": attempt.grade,
        "minutes": attempt.minutes,
        "hint": attempt.hint,
        "note": attempt.note,
    }

    ATTEMPTS.parent.mkdir(parents=True, exist_ok=True)

    with ATTEMPTS.open("a", encoding="utf-8") as log:
        log.write(json.dumps(record) + "\n")


@dataclass(frozen=True)
class State:
    id: str
    attempts: int
    reps: int
    ease: float
    interval: int
    last: date
    due: date
    lapses: int

    @property
    def is_leech(self) -> bool:
        return self.lapses >= LEECH_THRESHOLD


def _clamp_ease(ease: float) -> float:
    return max(MIN_EASE, min(MAX_EASE, ease))


def _advance(previous: State | None, attempt: Attempt) -> State:
    reps = previous.reps if previous else 0
    interval = previous.interval if previous else 0
    lapses = previous.lapses if previous else 0
    attempts = previous.attempts if previous else 0
    ease = _clamp_ease(
        (previous.ease if previous else INITIAL_EASE) + EASE_DELTA[attempt.grade]
    )

    if attempt.grade == 0:
        reps = 0
        interval = FIRST_INTERVAL
        lapses += 1
    else:
        reps += 1

        if reps == 1:
            interval = FIRST_INTERVAL
        elif reps == 2:
            interval = SECOND_INTERVAL
        else:
            interval = round(interval * ease)

    return State(
        id=attempt.id,
        attempts=attempts + 1,
        reps=reps,
        ease=ease,
        interval=interval,
        last=attempt.date,
        due=attempt.date + timedelta(days=interval),
        lapses=lapses,
    )


def schedule(attempts: list[Attempt]) -> dict[str, State]:
    states: dict[str, State] = {}

    for attempt in sorted(attempts, key=lambda attempt: attempt.date):
        states[attempt.id] = _advance(states.get(attempt.id), attempt)

    return states
