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
    
