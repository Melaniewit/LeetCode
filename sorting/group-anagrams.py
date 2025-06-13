class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        dict_list=defaultdict(list)
        for s in strs:
            key="".join(sorted(s))
            dict_list[key].append(s)
        return list(dict_list.values())