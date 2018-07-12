class Solution:
    def judgeCircle1(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        status = [0, 0]
        for i in range(len(moves)):
            op = moves[i]
            if op == "R":
                status[0] += 1
            elif op == "L":
                status[0] -= 1
            elif op == "U":
                status[1] += 1
            elif op == "D":
                status[1] -= 1
        return status == [0, 0]
    
    def judgeCircle(self, moves):
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")


