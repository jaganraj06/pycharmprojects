#formate
name = 'raj'
like1 = 'ice cream'
like2 = 'chips'
print(name + ' likes ' + like1 + ' and ' + like2 )
text = '{} likes {} and {}'
print(text.format(name,like1,like2))
print('{} likes {} and {}'.format(name,like1,like2))
text = '{0} likes {2} and {1}'
print(text.format(name,like1,like2))

#padding
print("******{msg}******".format(msg="welcome"))
print("******{msg:10}******".format(msg="welcome"))
print("******{msg:^}******".format(msg="welcome"))
print("******{:<20}******".format("welcome"))
print("******{msg:>20}******".format(msg="welcome"))

pi = 3.14159

print("the val of pi is {:.2f}".format(pi))

num = 1000000

print("the num is {:,}".format(num))

num = 101

print("the num is {:b}".format(num))
print("the num is {:o}".format(num))
print("the num is {:x}".format(num))

def greet(fname,lname):
    print(" hello " + fname + " " + lname)
    print("how are you " + fname +"?")

n = "ram"
greet(fname="priya",lname="dharshan")

def sum(num):
    return num*(num+1)/2

Result = sum(11)
print(Result)
print(sum(20))
