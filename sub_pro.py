import random

#this is procedure
def knowledge():
    list=["page likes to code and play games in his free time", "page likes the color blue i think", "idk tbh"]
    return(random.choice(list))

question=input("You wanna know some things about Pagnaboth ")
if question=="yes" or question=="YES" or question=="Yes":
    print(knowledge())
else:
    print("ok bro")
    
#This is a function
def multiply(x,y):
    return (x*y)
x=int(input("First number "))
y=int(input("Second number "))
print (multiply(x,y))
