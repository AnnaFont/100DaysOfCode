import art
import random


def calculate_score(pc_cards_total, cards1, cards2):
    user_score1 = 0
    user_score2 = 0
    pc_score_total = 0
    # 2 users scores depending on the As value
    for card in user_cards:
        user_score1 += cards1[card]
        user_score2 += cards2[card]
    if 21 >= user_score2 > pc_score_total or user_score2 <= 21 < pc_score_total:
        print("You win")
    elif user_score2 <= 21 and pc_score_total > user_score2:
        print("You loose")
    elif 21 >= user_score1 > pc_score_total or user_score1 <= 21 < pc_score_total:
        print("You win")
    elif user_score2 == pc_score_total or user_score1 == pc_score_total:
        print("Drawn")
    else:
        print("You loose")


# Blackjack game
art.print_cards()
new_game = input("Do you want to play a game? (y/n)").lower()
while new_game == 'y':
    # Two list as A's can be 1 or 11
    cards_value1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards_value2 = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_card1 = random.randint(1, 13)
    user_card2 = random.randint(1, 13)
    user_cards = [user_card1, user_card2]
    pc_card1 = random.randint(1, 13)
    pc_card2 = random.randint(1, 13)
    pc_cards = pc_card1 + pc_card2
    print(f"Your cards: [{user_card1}, {user_card2}]")
    print(f"Computer's first card: {pc_card1}")
    game_finished = False
    while not game_finished:
        another_card_input = input("Type 'y' to get another card, type 'n' to pass:")
        if another_card_input == 'n':
            game_finished = True
        else:
            new_card = random.randint(1, 13)
            user_cards.append(new_card)
            print(f"You got an {new_card}")
    print(f"Your final hand: {user_cards}")
    print(f"Computer's final hand: [{pc_card1}, {pc_card2}]")
    calculate_score(pc_cards, cards_value1, cards_value2)
    new_game = input("Do you want to play a game? (y/n)").lower()
