def bridge():
    print("You are pushed off of a bridge, what do you do?")
    print("1 is Yes and 2 is No")
    print("Beware! You can only choose Yes for one, so be careful!!!")

    a = eval(input("You decide to pretend you're bungey jumping "))
    b = eval(input("You pretend you can swim mid air like an Air Fish "))
    c = eval(input("You accept your death in tears "))

    if a == 1:
        print("Wow you're definently either stupid or brave. Either way you still die")
    if a == 2:
        print("Good choice!")
    if b == 1:
        print("YOU ARE NOT AN AIR FISH DUMMY!!! You die")
    if b == 2:
        print("Good job!")
    if c == 1:
        print("God takes pity upon you and admires your honesty in the face of death. He saves you! Now you really can fly!!! Good choice")
    if c == 2:
        print("So close! But not close enough!")

bridge()
