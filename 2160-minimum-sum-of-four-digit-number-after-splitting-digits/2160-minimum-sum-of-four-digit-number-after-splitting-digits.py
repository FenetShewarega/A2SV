class Solution:
    def minimumSum(self, num: int) -> int:
            s = " "
            st = [int(x) for x in str(num)]

            for i in range(len(st)):
                for j in range(i,len(st)):
                    if st[i] > st[j] :
                        st[i],st[j] = st[j],st[i]
            # print (st)            
            s = int( str(st[0]) + str(st[2]) ) + int( str(st[1])+ str(st[3]))
            return s
