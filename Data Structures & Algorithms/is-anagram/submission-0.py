class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_tracker = {}
        for char in s:
            s_tracker.setdefault(char, 0)
            s_tracker[char] += 1
        
        t_tracker = {}
        for char in t:
            t_tracker.setdefault(char, 0)
            t_tracker[char] += 1
        
        return s_tracker == t_tracker
        