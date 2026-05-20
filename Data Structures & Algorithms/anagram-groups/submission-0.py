class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=[]
        out = []
        for i in strs:
            a=[0]*26
            for j in i:
                a[ord(j)-ord('a')]+=1
            if a in d:
                out[d.index(a)].append(i)
            else:
                d.append(a)
                out.append([i])
        return out

