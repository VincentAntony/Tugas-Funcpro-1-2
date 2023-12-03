def sequenceGenerator(start,stop):
    x = []
    for i in range(start, stop+1):
        x.append(i)
        return x
print(sequenceGenerator(1,10))

def fizzBuzz(a,b):
    x = []
    for num in range(a,b):
        if num % 3 == 0 and num % 5 == 0:
            x.append('FizzBuzz')
        elif num % 3 == 0:
            x.append('Fizz')
        elif num % 5 == 0:
            x.append('Buzz')
        else:
            x.append(num)
    return x

def twonumber(1):
    res = []
    for i in 1:
        if 1.index(i) == len(1)-1:
            break
        z = i + 1[i+1]
        res.append(z)
    return res