class Solution(object):
     def nextGreaterElement(self, nums1, nums2):
            ans = [-1]* len(nums1)
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    for j in range(nums2.index(nums1[i]) , len(nums2)):
                        if nums2[j] > nums1[i]:
                            ans[i] = nums2[j]
                            break
            return ans
       
        