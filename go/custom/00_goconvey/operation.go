package _0_goconvey

import "errors"

func Add(a, b int) int {
	return a + b
}

func Sub(a, b int) int {
	return a - b
}

func Mul(a, b int) int {
	return a * b
}

func Div(a, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("被除数不能为0")
	}
	return a / b, nil
}
