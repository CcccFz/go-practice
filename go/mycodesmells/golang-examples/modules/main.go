package main // import "github.com/mycodesmells/golang-examples/modules"

import (
	"flag"
	"fmt"

	"github.com/pkg/errors"
)

func main() {
	name := flag.String("name", "", "name")
	flag.Parse()

	if err := greet(*name); err != nil {
		fmt.Printf("Failed to greet you: %v", err)
	}
}

func greet(name string) error {
	if name == "" {
		return errors.New("no name provided")
	}
	fmt.Printf("Hello %s! I'm not in the $GOPATH!\n", name)
	return nil
}
