#pragma once

#include <vector>

inline std::vector<int> get_concatenation(const std::vector<int>& nums) {
    std::vector<int> result(nums.size() * 2);
    
    for (std::size_t i = 0; i < nums.size(); i++) {
        result[i] = nums[i];
        result[i + nums.size()] = nums[i];
    }

    return result;
}
