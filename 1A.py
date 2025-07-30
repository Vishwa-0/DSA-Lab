tup=[(1,2,3),(4,5,6)]
res=[]
for i in tup:
    s=0
    s+=sum(i)
    res.append(s)
print("The sum of the tuples inside the list is:",res)
