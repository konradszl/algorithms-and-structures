package solution

func getConcatenation(nums []int) []int {
	result := make([]int, len(nums)*2)

	for i := range nums {
		result[i] = nums[i]
		result[i+len(nums)] = nums[i]
	}

	return result
}
