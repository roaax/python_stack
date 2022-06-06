from re import I


print("------------------Selection Sort---------------------")
list=[8,5,2,6,9,3,1,4,0,7]
print("List befor iteration sort ", list )
def Iteration(list):
    for i in range(1 , len(list)):
        j = i
        while list[j -1 ] > list[j] and j>0:
            list[j-1], list[j], list[j- 1]
            j -= 1
Iteration(list)
print("List after sort ", list )
