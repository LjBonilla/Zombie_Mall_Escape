#### Choose your own adventure game - First Project
#### Bonilla_09_16_21
###Theme_Zombie_Mall_Escape
print('Welcome to my first game!')
name = input("Hello... im sorry i dont think we've met yet, what is your name? ")
age = int(input("how old are you? "))

health = 15

if age >=18:
    print('Perfect! You are old enough to play! ')

    wants_to_play = input("Would you like to play? ").lower()
    if wants_to_play == "yes":
        print("great! lets play!")
        print("you begin with", health,"health. Good Luck\n"
                                       "")
        print("You begin on the rooftop of a small mall, filled with zombies. Outside the entrance is your truck. Can you make it out alive?"
              "")
        print("you find a large rope coiled on the roof, and also notice a doorway leading to the stairwell")
        rope_or_stairs = input("will you use the rope to rappel down the building, or use the stairwell(rope/stairs)").lower()
        if rope_or_stairs == "stairs":
            print("you grab the rope and then quietly open the door, and slowly make your way down the stairs")
            print("you descend the stairs and find a makeshift barricade blocking the stairs leading past the 3rd floor")
            print("you enter into the mall from the 3f stairwell and cant believe your eyes. There is blood everywhere. \n"
                  "a faint thumping noise can be heard in the distance. you know you need to keep moving")
            left_or_right = input("which way will you explore? (left or right)" ).lower()
            if left_or_right == "right":
                print("the noise sounds like its coming from the left, so you move to the right")
                print("as you head to the right you see an elevator leading to the main floor")
                elevator_or_pass = input("will you take the elevator down to the first floor, or keep moving? (elevator/pass) ").lower()
                if elevator_or_pass == "elevator":
                    print("you board the elevator, hit 1F and ride it down")
                    print("there are 2 zombies a few yards in front of the soon to be opening elevator door")
                    run_or_hide = input("will you run to the exit, or hide in the food court? (run/hide) ").lower()
                    if run_or_hide == "run":
                        print("the door opens, you sprint forward, ducking out of reach and falling in the process. \n"
                              "you bust your knee, but get up, limping, and keep moving. You exit out the front door\n"
                              "and try to run for your truck, but are too slow from your fall")
                        print("your knee gives out just feet from your truck, and before you can reach it, \n"
                              "you feel a cold grip coming from behind you. the zombies caught up, and before you \n"
                              "know it, you are swarmed. you call for help but all it does is attract more zombies")
                        print("you did not survive... Better luck next time!")

                    elif run_or_hide == "hide":
                        print("you quietly exit the elevator and duck behind the fountain to the right")
                        print("your patience pays off as you hear a voice off to the side")
                        print("its another survivor! and they've found a way out through the kitchen in the food court")
                        print("you follow them through the kitchen and exit the mall. You follow them down a \n"
                              "wooded path past the parking lot. You board a large cargo van and see 4 other survivors")
                        print("you breathe a sigh of relief, you're safe... for now")
                        print("congratulations, you have made it out of the mall in one piece!")
                    else:
                        print("you hesitate... the zombies shuffle into the elevator and eat you alive")
                        print("better luck next time...")

                elif elevator_or_pass == "pass":
                    print("you move past the elevator, into a nearby department store to search for a way out"
                          "theres nothing of use in here so you head back to the mall and move forward, you head down"
                          "the escalator, as it appears to be free of any of those monsters. You are now on the 2nd floor")
                    floor1_or_2 = input("will you explore the 2f or continue down the escalator to 1f? (1f/2f) ").lower()
                    if floor1_or_2 == "2f":
                            print("you explore the 2f and find a fire escape leading to the side of the mall. you descend \n"
                              "and carefully make way to your truck. You start it up and drive away, only to find \n"
                              "that whatever is happening isnt contained to the mall.. and this nightmare \n"
                              "has just begun....\n"
                              "Congratulations, you survived... for now!")

                    else:
                        print("you move down to the 1f and see a few zombies by the elevator, so you turn and "
                        "make your way to the hallway leading to the side entrance of the mall. As you approach"
                        "a noise comes from the nearby bathroom. As the door flys open and a mob of zombies pours"
                        "into the hallway, you start running. You burst through the door and with no time to stop"
                        "and think, you quickly take the rope from the roof, tie it from the door handle to a"
                        "nearby bollard. This buys you enough time to make it to your truck.")
                        print("After making it to your truck, you realize your keys must have fell out when scrambling"
                        "to escape the zombies in the hallway")
                        print("Cautiously, you proceed to leave the mall grounds by foot, at which point you see"
                        "the streets are overrun with these creatures and the nightmare has only just begun..")
                        print("congratulations, you have survived...for now")

                else:
                    print("you pass the elevator") ##test****

            else:
                print('you move left, past a barricaded toy store')
                print("as you move past the boarded up doorway, the wooden planks give away and the door bursts open\n"
                    "and you are devoured by the shambling undead")
                health -=15
            if health == 0:
                    print("you satisfy the undeads ravenous hunger... for now...")
                    print("you did not survive. Better luck next time..")

        else:
            print("you tie the rope and begin to rappel down the building. you can see your truck, youll be out of here before you know it!")
            print("*SNAP*")
            print("your rope tears, luckily, you were almost at the bottom so you only twist your ankle \n "
                  "not so luckily...the zombies heard everything. \n "
                  "you become zombie chow")
            health -= 15
            if health == 0:
                print("your health has reached" , health , ",you did not survive.. better luck next time!")
    else:
        print("ok then... goodbye")


else:
    print("im sorry, you're not quite old enough, please return when you're older. ")




