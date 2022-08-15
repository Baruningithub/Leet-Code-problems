


class Solution:
    def romanToInt( s: str) -> int:
        ri = {'I':1,'V':5,'X':10,'L':50,"C":100,'D':500,'M':1000}
        sum=0
        for i in range(len(s)-1):
            if ri[s[i]]<ri[s[i+1]]:
                sum-=ri[s[i]]
            else:
                sum+=ri[s[i]]
        return sum+ri[s[-1]]
    s="LVIII"
    print(romanToInt(s))