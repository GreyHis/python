#输入两个数以空格隔开，输出两个数的和
a,b=map(int,input("请输入两个数以空格隔开").split())
print(a+b)
#level4
n=int(input("请输入人数"))
list=[0]*n
money=[0]*n
for i in range(n):
    list[i]=input("请输入每个人数据:").split()
for i in range(n):
    if int(list[i][1])>80 and int(list[i][5])>=1:
        money[i]=money[i]+8000
    if int(list[i][1])>85 and int(list[i][2])>80:
        money[i]=money[i]+4000
    if int(list[i][1])>90:
        money[i]=money[i]+2000
    if int(list[i][1])>85 and list[i][4]=="Y":
        money[i]=money[i]+1000
    if int(list[i][2])>80 and list[i][3]=="Y":
        money[i]=money[i]+850
max=0
sum=0
for i in range(len(money)):
    if money[i]>max:
        index=i
        max=money[i]
    sum+=money[i]

print(list[index][0])
print(money[index])
print(sum)



