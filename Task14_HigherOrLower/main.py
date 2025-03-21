import random
# Higher or lower game. Check which is higher than the other and later put the score
from game_data import data

def compare_results(account_a, account_b, guess_answer):
    if account_a["follower_count"] > account_b["follower_count"]:
        data_result = 'a'
    else:
        data_result = 'b'
    if data_result == guess_answer:
        return True
    else:
        return False


def score_sum (total_score, guess_ok):
    if guess_ok == True:
        total_score += 1
    return(total_score)


# 1st start game
print("Welcome to the higher and lower game")
total_score = 0
account_a = random.choice(data)
account_b = random.choice(data)
while account_b == account_a:
    account_b = random.choice(data)

end_game = False

while not end_game:

    account_a_name = account_a["name"]
    account_b_name = account_b["name"]

    # 2nd show the comparison
    guess_answer = input(f" Who have more followers in Instagram, A: {account_a_name} or B: {account_b_name}: ").lower()

    # 3rd Check if user right
    result = compare_results(account_a, account_b, guess_answer)

    # Print score
    if result:
        total_score += 1
        print(f"Well done. You have {total_score} points")
        if guess_answer == "b":
            account_a = account_b
        account_b = random.choice(data)
        while account_b == account_a:
            account_b = random.choice(data)
    else:
        print(f"Incorrect. You got {total_score} scores")
        end_game = True
