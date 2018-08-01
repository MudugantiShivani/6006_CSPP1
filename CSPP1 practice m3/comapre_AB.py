A=input("enter the first number")
B=input("enter second number")
x=type(A)
y=type(B)
if (x=="str" or y=="str"):
	print ("strings involved")
elif (A>B):
	print ("bigger")
elif (A==B):
	print ("equal")	
elif (A<B):
	print ("smaller")	