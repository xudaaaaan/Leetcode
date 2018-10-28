class Solution(object):
    def nextClosestTime1(self, time):
        """
        :type time: str
        :rtype: str
        """
        def is_legit(h, m):
            return 0 <= h < 24 and 0 <= m < 60

        def distance(h, m, h0, m0):
            t1 = h * 60 + m
            t2 = h0 * 60 + m0
            t = t1 - t2
            if t > 0:
                return t
            else:
                return 24 * 60 + t
                
            
            
        dis = float('inf')
        res = ""
        digits = time[:2] + time[3:]
        h0, m0 = int(time[:2]), int(time[3:])
        for a in digits:
            for b in digits:
                for c in digits:
                    for d in digits:
                        hour = int(a + b)
                        minute = int(c + d)
                        if is_legit(hour, minute):
                            dist = distance(hour, minute, h0, m0)
                            if dist < dis:
                                dis = dist
                                res = a + b + ":" + c + d
        return res   
    
    def nextClosestTime(self, time):
       
        return min((t <= time, t) \
                   for i in range(24 * 60) \
                  for t in ["%02d:%02d" % divmod(i, 60)] \
                  if set(t) <= set(time))[1]
    
    


