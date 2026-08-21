package solution

import "testing"

type testCase struct {
	name  string
	nums  []int
	value int
	want  int
}

func TestRemoveElement(t *testing.T) {
	tests := []testCase{
		{
			"leetcode example 1",
			[]int{3, 2, 2, 3},
			3,
			2,
		},
		{
			"leetcode example 2",
			[]int{0, 1, 2, 2, 3, 0, 4, 2},
			2,
			5,
		},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := removeElement(test.nums, test.value)
			if got != test.want {
				t.Errorf("removeElement(%v, %d) = %d, want %d", test.nums, test.value, got, test.want)
			}
		})
	}
}
