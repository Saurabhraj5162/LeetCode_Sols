class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = ['a','e','i','o','u']
        ans = 0
        count = 0
        n = len(s)
        
        
        for i in range(k):
            if s[i] in vowels:
                count +=1
        ans = count
        for i in range(k,n):
             
            if s[i] in vowels:
                count +=1
            if s[i-k] in vowels:
                count -=1
            ans = max(count,ans)
        return ans
        
