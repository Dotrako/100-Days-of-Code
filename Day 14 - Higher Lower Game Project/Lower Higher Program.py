# import useful library and modules
import random as rd
from Art import logo, vs
from game_data import data

# create a random variables to store the pseudo random cpu output fron our list data
first_subject = rd.choice(data)
second_subject = rd.choice(data)

# input a var to start or close the game
start = input("Press Y to play or N to leave the game").lower

def game_rules(subject_A, subject_B):
    print(f"Choose A for {first_subject["name"]}")
    print(f"Choose B for {second_subject["name"]}")
game_rules(subject_A = first_subject , subject_B = second_subject)

choice = input("Please enter your choice!").lower()

def game_player_process(player_choice):
    if player_choice == "a":
        player_choice = first_subject["follower_count"]
    else:
        player_choice = second_subject["follower_count"]
game_player_process(player_choice = choice)

cpu = ""
def game_cpu_process(cpu_choice):
    if choice == first_subject["follower_count"]:
        cpu_choice = player_choice = second_subject["follower_count"]
    else:
        player_choice = first_subject["follower_count"]
game_cpu_process(cpu_choice=cpu)    

if input =="y":
    game_rules()
    game_player_process()
    game_cpu_process()