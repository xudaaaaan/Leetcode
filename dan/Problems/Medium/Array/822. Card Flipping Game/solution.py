class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        cards = zip(fronts, backs)
        s = set()
        discard = set()
        for i in cards:
            if not i[0] == i[1]:
                s.add(i[0])
                s.add(i[1])
            else:
                discard.add(i[0])
        try: return min(s - discard)
        except: return 0
    
        
