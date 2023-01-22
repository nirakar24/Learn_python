# Program to check if the student is eligible to sit in exam or not

lect = int(input("No. of lectures held : "))
attend = int(input("no. of lectures attended : "))

percent=(attend/lect)*100

if attend<=lect:
    if percent>=75:
        print(f"\nYou attended {percent}% of lectures")
        print("You can sit for the Examination")
    
    else:
        print(f"\nYou attended {percent}% of lectures")
        print("You can't sit for the Examination")
else:
    print("No. of lectures attended should be less than the total no. of lectures")


