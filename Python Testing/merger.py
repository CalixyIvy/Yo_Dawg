#Trying to help make bigger ships

#griddy = print("How big do you want your battlefield? Ex. if you want 5x5, input 5! ")
#num_row = griddy
#num_col = griddy
#quest = input("would you like to customize your game? ")

#if (quest.lower() == "no"):
 #   size = input("What is the size you would like your battlefield: Small Medium or Large ")
    
  #  if (size.lower() == "small"):
   #     num_row = 5
    #    num_col = 5
        #we should random the boats
        
    #elif (size.lower() == "medium"):
     #   num_row = 8
      #  num_col = 8
        #we should random the boats
        
    #elif(size.lower() == "large"):
     #   num_row = 10
      #  num_col = 10
        #we should random the boats
        


# import random

# play_please = True
# #yoyoyo my diggity dog what's hopping and bopping and dropping in the hizzy yo!

# while (play_please) :

#     lose = True
    
#     Choices_A = []
#     Choices_AI = []
#     board = []
#     board_AI = []
#     ships = []
#     ships_AI = []
#     yes_no = ["Yes","yes","No","no","yEs","yeS","nO","NO","YES","YEs","YeS","yES"]
#     griddy = 0
    
#     def Print_Board ():
        
#         for n in range (0,num_row):
    
#             hiya = ""
    
#             for i in range (0,num_col):
    
#                 hiya = hiya + str(board[n][i]) + " "
    
#             print(hiya)
            
#     def Print_Board_AI ():
    
#         for c in range (0,num_row):

#             hiya = ""

#             for d in range (0,num_col):

#                 hiya = hiya + str(board_AI[c][d]) + " "

#             print(hiya)
            
            
#     def color(word,color):
#         word = ("\033[1;" + color + ";40m " + word + "\033[0;0m")
#         return word
    
#     def color_word(word,color,style):
#         word = ("\033[" + style + ";" + color + ";40m" + word + "\033[0;0m")
#         return word
    
    
#     def Input_Ver(input_text,error_message,check,index_check,min_numb,max_numb):
        
        
#         Integer = True
      
#         while (Integer):
    
#             print(" ")
#             print(" ")
#             Input = input(input_text)
#             print(" ")
#             print(" ")
            
#             if (check == "check_1") :
                   
#                 try:
#                     Input = eval(Input)
#                     Input = Input + index_check
                    
#                 except:
#                     yup = 3
                    
#                 if (type(Input) == int and Input > min_numb) :
#                     return (Input)
                
#                 else:
#                     print (" - " + str(error_message))
                    
#             elif (check == "check_2") :
                   
#                 try:
#                     Input = eval(Input)
#                     Input = Input + index_check
                    
#                 except:
#                     yup = 3
                    
#                 if ((type(Input) == int and Input > min_numb) and (Input < max_numb)):
#                     return (Input)
                
#                 else:
#                     print (" - " + str(error_message))
         
#             elif check == "check_3":
                
#                 if Input in yes_no:
#                     return (Input)
                
#                 else:
#                     print (" - " + str(error_message))
            
    
    
    
    
    
#     griddy = Input_Ver ("How big do you want your battlefield? Ex. if you want 5x5, input 5! "
#                             ,"That is NOT a battlefield!!! Try entering real dimesions like 8 for 8x8! ","check_2",0,0,21)
#     num_row = griddy
#     num_col = griddy
    
    
    
#     num_ships = Input_Ver("How many ships would you like in play? "
#                               ,"That is not a plausible integer of objects. Try entering a number like 4 for number of ships! ","check_2",0,0,(griddy**2)+1)
    
#     guesses = Input_Ver("How many guesses would you please kind gent? Input 10**10 if you just want to just play out the AI "
#                             ,"I guess you weren't so kind then! HMPH!!! How about we try this again? Enter a valid number of guesses!!! ","check_1",0,num_ships-1,0)
    
#     yoyoyo =  Input_Ver("Would you like to choose where to place your battleships? If not please enter no and AI will randomly select it for you! "
#                             ,"Nah uh! You must input yes or no for the previous question! ","check_3",0,0,0)
    
#     if (yoyoyo.lower() == "yes"):
    
#         for i in range(num_ships):
            
#             overlap = True
            
#             while overlap : 
                
#                 ccolumn = Input_Ver("Please input a column for ship-"+str(i+1)+" ",
#                                 "That is NOT a valid integer in the range ("+str(griddy)+"x"+str(griddy)+")!!! Try again!","check_2",0,0,griddy+1)
            
#                 crow = Input_Ver("Please insert a row for ship-"+str(i+1)+ " ",
#                                     "That is NOT a valid integer in the range ("+str(griddy)+"x"+str(griddy)+")!!! Try again!","check_2",0,0,griddy+1)
            
#                 if [ccolumn,crow] in ships:
#                     print (" ")
#                     print (" - Please input a position not already chosen")
#                     print (" ")
            
#                 else:
#                     overlap = False
            
#             ship = []
        
#             ship.append(ccolumn), ship.append(crow)
            
#             ships.append(ship)
            
#      #   print(ships)
        
            
    
#     elif (yoyoyo.lower() == "no"):
    
#         for i in range(num_ships):
            
#             ship = []
            
#             no_dupe = True
            
#             while (no_dupe):
        
#                 ccolumn = random.randint(1, num_col)
                
#                 crow = random.randint(1, num_row)
                
#                 ship.append(ccolumn), ship.append(crow)
                
#                 if ship in ships:
#                     ship.remove(crow) , ship.remove(ccolumn)
                    
#                 else:
#                     no_dupe = False
                
#             ships.append(ship)
            
  
            
        
#     for i in range(num_ships):
        
#         ship_AI = []
        
#         no_dupe_1 = True
        
#         while (no_dupe_1):
        
#             ccolumn = random.randint(1, num_col)
            
#             crow = random.randint(1, num_row)
            
#             ship_AI.append(ccolumn), ship_AI.append(crow)
            
#             if ship_AI in ships_AI:
#                 ship_AI.remove(crow) , ship_AI.remove(ccolumn)
                
#             else:
#                 no_dupe_1 = False
            
#         ships_AI.append(ship_AI)
        
#    # print (ships_AI)
        
        
            
#     # print(ships)
        
    
#     for n in range(0,num_col):
        
#         row = []
            
#         for i in range (0,num_row): 
                
#             row.append(color(str(0),"36"))
            
#         board.append(row)
        
#     for n in range(0,num_col):
    
#         row = []
            
#         for i in range (0,num_row): 
                
#             row.append(color("0","36"))
            
#         board_AI.append(row)
        
#    # print (ships_AI)
        
#     for i in range (len(ships)):
        
#         board[ships[i][1]-1][ships[i][0]-1] = color("B","37")
        
#     print(" ")
#     print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
#     print(" ")
   
        
        
     
#     print(" ")
#     print (color_word ("Your board","33","4"))
#     print(" ")
#     Print_Board()
    
#     print(" ")
#     print (color_word ("Opponents Board","33","4"))
#     print(" ")
#     Print_Board_AI() 
        
        
#     print(" ")
#     print(" ")
#     print("Hiya! Welcome to the wonderful, bloody, and terrifying world of Batttleship. There is no escape!!! ")
#     print(" ")
#     print(" ")
   
    
#     # print (ships)
    
#     while (lose):
        
#         Choice_n = []
        
            
#         chosen_col = Input_Ver("Enter your guess for the column you choose to blow up! ",
#                                    "Daiven really full-proofed this huh? WELP! Sucks for you! Now go ahead a please enter an integer in the range ("+str(griddy)+"x"+str(griddy)+") ",
#                                    "check_2",0,0,griddy+1)
            
      
        
#         chosen_row = Input_Ver("What's your guess for the row you want to bomb? ",
#                                    "HA! Really Benjamin? Please enter an integer within the range of the grid you chose ("+str(griddy)+"x"+str(griddy)+"), so that you can destroy it! ",
#                                    "check_2",0,0,griddy+1)
#         print(" ")
#         print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
#         print(" ")
       

       
#         bro = False
         
#         Choice_n = [chosen_col,chosen_row]
        
#         if Choice_n in Choices_A:
#             print (" ")   
#             print (" - You have already attacked there, Captain!")
#             print (" ") 
#             print ("Try again")
#             print (" ")
#             bro = True
        
#         else: 
#             Choices_A.append(Choice_n)   
            
        
    
#         if (bro != True) :
            
#             no_dupes_2 = True
        
#             while (no_dupes_2) :
                
#                 chosen_col_AI = random.randint(1,griddy)
#                 chosen_row_AI = random.randint(1,griddy)
#                 Choice_n_AI = [chosen_col_AI,chosen_row_AI]
            
#                 if Choice_n_AI in Choices_AI:
#                     yup = 3
                
#                 else: 
#                     print(" ")
#                     print("Your opponent guessed ("+str(chosen_col_AI)+","+str(chosen_row_AI)+")")
#                     print(" ")
#                     Choices_AI.append(Choice_n_AI) 
#                     no_dupes_2 = False   
                    
#         if (bro != True) :
            
#             if (Choice_n_AI in ships) :
                
#                 ships.remove(Choice_n_AI)
                
#                 board[chosen_row_AI-1][chosen_col_AI-1] = (" " + str (color_word ("B","31","1")))
                
#                 print(" ")
#                 print(" - The AI bombed one of your ships, Captain!!!")
                
                
#             else:
                
#                 board[chosen_row_AI-1][chosen_col_AI-1] = color("X","33")
                
#                 print(" ")
#                 print(" - L the Ai missed. It's a L O S E R!!!")
             
                
                
        
    
#         guesses = guesses - 1
        
#         if bro == True:
#             guesses = guesses + 1
    
        
#         elif Choice_n in ships_AI:
            
#             ships_AI.remove(Choice_n)
            
#             board_AI[chosen_row-1][chosen_col-1] = color("H","31")
            
#             print(" ")
#             print(" ")
#             print (" - You hit the AI's ship, Captain!!! Good Aim!")
#             print(" ")
#             print(" ")
                
            
#         else:
#             print(" ")
#             print(" ")
#             print(" - Are you blind?!? You missed! Let's try that again!!! ")
#             print(" ")
#             print(" ")
            
#             board_AI[chosen_row-1][chosen_col-1] = color("X","33")
        
      
#         print ("You have " + str(guesses) + " guesses")
#         print ("You have "+str(len(ships_AI))+" more battleships to hit")
#         print (" ")
            

#         print(" ")
#         print (color_word ("Your board","33","4"))
#         print(" ")
#         Print_Board()
        
#         print(" ")
#         print (color_word ("Opponents Board","33","4"))
#         print(" ")
#         Print_Board_AI() 
        
#         if (len(ships_AI) == 0) :
#             print(" ")
#             print(" ")
#             print(" ")    
#             print(" ")
#             print (color (" - Congratulations!!!!! You did it! You did it! Oh what a wonderful day!!! You murdered innocent lives. Leave before I make you repent for your sins!!!! Bye bye!","33"))
#             print (" ")
#             lose - False
#             break
        
        
#         elif ( (len(ships) == 0) or (guesses == 0) ):
            
#             if (len(ships) == 0):
                
#                 print(" ")
#                 print(" ")
#                 print(" ")
#                 print(" ")
#                 print (color(" - Wow you let that loser beat you!?! It's not even alive!!! I guess that makes you an even bigger loser. L!!!","31"))
#                 print (" ")
#                 lose - False
#                 break
            
            
#             else:
#                 print(" ")
#                 print(" ")
#                 print(" ")
#                 print(" ")
#                 print (color (" - You got real cocky inputing those guesses huh? You thought that you could win!?! HA! Welp, better luck next time!","31"))
#                 print (" ")
#                 lose - False
#                 break



#     print (" ")
#     print(" ")
#     print(" ")
#     game_reset = Input_Ver ("Would you like to play again? Yes or No? ",
#                             "Please input either Yes or No","check_3",0,0,0)
    
#     if game_reset.lower() == "yes":
#         yup = 4
        
#     else:
#         play_please = False
class ships:
    def __init__(self, Guppy, Dory, Reef, Shark, Tombo):
        self.ship1 = Guppy
        self.ship2= Dory
        self.ship3 = Reef
        self.ship4 = Shark
        self.ship5 = Tombo
        
        self.shipss = []

a = ships('Guppy')
b = ships('Dory')
c = ships('Reef')
d = ships('Shark')
e = ships('Tombo')

input("Type the ship that you want: ")

def add_coordinates(self, column, row):
    column = eval(input("Input column for ship: "))
    row = eval(input("Input row for ship: "))
    self.shipss.append(column)


#         class Dog:

#     def __init__(self, name):
#         self.name = name
#         self.tricks = []    # creates a new empty list for each dog

#     def add_trick(self, trick):
#         self.tricks.append(trick)

# >>> d = Dog('Fido')
# >>> e = Dog('Buddy')
# >>> d.add_trick('roll over')
# >>> e.add_trick('play dead')
# >>> d.tricks
# ['roll over']
# >>> e.tricks
# ['play dead']
        
        
        #AIdestroy("C'est la vie. You got got!!! But this battle isn't over yet, Captain...unless it is!?! Wake Up! Wake Up! Wake Up! Hahaha, nah just kidding. NOW GO ENACT YOUR REVENGE!!!! >:) ")
        #UserDestroy("BOOOOOOM! Yeah that ship is definently a goner. GOOD JOB CAPTAIN!!! Don't you just love taking the lives of other human beings! :) ")