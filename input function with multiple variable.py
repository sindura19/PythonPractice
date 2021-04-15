s=input("Enter two values")
a,b=s.split(" ")
print(a,b)
c=int(a)+int(b)
print(c)

a,b,c=input("Enter 3 values").split(" ")
d=int(a)+int(b)+int(c)
print(a,b,c,d)

x,y,z=map(int,input("Enter three values separated by ,:").split(","))
Total=x+y+z
print(x,y,z,Total)