def EX01():
    tuoi = int(input("Enter person's age: "))
    tuoi_hop_le = int(input("Enter valid age : "))

    if tuoi >= tuoi_hop_le:
        print("You can vote.")
    else:
        print("You can not vote.")

def EX02():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

def EX03():
    num = int(input("Enter a number: "))
    if num % 7 == 0:
        print("The number is divisible by 7.")
    else:
        print("The number is not divisible by 7.")

def EX04():
    numstr = input("Enter a num string: ")
    last_digit = int(numstr[-1:])
    if last_digit % 3 ==0:
        print(f"The last digit of {numstr} is divisible by 3.")
    else:
        print(f"The last digit of {numstr} is not divisible by 3.")

import random
def EX05():
    num = random.randint(1, 9)
    guess = int(input("Guess (1-9): "))
    if num == guess:
        print("Congratulations, you're beautiful!")
    else:
        print("Sorry, that's wrong. You're ugly.")

def EX06():
    num = int(input("Enter a number(1-7): "))
    if num == 1:
        print("Sunday.")
    elif num == 2:
        print("Monday.")
    elif num == 3:
        print("Tuesday.")
    elif num == 4:
        print("Wednesday.")
    elif num == 5:
        print("Thursday.")
    elif num == 6:
        print("Friday.")
    elif num == 7:
        print("Saturday.")
    else:
        print("Sorry, the number is out of range.")

if __name__ == '__main__':
    # EX01()
    # EX02()
    # EX03()
    # EX04()
    # EX05()
    EX06()