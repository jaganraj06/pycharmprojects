class User:
    #user_name = None
    #pwd = None
    #users =0
    #def __init__(self, user_name , pwd):
        #self.user_name = user_name
        #self.pwd = pwd
        #User.users += 1
    def register(self):
     print("Registering..." )

    def login(self):
     print("Logging in ...")
class Student(User):
   def greet_Student(self):
    print(" hi Students ... ")

class faculty(User):
   def greet_faculty(self):
    print(" hello teacher ... ")



