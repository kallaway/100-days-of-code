package main

import (
	"fibonacci_sequence/fibonacci"
	"fibonacci_sequence/handlers"
	"fmt"
)

func main() {
	seq := fibonacci.SequenceInitializer()
	for {
		partialSequence, err := handlers.App(&seq)
		if err != nil {
			fmt.Println(err.Error())
			continue
		}
		fmt.Printf("The element you're looking for is %d\n", partialSequence)
	}

}
