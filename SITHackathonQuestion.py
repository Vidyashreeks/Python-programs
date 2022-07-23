n=int(input())
arr=[]
res=[]

for i in range(n):
    arr.append(input())
clue=list(input()) 


for i in range(1,len(clue)):
    x=clue[i:] + clue[0:i]
    #print(x)
    x="".join(x)
    #print(x)
    if x in arr:
        res.append(arr.index(x))

        
y=res[::-1]
print(y)