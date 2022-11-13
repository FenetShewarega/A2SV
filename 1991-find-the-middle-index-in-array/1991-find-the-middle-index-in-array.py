class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
                total=0
                ans = 0
                pre_sum=[]
                suffix=[]
                for i in nums:
                    total+=i
                    pre_sum.append(total)    
                for j in range(len(nums)-1,-1,-1):
                    ans+=nums[j]
                    suffix.append(ans)    
                n=0   
                for m in range(len(pre_sum)):
                        if pre_sum[m]== suffix[len(nums)-n-1]:
                            return m
                            break
                        n+=1
                return -1        