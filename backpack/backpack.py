# getting informaton about the players
# storing the information about the players
players = []
for i in range(2):
    players.append({
        "name": "",
        "score": 0,
        "backpack": []
    })

    players[i]["name"] = input("Enter name for player " + str(i + 1) + ": ")
    print("Enter four (4) items to put into your backpack.")
    for j in range(4):
        backpack_item = input("Item name: ")
        players[i]["backpack"].append(backpack_item)
    print(players[i]["backpack"])

game_on = True
while game_on:
    for i in range(2):
        player_choice = input(players[i]["name"] + ", guess an item from the other backpack: ")
        other_player = players[(i+1) % 2]
        if player_choice in other_player["backpack"]:
            print("You guessed an item from the backpack!")
            players[i]["score"] += 1
        else:
            print("You did not guess an item from the backpack.")

        play_again = input("Do you want to play again? Type YES or NO: ")
        if (play_again == "NO"):
            game_on = False

for player in players:
    print(player["name"] + " score: " + str(player["score"]))