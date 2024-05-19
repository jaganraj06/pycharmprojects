class User:
    user_name = None
    pwd = None
    users =0
    def __init__(self, user_name , pwd):
        self.user_name = user_name
        self.pwd = pwd
        User.users += 1
    def register(self):
     print("Registering..." )
    def login(self):
     print("Logging in ...")
     return self
    def greet(self):
     print("hello user ...")
class Student(User):

   def __init__(self,username,pwd,course,fee):
       super().__init__(username,pwd)
       self.course = course
       self.fee = fee
    #return self
   def greet(self):  # methodoverrideing
       super().greet()
       print(" hi Students ... ")
#class Faculty(User,Student):
   # def greet(self):
   #  super().greet()
   #  print(" hello teacher ... ")







