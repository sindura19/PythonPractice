#program to add hexadecimal values
n1=input("Enter 1st hexadecimal value: ")
n2=input("Enter 2nd Hexadecimal value: ")
n3=int(n1,base=16)+int(n2,base=16)

print(n1,n2,hex(n3))