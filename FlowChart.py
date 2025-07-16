answer=input("Do you have money? Y/N ")
if answer=="Y":
    answer=input("Do you have 30 dollars? ")
    if answer=="Y":
        print("BUY A CHANCE PLUSHIE!!!!!")
    else:
        answer=input("Do you have a JOB? ")
        if answer=="Y":
            answer=input("BUY A CHANCE PLUSHIE!!!!!")
        else:
            answer=input("Will you get a job? ")
            if answer=="Y":
                print("BUY A CHANCE PLUSHIE!!!!!")
            else:
                print("Your execution will be held in an undisclosed area at 17th of August 12:56:01 AM")
else:
    answer=input("Do you have a JOB? ")
    if answer=="Y":
        answer=input("BUY A CHANCE PLUSHIE!!!!!")
    else:
        answer=input("Will you get a job? ")
        if answer=="Y":
            print("BUY A CHANCE PLUSHIE!!!!!")
        else:
            print("Your execution will be held in an undisclosed area at 17th of August 12:56:01 AM")
