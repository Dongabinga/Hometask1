def make_list(lenght,value=0):
    list=[]
    for i in range(lenght):
        list += [value]
    return list
result = make_list(5,1)
print(result)