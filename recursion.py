#recursion
def fact(num):
    if num == 0:
        return 1
    return num*fact(num-1)
print(fact(4))

#generator
def sq_num(num):
    sq = []
    for i in range(1,num+1):
        sq.append(i*i)
    return sq
print(sq_num(10))

