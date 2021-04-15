#Write a Program to add binary values 
b1=input("Enter 1st binary value: ")
b2=input("Enter 2nd binary value: ")

b3=int(b1,base=2)+int(b2,base=2)
print(type(b1))
print(type(b2))
print(type(b3))

print(b1,b2,bin(b3))