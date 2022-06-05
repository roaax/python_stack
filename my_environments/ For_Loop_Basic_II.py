def Biggie_Size(list):
    for x in range(len(list)):
        if list[x]>0:
            list[x]="big"
    return list
print(Biggie_Size([-1, 3, 5, -5]))


print("--------2----------")
def Count_Positives(list):
    count=0
    for x in range(len(list)):
        if list[x]>0:
            count = count + 1
    list[len(list)-1]=count
    return (list)
print(Count_Positives([-1,1,1,1]))
# print(Count_Positives([-1,1,1,1]))

print("--------3----------")

def Sum_Total(list):
    sum=0
    for x in range(len(list)):
        sum= sum+list[x]
    return sum
print(Sum_Total([1,2,3,4]))
print(Sum_Total([6,3,-2]))

print("--------4----------")
def Average(list):
    sum=0
    for x in range(len(list)):
        sum =list[x]+sum
    return sum/len(list)
print(Average([1,2,3,4]))

print("--------5----------")
def Length(list):
    count=0
    # return len(list)
    for x in list:
        count +=1
    return count
print(Length([37,2,1,-9]))

print("--------6----------")
def Minimum(list):
    if len(list)==0:
        return False
    for x in range(len(list)):
        mini = list[0]
        if (list[x]<mini):
            mini=list[x]
    return mini
print(Minimum([37,2,1,-9]))
print(Minimum([]))

print("--------7----------")
def Maximum(list):
    if len(list)==0:
        return False
    for x in range(len(list)):
        maxi = list[0]
        if (list[x]>maxi):
            maxi=list[x]
    return maxi
print(Maximum([37,2,1,-9]))
print(Maximum([]))

print("--------8----------")
def Ultimate_Analysis(list):
    _dictionary = {
            'sumTotal': [0],
            'average': [0],
            'minimum': [0],
            'maximum': [0],
            'length': [0]}
    _dictionary.update({"sumTotal" : Sum_Total(list)})
    _dictionary.update({"average" : Average(list)})
    _dictionary.update({"minimum" : Minimum(list)})
    _dictionary.update({"maximum" : Maximum(list)})
    _dictionary.update({"length" : Length(list)})
    return _dictionary
print(Ultimate_Analysis([37,2,1,-9]))


    # Example: ultimate_analysis([37,2,1,-9])
    #  should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

print("--------9----------")
def Reverse_List(list):
    return list[::-1]
print(Reverse_List([37,2,1,-9]))