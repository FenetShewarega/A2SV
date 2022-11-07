class Solution(object):
    def minSetSize(self, arr):
        half = len(arr) / 2 
        count=0
        response =0
        D = {}
        for a in arr:
            if a not in D:
                D[a] = 1
            else:
                D[a]+=1
        D = sorted(D.items(), key = lambda x: x[1], reverse = True)
        cnt = 0
        res = 0
        for k, v in D:
            cnt += v
            res +=1
            if cnt >= half:
                break
        return res
        