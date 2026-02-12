import random
import time

#The lists
choices=["Mouse","Lunar Calendar","2 weeks"]
Congrats=["You did great!", "You're brilliant!", "Correct!"]

#The 
print("Happy Chinese New Year!")
time.sleep(2)
start=input("Do you want to play a game? Y/N")
if start=="Y":
    print("Let's start the game!")
    time.sleep(2)
else:
    print("Alright then...")

#Sub-program
def question():
    answer=input("\nWhich is the missing word?\nMouse\nLunar Calendar\n2 weeks>>")
    return answer
    



#Question 1
time.sleep(2)
print("The first Chinese Zodiac is the_________")
answer=question()
if answer==choices[0]:
    print(random.choice(Congrats))
else:
    print("Do better")
    
#Question 2
time.sleep(2)
print("Chinese New Year follows the __________")
answer=question()
if answer==choices[1]:
    print(random.choice(Congrats))
else:
    print("Why are you so bad at this game?")
    
#Question 3
time.sleep(2)
print("Chinese New Year lasts for __________")
answer=question()
if answer==choices[2]:
    print(random.choice(Congrats))
else:
    print("Never play this game ever again")
