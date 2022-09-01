
from functools import cmp_to_key
class Solution:
    def com(self,t1,t2):
        return t1[1]-t2[1]
    
    def customSortString(self, order: str, s: str) -> str:
        rank = [10000000]*26
        
        for i in range(len(order)):
            rank[ord(order[i])-ord('a')] = i
        
        v = []
        
        for i in range(len(s)):
            v.append([s[i],rank[ord(s[i])-ord('a')]])
        
        ans = sorted(v,key = cmp_to_key(self.com))
        op = ''
        for i in ans:
            op += i[0]
            
        #print(op)
        return op
        
