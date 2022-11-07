class Solution(object):
    def topKFrequent(self, nums, k):
        frequency = {}
        for item in nums:
            if item in frequency:
                frequency[item]=frequency[item] + 1
            else:
                frequency[item] = 1
        
        sort_orders = sorted(frequency.items(), key = lambda x: x[1], reverse=True)
        lst=[]
        count=0
        for key,values in sort_orders:
            if count==k:
                break
            lst.append(key)
            count+=1
        return lst
   
  