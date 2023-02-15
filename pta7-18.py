x=int(input())
y=0
a=2
b=1
for i in range(x) :
    y=y+a/b
    c=a
    a=b+a
    b=c
print('%.2f'%y)