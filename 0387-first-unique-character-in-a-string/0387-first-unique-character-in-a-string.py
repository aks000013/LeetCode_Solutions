class Solution:
    def firstUniqChar(self, s: str) -> int:
        uni={}

        for word in s:
            if word in uni:
                uni[word] +=1
            else:
                uni[word]=1

        for i in range(len(s)):
            if uni[s[i]]==1:
                return i
        return -1

