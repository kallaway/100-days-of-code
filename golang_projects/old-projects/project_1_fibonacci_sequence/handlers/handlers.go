package handlers

import (
	"fibonacci_sequence/fibonacci"
	"fmt"
	"os"
	"reflect"
)

type Positions struct {
	InitialPosition int
	FinalPosition   int
}

func ReadUserInput() (int, error) {
	var interaction int
	_, err := fmt.Scanln(&interaction)
	if err != nil {
		return -1, err
	}
	return interaction, err
}

func App(s *fibonacci.Sequence) (interface{}, error) {
	fmt.Print(interactionText)

	var partialSequence interface{}
	interaction, err := ReadUserInput()
	partialSequence, err = Interaction(s, interaction)
	if err != nil {
		return nil, err
	}

	return partialSequence, nil
}

func Interaction(s *fibonacci.Sequence, interaction interface{}) (interface{}, error) {
	var partialSequence interface{}
	p := Positions{}
	switch interaction {
	case 0:
		os.Exit(0)
	case 1:
		err := p.OneElementUserInput()
		if err != nil {
			return nil, err
		}
		err = p.InputHandler()
		if err != nil {
			return nil, err
		}
		partialSequence = s.FibonacciElement(p.InitialPosition)
	case 2:
		err := p.PartialSequenceUserInput()
		if err != nil {
			return nil, err
		}
		err = p.InputHandler()
		if err != nil {
			return nil, err
		}
		partialSequence = s.FibonacciPartialSequence(p.InitialPosition, p.FinalPosition)
	case 3:
		partialSequence = s.EntireSequence()
	default:
		err := fmt.Errorf("please choose a valid entry")
		return nil, err
	}
	return partialSequence, nil
}

func (p *Positions) OneElementUserInput() error {
	fmt.Println("Which of the Fibonacci's Sequence element would you like to be returned? ")
	var err error
	p.InitialPosition, err = ReadUserInput()
	if err != nil {
		return err
	}
	return nil
}

func (p *Positions) PartialSequenceUserInput() error {
	fmt.Println("Initial position of the Fibonacci Sequence: ")
	var err error
	p.InitialPosition, err = ReadUserInput()
	if err != nil {
		return err
	}

	fmt.Println("Final position of the Fibonacci Sequence(Insert zero if you want to cover the slice length): ")
	p.FinalPosition, err = ReadUserInput()
	if err != nil {
		return err
	}
	return nil
}

func (p *Positions) InputHandler() error {
	if reflect.TypeOf(p.InitialPosition) != reflect.TypeOf(5) || p.InitialPosition <= 0 {
		return fmt.Errorf("wrong input. Please insert positive integer numbers for positions only")
	}
	if reflect.TypeOf(p.FinalPosition) != reflect.TypeOf(5) || p.FinalPosition < 0 {
		return fmt.Errorf("wrong input. Please insert positive integer numbers for positions only")
	}
	return nil
}
