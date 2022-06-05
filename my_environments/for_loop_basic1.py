print("---------------------------------------------")
# Basic - Print all integers from 0 to 150.
for x in range(0 , 151 , 1):
    print(x)

print("---------------------------------------------")
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range (5,1000,5):
    x=x*x
print(x)

print("---------------------------------------------")
#Counting, the Dojo Way - Print integers 1 to 100.
#  If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for b in range(1,101):
    if(b %5==0):
        print("Coding")
    if(b %10==0):
        print("Coding Dojo")


print("---------------------------------------------")
# Add odd integers from 0 to 500,000, and print the final sum.
#  odd=0
for o in range (0 , 500000 , 1):
    if o % 2 != 0:
        # print(x)
        o = o+o
print(o)


print("---------------------------------------------")
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for down in range(2018,0 ,-4):
    print(down)



print("---------------------------------------------")
# Flexible Counter - Set three variables: lowNum, highNum, mult. 
# Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum=2
highNum=9
mult=3
for FlexibleCounter in range (lowNum , highNum +1):
    if FlexibleCounter%mult==0:
        print(FlexibleCounter)
