import math

while(True):
    
    yes = input("Do you want to play? ")
    
    if (yes.lower() == "yes"):
            
            print("Hiya! It's time to calculate some stuff. ")

            print("Select what you want to do!")
            print("Add")
            print("Subtract")
            print("Multiply")
            print("Divide ")
            print("Exponent")
            print("Square Root")

            begin = input("So? ")
            begin = begin.lower()
            match begin:
                
                case "add":
                    try:
                        nu = eval(input("Input first number: "))
                        m = eval(input("Input second number: "))
                        print(nu + m)
                    except:
                        print("Error loading code... Try Again. ")
                    
            
                case "subtract":
                    try:
                        num = eval(input("Put number here: "))
                        ber = eval(input("Put number here: "))
                        print(num - ber)
                    except:
                        print("Error loading code... Try Again. ")
            
                case "multiply":
                    try:
                        n = eval(input("Insert #: "))
                        um = eval(input("Insert #: "))
                        print(n * um)
                    except:
                        print("Error loading code... Try Again. ")
                    
                case "divide":
                    try:
                        um = eval(input("Type #: "))
                        be = eval(input("Type #: "))
                        print(um / be)
                    except:
                        print("Error loading code... Try Again. ")
                        
                case "exponent":
                    try:
                        nu = eval(input("Number Here: "))
                        mber = eval(input("Number Here: "))
                        print(nu ** mber)
                    except:
                        print("Error loading code... Try Again. ")
                    
                case"square root":
                    try:
                        numb = eval(input("Number goes here: "))
                        print(math.sqrt(numb))
                    except:
                        print("Error loading code... Try Again. ")
                    
                case _:
                    print("Try typing: add, subtract, multiply, divide, exponent, square root, or entering a valid number. ")
    else:
        print ("Bye then!!!")
        break