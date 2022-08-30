class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        h = n-1
        while (l<=h):
            m = (l+h)//2
            
            if n == 1:
                return 0
            
            
                
            elif m == 0:
                if nums[m]>=nums[m+1]:
                    return m
                else:
                    l = m+1
            elif m == n-1:
                if nums[m] >= nums[m-1]:
                    return m
                else:
                    h = m-1
            elif nums[m]>=nums[m-1] and nums[m]>=nums[m+1]:
                return m
            elif nums[m-1] > nums[m] and nums[m+1] < nums[m]:
                # if m-1 == 0:
                #     return m-1
                h = m-1
            elif nums[m+1] > nums[m] and nums[m-1] < nums[m]:
                # if m+1 == n-1:
                #     return m+1
                l = m+1
                
            else:
                h = m-1
        
        
