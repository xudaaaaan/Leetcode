class Solution:
    # Time limit exceed
    def findPoisonedDuration1(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        s = set([])
        for ele in timeSeries:
            for t in range(duration):
                s.add(ele + t)
        return len(s)
        
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        t = duration
        for i in range(1, len(timeSeries)):
            t += min(duration, timeSeries[i] - timeSeries[i - 1])
        return t

