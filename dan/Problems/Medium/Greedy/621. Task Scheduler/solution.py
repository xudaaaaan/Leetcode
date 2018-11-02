from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c = sorted(Counter(tasks).values())
        max_n = c[-1]
        number_of_max = 1
        i = len(c) - 2
        while i >= 0 and c[i] == max_n:
            number_of_max += 1
            i -= 1
        idles = (max_n - 1) * (n - number_of_max + 1)
        t = sum(c) - number_of_max * max_n
        idles = max(0, idles - t)
        return sum(c) + idles
      
