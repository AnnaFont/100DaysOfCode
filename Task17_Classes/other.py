# PascalCase (for the class names), camelCase (not used in python), snake_case (for all the other things)
# Word "pass" can be used to do not add anything inside a function and do not get an error
class User:
    # initialize the attributes. It will execute prior to start the code.
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Add to the followers of the user that it is being followed
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "anna")
user_2 = User("002", "jack")
print(user_1.username)
print(user_1.followers)

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)
