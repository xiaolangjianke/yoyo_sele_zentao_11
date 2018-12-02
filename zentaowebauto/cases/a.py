a = range(1000, 3000)
temp = []
for i in a:
    s = str(i)
    Y = [False if int(i) % 2 else True for i in s]
    # print(Y)
    if False not in Y:
        temp.append(i)
        print(i)


