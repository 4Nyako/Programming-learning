import random
cont=0
for target_list in range(100):
    if random.randint(0,9)==4 :
        print(random.randint(0,9))
        cont=cont+1
    pass
print(f'{cont}%')