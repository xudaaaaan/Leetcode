# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints1(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        dic, res = {}, 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                k, b = self.generate_line(points[i].x, points[i].y, points[j].x, points[j].y)
                dic[(k, b)] = dic.get((k, b), 0) + 1
                res = max(res, dic[(k, b)])
        return res
                       
                   
    def generate_line(self, x1, y1, x2, y2):
      
        if x1 == x2:
            k = float('inf')
            b = x1
        else:
            k = (y2 - y1) / (x2 - x1)
            b = y1 - k * x1
        return (k, b)
    
    def gcd1(self, a, b):
        if a < b:
            a, b = b, a
        if b == 0:
            return a
        return self.gcd1(a - b, b)
    
    def gcd(self,a,b):
        if(b==0):
            return a
        else:
            return self.gcd(b,a%b)
    
    def maxPoints(self, points):
        l = len(points)
        m = 0
        for i in range(l):
            dic = {'i': 1}
            same = 0
            for j in range(i+1, l):
                tx, ty = points[j].x, points[j].y
                if tx == points[i].x and ty == points[i].y: 
                    same += 1
                    continue
                if points[i].x == tx: 
                    slope = 'i'
                else:
                    #slope = (points[i].y-ty) * 1.0 /(points[i].x-tx)
                    g = self.gcd(points[i].y - ty, points[i].x - tx)
                    slope = ((points[i].y - ty) // g, (points[i].x - tx) // g)
                    
                if slope not in dic: 
                    dic[slope] = 1
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)
        return m
