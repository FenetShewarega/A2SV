class Solution:
    def findOriginalArray(self, changed: List[float]) -> List[float]:
        if not changed or len(changed) % 2 == 1:
            return []
        from collections import Counter
        num2cnt = Counter(changed)
        
		# NlogN
        sorted_nums = sorted(changed)
        small_nums = []
        for num in sorted_nums:
            if num not in num2cnt:
                continue
            doubled_num = num * 2
            if doubled_num not in num2cnt:
                return []
            
            small_nums.append(num)
            num2cnt[num] -= 1
            if num2cnt[num] == 0:
                del num2cnt[num]
            num2cnt[doubled_num] -= 1
            if num2cnt[doubled_num] == 0:
                del num2cnt[doubled_num]
        
        return small_nums

         
        
        