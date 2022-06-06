
import random

# If no arguments are provided, the function should return a random integer between 0 and 100.
# If only a max number is provided, the function should return a random integer between 0 and the max number.
# If only a min number is provided, the function should return a random integer between the min number and 100
# If both a min and max number are provided, the function should return a random integer between those 2 values.
# 
print("---------1-------------")
def randInt(min = 0,max = 100):
    if max>0 and min<max: 
        if max != 100 and min != 0:
            return round(random.random()*(max-min)+min)
        if min != 0:
            return round(random.random()*(100-min)+min)
        if max != 100:
            return round(random.random()*max)
    else:
        print("Try again, The num should be min > max,and  max < 0")
    return round(random.random()*100)

print(randInt()) # should print a random integer between 0 to 100
print(randInt(max=50)) 	# should print a random integer between 0 to 50
print(randInt(min=50)) 	# should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500


