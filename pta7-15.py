x=int(input())
if (x>99&x<1000):
    a=int(x%10)
    b=int(x/10%10)
    c=int(x/100)
    y=a*a*a+b*b*b+c*c*c
    if (x==y):
        print("Yes")
    else :
        print("No")
else :
    print("Invalid Value.")

