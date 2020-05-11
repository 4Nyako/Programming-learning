import math

'''
计算圆的面积
:return:没有！
'''
def 输出好多个圆的面积(r_list):
    for r in r_list:
        print(math.pi*r*r)

def 输出好多个信息(inf_dict):
    for inf_key in inf_dict.keys():
        print(f'猫猫的{inf_key}是{inf_dict[inf_key]}')


inf_dict={'脑浆':'会喵喵叫的','电梯':'美味的'}
输出好多个信息(inf_dict)