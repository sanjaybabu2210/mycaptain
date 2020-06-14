def pos_find(num):
    lis = []
    for x in num:
        if x<0:
            continue
        else:
            lis.append(x)
    return lis


num = eval(input('enter the list'))
print(pos_find(num))
