package solution

func removeElement(nums []int, value int) int {
	k := 0

	for _, num := range nums {
		if num != value {
			nums[k] = num
			k++
		}
	}

	return k
}
