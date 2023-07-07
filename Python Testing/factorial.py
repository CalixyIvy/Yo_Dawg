#Program to compute the factorial of a number
#Illustrates for loop with an acculmulator

def main():
    n = eval(input("Please enter a whole number: "))
    fact = 1

    for factor in range (n,1,-1):
        fact = fact * factor
        print("fact: ", fact)
    
    print("The factorial of", n, "is", fact)

main()