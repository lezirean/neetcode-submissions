class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_tracker, t_tracker = {}, {}
        for idx in range(len(s)):
            s_tracker[s[idx]] = s_tracker.get(s[idx], 0) + 1
            t_tracker[t[idx]] = t_tracker.get(t[idx], 0) + 1
        
        return s_tracker == t_tracker
        