#ques1 print table of a number
num=int(input("Enter the number to print table of: "))
for i in range (1,11,1):
   print(f"{num}*{i} = {num*i})

#ques1 using while loop
num=int(input("Enter the number to print table of: "))
i=1
while(i<11):
    print(f"{num}*{i} = {num*i}")
    i+=1

# Print the multiplication table in reverse order METHOD 1
num=int(input("Enter the number to print table of: "))
for i in range (10,0,-1):
    print(f"{num}*{i} = {num*i}")

# Print the multiplication table in reverse order METHOD 2
num=int(input("Enter the number to print table of: "))
for i in range (1, 11):
    print(f"{num}*{11-i} = {num*(11-i)}")  
