while(True):
    mhm = input("Do you want to calculate your BMI? ")
    
    output = ["Please input your height in ", "Please input your weight in ", "Your BMI is ", "and you are ", "There was an error calculating your BMI. Try again!"]
    
    one = ["kilograms", "kilos", "kilo", "k", "grams", "kilogram"]
    two = ["lb", "lbs", "pounds", "p", "pound"]
    
    if (mhm.lower() == "yes"):
        next = input("Would you like it in kilograms or pounds? ")
        
        if (next.lower() in one):
            try:
                m = eval(input(output[0] + "centimeters: "))
                k = eval(input(output[1] + "kilograms: "))
                ans = k/(m)**2*10000
                if (ans < 18.6):
                    print(output[2], ans, output[3] + "underweight. ")
                elif (ans > 24.9):
                    print(output[2], ans, output[3] + "overweight. ")
                else:
                    print(output[2], ans, output[3] + "normal weight. ")
            except:
                print(output[4])
                
        elif (next.lower() in two):
            try:
                i = eval(input(output[0] + "inches: "))
                p =  eval(input(output[1] + "pounds: "))
                a = 703*(p)/(i)**2
                if (a < 18.4):
                    print(output[2], a, output[3] + "underweight. ")
                elif (a > 24.9):
                    print(output[2], a, output[3] + "overweight. ")
                else:
                    print(output[2], a, output[3] + "average weight. ")
            except:
                print(output[4])
    else:
        print("Bye bye!!! And stay POSITIVE!!! ")
        break