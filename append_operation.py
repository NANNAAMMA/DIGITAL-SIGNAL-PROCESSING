##program to perform append operation on lists
a=[1,2,3,4,5,6,7]
b=[4,5,6,7]
c=[2,4,68,34,98,10]
print("Here three lists a,b and c",a,"\t,",b,"\t",c)
for i in range(0,len(a)):
    b.append(a[i])
print("the new list formed is=",b)
for i in range(0,len(c)):
    if(c[i]%2==1):
        a.append(c[i])
print("new list ",a)

