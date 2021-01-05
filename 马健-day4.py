shop = [
    ["Iphonr8p",1000],
    ["Mac loptop",12000],
    ["IWatch",500],
    ["lenoco PC",4000],
    ["辣条",10],
    ["洗衣粉",23.5]
]
mycart = []
#1、展示商城商品
# for item,value in enumerate(shop):
#     print(item,value)
def showshop():
    for item,value in enumerate(shop):
        print(item,value)
#1.2 积分计算方法

def integrates(x):
    integrate = 0
    if x >=0 and x <= 5000 :
        integrate = integrate + 200
    elif x>5000 and x <= 10000:
        integrate = integrate + 400
    elif x > 10000 and x <= 15000:
        integrate = integrate + 600
    print("您的会员积分为",integrate,"分")

#1.3 随机赠送优惠劵
import random
def dollar(y):
    dollars = float(random.random()+8)/10
    if y >0 :
        y = y *dollars
    return y

#2.让用户输入自己的薪资
while True:
    salary = input("请输入您的薪资：")
    if salary.isdigit():      #isdigit()  判断某个字符串是否有数字组成
        salary = int(salary)
        break
    else:
        print("请输入合适的薪资！")
#3.开始购物
pay = 0
while True:
    #  3.1  展示商品
    print("---------------------------欢迎来到王瑞敏的小商店-----------------------------------")
    showshop()
    # 3.2  请输入要买的商品的编号
    chose = input("请输入要买的商品编号：")
    if chose.isdigit():     #判断是否是数字
        chose = int(chose)
        if chose >= len(shop):
            print("\33[41;20;1m您输入的商品不存在！\33[0m")
        else:
            if salary < shop[chose][1]:
                print("\33[41;20;1m您的余额不足，下个月再来吧！\33[0m")
            else:#正常购买商品，添加到我的购物车，从薪资中减去相应的商品金钱
                mycart.append(shop[chose])
                salary = salary - shop[chose][1]
                pay = pay +shop[chose][1]
                print("\33[32;20;1m购买成功！您的余额为：",salary,"\33[0m")
    elif chose =="Q"  or chose ==  "q":
        break
    else:
        print("\33[41;20;1m您的输入不合法！，请重新输入！\33[0m")
print("----------------------欢迎下次光临-----------------------------")
print("您的购物车商品如下：")
for item in mycart:
    print(item)
while True:
    if pay >= 0:
        t = int(dollar(pay))
        break
    else:
        print("无优惠券可使用！")
        break
print("使用优惠券之后的使用金额为：",t,"元")
salary = salary - t
print("所剩余额为：", salary,"元")
integrates(t)













