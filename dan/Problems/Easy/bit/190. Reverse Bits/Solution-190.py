class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits1(self, n):
        res = 0
        for _ in xrange(32):
            res = (res << 1) + (n & 1)
            n = n >> 1
        return res
    
    def reverseBits2(self, n):
        m = "{0:032b}".format(n)[::-1]
        return int(m, 2)
    
    #divide and conquer
    def reverseBits(self, n):
        n = ((n & 0x0000ffff) << 16 )| ((n & 0xffff0000) >> 16)
        n = (n & 0x00ff00ff) | (n & 0xff00ff00)
        
    def reverseBits(self, n):
        # For python, there is no 32bit int, so we need to force it 32 bits.
        n = (n >> 16) | (n << 16) & 0xffffffff
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8) & 0xffffffff
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4) & 0xffffffff
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2) & 0xffffffff
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1) & 0xffffffff
        return n
