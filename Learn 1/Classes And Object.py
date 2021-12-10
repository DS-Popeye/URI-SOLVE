class user:
    name = ""
    email = ""
    password = ""
    login = False

    def Login(self):
        email = input()
        password = input()

        if email  == self.email and password == self.password:
            login = True
            print("Login Succesfull!")
        else:
            print("Log in failed!")

    def logout(self):
        login = False
        print("Log Out!")

    def isloggedIn(self):
        if self.Login():
            return True
        else:
            return False

    def profile(self):
        if self.isloggedIn():
            print(self.name,"\n",self.email)
        else:
            print("User is not Logged in!")

user1 = user()
user1.name = "Shuvo"
user1.email = "shuvo@gmail.com"
user1.password = "123456789"

user1.Login()
user1.profile()
