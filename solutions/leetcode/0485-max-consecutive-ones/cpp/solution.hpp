#pragma once

#include <vector>

inline int find_max_consecutive_ones(const std::vector<int>& nums) {
    int result = 0;
    int count = 0;

    for (const auto& num : nums) {
        if (num == 0) {
            count = 0;
        } else {
            count++;
        }

        if (count > result) {
            result = count;
        }
    }

    return result;
}
