# create a String application in python and use built-in function
#----------------------------------------------------------------
# Q-1 W.A.A Enter first Name, Middle Name, Last name
#and print 1- String in Lowercase,
# Upper Case, Capatalize case, title..ext.
fnm=input("Enter first Name")
mnm=input("Enter Middle Name")
lnm=input("Enter last Name:")

fullname=fnm+" "+mnm+" "+lnm

print(" Student Full Name=",fullname)

print(" Name  in Other  Format")
print("Lower",fullname.lower())

print("Upper",fullname.upper())

print("Title",fullname.title())

print("Swapcase",fullname.swapcase())

print("Capitalize",fullname.capitalize())

print(" Total number of char=",len(fullname))


print(" Find Any char's duplication within String value")
ch=input("Enter any Char")

print(ch," find in",fullname,"=",fullname.count(ch))

ch=input("Enter any Char to find position  from R>H>S index")

print(ch," find in",fullname[::-1],"=",fullname[::-1].index(ch))

"""
print(" use ljust and rjust postion of string")

print(fullname.ljust(50,"*"))
print(fullname.rjust(50,"*"))
print(fullname.center(50,"*"))
"""
