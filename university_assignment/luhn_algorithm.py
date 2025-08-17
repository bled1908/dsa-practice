"""
Problem: Luhn Algorithm (Credit Card Validation)
Platform: General Algorithm / Coding Assignment
Link: https://en.wikipedia.org/wiki/Luhn_algorithm
Difficulty: Easy-Medium
Tags: Math, String, Validation, Simulation

Description:
The Luhn algorithm is used to validate identification numbers such as credit card numbers.  
It works by applying a checksum formula to the digits of the number. A number is valid if it passes this checksum test.

Steps of the algorithm:
1. Starting from the rightmost digit (check digit), moving left, double the value of every second digit.
2. If doubling results in a number greater than 9, subtract 9 from it.
3. Sum all the digits (after modification).
4. If the total sum is divisible by 10, the number is valid; otherwise, it is invalid.

Constraints:
- The input will be a string or integer representing the card number.
- Length of input ≥ 2
- Digits only (no spaces or symbols).

Approach:
1. Convert input to a list of digits (right-to-left).
2. Traverse through digits:
   - Double every second digit.
   - Adjust if > 9 (subtract 9).
3. Compute the total sum.
4. Check if divisible by 10 → return True/False.
 
Time Complexity: O(n), where n is the number of digits.
Space Complexity: O(1)

"""

class Solution:
    def luhn_check(self, num: str) -> bool:
        digits = [int(d) for d in num]
        total = 0
        n = len(digits)

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            d = digits[i]
            # Double every second digit from the right
            if (n - i) % 2 == 0:
                d *= 2
                if d > 9:
                    d -= 9
            total += d

        return total % 10 == 0


# Example usage & tests
if __name__ == "__main__":
    sol = Solution()
    print(sol.luhn_check("4539578763621486"))  # True  (valid Visa)
    print(sol.luhn_check("4485275742308327"))  # True  (valid Visa)
    print(sol.luhn_check("1234567812345670"))  # True  (valid test number)
    print(sol.luhn_check("1234567812345678"))  # False (invalid)