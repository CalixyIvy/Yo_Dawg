import random

lose = True

board = []
ships = []

griddy = eval(input("How big do you want your battlefield? Ex. if you want 5x5, input 5! "))
num_row = griddy
num_col = griddy

num_ships = eval(input("How many ship would you like? "))

yoyoyo =  input("Would you like put in the location of the battleships? ")

if (yoyoyo.lower() == "yes"):
    for i in range(num_ships):
        ship = []
        ccolumn = eval(input("What column would you like your ship? "))
        crow = eval(input("What row would you like your ship? "))
        ship.append(ccolumn + 1), ship.append(crow + 1)
        ships.append(ship)
        print(ships)
        
elif (yoyoyo.lower() == "no"):
    for i in range(num_ships):
        ship = []
        ccolumn = random.randint(1, num_col)
        crow = random.randint(1, num_row)
        ship.append(ccolumn), ship.append(crow)
        ships.append(ship)
        print(ships)
      
    
    
guesses = 5

for n in range(0,num_col):

    row = []

    for i in range (0,num_row): 

        row.append(0)

    board.append(row)

for n in range (0,num_row):

    hiya = ""

    for i in range (0,num_col):

        hiya = hiya + str(board[n][i]) + " "

    print(hiya)

row_ai = random.randint(0,num_row-1)
col_ai = random.randint(0,num_col-1)

print("Welcome to battleship")

print(" ")

while (lose):

    ver = True

    while (ver):


        chosen_col = input("- Input the number of the column you wish to select: ")

        try: chosen_col = eval(chosen_col)

        except:
            print(" ")
            print ("Please input the integer of the position you which to choose")
            print(" ")

        if int == type(chosen_col): 
            ver = False

        elif type(chosen_col) != str:
            print(" ")
            print ("Please input the integer of the position you which to choose")
            print(" ")


    ver = True

    while (ver):

        print(" ")
        chosen_row = input("- Input the number of the row you wish to select: ")

        try: chosen_row = eval(chosen_row)

        except:
            print(" ")
            print ("Please input the integer of the position you which to choose")
            print(" ")


        if int == type(chosen_row): 
            ver = False

        else:
            print(" ")
            print ("Please input the integer of the position you which to choose")
            print(" ")
            print(" ")
    
    if (chosen_col == col_ai) and (chosen_row == row_ai):
        print(" ")
        print(" ")
        print ("You sunk my battleship!")
        print(" ")
        print(" ")
        break
    
    elif (guesses > 0):
        print(" ")
        print(" ")
        print("You missed, try again")
        print(" ")
        print("")
        
        board[chosen_row][chosen_col] = "X"
        
        for n in range (0,num_row):

            hiya = ""

            for i in range (0,num_col):

                hiya = hiya + str(board[n][i]) + " "

            print(hiya)
            
    