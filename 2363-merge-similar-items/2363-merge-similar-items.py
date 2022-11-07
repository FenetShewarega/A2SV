class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
            dic = {}
            for i in items1:
                dic[i[0]] = i[1]
            for i in items2:
                if i[0] in dic:
                    dic[i[0]] += i[1]
                else:
                    dic[i[0]] = i[1]
            ans = []
            for i in dic:
                temp = [i, dic[i]]
                ans.append(temp)
            ans.sort()
            return ans
                    
                    
                    
        
        
        