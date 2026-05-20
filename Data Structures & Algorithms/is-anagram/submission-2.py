class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[0]*26
        for i in s:
            a[ord(i)-ord('a')]+=1
        for i in t:
            a[ord(i)-ord('a')]-=1
        if a ==[0]*26:
            return True
        return False
