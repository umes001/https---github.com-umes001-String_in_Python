unm=input("Enter Username in Alpha and Numberic mix")
pass1=input("Enter password in Numberic Numbers")

t=unm.isalnum()
print(t)

t1=pass1.isnumeric()
print(t1)

if (t==True and t1==True):
      print("match format")
      print("Login Sucess")
else:
     print(" format mismatch")
