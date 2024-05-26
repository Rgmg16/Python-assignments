list2 = [23, 45, 67, -10, 23, 50, -10]
seen= set()
list3=[]

for x in list2:
    if x not in seen:
        list3.append(x)
        seen.add(x)
            
list2=list3
            
print(list2)            