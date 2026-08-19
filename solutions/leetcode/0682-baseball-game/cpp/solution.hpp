#pragma once

#include <numeric>
#include <string>
#include <vector>

inline int cal_points(std::vector<std::string> operations) {
    std::vector<int> stack;

    for (const auto& operation : operations) {
 	    int stack_length = stack.size();

	    if (operation == "+") {
	        stack.push_back(stack[stack_length - 1] + stack[stack_length - 2]);
	    } else if (operation == "D") {
	        stack.push_back(stack[stack_length - 1] * 2);
	    } else if (operation == "C") {
	        stack.pop_back();
	    } else {
	        stack.push_back(std::stoi(operation));
	    }
    }

    return std::accumulate(stack.begin(), stack.end(), 0);
}
