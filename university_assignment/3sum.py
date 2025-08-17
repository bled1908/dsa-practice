"""
Problem: 3Sum
Platform: LeetCode
Link: https://leetcode.com/problems/3sum/
Difficulty: Medium
Tags: Array, Two Pointers, Sorting

Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

Approach:
1. Sort the array (important for two-pointer approach and avoiding duplicates).
2. Iterate through each element `nums[i]`:
   - Skip duplicates for i.
   - Use two pointers (left = i+1, right = n-1).
   - While left < right:
     - Compute sum = nums[i] + nums[left] + nums[right].
     - If sum == 0 → add triplet, then move both pointers skipping duplicates.
     - If sum < 0 → move left pointer forward.
     - If sum > 0 → move right pointer backward.
3. Return all unique triplets.

Time Complexity: O(n^2)  
Space Complexity: O(1) (excluding output list)
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return res


# Example usage & tests
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]))  
    # Expected: [[-1,-1,2], [-1,0,1]]
    print(sol.threeSum([]))                
    # Expected: []
    print(sol.threeSum([0,0,0,0]))         
    # Expected: [[0,0,0]]