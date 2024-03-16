package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	inputReader := bufio.NewReader(os.Stdin)

	println("Input the name of your city: ")
	city, _ := inputReader.ReadString('\n')
	city = city[:len(city)-1]
	println("Input the name of your pet: ")
	pet, _ := inputReader.ReadString('\n')
	pet = pet[:len(pet)-1]
	fmt.Printf("Your band name should be the %s %s \n", city, pet)
}
