class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        j, s, S = 0, list(s)+[''], []
    	while s[j]:
    		if s[j] == '(': S.append(j)
    		elif s[j] == ')':
    			i = S.pop()
    			s, j = s[0:i]+s[i+1:j][::-1]+s[j+1:], i-1
    		j += 1
    	return "".join(s)