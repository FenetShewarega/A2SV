class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        lis=[]
        check=0
        for i in range(left,right+1):
            for j,k in ranges:
                if j<=i<= k:
                    check+=1
                    break
                    
        return check==(right-left)+1                
                