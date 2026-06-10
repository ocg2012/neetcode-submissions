class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans=0
        for i in piles:
            ans=max(ans,i)
        l=1
        r=ans
        while l<=r:
            m=l+(r-l)//2
            count=0
            for i in range(len(piles)):
                count+=math.ceil(piles[i]/m)
            print(l,r)
            print(m)
            if count<=h:
                ans=m
                r=m-1
            elif count>h:
                l=m+1
            # else:
            #     return m
        return ans
