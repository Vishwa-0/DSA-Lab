s=input("Enter the elements spread by commas:")
l=list((map(str,s.split(","))))
for i in range(len(l)):
    for j in range(len(l)):
        print(l[i]+l[j])
        
