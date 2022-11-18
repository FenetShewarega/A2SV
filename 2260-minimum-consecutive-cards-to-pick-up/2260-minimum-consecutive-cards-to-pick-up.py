class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        right = 0
        counter=defaultdict(int)
        mn= len(cards)+1
        while right < len(cards):
            if cards[right] in counter:
                count=right-counter[cards[right]]
                counter[cards[right]]= right
                mn=min(count,mn)  
            else:             
                counter[cards[right]]=right 
                
            right+=1 
            
        return mn+1 if mn != len(cards)+1 else -1    
    
#         d={}
#         x=[]
#         for i in range(len(cards)):
#             if cards[i] not in d:
#                 d[cards[i]]=i
#             else:
#                 x.append(i-d[cards[i]])
#                 d[cards[i]]=i
#         if len(x)<=0:
#             return -1
#         return min(x)+1
    
#     [3,4,2,3,6,3,4,7]