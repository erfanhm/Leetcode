from typing import List
class Solution:
    def two_sum (self, nums: List[int],target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
        return []

tSum = Solution()
print(tSum.two_sum([2,4,7,9], 9)) 