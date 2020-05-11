def sum(*n_list):
    s=0
    for n in n_list:
        s+=n
    return(s)
def qiMathBit(n_list):
    return n_list[1::2]
def save2GeValueDeChar(**n_list):
    for key in n_list.keys():
        if len(n_list[key])>2:
            n_list[key]=n_list[key][:2]
    return(n_list)
print(save2GeValueDeChar(第一个='abcd',第二个='ff'))