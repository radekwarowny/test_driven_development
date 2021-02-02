class User:
    logins = []

    def set_username(self, username):
        self.logins.append(username)
        return len(self.logins) - 1

    def get_username(self, user_id):
        if user_id >= len(self.logins):
            return 'No username found'
        else:
            return self.logins[user_id]


if __name__ == "__main__":
    user = User()
    print("User has been added with id: ", user.set_username('defmasta'))
    print("User associated with id 0 is: ", user.get_username(0))
