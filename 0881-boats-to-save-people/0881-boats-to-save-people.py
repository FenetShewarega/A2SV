class Solution(object):
    def numRescueBoats(self, people, limit):
        # bo=[3,1,2,2]
        people=sorted(people)
        # limit=3
        count =0
        i=0
        j=len(people)-1
        while i <= j:
            count = count+1
            if people[i]+people[j] <= limit:
                i+=1
            j-=1
        return(count)    

        