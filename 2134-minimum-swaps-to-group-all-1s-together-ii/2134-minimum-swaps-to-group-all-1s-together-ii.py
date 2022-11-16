class Solution:
    def minSwaps(self, nums: List[int]) -> int:
#         one=0
#         zero=0
#         count_1=0
#         count_0=0
        
#         mn=len(nums)+1
#         counter=defaultdict(int)
#         for x in range(len(nums)):
#             if nums[x] == 1:
#                 one+=1
#             else:
#                 zero+=1
#         print(one)       
#         j=0      
#         for i in range(len(nums)):
#             if nums[i] == 1:
#                 count_1+=1
#             if nums[i] == 0:
#                 count_0+=1
#             print(count_0)
#             if i - j + 1 >= one:
#                 if j == 1:
#                     count_1-=1
#                 else:
#                     count_0-=1
#                 j+=1    
#             mn=min(count_0,mn)
        # return mn    
    
        ones = nums.count(1)    # Time: O(N)
        nums = nums + nums
        ones_in_window = 0
        res = 0
        for i in range(len(nums)):      # Time: O(N)
            if i >= ones:
                ones_in_window -= nums[i - ones]
            ones_in_window += nums[i]
            res = max(ones_in_window, res)

        return (ones - res)
                