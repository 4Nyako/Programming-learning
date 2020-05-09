import random
age=random.randint(1,100)
flag=True ##设定一个旗帜 判断是否重复进行游戏
user_input=0
while flag:  ##外层循环直到flag为false之前一直都会执行（如果猜对了会执行quit退出）
    for i in range(3): ##最多执行三次内层循环
        user_input=int(input("input age:"))##输入年龄
        if user_input==age:##如果猜对了
            print("恭喜你猜对了！")
            quit()##退出
        elif user_input>age:
            print("大了")
        elif user_input<age:
            print("小了")
        if i==2 :
            if input("嘤嘤嘤三次了还是没猜对，继续吗Y/N:")=="N" : flag=False##如果猜了三次还没有才对，就询问是否继续 如果不继续了就设为false旗帜