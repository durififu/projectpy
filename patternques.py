''' print the pattern
for n=3
  *
 ***
*****'''
n=int(input("Enter the number: "))
for i in range (1, n+1):
    print(" "*(n-i), end="") #for printing spaces at the starting
    print("*"*(2*i-1), end="")
    print("")
