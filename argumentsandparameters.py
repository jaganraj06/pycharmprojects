#argumentsandparameters
def greet (name):#parameter
    print(" hello " + name)
    print("how are you ?")
greet("ram")#argument

print("*******")
greet("hari")


num = 10
def welcome (name): #name-localvariable
    num=20
    print(" welcome " + name)
    print(str(num))



welcome("ravi")
print(" the val of num is " + str(num))
print(num)


# sum of numbers
def total(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(total(1,4,5,2,4,5,6,7,17,17))


#kwargs
def print_addr(**kwargs):
    for key , val in kwargs.items():
        print(val)
print_addr(door_no="84",street_name="JJnagar",place_name="solinganallur",city_name="chennai" )

def greet(fname,lname=''):
    print(" hello " + fname + " " + lname)
    print("how are you?")



greet(fname="rahul",lname="kavin")



#passinglist
def print_list(list):
    for i in range(0,len(list)):
        list[i] = list[i].title()
        print(list[i])


name = ["raj","ravi","ram","rani","radha"]
print_list(name[:])
print(name)

#returning dictionaries
def get_user_info():
    ''':return the users name and age .in dictionary'''
    user = {'name':'ravi','age':'17'}
    return user

user=get_user_info()
print(user)


