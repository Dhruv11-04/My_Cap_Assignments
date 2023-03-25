
i=[]
l=int(input( "Enter the no.: " ))
i.append(l)
l2=input("Do you want to enter more nos. (Y/N):")
while l2=="Y":
    l3=int(input( "Enter the no.: " ))
    i.append(l3)
    l2=input("Do you want to enter more nos. (Y/N):")

for j in i :
    if j < 0 :
        i.remove(j)
print("Positive no in the list are: ",i)