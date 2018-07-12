class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = "1"
        for _ in range(n - 1):
            temp, cnt, let = "", 0, seq[0]
            for l in seq:
                if l == let:
                    cnt += 1
                else:
                    temp += (str(cnt) + let)
                    let = l
                    cnt = 1
            seq = temp + (str(cnt) + let)
        return seq
    
                
                    
            



