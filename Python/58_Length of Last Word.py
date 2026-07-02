class Solution:
    def lengthOfLastWord(self, s):
        a=[]
        for i in s.split():
            a.append(i)
        return len(a[-1])
obj=Solution()
obj.lengthOfLastWord("Hello world")


        
