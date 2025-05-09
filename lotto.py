from random import randint
"""Lotto Game
First, create lists that will be used in functions later
"""
list = []
draw_list = []
same_values = []

def lotto():
    """This function is used to collect numbers from user.
    Function checks, if user puts valid number in range 1-49

    :return:
    """
    s = 6
    for i in range(s):
        t = False
        while t != True:
            try:
                num = int(input("Enter a number: "))
                if num not in range(1, 50):
                    print("Invalid number, try again.")
                elif num in list:
                    print("Number already in use, try again.")
                else:
                    list.append(num)
                    t = True
            except ValueError:
                print("Invalid input")

    list.sort()
    print(f"Your numbers are {list}")

def main():
    """This is main function.
    It calls  previous function Lotto.
    After that, it fillup the draw_list with random numbers in range 1-49
    and sort that list in ascending order.
    """
    lotto()

    for i in range(6):
        t = False
        while t != True:
            num = randint(1, 49)
            if num not in list:
                draw_list.append(num)
                t = True


    draw_list.sort()
    print(f"Lotto numbers are {draw_list}")
    print()

#Here, the function compare both list and the matching numbers are saved in "same_values" list
    for i in list:
        for v in draw_list:
            if i == v:
                same_values.append(v)


#Finally, there is a message for user, if he guessed any number or not
    if len(same_values) == 0:
        print("There is no match. Good luck next time")
    else:
        print(f"You guessed these numbers: {same_values}. Congratulations!")



if __name__ == "__main__":
    main()
