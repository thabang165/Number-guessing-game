
import random
def number_guessing_game():
    number = random.randint(1 , 100)
    difficulty = input("Chooose difficulty: Easy or Hard ")
    if difficulty.lower() == "easy":
        attempts = 10
    elif difficulty.lower() == "hard":
        attempts = 3
    tries = 0
    while True:
        user_number = int(input("Guess a number between 1 and 100 "))
        if user_number < 1 or user_number > 100:
            print("Please insert a valid number between 1 and 100 ⚠️ ⚠️ ")
            continue
        elif user_number != number and tries <= attempts:
            print("❌❌❌ Incorrect guess please try again ❌❌❌ ")
            print(attempts - tries, "tries remainig ")
            tries += 1
        elif tries >= attempts:
            print ("💀💀💀 You have ran out of attempts, game over 💀💀💀. The correct guess was ", number)
            break
        elif user_number == number:
            print ("🎉🎉🎉 CONGRATULATIONS YOU HAVE WON! 🎉🎉🎉")
            break

while True:
    number_guessing_game()
    replay = input("🔁Would you like to play again? (yes or no)🔁: ")
    if replay.lower() == "yes":
        continue
    else:
        print("👋  Thank you for playing, goodbye")
        break
