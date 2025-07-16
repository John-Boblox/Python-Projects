import random
import time

names=["John","Bob","Joe"]
print("Welcome to Professional Chatbot!")
time.sleep(2)
print("Who do you want to talk to?")
time.sleep(2)
choice=input(names)
if choice == "Bob" or "bob":
    ask=input("Hello, I'm Bob and you are?")
    YN=input("Nice to meet you,", ask, "How are you? (Y/N)")
    if YN=="Y" or "y":
        print("Thats good to hear!")
    else:
        print("That's bad. Hope your day gets better.")
elif choice == "John":
    ask2=input()
