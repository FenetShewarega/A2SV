class Solution:
    def divisorSubstrings(self, nums: int, k: int) -> int:
             # # 2 4 0
             #   l
             #     r 
            left=0
            count=0
            str_num=str(nums)
            # print (int(num[0:2]))
            left=0
           
            for right in range(k-1,len(str_num)):
                if  int(str_num[left:right+1]) != 0 and( right - left + 1 ==k and nums % int(str_num[left:right+1]) == 0):
                            count+=1
                left+=1
            return count          
     