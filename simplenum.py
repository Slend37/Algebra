a = int(input())
number = a


#Разложение на простые множители
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
    z=z+(str(n[i])+'^'+str(m[i])+' ')
print('Разложение на простые множители:',z)

#Нахождение кол-ва натуральных делителей
z=[]
for i in range(len(n)):
    z.append(m[i]+1)
y=1
for i in range(len(z)):
    y=y*z[i]
print('Кол-во натуральных делителей числа:',y)

#Сумма всех натуральных делителей
s=1
for i in range(len(n)):
    s=s*(n[i]**z[i]-1)/(n[i]-1)
print('Сумма всех натуральных делителей числа:',s)

#Произведение всех натуральных делителей числа
p = number**(y/2)
print('Произведение всех натуральных делителей числа:',p)

#Фукнция эйлера
f=number
for i in range(len(n)):
    f=f*(1-1/n[i])
print('Фукнция Эйлера:',f)