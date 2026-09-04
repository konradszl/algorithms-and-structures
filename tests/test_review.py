from datetime import date

import pytest

from dsa.review import MIN_EASE, Attempt, schedule


def attempt(id: str, day: int, grade: int) -> Attempt:
    return Attempt(
        id=id,
        date=date(2026, 1, day),
        grade=grade,
        minutes=None,
        hint=False,
        note="",
    )


def test_empty_log_has_no_states() -> None:
    assert schedule([]) == {}


def test_first_attempt_starts_the_ladder() -> None:
    states = schedule([attempt("two-sum", 1, 2)])

    state = states["two-sum"]

    assert state.reps == 1
    assert state.interval == 1
    assert state.due == date(2026, 1, 2)


def test_ladder_grows_with_the_ease_factor() -> None:
    states = schedule(
        [
            attempt("two-sum", 1, 2),
            attempt("two-sum", 2, 2),
            attempt("two-sum", 3, 2),
            attempt("two-sum", 4, 2),
        ]
    )

    state = states["two-sum"]

    assert state.reps == 4
    assert state.interval == 16
    assert state.due == date(2026, 1, 20)


def test_lapse_resets_the_ladder() -> None:
    states = schedule(
        [
            attempt("two-sum", 1, 2),
            attempt("two-sum", 2, 2),
            attempt("two-sum", 3, 2),
            attempt("two-sum", 4, 0),
        ]
    )

    state = states["two-sum"]

    assert state.reps == 0
    assert state.interval == 1
    assert state.lapses == 1
    assert state.due == date(2026, 1, 5)


def test_repeated_failure_marks_a_leech() -> None:
    states = schedule(
        [
            attempt("two-sum", 1, 0),
            attempt("two-sum", 2, 0),
            attempt("two-sum", 3, 0),
            attempt("baseball-game", 1, 0),
            attempt("baseball-game", 2, 0),
        ]
    )

    state_sum = states["two-sum"]
    state_baseball = states["baseball-game"]

    assert state_sum.is_leech
    assert not state_baseball.is_leech


def test_ease_never_drops_below_the_floor() -> None:
    states = schedule(
        [
            attempt("two-sum", 1, 0),
            attempt("two-sum", 2, 0),
            attempt("two-sum", 3, 0),
            attempt("two-sum", 4, 0),
            attempt("two-sum", 5, 0),
            attempt("two-sum", 6, 0),
            attempt("two-sum", 7, 0),
            attempt("two-sum", 8, 0),
        ]
    )

    state = states["two-sum"]

    assert state.ease == pytest.approx(MIN_EASE)
