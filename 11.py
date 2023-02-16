"""N=int(input())
for i in range(N):
    x,y=input().split(' ')
    y=float(y)
    if x=='M':
        z=y/1.09
    else :
        z=y*1.09
    print("%.2f"%z)"""
"""x=input()
for i in range(int(x)):
 N=float(input())
 if N<=15:
     z=N*0.4463
 elif N<=400:
     z=150*0.4463+(N-150)*0.4663
 else :
     z=150*0.4463+250*0.4663+(N-400)*0.5663
 print("%.2f"%z)"""
N=input()#输入循环次数，题目要求的用户数
i=0#统计循环次数，可以定义为1，但定义为1下面改成i<=N
while (i<int(N)):#进行循环循环次数为N
    x,y=input().split(' ')#分别进行输入性别和身高，注意Java中的数据类型定义，python不需要定义
    y=float(y)#这个不用管
    if x=='M':#进行判断性别是男是女
        z=y/1.09
    else :
        z=y*1.09
    print("%.2f"%z)#输出保留两位小数
    i=i+1 #每循环一次i就加一次



