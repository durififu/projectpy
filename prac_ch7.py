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
