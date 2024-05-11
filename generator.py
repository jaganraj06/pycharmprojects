def sq_num_gen(num):
    for i in range(1,num+1):
        yield i*i


sq_gen = list(sq_num_gen(11111))
for i in sq_gen:
    print(i)


