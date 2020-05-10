test='hello python '
print(f'首字母大写：{test.capitalize()}')
print(f'去除空格：{test.strip()}')
print(f'去除右空格：{test.rstrip()}')
a=test.find('y')
print(f'查找test中的y：{a}')
print(test[-2:])
print(test)