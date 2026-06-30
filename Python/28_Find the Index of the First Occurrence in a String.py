class Solution:
    def strStr(self, haystack: str, needle: str) :
        try:
          return haystack.index(needle)
        except ValueError:
          return -1
obj=Solution()
obj.strStr("sadbutsad","sad")
        
