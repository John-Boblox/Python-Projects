import random
import time

#The lists
choices=["Mitocondria","Radioactivity","Relativity"]
Congrats=["You did great!", "You're brilliant!", "Correct!"]
print("Welcome to the Missing Word game!")

#Sub-program
def question():
    answer=input("\nWhich is the missing word?\nMitocondria\nRadioactivity\nRelativity>>")
    return answer
    
#Question 1
time.sleep(2)
print("The _________ is the powerhouse of the cell")
answer=question()
if answer==choices[0]:
    print(random.choice(Congrats))
else:
    print("Do better")
    
#Question 2
time.sleep(2)
print("Marie Curie discovered __________")
answer=question()
if answer==choices[1]:
    print(random.choice(Congrats))
else:
    print("Why are you so bad at this game?")
    
#Question 3
time.sleep(2)
print("Albet Einstein created the Theory of __________")
answer=question()
if answer==choices[2]:
    print(random.choice(Congrats))
else:
    print("Never play this game ever again")
