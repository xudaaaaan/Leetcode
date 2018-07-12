class Solution:
    # Time limit exceed
    def countPrimes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        res = [1] * (n + 1)
        res[0], res[1], res[2] = 0,0,1
        
        def isPrime(num):
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
        
        for i in range(3,n + 1):
            if not isPrime(i):
                res[i] = 0
        return sum(res[:n])
    
    
    #2 3 5 7 11...
    def countPrimes(self, n):
        if n < 3:
            return 0
        a = [1] * n
        b = [0] * n
        a[0], a[1] = 0, 0
        """for i in range(2,(n - 1) // 2 + 1):
            for j in range(i,(n - 1) // i + 1):
                a[i * j] = 0"""
        for i in range(2, int((n - 1) ** 0.5) + 1):
            if a[i]:
                a[i * i : n : i] = b[i * i : n : i]
        return sum(a)
                
