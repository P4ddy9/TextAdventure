#Game started 27/12/2020 by Paddy.
name = input("What's your name?\n")

answer1 = input("Well, hello %s. Would you like to go on an adventure?\n" % name)


if "y" in answer1.lower():
    print("\nGreat!")
else:
    print("\nSorry but that was a trick question. You're about to go on an adventure whether you like it or not.")


#start of the story
answer2 = input("Would you like to save a village or slay a dragon?\n").lower()

possibleAnswersVillage = ["village","save"]
possibleAnswersDragon = ["slay","dragon"]
#Save the village path
if answer2 in possibleAnswersVillage:
    print("\nYou chose to save a village from evil. A choice not many decide to take. Let's start traveling my friend.")


    answer3 = input("You are on your way to the village when 3 goblins appear on the path ahead of you. Do you fight or try to outrun them?\n")
    answer3 = answer3.lower()

    possibleAnswersFightGoblin = ["fight"]
    possibleAnswersOutrun = ["outrun","run"]

    if answer3 in possibleAnswersFightGoblin:
        print("\nYou killed them off but now your leg in injured. You will need to find medication quickly.")
   
        
        answer4 = input("As you slowly go further down the path you see what looks like an abandoned town. It looks like there was a fight. Do you search the town for shelter or carry on?\n")
        answer4 = answer4.lower()
        
        possibleAnswersSearchTown = ["search","town","search the town"]
        possibleAnswersKeepGoing = ["carry","keep","on","go"]


        if answer4 in possibleAnswersSearchTown:
            print("\nYou search the town and find it completely empty. You find some medicine for your leg and it should heal soon. You also find a mostly intact small house to spend the night in.")


            answer5 = input("You are almost at the village when a mysterious trader walks up to you. He says that he will read your future if you tell him your deepest secret. Do you tell him a secrect or continue towards the village?\n")
            answer5 = answer5.lower

            possibleAnswersTellSecrect = ["tell him secrect","secrect","tell him your deepest secrect"]
            possibleAnswersContinueToVillage = ["continue towards the village","village","continue"]


            if answer5 in possibleAnswersTellSecrect:
                print("\nHe welcomes you into his small hut.")
                reply = input("What is your answer?\n")
                   
                #print("\nThe shaman sees the truth in your answer and begins to tell you your future. He tells you that he sees you remaining calm in a situation where you feel your chest is empty. Only by staying calm do you manage to free yourself.")
                #print(reply)



            elif answer5 in possibleAnswersContinueToVillage:
                print("\nYou arrive in the village and see people screaming in terror as what looks like strange whisps of dust like smoke slide acroos the ground towards them. When one catches up to a villager it slowly moves up their body before sorrounding their head and suffocating them.")


        elif answer4 in possibleAnswersKeepGoing:
            print("\nYou decide to carry on down the road. Night falls and you have no shelter and can hardly move because of your leg. A pack of wolves comes and there is nothing you can do. You get eaten alive. YOU DIED")

        else:
            print("That is an invalid answer. Please try again.\n")

    elif answer3 in possibleAnswersOutrun:
        print("\nYou managed to get away but in the process you lost some of the food in your bag. You will need to find more food soon.")


        answer4 = input("You see a small hut at the edge of a forest. Do you knock on the door or try to set up camp in a field?\n")
        answer4 = answer4.lower()

        possibleAnswersHut = ['door','hut','knock']
        possibleAnswersCamp = ['camp','field','set up']

        if answer4 in possibleAnswersHut:
            print("\nYou walk to the hut on the edge of the forest. There is an old man in there. When you knock on the door he welcomes you and says that if you help him move some wood he will give you a place to stay and wood for the night.")



#answer5 = input("You")


        elif answer4 in possibleAnswersCamp:
            print("\nYou set up a small tent in a field but have limited shelter and food. During the night a bear breaks through the tent easily. It eats you alive. YOU DIED")

        else:
            print("That is an invalid answer. Please try again.\n")

    else:
        print("That is an invalid answer. Please try again.\n")


#Slay the dragon path
elif answer2 in possibleAnswersDragon:
    print("\nSo you have chosen the mighty dragon. A choice not many decide to take. Let's start traveling my friend.")


    answer3 = input("You are on your way to the dragons lair when you come across a patch of berries. Do you try and pick them or carry on?\n")
    answer3 = answer3.lower()

    possibleAnswersPickBerries = ["pick","berries","berry"]
    possibleAnswersCarryOn = ["carry","on","keep"]

    if answer3 in possibleAnswersPickBerries:
        print("\nYou went to the berry patch but a farmer sees you. He looks andgry and is getting out his shotgun.")


        answer4 = input("Do you try to fight or hide somewhere?\n")
        answer4 = answer4.lower()

        possibleAnswersTryToFight = ["fight"]
        possibleAnswersHide = ["hide"]

        if answer4 in possibleAnswersTryToFight:
            print("\nYou decide to fight the farmer. Luckily he was just threatening you with the gun as he doesnt have any ammunition left. You easily take him down so now you have food and shelter for the night.")

        elif answer4 in possibleAnswersHide:
            print("\nYou find a tree to hide in. The farmer looks around a bit but can't seem to find you. You are safe but it is getting dark and you have little food left.")

        else:
            print("That is an invalid answer. Please try again\n")

    elif answer3 in possibleAnswersCarryOn:
        print("\nYou keep moving down the road. You need to find another food source soon otherwise you will starve.")


        answer4 = input("You have little food left now and it is getting dark. You see an old lady with a bag of apples. Do you steal the apples or leave her alone?\n")
        answer4 = answer4.lower

        possibleAnswersStealApples = ["steal","apples"]
        possibleAnswersLeaveHer = ["leave","her"]

        if answer4 in possibleAnswersStealApples:
            print("\nYou try to snatch the apples out of the old lady's grasp but she is actually a Russian spy in disguise and does some advanced Tai Chi to defeat you. YOU DIED.")


        elif answer4 in possibleAnswersLeaveHer:
            print("\nYou have no food left now and it is getting dark. You search and find a patch of carrots. In your hunger you pull one out and eat it without noticing the 'Poison Do Not Eat' sign. YOU DIED")

        else:
            print("THat is an incalid answer. Please try again.\n")

    else:
        print("That is an invalid answer. Please try again.\n")

else:
    print ("That is an incalid answer. Please try again.\n")
