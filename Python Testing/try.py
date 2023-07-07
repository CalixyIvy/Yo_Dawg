type_of_fruit = input("Welcome to THE GAME! Would you like to play? ")

answer = ["yes","no"]

if (type_of_fruit.lower() == "yes"):
    begin = input("Good now let's begin! Today your grandmother askes you if you'd like to go outside. Do you? ")

    if (begin.lower() == "yes"):
        outside = input("Your grandmother, 'Thank Goodness! You were starting to worry your dear old Granny...but before you go would you like some lunch to take with you?' ")

        if (outside.lower() == "no"):
            no_lunch = input("Your grandmother seems disappointed and bids you farwell as she feels as though she has been disrespected and unloved, but you leave without a care. You continue outide to see sunny skies! Do you go to the forest, the town, or the beach? ")

            if (no_lunch.lower() == "forest"):
                print("You go forward into the forest. Once you enter it seems as though day has simultaneously turned to night. It is silent and pitch black. You feel as though something is watching you, but you continue forward anyways. A purple slime jumps out of the trees at you. You are on your last breaths as you murmur, 'If only I had something good to eat.' You Died! ")
                
                #END
                
            elif (no_lunch.lower() == "town"):
                no_town = input("You turn to the right and enter the town. It's a lovely town by the ocean. The sun is shining, the flowers are blooming, and on days like these kids like you...GRAB ICECREAM. I SCREAM, YOU SCREAM, WE ALL SCREAM FOR ICECREAM!!! Do you get chocolate, vanilla, or strawberry? ")

                if (no_town.lower() == "chocolate"):
                    print("Unfortunately, you forgot that you have an allergy to chocolate. You proceed to have an allergic reaction, and right before you die all you can think is, 'If only I had taken my handy dandy lunchbox. Grandmother always packs an epipen just in case...' You Died! ")

                    #END
                    
                elif(no_town.lower() == "vanilla"):
                    vanilla = print("Even though it's basic and a common choice, it's a basic and common choice for a reason! You try to enjoy your ice cream, but it's such a common choice that some punk kid steals it for you and with no regard to your salivac claim to the icecream the kid eats it all. You Died...of an empty stomach. ")

                    #END
                    
                elif(no_town.lower() == "strawberry"):
                    strawberry = input("THE BEST CHOICE!!! The creamy texture perfectly compliments the naturally sweet and fruity flavor of your treat. You devour it! Do you now go shopping? ")

                    if (strawberry.lower() == "yes"):
                        no_money = input("Unfortunately, you are now broke so you can't go buy anything at the moment. There is nothing else of interest to you in town, so you leave. Where would you like to go next? The forest or the beach? ")
                        
                        if (no_money.lower() == "forest"):
                            lets_forest = input("You decide to go to the forest in front of your house. Once you enter the darkness consumes you, but you keep walking. You walk and walk and walk until you stumble uon a bit of light and some ruins. Do you explore the ruins? ")
                        
                        elif (no_money.lower() == "beach"):
                            lets_beach = input("You walk through the town and are about to reach the beach when you run into your best friend since Pre-K. She tries to talk to you. Do you RUN away or STAY? ")
                            
                            

                    elif (strawberry.lower() == "no"):
                        no_money = input("Good thing! Because you have no money left and are officially broke. There is nothing else of interest to you in town, so you leave. Where would you like to go next? The forest or the beach? ")

                        if (no_money.lower() == "forest"):
                            no_lets_forest = input("You decide to go to the forest in front of your house. Once you enter the darkness consumes you, but you keep walking. You walk and walk and walk until you stumble uon a bit of light and some ruins. Do you explore the ruins? ")
                            
                            
                        
                        elif (no_money.lower() == "beach"):
                            no_lets_beach = input("Luckily you didn't spend your time trying to shop even though you are broke, so there is a clear and easy path you take to the beach because people are distracted by street performers right now. You make it to the beach, but it seems as though it's about to storm as tides pick up and clouds begin to roll in. Do you go in the OCEAN or go HOME? ")




            elif (no_lunch.lower() == "beach"):
                no_beach = input("You take the right path that leads you through the town to the beach. It's bright and sunny. A perfect day to for the beach. What do you do? Do you go SWIMMING, get a TAN, or collect SEASHELLS? ")

                if (no_beach.lower() == "swimming"):
                    swim = print("You decide to take a dip in the ocean, but it's just your luck because you get caught in a riptide! You were never taught how to escape one, so no matter how hard you try you can't escape the ocean's clutches. You drown to death wishing you brought your handy dandy lunchbox to float on. You Died. ")

                            #END
                            
                elif(no_beach.lower() == "tan"):
                    tan = input("You lay out in the sand, but having forgotten a towel you get a funky tan. The tan is so funky that when you best friend since Pre-K walks up to you at the beach and they can't help but laugh at you. You are so insecure now that you run home not thinking because you just want to hide from everyone. When you return home you realize no one is there to greet you. 'Where's Grandmother?' you think to yourself. She is nowhere to be found. Do you go search for her? ")

                    if (tan.lower() == "yes"):
                        print("N/A")

                    elif(tan.lower() == "no"):
                        print("N/A")

                elif (no_beach.lower() == "seashells"):
                    seashells = input("You go walking along the shore line collecting seashells. Then you find a HUGE, PERFECT seashell and you pick it up. Off in the distance you then hear, 'HEY! THAT'S MY SEASHELL!!!' A young woman with fish tail swims up to you. 'GIVE THAT BACK!!!' she screeches. Do you give it back? ")

                    if (seashells.lower() == "yes"):
                        uh = input("'Oh! Thank you!' she says. You made a mermaid friend and she gives you a seashell. You are done at the beach and a storm seems to be rolling in, so you head home. No one is home when you get there. Your grandmother is nowhere to be found. Do you go find her? ")

                    elif (seashells.lower() == "no"):
                        print("'ARE YOU SERIOUS RIGHT NOW!?!?' she screams. She then drags you into the ocean and you drown with your corpse never being found. You Died! ")
                        
                        #END
                        
        elif (outside.lower() == "yes"):
            lunch = input("Your grandmother seems happy that you took your lunch. You now say goodbye to grandmother and give her a hug like it's your last. Then you venture outside to join the rest of the world. Do you go to the forest, the town, or the beach? ")

            if (lunch.lower() == "forest"):
                forest = input("You go forward with your handy dandy lunchbox towards the forest. Once you enter the bewitching forest it's as if day has turned to night. You hear rustiling in a tree ahead of you, and through the pitch black leaves a purple slime jumps out and attacks you. Luckily, you have grandmother's lunch and gain 5 HP. Additionally, you use your handy dandy lunchbox to defend yourself and kill the slime. Do you take the slime's drops? ")

            elif (lunch.lower() == "town"):
                town = input("You with your handy dandy lunchbox in hand turn right and enter the town. The town is bustling with life and people because it's finally warming up enough to go to the beach, and since the town is overlooking the ocean's shore everybody comes to visit this time of year. Look Over There! It's your best friend since Pre-K. Do you go greet her? ")

            elif (lunch.lower() == "beach"):
                beach = input("You and your handy dandy lunchbox turn right and walk through the town to the beach! You love the beach and it is the perfect day to explore. You have arrived at the beach and lay down your towel in the sand. Then you get out your lunch from grnadmother. OH NO!!! A group of seagulls begin to attack you! You lose your lunch, but the birds dropped some feathers. Do you take the feathers? ")
                

    elif (begin.lower() == "no"):
        inside = input("Your grandmother is disappointed, but doesn't push you to go outside, so for the rest of your days you are locked in your room with nothing to do. The isolation infects your mind and you begin to see scary figures lingering in the four corners of your room. Do you stay inside? ")

        if (inside.lower() == "no"):
            alone = input("Your grandmother isn't anywhere to be found when you exit your room. Do you find her? ")

            if (alone.lower() == "no"):
                nah = input("' She'll be fine! I mean she's a grown woman!' you think to yourself. You exit the house and it's storming. Do you grab your umbrella? ")

                if (nah.lower() == "no"):
                    print("You aren't afraid of no rain! So, you venture outside and it's a clear field. You get struck by lightning five times in a row! Just your luck! Should have been safe instead of sorry. You Died. ")

                    #END
                    
                elif(nah.lower() == "yes"):
                    umbrella = input("You grab your colorful umbrella and go outside. 'Was it worth it?' Your hear a voice coming from behind you. You turn around to find someone standing in a dark shadow. Do you come closer? ")
                    
                    if (umbrella.lower() == "no"):
                        RUN = input("'WHAT IS THAT!?!' you think. 'I don't want to die!' you accidentally scream aloud as you turn around and run. You run yourself all the way into the forest where it is pitch black. Luckily for you nothing jumps out at you in the darkness, because all of the monsters are hiding from the rain. You then stumble upon a light spot with some ruins at the center of it. Do you explore the ruins? ")
                        
                        if (RUN.lower() == "yes"):
                            print("It seems as though your luck has run out. The storm is making the ruins around you crumble because of how old they are. You get stuck under a fallen ruin boulder due to the storm. You Died. ")
                            
                            #END
                        elif (RUN.lower() == "no"):
                            im_good = input("You decide that you're good and don't need to be a dangerous archeaologist today. Plus, you decide that you miss grandmother and have a mission! You must find grandmother! You exit the forest and feel drawn to take the left path do you? ")
                            
                            if (im_good() =="yes"):
                                print("You decide to go with your hunch and go down the left path. The rain stops and you see a figure off in the distance. You continue to get closer and realize it's grandmother...but you're too late. Her dead and lifeless body is leaned up against a lone tree in a clear ands sunny and green field. You think, 'It's unfair that there is all of this life and cheer surrounding Grandmother when she is dead. It's just so unfair that she died.' You don't know who killed her but you want revenge. You storm into town and one by one take the life of everyone who once lived there. The only person you nvever killed was your best friend because you knew that they could have never killed grandmother. The two of you live the rest of eternity together F O R E V E R! The End... ")
                                
                                #END
                            elif (im_good() == "no"):
                                print("The storm begins to clear and right before you finally decide where to look for grandmother, a purple slime sneaks up from behind you and kills you. You Died. ")
                                
                                #END
                                
                    elif (umbrella.lower() == "yes"):
                        friend = input("You get closer to the figure standing in the shadows. It's your best friend since Pre-K. 'Do you even remember my name?' they say. You can't seem to remember their name for some reason. They are stricken with sadness at your silence. Do you comfort them? ")
                        
                        if (friend.lower() == "no"):
                            comfort = input("You don't care enough to help. You haven't talked to them in a while so why would you? You're about to walk away when they ask, 'Where's Granmother?' You explain how she is missing then walk towards the town to go find her. They seem to keep walking in the same direction. Do you try to lose them? ")
                            
                            if (comfort.lower() == "yes"):
                                you = input("You can't seem to lose them. Either way they are joining you. You are their best friend and your grandmother was always like their own. So, they won't stop trying to 'help.' You get to town and the rain is picking up but you keep searching. You're tired. You want to go home. You're hungry. Your 'friend' can tell so you two take a break in a restuarant noutorious for lovebirds. It is a candle lit dinner and after a few bites of food and a bit of conversation with your friend you can't help but feel a sort of affection for them stronger than before. You don't know if it's the atmosphere or their eyes, but for some reason they look really good even though their soaking wet and muddy. Do you continue this date? ")

                                if (you.lower() == "yes"):
                                    print("You can't help but fall in love. The date continues without a hitch. You don't even remember what you were doing in this storm in the first place. All you can think about is your friend. You two go home together and you confess to them. Over time you live your lives together F O R E V E R ! One day you find a letter you think you wrote but you don't remember when. It's written to someone named grandmother. 'Who's Grandmother anyway?!' you think to yourself. You brush it off and throw the letter away. You continue to live forever with your wife. The End... ")
                                    
                                    #END
                                    
                                elif (you.lower() == "no"):
                                    naaah = input("You run out of the restuarant and don't stop running. Your 'friend' can't catch up to you. You are at a crossroads, but you remember the feeling you had earlier. Do you go to the forest, the beach or left?  ")
                                    
                                    if (naaah.lower() == "forest"):
                                        print("Your friend is waiting at the entrance to the forest. 'I guess this was never going to work out for me huh?' they mumble almost directed towards themself. They then pull out a knife and stab you repeatedly, they never stop... You Died. ")
                                        
                                        #END
                                        
                                    elif(naaah.lower() == "beach"):
                                        print("You turn around to go to the beach only to find your friend is waiting at the entrance of the beach. 'I guess this was never going to work out for me huh?' they mumble almost directed towards themself. They then pull out a knife and stab you repeatedly, they never stop... You Died.")
                                        
                                        #END
                                        
                                    elif(naaah.lower() == "left"):
                                        print("You find yourself pulled towards the left path almost as if it's meant to be. As you walk on for miles the rain starts to clear. You are in the middle of a clear green field with luscious grass and burning rays of sunshine and happiness. You stumble upon a lone tree in the middle of the field. The closer you get the more you realize. 'IT'S GRANDMOTHER!' you think to yourself, but grandmother is dead. She is pearched against this thriving tree just dead...murdered. You think, 'It's unfair how all of this life gets to thrive and be happy, but grandmother id dead!' You are filled with regret and driven insane. You make a vow to kill EVERYONE that could have possibly killed granmother and you do. You Die...alone...forever.  ")

                                        #END
                                    
                            elif (comfort.lower() == "no"):
                                follower = input("Either way they are joining you. You are their best friend and your grandmother was always like their own. So, they won't stop trying to 'help.' You get to town and the rain is picking up but you keep searching. You're tired. You want to go home. You're hungry. Your 'friend' can tell so you two take a break in a restuarant noutorious for lovebirds. It is a candle lit dinner and after a few bites of food and a bit of conversation with your friend you can't help but feel a sort of affection for them stronger than before. You don't know if it's the atmosphere or their eyes, but for some reason they look really good even though their soaking wet and muddy. Do you continue this date? ")
                                
                                if (follower.lower() == "yes"):
                                    print("You can't help but fall in love. The date continues without a hitch. You don't even remember what you were doing in this storm in the first place. All you can think about is your friend. You two go home together and you confess to them. Over time you live your lives together F O R E V E R ! One day you find a letter you think you wrote but you don't remember when. It's written to someone named grandmother. 'Who's Grandmother anyway?!' you think to yourself. You brush it off and throw the letter away. You continue to live forever with your wife. The End... ")
                                    
                                    #END
                                    
                                elif (follower.lower() == "no"):
                                    input("You run away")
                                    
                        elif (friend.lower() == "yes"):
                            best = input("You go over to comfort them. You don't know why you don't remember their name, but you take responsibility for it. Your friend forgives you because you've been best friends after all of this time haven't you and they remind you of their name. After that incident they ask where your grandmother is and can see your worry. Do you invite them on your adventure? ")
                            
                            if (best.lower() == "yes" or "no"):
                                dont = input("Either way they are joining you. You are their best friend and your grandmother was always like their own. Together you think of all of the places grandmother might be, but can't think of any until your friend suggests the town but you can't help but look left. Do you go to the TOWN or LEFT?  ")
                                
                                if (dont.lower() == "town" or "left"):
                                    work = input("Before you can answer your friend is already dragging you away to the town. You get to town and the rain is picking up but you keep searching. You're tired. You want to go home. You're hungry. Your friend can tell so you two take a break in a restuarant noutorious for lovebirds. It is a candle lit dinner and after a few bites of food and a bit of conversation with your friend you can't help but feel a sort of affection for them stronger than before. You don't know if it's the atmosphere or their eyes, but for some reason they look really good even though their soaking wet and muddy. Do you continue this date? ")
                                    
                                    if (work.lower == "yes" or "love"):
                                        print("You can't help but fall in love. The date continues without a hitch. You don't even remember what you were doing in this storm in the first place. All you can think about is your friend. You two go home together and you confess to them. Over time you live your lives together F O R E V E R ! One day you find a letter you think you wrote but you don't remember when. It's written to someone named grandmother. 'Who's Grandmother anyway?!' you think to yourself. You brush it off and throw the letter away. You continue to live forever with your wife. The End... ")
                                        
                                        #END
                                        
            elif (alone.lower() == "yes"):
                grandma = input("'Oh No!!! Where's Grandmother!' you think to yourself. You never even said 'I love you,' to her. You leave your home. Where do you look for grandmother? Do you go to the forest, the town, or the beach? ")

        elif (inside.lower() == "yes"):
            print("You let the figures absorb you as they creep towards you. You sink into despiar. 'Nobody loves me. Nobody wants me. Nobody likes me,' are thoughts that repeat in your mind and consume you whole. You Died...alone. ")
            
            #END

elif (type_of_fruit.lower() == "no"):
    print("Then why are you even here???")
    
    #END

else:
    print("Let's try that again Alec", answer)
    
    #END
    
    # pip install graphics.py
    #Make a name thing and make the name of the player the name of the best friend