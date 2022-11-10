class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:     
            i = 1
            lis=[]
            x=[]
            mx=len(nums) +1
            total=0
            for i in range(len(nums)):
                total+=nums[i]
                lis.append(total)
            n=len(lis) - 1  
            r=0 
            while r <= n: 
                left = lis[r]//(r+1)
                if r < n:
                    right = (lis[n] - lis[r])//(n - r)
                else:
                    right = 0
                ans = abs(left - right)
                x.append(ans)
                r += 1
            return x.index(min(x))      
                
            
        
        
                
           
            
            
        