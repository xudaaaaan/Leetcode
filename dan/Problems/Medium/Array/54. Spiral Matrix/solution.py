class Solution(object):
    def spiralOrder1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        
        r, c = len(matrix), len(matrix[0])
        
        if r == 1 and c == 1:
            return [matrix[0][0]]
        
        res = []
        
        
        def next_step(i, j, state):
            res.append(matrix[i][j])
           
            if not state:
                return
            else:
                if state == 1:
                    j += 1
                    if i + j == c - 1:
                        state += 1
                        if j - i == c - r:
                            state = 0
                elif state == 2:
                    i += 1
                    if j - i == c - r:
                        state += 1
                        if i + j == r - 1:
                            state = 0
                elif state == 3:
                    j -= 1
                    if i + j == r - 1:
                        state += 1
                        if i - j == 1:
                            state = 0
                elif state == 4:
                    i -= 1
                    if i - j == 1:
                        state = 1 
                        if i + j == c - 1:
                            state = 0
            next_step(i, j, state)
            
        if c > 1:
            s0 = 1
        else:
            s0 = 2

        next_step(0, 0, s0)
        return res
    
    def spiralOrder(self, matrix):
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])

                    
                
            
                
        
