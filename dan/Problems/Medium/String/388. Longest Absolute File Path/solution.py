import collections
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlen, pathlen = 0, {0:0}
        for line in input.splitlines():
            filename = line.lstrip("\t")
            depth = len(line) - len(filename)
            if "." in filename:
                maxlen = max(maxlen, pathlen[depth] + len(filename))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(filename) + 1
        return maxlen
       
