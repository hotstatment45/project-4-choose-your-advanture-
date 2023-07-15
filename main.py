
name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. which way would you like to go? ").lower()



if answer == "left":
    answer = input(" You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross?")

    if answer == "swim":
        print("YOu swim accross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, rand out of water and you lost the game.")
    else:
        print("not a valid option . you lose.")




elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back)")

    if answer == "back":
        print("you go back and lose.")

    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/NO) ?? ")

        if answer == "yes":
            print("You talk to the stranger and they give you gold and you win!")
        elif answer == "no":
            print("You ignored the stranger and they are offended and you lose!.")
        else:
            print("Not a valid option. YOu lose.")

    else:
        print("not a valid option . you lose.")


else:
    print("not a valid option . you lose.")


print("Thankyou for typing, them!")


