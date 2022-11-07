class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # lis=[]
        mx = -1
        dic=defaultdict(int)
        
        for i in nums :
            
            sumOfDigits = 0
            
            for digit in str(i) :
                sumOfDigits += int (digit)
            
            if sumOfDigits in dic :
                dic[sumOfDigits] += [i]
                
            else :
                dic[sumOfDigits] = [i]
                
        res = -1

        for i in dic.values() :
            if  len(i) >= 2:
                res = max( res , sum(sorted(i,reverse=True)[0:2]) ) 


        return res
        
  
                
   