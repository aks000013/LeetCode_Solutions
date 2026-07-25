class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal=[]
        for word in s:
            if word.isalnum():
                pal.append(word.lower())
        return pal == pal[::-1]
       


            


