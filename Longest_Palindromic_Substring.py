from itertools import permutations

class Solution:
    
    def longestPalindrome( self,s: str) -> str:
        l = self.allPermutations(s)
        
        for i in l:
            if self.isPallindrome(i):
                return i
        return ""
    def isPallindrome(self,s:str):
        return s==s[::-1]
    def allPermutations(self,str):
     permList = permutations(str)
     for perm in list(permList):
         return (''.join(perm))
    s="abab"
    print(longestPalindrome(s))