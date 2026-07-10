class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        u: given a string s, find the len of the longest contiguous substring 
        without duplicates in the substring
        so for example, abcabcabc, the answer would be abc because it
        has completely unique chars and it's the longest.
        return the length, not the substring.

        m: we use a sliding window to keep track of the substring. we can
        use a set to keep track of the chars, and pointers to mark the 
        edges of the windows. 

        p: so basically, we initialize the l pointer = 0, and we use
        a for loop with r as the index. one pass through
        we use a set called seen.
        initialize maxlen
        we start the for loop 
            if s[r] in seen:
                we get 
                maxlen(maxlen, r-l)
                make l = r + 1
                seen.clear()
            else:
                add s[r] to set
        check maxlen again
        return maxlen
        '''
        l = maxlen = 0
        seen = set()
        r = 0
        while r < len(s):
            if s[r] in seen:
                maxlen = max(maxlen, r - l)
                l += 1
                r = l 
                seen.clear()
            else:
                seen.add(s[r])
                r += 1
        maxlen = max(maxlen, r - l)
        return maxlen
        '''
        seen ()
        p w w k e w
              l
            r
        maxlen = 2

        seen (d)
        d v d f
        l
            r
        maxlen = 2
        '''

            