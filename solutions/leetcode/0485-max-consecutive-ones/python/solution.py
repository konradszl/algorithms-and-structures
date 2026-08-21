def find_max_consecutive_ones(nums: list[int]) -> int:
    result = 0
    count = 0

    for num in nums:
        if num == 0:
            count = 0
        else:
            count += 1
        
        if count > result:
            result = count

    return result
