'''
编程实现下列图形的打印
'''
#
# for i in range(0,7):
#     for l in range(0,6 - i):
#         print(" ", end="")
#     for g in range(0,i + 1):
#         print("*", end=" ")
#     print("")


'''
一只青蛙掉在井里了，井高20米，青蛙白天往上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
'''
# max = 0
# i= 20
# for x in range(0,20):
#     x = x + 1
#     if max + 3 == 20:
#         print("一共用了：",x,"天")
#         break
#     else:
#         max = max +3-2

'''
用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
'''
# max = 0
# max1=1
# for i in range(1,21):
#     max1=max1 * i
#     max =max +max1
# print("20以内的阶乘为：",max)


'''
有以下一个列表，求其中是5的倍数的和
'''
# a=[15,20,12,63,3,8,94,61,27,5,10]
# sum = 0
# for i in range(0,len(a)):
#     if a[i] % 5 == 0:
#         sum = sum +a[i]
# print("5的倍数的和为：",sum)

'''
请对下列列表进行冒泡排序
'''
# a=[15,20,12,63,3,8,94,61,27,5,10]
#
# for i in range(0,len(a)):
#     for j in range(0,len(a)-i-1):
#         if a[j] > a[j+1]:
#             c = a[j]
#             a[j]=a[j+1]
#             a[j+1]=c
# print(a)

'''
有下列列表，请编程实现列表的数据翻转
'''

# list = [1,2,3,4,5,6,7,8,9]
# for i in range(0,len(list)):
#     for j in range(0,len(list)-i-1):
#         c = list[j]
#         list[j]=list[j+1]
#         list[j+1]=c
# print(list)


'''
请编程统计列表中的每个数字出现的次数
'''
# list= [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# for x in range(0,10):
#     max = 0
#     for i in range(0,len(list)):
#         if x + 1 == list[i]:
#             max = max + 1
#     x = x+1
#     print(x, "在列表中出现了：", max, "次")




'''
有下列人员数据库，请按要求实现

姓名names[0]  年龄names[1]  性别names[2]  编号names[3]   任职公司names[4]   薪资names[5]   部门编号names[6]
1.统计每个人的平均薪资
2.统计每个人的平均年龄
3.公司新来一个员工，张佳伟，45，男，220，alibaba，500,30，添加到列表中
4.统计公司男女人数
5.每个部门的人数
'''
names = [
    ["何登勇","56","男","106","IBM", 500 ,50],
    ["曹东雪","19","女","230","微软", 501 ,60],
    ["刘营营", "19", "女", "210", "Oracle", 600, 60],
    ["李汉聪", "45", "男", "230", "Tencent", 700 , 10]
]
num = 0
num1 = 0
for i in range(0,len(names)):
    num =num + names[i][5]
print("每个人的平均工资为：",num/i)
for j in range(0,len(names)):
    num1= num1 + int(names[j][1])
print("每个人的平均年龄为：",num1/j)


# a=input("请输入员工姓名：")
# b=input("请输入员工年龄：")
# c=input("请输入员工性别：")
names.append(["张佳伟",45,"男","220","alibaba",500,30])
# names[4][3]=input("请输入员工编号：")
# names[4][4]=input("请输入员工任职公司：")
# names[4][5]=input("请输入员工薪资：")
# names[4][6]=input("请输入员工部门编号：")

man = 0
woman = 0
for i in range(0,len(names)):
    if names[i][2] == "男" :
        man = man + 1
    else:
        woman = woman + 1
    i= i+1
print("男士人数为：",man,"人，女士人数为：",woman,"人")

for x in range(0,100):
    max = 0
    for i in range(0,len(names)):
        if x + 1 == names[i][6]:
            max = max + 1
    x = x+1
    print("部门",x, "在列表中出现了：", max, "次")






