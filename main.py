name = input("Enter your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road. It has come to an end, and you can go left or right: ")

if answer == "left":
    answer = input("You come to a river. Do you want to walk around it or swim across the river? ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for miles, ran out of water, and you lost.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly. Do you want to cross the bridge? ")

    if answer == "cross":
        print("You cross the bridge and encounter a troll. Do you want to fight or run?")

        fight_or_run = input("Enter 'fight' or 'run': ")

        if fight_or_run == "fight":
            print("You fought the troll and won! Congratulations, you continue your adventure.")
        elif fight_or_run == "run":
            print("You ran away from the troll, but you tripped and fell. You lose.")
        else:
            print("Not a valid option. You lose.")

    elif answer == "back":
        print("You go back, you lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")


print("You reach a mysterious cave. Do you want to enter the cave or keep going forward?")

cave_or_forward = input("Enter 'cave' or 'forward': ")

if cave_or_forward == "cave":
    print("You enter the cave and find a treasure chest. Congratulations, you win!")
elif cave_or_forward == "forward":
    print("You continue forward and find a group of friendly travelers. They offer you food and water. You continue your journey.")
else:
    print("Not a valid option. You lose.")
