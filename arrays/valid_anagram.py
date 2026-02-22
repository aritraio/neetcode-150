"""
LeetCode / NeetCode 150
Problem: Valid Anagram
Difficulty: Easy

Given two strings s and t, return True if t is an anagram of s,
otherwise return False.

Approach:
- If lengths differ → not an anagram.
- Count character frequencies in s.
- Decrease frequencies using t.
- If any count goes negative → not an anagram.
- If all balanced → valid anagram.

Time Complexity: O(n)
Space Complexity: O(1)  (since only 26 lowercase letters)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Length check
        if len(s) != len(t):
            return False

        # Step 2: Frequency array for 26 lowercase letters
        count = [0] * 26

        # Step 3: Count characters in s
        for char in s:
            index = ord(char) - ord('a')
            count[index] += 1

        # Step 4: Subtract using characters in t
        for char in t:
            index = ord(char) - ord('a')
            count[index] -= 1

            # If count becomes negative → extra character in t
            if count[index] < 0:
                return False

        return True