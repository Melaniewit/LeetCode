class Solution(object):

    def isAnagram(self, s, t):
        from collections import Counter
        if Counter(s)==Counter(t):
            return True
        else:
            return False