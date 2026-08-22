package solution

import (
	"slices"
	"testing"
)

type testCase struct {
	name string
	nums []int
	want []int
}

func TestSolve(t *testing.T) {
	tests := []testCase{
		{
			"leetcode example 1",
			[]int{1, 2, 1},
			[]int{1, 2, 1, 1, 2, 1},
		},
		{
			"leetcode example 2",
			[]int{1, 3, 2, 1},
			[]int{1, 3, 2, 1, 1, 3, 2, 1},
		},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := getConcatenation(test.nums)
			if !slices.Equal(got, test.want) {
				t.Errorf("getConcatenation(%v) = %v, want %v", test.nums, got, test.want)
			}
		})
	}
}
