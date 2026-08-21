def remove_element(nums: list[int], value: int) -> int:
    k = 0

    for num in nums:
        if num != value:
            nums[k] = num
            k += 1

    return k
