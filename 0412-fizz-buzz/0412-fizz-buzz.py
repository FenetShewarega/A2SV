class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        c=[]
        for i in range (1,n+1):
            if i%3==0 and i%5==0:
                c.append ("FizzBuzz")
            elif i%5==0:
                c.append ("Buzz")
            elif i%3==0:
                c.append("Fizz")
            else:
                i=str(i)
                c.append(i)
        return (c)       
        