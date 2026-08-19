package solution

import "testing"

type testCase struct {
	name       string
	operations []string
	want       int
}

func TestCalPoints(t *testing.T) {
	tests := []testCase{
		{
			"leetcode example 1",
			[]string{"5", "2", "C", "D", "+"},
			30,
		},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := calPoints(test.operations)
			if got != test.want {
				t.Errorf("calPoints(%v) = %d, want %d", test.operations, got, test.want)
			}
		})
	}
}
