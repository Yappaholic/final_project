from lib import answers, method, questionnaire
import time
import sys
global_list = []
def main():
    print ("Hello, this is a test for evaluating depression level")
    time.sleep(2)
    print ("Do you want to participate?")
    print("1: yes    2: no")
    enter(input())
def calculate(lis: list):
    n = sum(lis) - 21
    return n
def enter(n):
    try:
        n = int(n)
    except ValueError:
        sys.exit("Please type 1 or 2")
    if n == 1:
        questions()
    elif n == 2:
        sys.exit("Have a good day!")
    elif 0 > n or n > 2:
        print("Please type 1 or 2")
def answer():
    while True:
        number = input()
        try:
            number = int(number)
        except ValueError:
            print("Choose between 1 and 4")
            continue
        if 0 > number or number > 4:
            print("Choose between 1 and 4")
        else:
            global_list.append(number)
            break
def questions():
    i = 0
    print("Please choose the correct number for how you feel at the moment.")
    time.sleep(2)
    while i < len(questionnaire):
        n = enumerate(questionnaire[i], start=1) 
        print("Question #" + str(i+1))
        time.sleep(1)
        for a in list(n):
            (number, question) = a
            print(number, question)
        answer()
        i += 1
    x = calculate(global_list)
    print(result(x))
def result(x):
    print(f"Your total is {x} points")
    time.sleep(1)
    if 1 <= x <= 10:
        return("Your ups and downs are considered normal")
    elif 11 <= x <= 16:
        return("You might have mild mood disturbance")
    elif 17 <= x <= 20:
        return("You might have borderline clinical depression")
    elif 21 <= x <= 30:
        return("You might have moderate depression")
    elif 31 <= x <= 40:
        return("You might have severe depression")
    elif x > 40:
        return("You might have extreme depression")


    








if __name__ == "__main__":
    main()

