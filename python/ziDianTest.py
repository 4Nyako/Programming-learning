a={}
a['脑壳']=1
a['青蛙']='喵喵叫'
print(a)
a['frog']=a
print(sorted(a.items(),key=lambda d: d[0]))
# print(sorted(a.items(),key=lambda d: d[1]))
