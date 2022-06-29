class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        n = len(nums)
        min_num = min(nums)
        max_num = max(nums)
        
        if (min_num == max_num):
            return 0
        gap = (max_num - min_num)/(n-1)
        if (max_num - min_num)%(n-1) != 0:
            gap += 1
        
        INT_MIN = -9223372036854775807
        INT_MAX = 9223372036854775807
        
        minA = [INT_MAX]*n
        maxA = [INT_MIN]*n
        
        for i in range(n):
            bkt = int((nums[i] - min_num)//gap)
            minA[bkt] = min(minA[bkt],nums[i])
            maxA[bkt] = max(maxA[bkt],nums[i])
            
        ans = INT_MIN
        prev = INT_MIN
        
        for i in range(n):
            if (minA[i] == INT_MAX ):
                continue
            if (prev == INT_MIN):
                prev = maxA[i]
            else:
                ans = max(ans, minA[i]-prev)
                prev = maxA[i]
                
        return ans
