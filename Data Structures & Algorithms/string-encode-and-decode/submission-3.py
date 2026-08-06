class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ''
        for word in strs:
            newStr += (word + "\n")
        return newStr
        
        

    def decode(self, s: str) -> List[str]:
        out = []
        word = ''
        for c in s:
            if c != '\n':
                word += c
            else:
                out.append(word)
                word = ''
        return out

