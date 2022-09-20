#sort
ar=[100,-2,-14,25,7,3,5,109]
x=0
y=0
for i in range(0,len(ar)):
    for j in range(i+1,len(ar)):
        if ar[i]>ar[j]:
            x=ar[j]
            y=ar[i]
            ar[i]=x
            ar[j]=y
print(ar)