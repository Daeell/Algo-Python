class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, zero_count, res = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            res = max(res, right - left + 1 - zero_count)
        
        return res - 1 if res == len(nums) else res
