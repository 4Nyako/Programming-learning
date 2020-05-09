class human:
    height=0
    weight=0
    def __init__(self,h,w):
        self.height=h
        self.weight=w
    def setHeight(self,h):
        self.height=h
    def setWeight(self,w):
        self.weight=w
    def getHeight(self):
        return self.height
    def getWeight(self):
        return self.weight
    pass

wang=human(175,80.5)
nya=human(135,1)
bmi=wang.getWeight()/(wang.getHeight()**2)
if bmi<18.5:
    print("轻")
elif bmi<25:
    print("正常")
elif bmi<28:
    print('过重')
elif bmi<32:
    print('肥胖')
else:
    print('严重肥胖')
