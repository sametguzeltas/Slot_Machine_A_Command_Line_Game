# Requirements about the slot machine was taken from the following link. 
# It was a java-based assignment. I only used the question. Solution (all the pyhton syntax) is unique and done by me.
# https://stackoverflow.com/questions/22324612/java-slot-machine-program-now-what-to-correct

import random
import sys
import time

gameSpeed = 0.001

class SlotMachine:
    
    totalWin = 0
    totalEntry = 0

    def __init__(self,player,age):
        self.player = player
        self.age = age

        slotMac =f'''
Welcome to the Slot Machine {self.player}!

The slot machine is a gambling device into which you need to insert money and then pull the lever. 
The slot machine then displays a set of three random images from the following list: 
Cherries, Oranges, Plums, Bells, Melons, Bars.

If two or more of the images match, you will win an amount of money, which the slot machine dispenses back to you.
  * If all three images match, you win three times the amount entered.
  * If two of the images match, you win twice the amount wagered in the first step.
  * If none of the randomly selected images match, you win nothing.

You could pull the lever to play again as much as you want. 

Do not forget! You are allowed to play slot machines only if you are 18 or over! And you are {self.age} years old.

'''
        for letter in slotMac:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(gameSpeed)

class PullTheLever(SlotMachine):

    def __init__(self,player,age):
        super().__init__(player,age)

        if self.age < 18:
            print(f"So sorry {self.player}, you are not old enough to pull the lever.")
            print(f"We are looking forward to see you again {18-self.age} years later!")
        else:
            ans = "yes"
            while ans.strip().lower() == "yes" or ans.strip().lower() == "y":
                active = False
                while not active:
                    money_str = input("How much money do you want to enter: ")
                    if money_str.isdigit():
                        money = int(money_str)
                        active = True
                        break
                    else:
                        print("Invalid number! Please try again!")

                PullTheLever.totalEntry += money

                for letter in ("\nYou pulled the lever.\nColumns are spinning fast.\nAnd the result is coming: \n\n"):
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(gameSpeed)

                pictures = {
                    "Cherries": 0, 
                    "Oranges": 0,
                    "Plums": 0,
                    "Bells": 0,
                    "Melons": 0,
                    "Bars": 0}

                pics = list(pictures.keys())

                for i in range(3):
                    index = random.choice(pics)
                    pictures[index] += 1
                    print(f"{i+1}: {index}")

                if any(x == 3 for x in pictures.values()):
                    win = money * 3
                    PullTheLever.totalWin += win 
                    print("\nTRIPLE! \nCongratulations! You win!!")
                    print(f"Your winning amount is {win}\n")
                elif any(x == 2 for x in pictures.values()):
                    win = money * 2
                    PullTheLever.totalWin += win 
                    print("\nDOUBLE! \nCongratulations! You win!!")
                    print(f"Your winning amount is {win}\n")  
                else: 
                    PullTheLever.totalWin -= money
                    print(f"\nSorry Mate!, you lost {money}\n")

                ans = input("Do you want to play again? Yes/No: ")
                if ans.strip().lower() not in ["yes", "y", "no", "n"]:
                            flag = True
                            while flag:
                                ans = input("Invalid answer! \nPlease write Yes or No! \nEnter your answer again: ")
                                if ans.strip().lower() in ["yes", "y", "no", "n"]:
                                    flag = False
            else:
                print(f"\nTotal amount you enter : {PullTheLever.totalEntry}")
                print(f"Total amount you win   : {PullTheLever.totalWin}\n")

            for letter in ("\nThank you very much!\nBelieve that you will win lots of money from our slot machine next time.\nSee you soon!\n"):
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(gameSpeed)
        time.sleep(1)
        print("\n\tTHANKSS!!!\n")



# PullTheLever("Samed", 10)
PullTheLever("Ali", 20)