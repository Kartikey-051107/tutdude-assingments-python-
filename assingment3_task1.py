n=int(input("enter a number:"))
def factorial(n):
    if n<0:
        print("please enter a valid number")
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

print(f"the factorial of the given no is {factorial(n)}")