import time
import random

# Start the Story

#comment

#we are dope


def start_adventure():
    print("Welcome to your adventure!")
    print("You find yourself at a fork in the road. What will you do?")
    print("1. Go left to the mysterious forest.")
    print("2. Go right to the bustling town.")
    print("3. Head straight towards the towering mountains.")
    print("4. Explore the dark cave nearby.")
    print("5. Stay where you are and set up camp.")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        forest_path()
    elif choice == "2":
        town_path()
    elif choice == "3":
        mountain_path()
    elif choice == "4":
        cave_path()
    elif choice == "5":
        camp_path()
    else:
        print("Invalid choice. Please try again.")
        start_adventure()

def forest_path():
    print("You venture into the forest and hear the rustling of leaves...")
    # Add more story development here.

def town_path():
    print("You walk into the lively town and meet an old merchant...")
    # Add more story development here.

def mountain_path():
    print("You begin climbing the mountains, feeling the cold wind against your face...")
    # Add more story development here.

def cave_path():
    print("You enter the dark cave and feel a chill run down your spine...")
    # Add more story development here.

def camp_path():
    print("You set up camp and gaze at the stars above. It's peaceful here...")
    # Add more story development here.

# Start the adventure
start_adventure()