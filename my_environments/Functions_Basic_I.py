print("-------------1-----------")
#1
def a():
    return 5
print(a())
# Output:5

print("-------------2-----------")
#2
def a():
    return 5
print(a()+a())
# Output:10

print("-------------3-----------")
#3
def a():
    return 5
    return 10
print(a())
# Output:5

print("-------------4-----------")
#4
def a():
    return 5
    print(10)
print(a())
# Output:5

print("-------------5-----------")
#5
def a():
    print(5)
x = a()
print(x)
# Output:5
# None

print("-------------6-----------")
# 6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3)) 
# # Output:3
# 5
# unsupported operand type(s) for +: 'NoneType' and 'NoneType

print("-------------7-----------")
#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# Output:25

print("-------------8-----------")
#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# Output:100
# 10

print("-------------9-----------")
#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# Output:7
# 14
# 21

print("-------------10-----------")
#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# Output:8

print("-------------11-----------")
#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# Output:500
# 500
# 300
# 500

print("-------------12-----------")
#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# Output:500
# 500
# 300
# 500

print("-------------13-----------")
#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# Output:500
# 500
# 300
# 300

print("-------------14-----------")
#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# Output:1
# 3
# 2

print("-------------15-----------")
#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# Output:1
# 3
# 5
# 10