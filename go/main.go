package main

import (
	"encoding/json"
	"fmt"

)

type Inner struct {
	Name string  `json:"name"`
}

type People struct {
	A Inner
	Age int  `json:"age"`
}

func main() {
	p := People{Age: 1, A: Inner{Name: "a"}}


	r, _ := json.Marshal(p)

	fmt.Println(string(r))
}