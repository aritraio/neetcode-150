# # NeetCode 150 Solutions

# ## Arrays

# ### 1. Contains Duplicate

# **Problem:**  
# Given an integer array `nums`, return `true` if any value appears more than once.

# **Approach:**  
# Use a hash set to track seen numbers.

# **Time Complexity:** O(n)  
# **Space Complexity:** O(n)

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False