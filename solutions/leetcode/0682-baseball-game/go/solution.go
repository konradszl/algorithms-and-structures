package solution

import "strconv"

func calPoints(operations []string) int {
	stack := make([]int, 0, len(operations))

	for _, operation := range operations {
		stackLength := len(stack)

		switch operation {
		case "+":
			stack = append(stack, stack[stackLength-1]+stack[stackLength-2])
		case "D":
			stack = append(stack, stack[stackLength-1]*2)
		case "C":
			stack = stack[:stackLength-1]
		default:
			value, _ := strconv.Atoi(operation)
			stack = append(stack, value)
		}
	}

	sum := 0
	for _, score := range stack {
		sum += score
	}

	return sum
}
