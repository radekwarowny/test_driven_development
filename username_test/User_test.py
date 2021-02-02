import unittest

import User as UserClass  # the class to be tested


class Test(unittest.TestCase):
    """ The basic class that inherits unittest.TestCase """
    user = UserClass.User()  # instantiate the User Class
    user_id = []  # variable that stores obtained user_id
    logins = []  # variable that stores person name

    # test case function to check the User.set_username function
    def test_0_set_username(self):
        print("Start set_name test\n")
        """ Any method which starts with 'test_' will be considered as a test case. """

        for i in range(4):
            # initialise username
            username = 'username' + str(i)
            # store the username in a list
            self.logins.append(username)
            # get the user id obtained form the function
            user_id = self.user.set_username(username)
            # check if the obtained user id is not null
            self.assertIsNotNone(user_id)  # null user_id will fail the test
        print("user_id length = ", len(self.user_id))
        print(self.user_id)
        print("username length = ", len(self.logins))
        print(self.logins)
        print("\nFinish set_username test\n")

    # test case function to check the User.get_username function
    def test_1_get_username(self):
        print("\nStart get_username test\n")
        """ Any method that starts with 'test_' will be considered as a test case. """
        length = len(self.user_id)  # total number of stored user details
        print("user_id length = ", length)
        print("username length = ", len(self.logins))
        for i in range(6):
            # if i does not exceed total length then verify the returned username
            if i < length:
                # if username and user_id does not match then the test will fail.
                self.assertEqual(self.logins[i], self.user.get_username(self.user_id[i]))
            else:
                print("Testing for get_username no user test")
                # if length exceeds the range then check the 'no user' type message
                self.assertEqual("There is no such user", self.user.get_username(i))
        print("\nFinish get_username test\n")


if __name__ == "__main__":
    # driver method
    unittest.main()
