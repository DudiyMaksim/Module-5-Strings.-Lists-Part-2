import random
# # task 1
a=input("Введіть вираз : ")
x=''
n=''
m=''
for i in a:
    if i=='+' or i=='-' or i=='*' or i=='/':
        x=i
    elif x=='':
        n+=i
    else:
        m+=i
n=int(n)
m=int(m)
if x=='+':
    print(n+m)
elif x=='-':
    print(n-m)
elif x=='*':
    print(n*m)
elif x=='/':
    print(n/m)
# task 2
a=[]
for i in range(20):
    a.append(random.randint(-30,30))
print(f"min: {min(a)}")
print(f"max: {max(a)}")
x=0
b=0
n=0
for i in a:
    if i<0:
        x+=1
    elif i>0:
        b+=1
    else:
        n+=1
print(f">0: {x}")
print(f"<0: {b}")
print(f"=0: {n}")