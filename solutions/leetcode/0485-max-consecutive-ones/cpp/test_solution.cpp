#include <catch2/catch_test_macros.hpp>
#include "solution.hpp"

/*
 * Mirror the cases in ../cases.json
 */

TEST_CASE("0485 Max Consecutive Ones") {
    SECTION("LeetCode example 1") {
        REQUIRE(find_max_consecutive_ones({1, 1, 0, 1, 1, 1}) == 3);
    }

    SECTION("LeetCode example 2") {
        REQUIRE(find_max_consecutive_ones({1, 0, 1, 1, 0, 1}) == 2);
    }
}
