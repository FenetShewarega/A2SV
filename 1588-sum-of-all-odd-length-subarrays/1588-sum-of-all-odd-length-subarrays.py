class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # [1,4,2,5,3]
        total=0
        for left in range(len(arr)):
            _sum = 0
            for right in range(left,len(arr)):
                
                _sum += arr[right]
                   
                total += _sum if (right - left+1)  % 2 != 0 else 0
                    
        return total        
                
                
            
     
         
        