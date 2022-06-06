
print("------------------Selection Sort---------------------")
list=[8,5,2,6,9,3,1,4,0,7]
print("List befor sort ", list )
def Sort(list):
    for j in range(len(list)-1):
        for i in range(len(list)-1-j):
            if list[i]> list[i+1]:
                list[i], list[i+1]= list[i+1], list[i]
    return list
print("List after sort ", Sort(list) )
