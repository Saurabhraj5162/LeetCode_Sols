from functools import cmp_to_key
class point:
    def __init__(self,x,y,d):
        self.x = x
        self.y = y
        self.d = d
        
    def __repr__(self):
        return {'x':self.x, 'y':self.y, 'd':self.d}
    
    def com(p1,p2):
        if p1.d != p2.d:
            return p1.d - p2.d
        return p1.d
        

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        v = []
        for p in points:
            cur_point = point(p[0],p[1],p[0]*p[0] + p[1]*p[1])
            v.append(cur_point)
        ans = sorted(v,key = cmp_to_key(point.com))
        ans = ans[:k]
        op = []
        for i in ans:
            op.append([i.x,i.y])
        #print(op)
        
        return op   
            
        
        
