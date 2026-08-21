#include <catch2/catch_test_macros.hpp>
#include <vector>
#include "solution.hpp"

/*
 * Mirror the cases in ../cases.json
 */

TEST_CASE("0027 Remove Element") {
    SECTION("LeetCode example 1") {
        std::vector<int> nums{3, 2, 2, 3};

        REQUIRE(remove_element(nums, 3) == 2);
    }

    SECTION("LeetCode example 2") {
        std::vector<int> nums{0, 1, 2, 2, 3, 0, 4, 2};

        REQUIRE(remove_element(nums, 2) == 5);
    }
}
