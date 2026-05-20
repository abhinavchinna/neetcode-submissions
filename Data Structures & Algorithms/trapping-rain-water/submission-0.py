class Solution:
    def trap(self, height: List[int]) -> int:
        l=[]
        m=0
        for i in height:
            if i>m:
                m=i
            l.append(m)
        # print(l)
        r=[0]*len(height)
        m=0
        for i in range(len(height)-1,-1,-1):
            if height[i]>m:
                m=height[i]
            r[i]=m
        # print(r)
        f=[]
        for i in range(len(height)):
            f.append(min(l[i],r[i])-height[i])
        # print(f)
        return sum(f)
            
                
            

        