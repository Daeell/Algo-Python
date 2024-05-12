from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        n = len(senate)

        for i, s in enumerate(senate):
            if s == "R":
                r.append(i)
            else:
                d.append(i)
        
        while r and d:
            ridx = r.popleft()
            didx = d.popleft()

            if ridx < didx:
                r.append(ridx + n)
            else:
                d.append(didx + n)
        
        if r:
            return "Radiant"
        else:
            return "Dire"