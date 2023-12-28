# import useful library and modules
import random as rd
from Art import logo, vs
from game_data import data

first_subject = rd.choice(data)
second_subject = rd.choice(data)

start = input("Press Y to play or N to leave the game: ").lower()

def game_rules(subject_A, subject_B):
    print(f"Choose A for {subject_A['name']}")
    print(f"Choose B for {subject_B['name']}")

def game_player_process(player_choice, subject_A, subject_B):
    if player_choice == "a":
        return first_subject["follower_count"]
    else:
        return second_subject["follower_count"]

def game_cpu_process(player_choice, subject_A, subject_B):
    if player_choice == first_subject["follower_count"]:
        return second_subject["follower_count"]
    else:
        return first_subject["follower_count"]

if start == "y":
    game_rules(first_subject, second_subject)
    choice = input("Please enter your choice: ").lower()
    choice1 = input("Please enter your choice: ").lower()
    
    player_result = game_player_process(choice, first_subject, second_subject)
    print(f"Player choice result: {player_result}")
    
    cpu_result = game_cpu_process(choice1, first_subject, second_subject)
    print(f"CPU choice result: {cpu_result}")