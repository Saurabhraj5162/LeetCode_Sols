class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # cook your dish here

        n = len(nums)
        ans = 0
        if n==1:
            return 1
        else:
            for i in range(n):
                count = 1
                if nums[i] > 0:
                    next_idx = nums[i]
                    while next_idx != i:#checking if next index is not equal to starting index
                        temp = nums[next_idx]
                        nums[next_idx] = -(nums[next_idx]+1)
                        next_idx = temp
                        count += 1 
                        #print(count)

                ans = max(ans,count)       

            return ans


        
