#lambda function:
X = lambda a: a + 9
print(X(1))


def add_ten(num):
    return num+10
print(add_ten(6))

product = lambda a,b,c:a*b*c
print(product(5,8,9))

tall_enough = lambda h:h>175
print(tall_enough(189))

strong_enough = lambda w: "yes" if w>70 else "no"
print(strong_enough(89))


