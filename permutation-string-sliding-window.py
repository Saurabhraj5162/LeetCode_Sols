class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alphVect = "abcdefghijklmnopqrstuvwxyz"
        k = len(s1)
        n = len(s2)
        count = 0
        maxc = 0
        idx = {}
        s1map = [0]*26
        s2map = [0]*26
        
        if n < k:
            return False
        
        for i in range(k):
            s1map[alphVect.find(s1[i])] += 1
            s2map[alphVect.find(s2[i])] += 1
            
        if s1map == s2map:
            return True
        
        
        for i in range(k,n):
            
            s2map[alphVect.find(s2[i])] += 1
            s2map[alphVect.find(s2[i-k])] -= 1
            if s1map == s2map:
                return True
          
                    
        return False
        
        
