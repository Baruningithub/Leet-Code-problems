class Solution(object):
    def lengthOfLastWord(s) ->int :
        words = s.split()
        return len(words[-1])
    a="luffy is still joyboy"
    b="   fly me   to   the moon  "
    print(lengthOfLastWord(a))
    print(lengthOfLastWord(b))
#simple two line code 
#Memory Usage: 13.9 MB, less than 80.81% 