import random

while 0 < 1 :
    def Win():
        if(comp == you):
            return None

        if(comp == "s"):
            if(you == "g"):
                return True
            elif(you == "w"):
                return False

        elif(comp == "w"):
            if(you == "s"):
                return True
            elif(you == "g"):
                return False

        if(comp == "g"):
            if(you == "w"):
                return True
            elif(you == "s"):
                return False

    comp = print("Computer's Turn : Snake(s) Water(w) Gun(g)")

    randNO = random.randint(1,3)

    if (randNO == 1):
        comp = "s"
    elif(randNO == 2):
        comp = "w"
    else:
        comp = "g"

    you = input("Ypur turn : Snake(s) Water(w) Gun(g)")

    if(Win()== True):
        print("You win !!!")
    elif(Win() == None):
        print("It's a tie :)  Play again")
    else:
        print("You loose :( ")


    


