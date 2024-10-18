''' PATTERN 1 print the pattern without using loops
for n=3
  *
 ***
*****'''
n=int(input("Enter the number: "))
for i in range (1, n+1):
    print(" "*(n-i), end="") #for printing spaces at the starting
    print("*"*(2*i-1), end="")
    print("")
 
''' PATTERN 2 printing pattern
*
**
***
'''
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print("*"*i, end="")
    print("")
 
'''  PATTERN 3 printing pattern
***
* *
***
'''
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    if(i==1 or i==n):  # for rows
        print("*"*n, end='')
    else:
        print("*", end='')
        print(" "*(n-2), end='')
        print("*", end='')
    print("") #used to print new line
