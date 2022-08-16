class Solution:
    def plusOne( self,digits: list[int]) -> list[int]:
        if digits==[]:
            return [1]
        elif digits[-1]==9:
            digits=self.plusOne(digits[:-1])+[0] 
        else:
            digits[-1]+=1
        return digits
#Runtime: 44 ms, faster than 69.98% 
    
