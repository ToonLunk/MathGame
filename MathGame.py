# This is a logic and math game that will get harder as you succeed, created by me (Tyler Brock)
import random # this is a module used so we can make random choices
import operator # this module is useful for letting us use random operators, so the questions are random

operators = {'+':operator.add, # this is a list of operators to use to make random questions
           '-':operator.sub,
           '*':operator.mul,}

correct = 0 # how many questions the player answered correctly
num1_range = 1 # starting number for the first number
num2_range = 1 # starting number for the second number



def greet_player(): # this function will greet the player and start the game, only shown once in program
    print("Welcome to Math and Logic v 1.0 by Tyler Brock")
    print("\nThis game will test your logic skills, as well as your math skills, and display how many you get correct\n")
    play_game() # call the function that starts the game

def play_game(): # this function starts the game
    questions_list = [math_questions,math_not_questions] # make a list contanting the functions that generate questions
    random.choice(questions_list)() # pick a random function to make a brand new question

def math_questions(): # this function generates real questions 
    global correct,num2_range,num1_range # grab the global variables (they must be global so they can be used by both functions)
    op = random.choice(list(operators.keys())) # choose a random operator from the list we made earlier and name it "op"
    num1 = random.choice(range(1, num1_range+1)) #  make a new random number from 1 to our max number (starts at 1)
    num2 = random.choice(range(1, num2_range+1)) #  make a new random number from 1 to our max number (starts at 1)
    answer = operators.get(op)(num1, num2) # generate the answer to our new question
    print('\nWhat is {} {} {}?\n'.format(num1, op, num2)) # ask the user the question. The .format will replace all the {} with the parameters (num1, op, num2)
    player_answer = int(input("Answer: ")) # ask the player for the answer
    if player_answer == answer: # if the answer is correct,
        correct += 1 # add a point to their score
        num1_range +=5 # makes the game harder by adding higher numbers to the baseline number
        num2_range +=3 # makes the game harder by adding higher numbers to the baseline number
        play_game() # generate a new question
    elif player_answer != answer: # if the answer is incorrect
        print("\nWrong! The answer was:",answer) # display the correct answer
        player_lose() # call player_lose function which ends the game


def math_not_questions():# this function generates fake questions; it is the exact same as the previous functions with two differences which I will point out
    global correct, num2_range, num1_range
    op = random.choice(list(operators.keys()))
    num1 = random.choice(range(1, num1_range + 1))
    num2 = random.choice(range(1, num2_range + 1))
    answer = operators.get(op)(num1, num2)
    print('\nWhat is NOT {} {} {}?\n'.format(num1, op, num2)) # asks the player to enter any answer EXCEPT the correct one
    player_answer = int(input("Answer: "))
    if player_answer != answer: # if the player's answer is NOT the same as the actual answer, they get the point
        correct += 1
        num1_range += 5
        num2_range += 3
        play_game()
    elif player_answer == answer: # if the player's answer is the correct answer, they lose
        print("\nWrong! The answer was ANYTHING except:",answer)
        player_lose()


def player_lose(): # this function will be called when the player loses
    print("\nYou lost!")
    for i in range(1,correct+1):
        print("You got 1 point!")
        print("Total points:",i)
    again = int(input("\nAgain?\n1. Yes \n2. No\n")) # this will ask the user if they woiuld like to play again and store their answer in a variable called "again"
    if again == 1: # if the player wants to play again,
        greet_player() # restart the game by calling the start function
    elif again != 1: # if the player doesn't want to play again,
        print("Thank you for playing!") 
        return # return to home, exit game



greet_player() # callthe greeting function which starts the game
