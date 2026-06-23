class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = {}
        t2 = {}
        for char in s:
            if char not in s1:
                s1[char] = 1
            else:
                s1[char] += 1
        for char in t:
            if char not in t2:
                t2[char] = 1
            else: 
                t2[char] += 1
        return s1 == t2