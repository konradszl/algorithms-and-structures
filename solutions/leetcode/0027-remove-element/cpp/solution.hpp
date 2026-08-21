#pragma once

#include <vector>

inline int remove_element(std::vector<int>& nums, int value) {
    int k = 0;

    for (const auto& num : nums) {
        if (num != value) {
            nums[k] = num;
            k++;
        }
    }

    return k;
}
