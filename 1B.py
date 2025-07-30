dict={"A":["A","B","C"],"B":["D","E","F"]}
for i in dict["A"]:
    for j in dict["B"]:
        temp=i+j
        print(temp)
        print(temp[-1:]+temp[:-1])
