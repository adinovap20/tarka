package main

import (
	"fmt"
	"os"
	"os/user"
	"tarka/src/repl"
)

func main() {
	fmt.Println("-- Tarka --")
	fmt.Println("")
	user, err := user.Current()
	if err != nil {
		panic(err)
	}
	fmt.Printf("Hello %s! This is the Tarka Programming Language!\n", user.Username)
	fmt.Printf("Type your code!\n")
	repl.Start(os.Stdin, os.Stdout)
}
