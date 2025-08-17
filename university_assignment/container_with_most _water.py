"""
Problem: Container With Most Water
Platform: LeetCode
Link: https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium
Tags: Array, Two Pointers, Greedy

Description:
You are given an integer array `height` of length n. 
There are n vertical lines such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container holds the most water.
Return the maximum amount of water a container can store.

Constraints:
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Approach:
1. Use a two-pointer approach:
   - Place one pointer at the start (left = 0) and another at the end (right = n-1).
   - Calculate the area = min(height[left], height[right]) * (right - left).
   - Update the maximum area.
   - Move the pointer that points to the smaller height (to try and find a taller line).
2. Continue until left < right.
3. Return the maximum area found.

Reasoning:
- Moving the taller line inward cannot help because the height is limited by the shorter line.
- Hence, always move the shorter pointer.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, h * width)

            # Move the pointer at the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Example usage & tests
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))   # 49
    print(sol.maxArea([1,1]))                 # 1
    print(sol.maxArea([4,3,2,1,4]))           # 16
    print(sol.maxArea([1,2,1]))               # 2