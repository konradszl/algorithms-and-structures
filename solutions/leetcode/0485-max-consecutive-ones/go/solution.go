package solution

func findMaxConsecutiveOnes(nums []int) int {
	result := 0
	count := 0

	for _, num := range nums {
		if num == 0 {
			count = 0
		} else {
			count++
		}

		if count > result {
			result = count
		}
	}

	return result
}
