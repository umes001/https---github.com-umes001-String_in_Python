#W.a.p Enter two Number from keyboard and print
 # 1-largest 2- smallest 3- add 4- power
fullname="Menu"
#print(" use ljust and rjust postion of string")

#print(fullname.ljust(10,"*"))
#print(fullname.rjust(10,"*"))
while(1):
    a,b=int(input("Enter 1st number")),int(input("Enter 2nd number"))
    print(fullname.center(20,"-"))
    print("1-Largest\n 2- Smallest \n 3- add \n 4- Power")
    ch=input("Enter your choice:")

    if ch=='1':
        if a>b:
            print(a,"is largest number")
        else:
            print(b,"is largest number")
    if ch=='2':
        if a<b:
            print(a,"is smallest number")
        else:
            print(b,"is smallest number")        


