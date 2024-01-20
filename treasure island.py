print("Welcome tol Tresure Island.")
print("Your mission is to find treasure.")
way = input("You're at a cross road. where do you want to go ? Type left or right ")
if way == "right":
    print(input("You come to lake. there is an island in the middle of the lake.type wait to wait for boat . type swim to swim across."))
    door=input("You arrive at the islandun harmed. there is a house with 3 doors.one red, one yellow and one blue. which colour you choose? ")
    if door=="red":
        print("you enter a room of tresure . you win,GAME OVER.")
    elif door=="yellow":
        print("you enter a room of beast. GAME OVER")
    elif door=="blue":
        print("you enter in other UNIVERSE. you can live here with magic powers.GAME STARTED")
    else:
        print("game over")
else:
    print("you came to the city ,GAME OVER")
