#CONDITIONALS
# a=int(input("enter the age:"))
# if(a>18):
#     print("You can vote")
# elif(a<0):
#     print("Enter valid age")
# else:
#     print("You can't vote")
''' QUESTIONS PRACTICE'''
num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
num3=int(input("Enter the 3rd number:"))
num4=int(input("Enter the 4th number:"))
if(num1>num2 and num1>num3 and num1>num4):
    print("1st number is greatest")
elif(num2>num1 and num2>num3 and num2>num4):
    print("2nd number is greatest")
elif(num3>num1 and num3>num2 and num3>num4):
    print("3rd number is greatest")
elif(num4>num1 and num4>num3 and num4>num2):
    print("4th number is greatest")
else:
    print("Invalid input!")
print("END OF PROGRAM")    