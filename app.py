from icecream import ic

def fizi():
    for x in range(1,100):
        if (x % 15 == 0): ic ("fizzbuzz")
        elif (x % 3 == 0): ic ("fizz")
        elif (x % 5 == 0): ic ("buzz")
        else: ic (x)
        
fizi()

def evenNumbers():
    for x in range(100):
        if (x % 2 == 0): ic (x)
        

evenNumbers()

def notevenNumbers():
    for x in range(-100,-1):
        if (x % 2 == 1): ic (x)
        
        
notevenNumbers()