/*jslint devel: true */
const computerChoiceDisplay = document.getElementById('computer-choice')
const userChoiceDisplay = document.getElementById('user-choice')
const resultDisplay = document.getElementById('result')
//pick out all the buttons by id
const possibleChoices = document.querySelectorAll('button')
//global declaration
let userChoice

possibleChoices.forEach(possibleChoice => possibleChoice.addEventListener('click', (e) => {
    userChoice = e.target.id
    userChoiceDisplay.innerHTML = userChoice
    generateComputerChoice()
    getResult()
}))

function generateComputerChoice(){
    const randomNumber = Math.floor(Math.random() * possibleChoices.length) + 1

    if(randomNumber === 1){
        computerChoice = 'rock'
    }else if(randomNumber === 2){
        computerChoice = 'scissors'
    }else{
        computerChoice = 'paper'
    }
    computerChoiceDisplay.innerHTML = computerChoice

    console.log(userChoice + ' ' + randomNumber)
}

function getResult() {
    if(computerChoice === userChoice){
        result = 'Its a draw!'
    }
    if(computerChoice === 'rock' && userChoice === "paper"){
        result = "Paper covers rock. You Won!!"
    }else if(computerChoice === 'rock' && userChoice === "scissors"){
        result = "Rock beats scissors. You lost :-("
    }

    if(computerChoice === 'paper' && userChoice === "scissors"){
        result = "Scissors cut paper. You Won!!"
    }else if(computerChoice === 'paper' && userChoice === "rock"){
        result = "Paper covers rock. You lost :-("
    }

    if(computerChoice === 'scissors' && userChoice === "rock"){
        result = "Rock beats scissors. You Won!!"
    }else if(computerChoice === 'scissors' && userChoice === "paper"){
        result = "Scissors cut paper. You lost!!"
    }

    resultDisplay.innerHTML = result
}
