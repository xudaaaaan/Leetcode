# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
from collections import deque
class Solution(object):
    def __init__(self):
        self.queue = deque()
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while n > 0 and self.queue:
            buf[idx] = self.queue.popleft()
            idx += 1
            n -= 1
        buf4 = [""] * 4
        while n > 0:
            r = read4(buf4)
            cnt = min(r, n)
            buf[idx:idx + cnt] = buf4[:cnt]
            idx += cnt
            n -= cnt
            if n == 0 and r - cnt > 0:
                for i in range(cnt, r):
                    self.queue.append(buf4[i])
            if r < 4:
                break
        return idx
        
