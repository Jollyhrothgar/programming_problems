# Question

Given an integer num, return its string representation in base 13.

In case you don’t use base 13 that much (who does, right?), here’s a quick
rundown: just like base 10 uses digits from 0 to 9. But also for 10, 11 and 12,
we use the letters A, B, and C.

For example:

9 in base 13 is still "9"
10 in base 13 is "A"
11 in base 13 is "B"
12 in base 13 is "C"
13 in base 13 is "10"
14 in base 13 is "11"
49 in base 13 is "3A" (since 3 _ 13 + 10 = 493 _ 13 + 10 = 49)
69 in base 13 is "54" (since 5 _ 13 + 4 = 69 5 _ 13 + 4 = 69)

# Thinking

- Let's define what base 13 means: it means that you write numbers as (13)^N +
  ... (13)^3 + (13)^2 + (13)^1 + (13)^0, with each place value having a
  coefficient of how many times it appears, and now we represent a coefficient as
  a digit (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A=10, B=11, C=12).
- The issue with any number is that they are unbounded. And with string
  repreesentations, we have basically unlimited precision. So, we'll make some
  assuptions about the precision of the number.
- We'll assume up to a 5 digit base 13 number and add more precision as we
  discover issues.

---

## Solution Analysis

### 1. Standard Solution (`solution.py`)
-   **Approach:** This solution iterates from the largest possible power of 13 down to 0. In each step, it determines how many times that power of 13 fits into the number, which gives the digit for that place value. It subtracts that value from the number and continues. This approach requires pre-calculating or knowing the maximum number of digits required.
-   **Time Complexity:** `O(log_13(n))` or `O(d)` where `d` is the number of digits in the base-13 representation. The loop runs a fixed number of times based on the assumed maximum number of digits.
-   **Space Complexity:** `O(d)` to store the resulting string.

### 2. Optimal Solution (`optimal_solution.py`)
-   **Approach:** The optimal solution uses the standard algorithm of repeated division and modulo. It repeatedly takes the number modulo 13 to get the rightmost digit and then divides the number by 13 to "shift" the digits to the right, until the number becomes 0. The digits are prepended to the result string.
-   **Time Complexity:** `O(log_13(n))` or `O(d)` where `d` is the number of digits. Each division and modulo operation is constant time, and the number of operations is proportional to the number of digits.
-   **Space Complexity:** `O(d)` to store the resulting string.

Explanation:

#### 1. Why `num % 13` Finds the Right-Most Digit

The modulo operator gives you the remainder of a division. It works because, by definition, every place value *except* the "ones" place is a multiple of the base.

Consider the number **493** in base 10. We can write it as `(4 * 100) + (9 * 10) + 3`. When we do `493 % 10`, the `(4 * 100)` and `(9 * 10)` parts have a remainder of 0, leaving only the `3`.

The same is true for base 13. The number **493** is **"2BC"** in base 13, which is:
`(2 * 13²) + (11 * 13¹) + 12`

When you calculate `493 % 13`:
* `(2 * 13²) % 13` is `0`.
* `(11 * 13¹) % 13` is `0`.
* This leaves only the `12`, which is our right-most digit ("C").

The modulo operator is a mathematical tool to isolate the value in the "ones" place for any given base.

#### 2. Why `num //= 13` Moves to the Next Digit

The floor division operator (`//`) divides and then rounds down, effectively "chopping off" the right-most digit you just found.

When we calculate `493 // 13`, the result is `37`. This `37` represents the rest of the number: `(2 * 13¹) + 11`. We have successfully removed the "C" digit and can now repeat the process on `37` to find the next digit, "B".


### Trade-Offs
The "standard" solution is less efficient and more complex than it needs to be. It assumes a fixed number of digits and iterates that many times, which can be inefficient if the number is small. The "optimal" solution is the idiomatic way to perform base conversion. It's more efficient as it only performs as many operations as are necessary, and it's more elegant and easier to understand.
