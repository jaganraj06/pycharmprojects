import random

print("welcome to random passward generator")
randomechars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
nbrofpwds =int(input("please enter the number of passwards want to be generated: "))
pwdlen = int(input("please enter the length of passward needed :"))
print("here are your random passwords:")
for x in range(nbrofpwds):
    pwd = ""
    for chars in range(pwdlen):
        pwd =pwd + random.choice(randomechars)
    print([pwd])