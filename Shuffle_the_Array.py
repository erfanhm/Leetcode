from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans

solution = Solution()
print(solution.shuffle([1,2,3,2,6,7],3))