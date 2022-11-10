class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
            hold=0
            nums.sort()
            j=1    
            for i in nums:
                j = abs(i)
                if nums[j]  < 0:
                    dup = j 
                    break
                nums[j] =- nums[j]    
            for n in range(len(nums)):
                nums[n] = abs(nums[n])
            return dup 
                # while   nums[i] == nums[j]:
                #     return (nums[i])

            #                 j+=1
                     # [1,3,4,3,2]
                     #      l 
                     #        r
                     #  h=1+3   
                     # for num in nums:
                     #    cur = abs(num)
                     #    if nums[cur] < 0:
                     #        duplicate = cur
                     #        break
                     #    nums[cur] = -nums[cur]

                    # Restore numbers
      