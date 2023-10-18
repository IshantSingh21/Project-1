import random

while True:
    response = input("do you want to roll a die? (y/n): ")
    if response.lower()== 'y':
        no= random.randint(1,6)
        if no==1:
            print("---------")
            print("|       |")
            print("|   0   |")
            print("|       |")
            print('---------')
        elif no==2:
            print("---------")
            print("|       |")
            print("| 0   0 |")
            print("|       |")
            print('---------')
        elif no==3:
            print("---------")
            print("|       |")
            print("|0  0  0|")
            print("|       |")
            print('---------')
        elif no==4:
            print("---------")
            print("| 0   0 |")
            print("|       |")
            print("| 0   0 |")
            print("---------")
        elif no == 5:
            print("---------")
            print("| 0   0 |")
            print("|   0   |")
            print("| 0   0 |")
            print("---------")
        else:
            print("---------")
            print("| 0   0 |")
            print("| 0   0 |")
            print("| 0   0 |")
            print("---------")
    elif response.lower() =='n':
        print("Thanks for playing!")
    else:
        print("Invalid input. Please enter 'y' to roll the dice or 'n' to roll the dice ")
