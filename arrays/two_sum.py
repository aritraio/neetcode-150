"""
Problem: Two Sum
Platform: LeetCode / NeetCode 150
Difficulty: Easy
Topic: Arrays, Hashing

------------------------------------------------------------

Given an array of integers `nums` and an integer `target`,
return the indices of the two numbers such that:

    nums[i] + nums[j] == target
    and i != j

You may assume that each input has exactly one solution.

Return the answer with the smaller index first.

------------------------------------------------------------

Example 1:
Input: nums = [3,4,5,6], target = 7
Output: [0,1]

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]

------------------------------------------------------------

Optimal Approach:
Use a Hash Map (Dictionary) to store:
    value -> index

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Returns indices of two numbers that add up to target.
        """

        hashmap = {}  # value -> index

        for i in range(len(nums)):
            complement = target - nums[i]

            # If complement already seen, we found the answer
            if complement in hashmap:
                return [hashmap[complement], i]

            # Store current number and its index
            hashmap[nums[i]] = i


# ------------------------------------------------------------
# Optional: Local Testing
# ------------------------------------------------------------
if __name__ == "__main__":
    solution = Solution()

    print(solution.twoSum([3, 4, 5, 6], 7))   # Expected: [0,1]
    print(solution.twoSum([4, 5, 6], 10))     # Expected: [0,2]
    print(solution.twoSum([5, 5], 10))        # Expected: [0,1]