
# 1-Update Values in Dictionaries and Lists
print("-------------1-----------------")
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# first_name - Michael, last_name - Jordan
#         first_name - John, last_name - Rosales
#         first_name - Mark, last_name - Guillen
#         first_name - KB, last_name - Tonel

#     # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)


# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name']='Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]='Andres'
print(sports_directory)


# Change the value 20 in z to 30
z[0]['y']=30
print(z)

# 2-Iterate Through a List of Dictionaries
print("-------------2-----------------")
studentss= [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(studentss):
    for x in studentss:
        return(studentss)
print(iterateDictionary(studentss))


# 3-Get Values From a List of Dictionaries
print("-------------3-----------------")

def iterateDictionary2(key_name, studentss):
    for x in studentss:
        print(x[key_name])
print("------first names ----")
iterateDictionary2('first_name', studentss)
print("------last names ----")
iterateDictionary2('last_name', studentss)


print("-------------4-----------------")
# 4-Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(_dict):
    for x in _dict:
        print(len(_dict[x]), x.upper())
        for i in _dict[x]:
            print(i)
        print("")

printInfo(dojo)