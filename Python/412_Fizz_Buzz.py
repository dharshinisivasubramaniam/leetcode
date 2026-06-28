class Solution:
    def fizzBuzz(self, num):
        n=[]
        for i in range(1,num+1):
            if(i%3==0 and i%5==0):
                n.append("FizzBuzz")
            elif(i%3==0):
                n.append("Fizz")
            elif(i%5==0):
                n.append("Buzz")
            else:
                n.append(str(i))
        return n
obj=Solution()
obj.fizzBuzz(3)
        
