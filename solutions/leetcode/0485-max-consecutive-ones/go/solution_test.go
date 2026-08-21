package solution

import "testing"

type testCase struct {
	name string
	nums []int
	want int
}

func TestFindMaxConsecutiveOnes(t *testing.T) {
	tests := []testCase{
		{
			"leetcode example 1",
			[]int{1, 1, 0, 1, 1, 1},
			3,
		},
		{
			"leetcode example 2",
			[]int{1, 0, 1, 1, 0, 1},
			2,
		},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := findMaxConsecutiveOnes(test.nums)
			if got != test.want {
				t.Errorf("findMaxConsecutiveOnes(%v) = %d, want %d", test.nums, got, test.want)
			}
		})
	}
}
