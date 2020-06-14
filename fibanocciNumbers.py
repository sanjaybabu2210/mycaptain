# recurrence solotion but not effiecient for large numbers

def fibonacci(num):
    if num <= 1:
        return num;
    else:
        return fibonacci(num-1) + fibonacci(num-2)
fibonacci(5)
#array based solution

def fib(num):
    x = [0,0]
    x[0] = 0
    x[1] = 1
    for i in range(2,num+1):
        x.append(x[i-1] + x[i-2])
    

    return x[num]

fib(10)
