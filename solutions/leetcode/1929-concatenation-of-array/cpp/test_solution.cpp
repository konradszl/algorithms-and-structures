#include <catch2/catch_test_macros.hpp>
#include "solution.hpp"

/*
 * Mirror the cases in ../cases.json
 */

TEST_CASE("1929 Concatenation of Array") {
    SECTION("LeetCode example 1") {
        std::vector<int> nums{1, 2, 1};
        std::vector<int> expected{1, 2, 1, 1, 2, 1};

        REQUIRE(get_concatenation(nums) == expected);
    }

    SECTION("LeetCode example 2") {
        std::vector<int> nums{1, 3, 2, 1};
        std::vector<int> expected{1, 3, 2, 1, 1, 3, 2, 1};

        REQUIRE(get_concatenation(nums) == expected);
    }
}
