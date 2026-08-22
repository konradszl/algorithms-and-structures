def get_concatenation(nums: list[int]) -> list[int]:
    result = [0] * (len(nums) * 2)

    for i in range(len(nums)):
        result[i] = nums[i]
        result[i + len(nums)] = nums[i]
    
    return result
    
