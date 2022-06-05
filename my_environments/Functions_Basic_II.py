print("-------------1--------------")
def Countdown(x):
    return list( range (x,0,-1))
print(Countdown(5))

print("-------------2--------------")
def Print_and_Return(list):
    print(list[0])
    return (list[1])
print(Print_and_Return([1,2]))


print("-------------3--------------")
def First_Plus_Length(list):
    return len(list) + list[0]
print(First_Plus_Length([1,2,3,4,5]))


print("--------------4-------------")
def Values_Greater_than_Second(list):
    newList=[]
    if len(list)<2:
        return False
    for x in list:
        if (x> list[1]):
            newList.append(x)
    print(len(newList))
    return newList
    
        
print(Values_Greater_than_Second([5,2,3,2,1,4]))
    
print("-------------5--------------")
def length_and_value(size , value):
    list=[]
    for x in range(size):
        list.append(value)
    return list
print(length_and_value(4,7))