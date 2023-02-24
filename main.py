import random

def num(x):
    random_number = random.randint(1, x)
    guese = 0
    while guese != random_number:
         guese = int(input(f"Enter a random number between 1 and {x}: "))
         if guese > random_number:
             print("Too High please try again")
         elif guese < random_number:
             print("Too low please try again")

    print("Yeey,you got that right!!")

num(10)




