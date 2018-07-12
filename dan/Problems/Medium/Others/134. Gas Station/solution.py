class Solution:
    #Time limit exceeded
    def canCompleteCircuit1(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        def trip(k, remain, determination, flag):
            if remain < 0:
                return False
            if k == determination and flag:
                return True
            if k == len(gas) - 1:
                k = -1
            flag = True
            return trip(k + 1, remain + gas[k] - cost[k], determination, flag)
            
            
        for i in range(len(gas)):
            if trip(i, 0, i, False):
                return i
        return -1
    #Time limit exceeded
    def canCompleteCircuit2(self, gas, cost):
        n = len(gas)
        for i in range(n):
            begin, remains, flag = i, 0, False
            while remains >= 0:
                if flag and i == begin:
                    return i
                remains += (gas[i] - cost[i])
                if i == n - 1:
                    i = -1
                i += 1
                flag = True
        return -1
    
    def canCompleteCircuit(self, gas, cost):
        net = [(gas[i] - cost[i]) for i in range(len(gas))]
        remain, lowest, l_index = net[0], net[0], 0
        for i in range(1, len(net)):
            remain += net[i]
            if remain < lowest:
                lowest = remain
                l_index = i
        if l_index == len(net) - 1:
            l_index = -1
        return l_index + 1 if remain >= 0 else -1


