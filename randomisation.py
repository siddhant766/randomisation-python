n1=0
n2=1
n=int(input())
if n==1:
    print(n1)
if n==2:
    print(n1)
    print(n2)
else:
    i=3
    print(n1)
    print(n2)
    while(i<=n and i>2):
        sum=n1+n2
        n1=n2
        n2=sum
        i=i+1
        print(sum)
