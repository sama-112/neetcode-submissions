class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       strDict = {}
       for s in strs:
        if ''.join(sorted(s)) not in strDict:
            strDict[''.join(sorted(s))] = [s]
        else:
            strDict[''.join(sorted(s))].append(s)
       

       return list(strDict.values())
        