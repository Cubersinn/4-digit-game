import random

number = random.randint(1000, 9999)
print(number) # Для проверки, позже убрать.

number = str(number)
trues = 0
place = 0
while True:
    usernum = input("What number do you think I have made :)? ")

    if usernum == number:
        print("You win!")
        break
    else:
        try:
            int(usernum)
            str(usernum)
            for i in range(4):
                if usernum[i] == number[i]:
                    trues += 1
                    place += 1
                elif usernum[i] == number[0] or usernum[i] == number[1] or usernum[i] == number[2] or usernum[i] == number[3]:
                    trues += 1
            print("There are {0} digits are right and {1} digits are on their places".format(trues, place))
            trues = 0
            place = 0
        except:
            print("Enter a valid number!")
