class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        group4 = IP.split(".")
        group6 = IP.split(":")
        if len(group4) == 4:
            for unit in group4:
                if not (unit.isdigit() and 0 <= int(unit) <= 255 and str(int(unit)) == unit):
                    return "Neither"
            return "IPv4"
        elif len(group6) == 8:
            for unit in group6:
                if not(0 < len(unit) <= 4 and sum(("0"<=char<="9") or ("a"<=char<="f") or ("A"<=char<="F") for char in unit) == len(unit)):
                    return "Neither"
            return "IPv6"
                    
        else:
            return "Neither"
        
