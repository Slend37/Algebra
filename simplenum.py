a = int(input())

b=0
m=[]
n=[]
for i in range(2,a//2+1):
    while a%i==0:
        b+=1
        a/=i
    if b>0:
        m.append(b)
        n.append(i)
    b=0

z=''
for i in range(len(n)):
    z=z+(str(n[i])+'^'+str(m[i])+'\n')

print(z)