class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        return group(strs)
        
def hash_function(s):
    string = ""
    for c in sorted(s):
        string+=c
    return string

def group(strs):
    dictionary = {}
    for i in strs:
        h_i = hash_function(i)
        
        if h_i in dictionary:
            dictionary[h_i].append(i)
        else:
            dictionary[h_i] = [i]
    answer = []
    for k in dictionary:
        answer.append(dictionary[k])
    return answer