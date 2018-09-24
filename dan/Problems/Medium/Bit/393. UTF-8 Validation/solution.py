import collections
class Solution(object):
    #String manipulation
    def validUtf81(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        def convert(n):
            byte = bin(n)[2:]
            if len(byte) < 8:
                byte = "0" * (8 - len(byte)) + byte
            elif len(byte) > 8:
                byte = byte[-8:]
            return byte
                
        flag = collections.defaultdict(int)
        for idx, num in enumerate(data):
            byte = convert(num)

            print(byte)
            if flag[idx] == 0:
                ones = 0
                for bit in byte:
                    if bit == "0":
                        break
                    if ones > 3:
                        return False
                    ones += 1
                if ones == 1:
                    return False
                if ones > 1:
                    for i in range(1, ones):
                        flag[idx + i] = 1
                    ones -= 1
                    
            elif byte[0:2] == "10":
                ones -= 1
            else:
                return False
        return False if ones else True
    
    
    #Bit manipulation
    def validUtf8(self, data):
        cnt = 0
        for byte in data:
            if 128 <= byte <= 191:
                if not cnt:
                    return False
                cnt -= 1
                
            else:
                if cnt:
                    return False
                elif byte < 128:
                    continue
                elif byte <= 223:
                    cnt = 1
                elif byte <= 239:
                    cnt = 2
                elif byte <= 247:
                    cnt = 3
                else:
                    return False
        return cnt == 0
