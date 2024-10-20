# Printing factorial of a number
def fact(n):
    if (n==1 or n==0):
        return 1
    return n * fact(n-1)
n=int(input("Enter the number: "))
print(f"The factorial is {fact(n)}")

#Write a recursive function to print sum of n natural numbers
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
num=int(input("Enter the number: "))
a=sum(num)
print(f"The sum of {num} natural numbers is {a}")
