# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        buf4 = [""] * 4
        idx = 0
        while n > 0:
            r = read4(buf4)
            cnt = min(r, n)
            buf[idx:(idx+cnt)] = buf4[:cnt]
            idx += cnt
            n -= cnt
            if r < 4:
                break
        return idx


