class Solution:

    def check_alnum(self,c):
        return ord('A')<=ord(c)<=ord('Z') or ord('a')<=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9')
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while(i<j):
            while(i<j and not self.check_alnum(s[i])):
                i+=1
            while(j>i and not self.check_alnum(s[j])):
                j-=1
            if i<j:
                if s[i].lower()!=s[j].lower():
                    return False
                i+=1
                j-=1
        return True
        