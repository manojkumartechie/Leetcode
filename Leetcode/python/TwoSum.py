class Solution:
    class TwoSumSolver:
        def find_two_sum(self, nums: list[int], target: int) -> list[int]:
            seen = {}
            for i, num in enumerate(nums):
                if target - num in seen:
                    return [seen[target - num], i]
                seen[num] = i

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return Solution.TwoSumSolver().find_two_sum(nums, target)

