# a = int(input('Основание:'))
# degree = int(input('Степень:'))
# mod = int(input('Второе число:'))

a= 7777
degree = 7777
mod = 25

n1 = a
n2= mod

while mod+n2<a:
    mod+=25

x = a-mod
n3=n2
n = []
b=0

for i in range(2,n2//2+1):
    while n2%i==0:
        b+=1
        n2/=i
    if b>0:
        n.append(i)
    b=0


f=n3
for i in range(len(n)):
    f=f*(1-1/n[i])

y = a//f
z = a-y*f

ans = x**z // n3
answer = x**z - ans*n3
print(answer)