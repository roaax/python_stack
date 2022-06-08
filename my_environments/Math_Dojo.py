class MathDojo:

    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result+= num
        if len(nums)>= 0 :
            for i in nums:
                self.result += i
        return self
    def subtract(self, num, *nums):
        self.result -= num
        if len(nums) >= 0 :
            for i in nums:
                self.result -= i
        return self


# to create an instance:
Ajwan = MathDojo()
Roaa = MathDojo()
#----------------------------
Ajwan = Ajwan.add(5).add(3,10,2).subtract(4,3).result
print(Ajwan) 
#----------------------------
x =Roaa.add(20).add(3,9,2).add(6,2).subtract(8,3).subtract(6).subtract(4,3,2).result
print(x)	
