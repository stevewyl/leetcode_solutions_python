'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
'''

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        new = []
        num = bin(num)[2:]
        for n in num:
            if n == '1':
                new.append('0')
            elif n == '0':
                new.append('1')
        complement = int(('').join(new),2)
        
        return complement