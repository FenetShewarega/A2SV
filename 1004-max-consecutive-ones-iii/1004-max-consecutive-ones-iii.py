class Solution: 
    def longestOnes(self, num: List[int], k: int) -> int:
        
        # [1,1,1,0,0,0,1,1,1,1,0]
        #            l
        #                       r
        left =0
        right =0
        mx=0
        for  right  in range(len(num)):
            while k <= 0 and num[right] == 0:
                if num[left] == 0:
                    k+=1
                left+=1    
            mx=max(mx,right-left+1)
            if num[right] == 0:
                k-=1
                
        return mx       
                
                
            
            
            