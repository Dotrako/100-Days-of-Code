class User:
    def __init__(self, user_id, username):
        """Initialize a User object with a user ID and username."""
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        """Increment the followers count for the user being followed and following count for the current user."""
        user.followers += 1
        self.following += 1


user_1 = User("001", "Dot")
print(f"your user id is: \n {user_1.id}")
print(f"your user name is: \n {user_1.username}")


user_2 = User("002", "Lk")
print(f"your user id is: \n {user_2.id}")
print(f"your user name is: \n {user_2.username}")

# add more followers
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following) # user 1 is following user2
print(user_2.followers) # user 2 is followed by user 1
print(user_2.following)