#include <catch2/catch_test_macros.hpp>
#include "solution.hpp"

/*
 * Mirror the cases in ../cases.json
 */

TEST_CASE("0682 Baseball Game") {
    SECTION("LeetCode example 1") {
        REQUIRE(cal_points({"5", "2", "C", "D", "+"}) == 30);
    }

    SECTION("LeetCode example 2") {
        REQUIRE(cal_points({"5", "-2", "4", "C", "D", "9", "+", "+"}) == 27);
    }

    SECTION("LeetCode example 3") {
        REQUIRE(cal_points({"1"}) == 1);
    }
}
