class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "Zero"
        a = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        bs = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        res = []
        b = num // 1e9
        if b:
            #print(b)
            res.append(self.numberToWords(b))
            res.append("Billion")
            num -= b * 1e9
        
        m = num // 1e6
        if m:
            #print(m)
            res.append(self.numberToWords(m))
            res.append("Million")
            num -= m * 1e6
            
        t = num // 1e3
        if t:
            #print(t)
            res.append(self.numberToWords(t))
            res.append("Thousand")
            num -= t * 1e3        

        h = num // 100
        if h:
            #print(h)
            res.append( self.numberToWords(h))
            res.append( "Hundred")
            num -= h * 100
            
        if not num:
            return " ".join(res)
             
        if 0 < num < 20:
            res.append(a[int(num)])
        else:
            ten = num // 10
            res.append( bs[int(ten - 2)])
            num -= ten * 10
            if num:
                res.append( a[int(num)])
        #print(res)
        return " ".join(res)
                
            
