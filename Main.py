#Game started 27/12/2020 by Paddy.
name = input("What's your name?\n")

answer1 = input("Well, hello %s. Would you like to go on an adventure?\n" % name)


if answer1 == "yes" or answer1 == "Yes" or answer1 == "YES" or answer1 == "y" or answer1 == "Y":
    print("\nGreat!")
else:
    print("\nSorry but that was a trick question. You're about to go on an adventure whether you like it or not.")


#start of the story
answer2 = input("Would you like to save a village or slay a dragon?\n")
#Save the village path
if answer2 == "save a village" or answer2 == "SAVE A VILLAGE" or answer2 == "Save a village" or answer2 == "Save a Village" or answer2 == "Save A Village" or answer2 == "village" or answer2 == "save village":
    print("\nYou chose to save a village from evil. A choice not many decide to take. Let's start traveling my friend.")


    answer3 = input("You are on your way to the village when 3 goblins appear on the path ahead of you. Do you fight or try to outrun them?\n")

    if answer3 == "fight" or answer3 == "Fight" or answer3 == "FIGHT" or answer3 == "fight them" or answer3 == "Fight them":
        print("\nYou killed them off but now your leg in injured. You will need to find medication quickly.")
   
        
        answer4 = input("As you slowly go further down the path you see what looks like an abandoned town. It looks like there was a fight. Do you search the town for shelter or carry on?\n")

        if answer4 == "search town" or answer4 == "Search town" or answer4 == "Search Town" or answer4 == "SEARCH TOWN" or answer4 == "search the town" or answer4 == "Search the town" or answer4 == "search the town for shelter":
            print("\nYou search the town and find it completely empty. You find some medicine for your leg and it should heal soon. You also find a mostly intact small house to spend the night in.")

        elif answer4 == "carry on" or answer4 == "Carry on" or answer4 == "CARRY ON" or answer4 == "Carry On" or answer4 == "Keep going" or answer4 == "KEEP GOING":
            print("\nYou decide to carry on down the road. Night falls and you have no shelter and can hardly move because of your leg. A pack of wolves comes and there is nothing you can do. You get eaten alive. YOU DIED")

        else:
            print("That is an invalid answer. Please try again.\n")

    elif answer3 == "outrun them" or answer3 == "OUTRUN THEM" or answer3 == "Outrun them" or answer3 == "outrun" or answer3 == "Outrun" or answer3 == "Outrun Them":
        print("\nYou managed to get away but in the process you lost some of the food in your bag. You will need to find more food soon.")


        answer4 = input("You see a small hut at the edge of a forest. Do you knock on the door or try to set up camp in a field?\n")

        if answer4 == "Knock on the door" or answer4 == "KNOCK ON THE DOOR" or answer4 == "Go to the hut" or answer4 == "knock on the door" or answer4 == "GO TO THE HUT":
            print("\nYou walk to the hut on the edge of the forest. There is an old man in there. When you knock on the door he welcomes you and says that if you help him move some wood he will give you a place to stay and wood for the night.")

        elif answer4 == "set up camp" or answer4 == "set up camp in a field" or answer4 == "SET UP CAMP" or answer4 == "Set up camp" or answer4 == "set up cam in the field":
            print("\nYou set up a small tent in a field but have limited shelter and food. During the night a bear breaks through the tent easily. It eats you alive. YOU DIED")

        else:
            print("That is an invalid answer. Please try again.\n")

    else:
        print("That is an invalid answer. Please try again.\n")


#Slay the dragon path
elif answer2 == "slay a dragon" or answer2 == "SAVE A VILLAGE" or answer2 == "Slay a dragon" or answer2 == "Slay a Dragon" or answer2 == "Slay A Dragon" or answer2 == "dragon" or answer2 == "slay dragon":
    print("\nSo you have chosen the mighty dragon. A choice not many decide to take. Let's start traveling my friend.")


    answer3 = input("You are on your way to the dragons lair when you a patch of berries. Do you try and pick them or carry on?\n")

    if answer3 == "pick berries" or answer3 == "Pick the berries" or answer3 == "pick them" or answer3 == "PICK BERRIES" or answer3 == "berries" or answer3 == "Berries":
        print("\nYou went to the berry patch but a farmer sees you. He looks andgry and is getting out his shotgun.")


        answer4 = input("Do you try to fight or hide somewhere?\n")

        if answer4 == "fight" or answer4 == "FIGHT" or answer4 == "Fight" or answer4  =="try to fight" or answer4 == "fight the farmer":
            print("\nYou decide to fight the farmer. Luckily he was just threatening you with the gun as he doesnt have any ammunition left. You easily take him down so now you have food and shelter for the night.")

        elif answer4 == "hide" or answer4 == "HIDE" or answer4 == "Hide" or answer4 == "hide somewhere" or answer4 == "Hide somewhere":
            print("\nYou find a tree to hide in. The farmer looks around a bit but can't seem to find you. You are safe but it is getting dark and you have little food left.")

        else:
            print("That is an invalid answer. Please try again\n")

    elif answer3 == "carry on" or answer3 == "CARRY ON" or answer3 == "Carry on" or answer3 == "Carry On" or answer3 == "keep going":
        print("\nYou keep moving down the road. You need to find another food source soon otherwise you will starve.")


        answer4 = input("You have little food left now and it is getting dark. You see an old lady with a bag of apples. Do you steal the apples or leave her alone?\n")

        if answer4 == "steal"  or answer4 == "steal the apples" or answer4 == "Steal" or answer4 == "STEAL" or answer4 == "Steal the apples" or answer4 == "STEAL THE APPLES":
            print("\nYou try to snatch the apples out of the old lady's grasp but she is actually a Russian spy in disguise and does some advanced Tai Chi to defeat you. YOU DIED.")


        elif answer4 == "leave her alone" or answer4 == "LEAVE HER ALONE" or answer4 == "Leave her alone" or answer4 == "leave her" or answer4 == "Leave her":
            print("\nYou have no food left now and it is getting dark. You search and find a patch of carrots. In your hunger you pull one out and eat it without noticing the 'Poison Do Not Eat' sign. YOU DIED")

        else:
            print("THat is an incalid answer. Please try again.\n")

    else:
        print("That is an invalid answer. Please try again.\n")

else:
    print ("That is an incalid answer. Please try again.\n")
