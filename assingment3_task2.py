import math
n=int(input("enter a number:"))

def arithmetic(n):
    squareroot=math.sqrt(n)
    log=math.log(n)
    sine=math.sin(n)
    return squareroot,log,sine

a,b,c=arithmetic(n)
print(f"square root:{a}")
print(f"logarithm:{b}")
print(f"sine:{c}")