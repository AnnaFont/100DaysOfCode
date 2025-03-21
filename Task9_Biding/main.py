# Dictionaries
"""
program_dictionary = {"bug": "Error of a program",
                      "function": "Piece of code",
                      "loop": "iterate again",
}
print(program_dictionary["bug"])
program_dictionary["Hi"] = "To say hello"
print(program_dictionary)
for key in program_dictionary:
    print(key)
    print(program_dictionary[key])

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionaries
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Stuttgart","Berlin"],
        "total_visits": 2
    }
}
print(travel_log["France"]["cities_visited"][1])
"""
# Blind Auction Project
print("Welcome to the secret auction program.")
stop_program = False
answerUser = "yes"
bidders_log = {}
# Check the bidders and save it in the dictionary
while answerUser == "yes":
    name_user = input("What is your name?:")
    money_user = int(input("What's your bid?: $"))
    bidders_log[name_user] = money_user
    answerUser = input("Are there any other bidders?(Yes/No)").lower()
    print("\n"*100)
# Check who wins the bidder
winner = max(bidders_log, key=bidders_log.get)
print("The winner is", winner)
print("The amount is $", bidders_log[winner])
