from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + nums
        for i in range (len(nums)):
            if not ans[i] == nums[i] and ans[i+len(nums)] == nums[i]:
                return []
            return ans
solution = Solution()
print(solution.getConcatenation([1,3,4,5]))