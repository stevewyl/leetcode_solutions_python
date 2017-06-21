'''
Example:
Given s = "hello", return "olleh".
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = [s[-i] for i in range(1,len(s)+1)]
        return ('').join(result)
        
        #return s[::-1]