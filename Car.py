import re
print("Let's check your vehical is from Madhya pradesh or not")
s=input("Enter Full Vehical Number :")
m=re.fullmatch('MP[012345][0-9][a-z]{2}\d{4}',s,re.IGNORECASE)
if m!=None:
	print("Your Vehical is registered in Madhya Pradesh !!")
else:
	print("It's seems your vehical is not registered in Madhya Pradesh")