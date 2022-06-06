class Solution(object):
    def isPalindrome(self, x):
        y1=list(str(x))
        y2=list(y1)
        y2.reverse()
        if y1==y2:
            return True
        else:
            return False
num=Solution()
print(num.isPalindrome(122))