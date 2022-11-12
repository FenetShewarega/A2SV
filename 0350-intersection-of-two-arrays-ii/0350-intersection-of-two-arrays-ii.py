class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lis=[]
        dic=defaultdict(int)
        
        for i in range (len(nums1)):
            dic[nums1[i]]+=1
        for j in range(len(nums2)):
            if nums2[j] in dic and dic[nums2[j]] > 0:
                lis.append(nums2[j])   
                dic[nums2[j]]-=1
        return(lis) 
