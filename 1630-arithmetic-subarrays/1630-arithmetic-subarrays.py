class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            temp = []
            for j in range(l[i],r[i]+1):
                temp.append(nums[j])
            temp = sorted(temp)
            diff_list=[]
            for k in range(1,len(temp)):
                diff = temp[k] - temp[k-1]
                diff_list.append(diff)
            if diff_list.count(diff_list[0]) == len(diff_list):
                result.append(True)
            else:
                result.append(False)
        return result
        