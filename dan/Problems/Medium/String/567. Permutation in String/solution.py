class Solution(object):
    #Find all permutations
    def checkInclusion1(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        for char in s1:
            if s1.count(char) > s2.count(char):
                return False
        stack = [("", s1)]
        while stack:
            present, unused = stack.pop()
            if unused == "":
                if present in s2:
                    return True
            else:
                s = set([]) 
                for i, char in enumerate(unused):
                    if not char in s:
                        if i == 0:
                            stack.append((present + char, unused[1:]))
                        elif i == len(unused) - 1:
                            stack.append((present + char, unused[:-1]))
                        else:
                            stack.append((present + char, unused[:i] + unused[i+1:]))
                            
                        s.add(char)
        return False
    #Use a list to store the frequency 
    def checkInclusion(self, s1, s2):
        l1, l2 = len(s1), len(s2)
        if l2 < l1:
            return False
        f1 = [0 for i in range(26)]
        for char in s1:
            f1[ord(char) - ord('a')] += 1
        f2 = [0 for i in range(26)]
        for char in s2[:l1]:
            f2[ord(char) - ord('a')] += 1
        if f2 == f1:
            return True
        
        for i in range(1, l2 - l1 + 1):
            f2[ord(s2[i - 1]) - ord('a')] -= 1
            f2[ord(s2[i + l1 - 1]) - ord('a')] += 1
            if f2 == f1:
                return True
        return False
            
            
        
        
