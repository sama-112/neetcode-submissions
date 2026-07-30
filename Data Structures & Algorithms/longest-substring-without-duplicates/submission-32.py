class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0 
        letters = {}
        maxSub = 0
        i = 0
        
        while i < len(s):
            count+=1
            letters[s[i]] = i
            if (i+1 < len(s) and s[i+1] in letters):
                maxSub = count if count > maxSub else maxSub
                restart_index = letters[s[i+1]]
                letters.clear()
                count = 0
                i = restart_index + 1
                continue
            elif i+1 == len(s):
                maxSub = count if count > maxSub else maxSub
                i+=1
            i+=1
       
        return maxSub