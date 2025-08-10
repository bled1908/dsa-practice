"""
Problem: Reordered Power of 2
Platform: LeetCode
Link: https://leetcode.com/problems/reordered-power-of-2/description/
Difficulty: Medium
Tags: Hash Table, Math, Sorting, Counting, Enumeration

Description:
You are given an integer n. We reorder the digits in any order (including the original order) 
such that the leading digit is not zero. Return True if and only if we can do this so that 
the resulting number is a power of two.

Constraints:
1 <= n <= 10^9

Approach:
1. Get the digit frequency of n → target.
2. Loop through all powers of 2 from 2^0 to 2^30 
   (2^30 = 1073741824 is the largest power of 2 with ≤ 10 digits).
3. For each power of 2:
   - Convert it to a digit frequency.
   - Compare with target's frequency.
   - If they match → n can be rearranged to that power of 2 → return True.
4. If none match → return False.

Time Complexity: O(31 * k) where k ≤ 10 (digits in n)
Space Complexity: O(1)
"""

class Solution:
    def to_freq_arr(self, n):
        freq = [0] * 10
        while n > 0:
            freq[n % 10] += 1
            n //= 10
        return freq

    def reorderedPowerOf2(self, n: int) -> bool:
        target = self.to_freq_arr(n)
        for i in range(31):
            if target == self.to_freq_arr(1 << i):
                return True
        return False

# Example usage & tests
if __name__ == "__main__":
    sol = Solution()
    print(sol.reorderedPowerOf2(1))       # True
    print(sol.reorderedPowerOf2(10))      # False
    print(sol.reorderedPowerOf2(16))      # True
    print(sol.reorderedPowerOf2(125))     # True
    print(sol.reorderedPowerOf2(128))     # True
    print(sol.reorderedPowerOf2(821))     # True (reorder to 128)
    print(sol.reorderedPowerOf2(123456))  # False