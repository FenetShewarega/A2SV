class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        def check(random):
            return random[1]
            
        dic=defaultdict()
        lis=[]
        sort_lis=[]
        for i in range(len(names)):
            lis.append((names[i],heights[i]))
        lis.sort(key=check)
        lis.reverse()
        for j in lis:
            sort_lis.append(j[0])
        return sort_lis    