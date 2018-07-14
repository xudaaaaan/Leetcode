class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res, dic, k = [], {}, 0
        for word in strs:
            word_s = "".join(sorted(word))
            if not word_s in dic:
                dic[word_s] = k
                res.append([])
                res[k].append(word)
                k += 1
            else:
                res[dic[word_s]].append(word)
        return res
                
