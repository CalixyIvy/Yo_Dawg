def gamer():
    print("You enter a Haunted House, what do you do?")
    print("1 is for Yes and 2 is for No")

    a = eval(input("Do you leave the house? "))

    if a == 1:
        b= eval(input("You fall through a trapdoor on your way out and break your legs. Do you crawl your way forward? "))
       
        if b == 2:
            print("You wait for hours that turn to days that turn to weeks until you die in misery. You Die! Boo!!! Try Again! ")
       
        elif b == 1:
            c = eval(input("You hear spooky noises and load screeches further down the path. Do you go forward? "))
        
            if c == 1:
                print("Turns out that the scary noises was just a lonely kitten. The kitten leads you to the exit where you find a friend of yours who takes you to the hospital. You Survive! HooRah!!! Try for a new ending!")

            elif c == 2:
                print("The tunnel caves in on itself and you get buried alive. You Die! Boo!!! Try Again! ")
   
    elif a == 2:
        d = eval(input("Wow you're an adventurous one! Do you go find the voice? "))

        if d == 1:
            print("You follow the voice to find the owner of the house, and they give you a HOUSE TOUR!!! Afterwards you and your new friend part ways, but you frequently come back to visit. You Survived! HooRah!!! Try for a new ending! ")

        elif d == 2:
            e = eval(input("You go in the opposite direction of the voice because you are a scaredy cat. You now are in front of some stairs. Do you go up? "))

            if e == 1:
                print("The stairs can't hold your weight and break under pressure. You Die! Boo!!! Try Again! ")

            elif e == 2:
                print("You turn around to find a stained glass window and escape out of it. You Survived! HooRah!!! Try for a new ending!")

    while(True):
        print("Answer Now You Plebian!!!")
        
        a = eval(input("Do you leave the house? "))

        if a == 1:
            b= eval(input("Unfortunately for you it is too late to exit because the door is aleady locked. There is a hallway full of cobwebs ahead of you. Do you move forward? "))
        
            if b == 2:
                print("You are too much of a wimp to move on and a poltergiest appears. It kills you in one shot! You Died! Boo!!! ")
                break
        
            elif b == 1:
                c = eval(input("Momma didn't raise no wimp! You move forward and stumble into a wall, and you accidentally open a passage way that wasn't there before. Do you dare to enter? "))
                
                if c == 2:
                    print("You know the saying 'Curiousity killed the cat'? Well it was a lie. Instead you get caught by a resident of the house and the are afraid of humans, so they accidentally kill you. You Died! Boo!!! ")
                    break
            
                elif c == 1:
                    f = eval(input("The passage way leads you to a mystical looking library and there is a living skeleton inside. Do you talk to it? "))

                    if f == 2:
                        print("While trying to sneak your way away from the skeleton you run into a candle and catch yourself on fire. You Died! Boo!!! ")
                        break

                    elif f == 1:
                        h = eval(input("You find out that the skeleton is the keeper of this magic library! You and your new friend tell each other interesting stories from your lives. They want to see the outside world again. Do you help their dream come true? "))

                        if h == 1:
                            print("You find a way out of the haunted house together. Once your friend exits the house a blue orb floats freely away up into the sky from their now limp corpse. Good job! Not only did you save yourself, you saved your friend!!! *Best Ending* ")
                            break

                        elif h == 2:
                            print("You make your one and only friend cry and they leave you alone forever. You die of a broken heart. You Died! Boo!!! ")
                            break


        elif a == 2:
            d = eval(input("I don't know if you are brave or stupid, but I like it. A key falls right into your opened hand. Do you use it on the only other door in the room? "))

            if d == 2:
                print("You instead use it on the front door. It opens and you run out of it, but you fall down because a trap door has opened under you. Turns out you weren't as brave as I thought, and you land on your head. You Died! Boo!!!  ")
                break

            elif d == 1:
                e = eval(input("Behind the door you find a dog and a cat. They both walk up to you and follow you everywhere you go. You also find a way out of the house, but you can only take one animal with you. Do you take the dog? "))

                if e == 1:
                    print("Turns out the dog was a hell hound and it kills you when you are finally alone. You Died! Boo!!! ")
                    break

                elif e == 2:
                    print("The cat is clever and leads you to a secret exit where you can take both animals. You now have escaped with two new best friends! Congrats!!! ")
                    break
gamer()
#.lower is OP
#If you just name things stuff you'll be okay!!!
#Then you can make a loop without while()
#Ooga Booga
#tired
#Common Link Integration Processing