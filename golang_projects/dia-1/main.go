package main

import (
	"fmt"
	"strings"
)

/*
Acknowledgments:
I thank yvonne-liu for the idea and for the example tests :)

Description:
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter must be converted to its ASCII code.
The second letter must be switched with the last letter
Keepin' it simple: There are no special characters in the input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
*/

func main() {
	fmt.Println(EncryptThis("Hello World!"))
}

func EncryptThis(text string) string {
	words := strings.Split(text, " ")
	var encryptedWords []string
	for _, word := range words {
		if len(word) == 0 {
			encryptedWords = append(encryptedWords, "")
			continue
		}
		if len(word) == 1 {
			encryptedWords = append(encryptedWords, fmt.Sprintf("%d", word[0]))
			continue
		}
		if len(word) == 2 {
			encryptedWords = append(encryptedWords, fmt.Sprintf("%d%c", word[0], word[1]))
			continue
		} else {
			encryptedWords = append(encryptedWords, fmt.Sprintf("%d%c%s%c", word[0], word[len(word)-1], word[2:len(word)-1], word[1]))
		}

	}
	return strings.Join(encryptedWords, " ")
}
