def make_list(lenght,value=0):
    list=[]
    for i in range(lenght):
        list += [value]
    return list
def make_matrix(width,height=0,value=0):
    if height == 0:
        height=width
    matrix=[]
    for i in range(height):
        matrix +=[make_list(width,value)]
    return matrix
result = make_matrix(4,2,1)
print(result)