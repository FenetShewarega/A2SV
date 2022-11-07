class Solution:
    def kthLargestNumber(self, a: List[str], k: int) -> str:
        b=[]
        for i in a:
            b.append(int(i))
        b.sort()    
        return(str(b[len(a)-k]))