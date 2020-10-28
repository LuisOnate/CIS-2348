# Luis Onate
# 1596900

# Request user input for for player 1 jersey number and player rating
player1_jersey = int(input("Enter player 1's jersey number:\n"))
player1_rating = int(input("Enter player 1's rating:\n"))
print()

# Request user input for for player 2 jersey number and player rating
player2_jersey = int(input("Enter player 2's jersey number:\n"))
player2_rating = int(input("Enter player 2's rating:\n"))
print()

# Request user input for for player 3 jersey number and player rating
player3_jersey = int(input("Enter player 3's jersey number:\n"))
player3_rating = int(input("Enter player 3's rating:\n"))
print()

# Request user input for for player 4 jersey number and player rating
player4_jersey = int(input("Enter player 4's jersey number:\n"))
player4_rating = int(input("Enter player 4's rating:\n"))
print()

# Request user input for for player 5 jersey number and player rating
player5_jersey = int(input("Enter player 5's jersey number:\n"))
player5_rating = int(input("Enter player 5's rating:\n"))

# creates list for jersey number
jersey = [player1_jersey, player2_jersey, player3_jersey, player4_jersey, player5_jersey]
# creates list for player rating
rating = [player1_rating, player2_rating, player3_rating, player4_rating, player5_rating]

# creates dictionary with keys added from the jersey list and values added from the rating list
players = {jersey[i]: rating[i] for i in range(len(jersey))}
list_of_players = list(players.keys())  # creates list from dictionary
lis = sorted(list_of_players)  # sorts list in ascending order

# prints roster of players with jersey numbers in ascending order
print("\nROSTER")
for num in lis:
    print('Jersey number: {}, Rating: {}'.format(num, players[num]))

# variable menu created assigned with menu for user
menu = ("\nMENU\n"
        "a - Add player\n"
        "d - Remove player\n"
        "u - Update player rating\n"
        "r - Output players above a rating\n"
        "o - Output roster\n"
        "q - Quit\n")
option = ''
print(menu)  # prints menu
while option != 'q':  # exits loop with input of q
    option = input("Choose an option:")  # requests user to select an option from the menu
    print()
    if option == 'a':  # appends new player's info to the dictionary
        new_player_jersey = int(input("Enter a new player's jersey number:\n"))
        new_player_rating = int(input("Enter the player's rating:\n"))
        print()

        jersey.append(new_player_jersey)
        rating.append(new_player_rating)

        players = {jersey[i]: rating[i] for i in range(len(jersey))}
        list_of_players = list(players.keys())
        lis = sorted(list_of_players)

    if option == 'd':  # removes existing player's info from the dictionary
        remove_jersey = int(input("Enter a jersey number:\n"))
        jersey.remove(remove_jersey)

        players = {jersey[i]: rating[i] for i in range(len(jersey))}
        list_of_players = list(players.keys())
        lis = sorted(list_of_players)

    if option == 'u':  # updates the rating for a selected player in the dictionary
        current_jersey = int(input("Enter a jersey number:\n"))
        updated_rating = int(input("Enter a new rating for player:\n"))
        j = [current_jersey]
        r = [updated_rating]
        p = {j[i]: r[i] for i in range(len(j))}
        players.update(p)

        list_of_players = list(players.keys())
        lis = sorted(list_of_players)

    if option == 'r':  # prints all players with ratings larger than the one inputted
        rate = int(input("Enter a rating:"))
        print("ABOVE {}".format(rate))

        players = {jersey[i]: rating[i] for i in range(len(jersey))}
        list_of_players = list(players.keys())
        lis = sorted(list_of_players)

        for i in players:
            if players[i] > rate:
                print("Jersey no: {} , Rating : {}".format(i, players[i]))
        print()

    if option == 'o':  # outputs roster when user selects the o option
        for num in lis:
            print('Jersey number: {}, Rating: {}'.format(num, players[num]))
        print()
