class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = int(a,2)+int(b,2)
        ans=bin(sum)
        #to remove 0b from ans string(since bin(int) gives "0b10101")
        return ans[2:]

#Runtime: 35 ms, faster than 92.35%
#Memory Usage: 13.8 MB, less than 72.92%