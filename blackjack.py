import random

cards = {"ace": 11, 
         "2": 2,
         "3": 3, 
         "4": 4, 
         "5": 5, 
         "6": 6, 
         "7": 7, 
         "8": 8, 
         "9": 9, 
         "10": 10, 
         "j": 10, 
         "q": 10, 
         "k": 10
}
players = {
  "dealer": [],
}
stand_players = {}

def init_players():
    add_player = True
    while add_player:
        choice = input("Add player? Enter 'y' or 'n': ")
    
        if choice == "n":
            add_player = False
        elif choice == "y":
            players[input("Player name? ").lower()] = []
        else:
            print("Wrong choice.")

def deal_card():
    return random.choice(list(cards.keys()))

def first_deal():
    for player_name in players:
        for _ in range(2):
            players[player_name].append(deal_card())
        if player_name == "dealer":
            print(f"{player_name.title()}'s first card: {players[player_name][0]} \n _")

def player_turn(current_player):
    current_round = True
    while current_round:
        print(current_player.title(), "is playing: Current hand: " , players[current_player])
        player_choice = input("New card? Enter 'y' or 'n':  \n ")
        if player_choice == "n":
            stand_players[current_player] = players.pop(current_player)
            current_round = False
            return
        elif player_choice == "y":
            players[current_player].append(deal_card())
            return
        else:
            print("Wrong choice.")

def card_count(player):
    tot = 0
    has_ace = False
    hands = players[player].copy()  # Create a copy of the list to avoid modifying it during iteration
    for card_key in hands:
        tot += cards[card_key]
        if card_key == "ace":
            has_ace = True
    return tot , has_ace

def game_play():

    while players:

        for player in list(players.keys()):  # Iterate over player names
            tot, has_ace = card_count(player)
            if len(players) == 1:
                stand_players[player] = players.pop(player)
            elif player == "dealer":
                
                if tot >= 17:
                    stand_players[player] = players.pop(player)
                    break
                else:
                    players[player].append(deal_card())
                    card_count(player)    

            else:
                if tot == 21:
                    print(player.title() , " has a total of: " , tot , " \n _")
                    stand_players[player] = players.pop(player)
                elif tot > 21 and has_ace == False:
                    print(player.title() , " is out: Total: " , tot , " \n _")
                    stand_players[player] = players.pop(player)
                else:
                    player_turn(player)
    return stand_players

def end(results):
    finals = {}
    for player, result in results.items():
        total_score = 0
        for x in result:
            total_score += cards[x]
        if total_score > 21:
            for x in result:
                if x == "ace" and total_score > 21:
                    total_score -= 10

        print(f"{player.title()}: {result}, Total: {total_score}")
        if total_score <= 21:
            finals[player] = total_score

    max_score = max(finals.values())
    for player, score in finals.items():
        if score == max_score:
            print(f"{player.title()} wins with a total score of {score}  \n _")


if __name__ == "__main__":
    init_players()
    first_deal()
    end(game_play())
    exit()