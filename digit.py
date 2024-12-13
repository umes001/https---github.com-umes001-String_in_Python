pincode=input("Enter Valid pincode number")
t=pincode.isdigit()

if(t==True):
      
   length=len(pincode)

   if(length==6):
      print("valid pincode number")
   else:
     print("Enter Only 6 Digit pincode")
else:
      print("Enter Valid Pincode digit")
     

