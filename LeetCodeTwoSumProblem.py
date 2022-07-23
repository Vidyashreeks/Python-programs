target=int(input())
l=[1,2,3,4,5,6]
count=0
for i in range(len(l)-1):
    for j in range(1,len(l)-1):
        #print(l[i],l[j])
        if l[i]+l[j]==target:
            count=1
            print(l[i],l[j])
            
if count!=1:
    print("not found")
