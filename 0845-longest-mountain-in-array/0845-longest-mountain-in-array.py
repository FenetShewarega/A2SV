class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rt    ype: int
        """
        length = len(arr)
        left=0
        mountain=0
        while left < length:
            while left < length-1 and arr[left] >= arr[left+1]:
                left+=1
            right=left+1
            while right < length-1 and arr[right] < arr[right+1]:
                right+=1
            while right < length-1 and arr[right] > arr[right+1]:
                right+= 1
                mountain=max(mountain,right-left+1)
            left =right
        return mountain   
    