class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        while i < len(arr):
            if arr[i] == 0 :
                if i == len(arr) - 1:
                    pass
                arr.pop()
                arr.insert(i+1,0)
                i+=2
                
            else:
                i+=1