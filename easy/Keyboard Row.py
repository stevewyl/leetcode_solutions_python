'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard.
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
'''

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        char_list1 = ['q','w','e','r','t','y','u','i','o','p']
        char_list2 = ['a','s','d','f','g','h','j','k','l']
        char_list3 = ['z','x','c','v','b','n','m']
        out_index = []
        for ii,word in enumerate(words):
            index = []
            word_split = list(set(w.lower() for w in word))
            for char in word_split:
                if char in char_list1: 
                    index.append(1)
                elif char in char_list2:
                    index.append(2)
                else:
                    index.append(3)
            index = set(index)
            if len(index) == 1:
                out_index.append(ii)
        output = [words[ii] for ii in out_index]
        return output