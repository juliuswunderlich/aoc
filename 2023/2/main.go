package main

import (
	"log"
	"fmt"
	"strings"
	"os"
	"strconv"
	"bufio"
)

func main() {

	//Pass the file name to the ReadFile() function from 
	//the ioutil package to get the content of the file.

	file, error := os.Open("input.txt")


	// Check whether the 'error' is nil or not. If it 
	//is not nil, then print the error and exit.
	if error != nil {
		log.Fatal(error)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	max_red, max_green, max_blue := 12, 13, 14

	sumPossible := 0
	id := 1
	for scanner.Scan() { 
		//id, err := strconv.Atoi(strings.Trim(scanner.Text()[5:8], ": "))
		text := scanner.Text()[8:]
		games := strings.Split(text, ";") // each game
		fmt.Println("Game", id, games)
		game_success := true
		for _, game := range games {
			pulls :=  strings.Split(game, ",") // each pull
			pull_success := true
			for _, pull := range pulls {
				pull = strings.Trim(pull, ": ")
				num_str, col := strings.Split(pull, " ")[0], strings.Split(pull, " ")[1]
				num, err := strconv.Atoi(num_str)
				if err != nil {
					log.Fatal(err)
				}
				switch col {
				case "red":
					pull_success = (num <= max_red)
					fmt.Println("red", pull_success)
				case "green":
					pull_success = (num <= max_green)
					fmt.Println("green", pull_success)
				case "blue":
					pull_success = (num <= max_blue)
					fmt.Println("blue", pull_success)
				default:
					log.Fatal("error")
				}
				if !pull_success {break}
			}
			game_success = pull_success
			if !game_success {break}
		}
		if game_success {
			sumPossible += id
		}
		id += 1
	}
	fmt.Print(sumPossible)
}
