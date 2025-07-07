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

# Solution

## The Standard Algorithm: Division and Modulo

The classic way to solve any base conversion problem is to work from right to left, finding the least significant digit first.

Here's the logic:

1.  Take your number, `num`.
2.  Calculate the remainder when you divide by 13 (`num % 13`). This remainder is your **right-most digit**.
3.  Update your number by performing integer division (`num //= 13`). This effectively "removes" the digit you just found.
4.  Repeat steps 2 and 3 until your number becomes 0.
5.  Since you found the digits from right to left, you just need to reverse them to get the final answer.

### Why This Algorithm Works: A Deeper Dive

The magic of this method lies in two simple mathematical operators: **modulo (`%`)** and **floor division (`//`)**.

#### 1. Why `num % 13` Finds the Right-Most Digit

The modulo operator gives you the remainder of a division. It works because, by definition, every place value _except_ the "ones" place is a multiple of the base.

Consider the number **493** in base 10. We can write it as `(4 * 100) + (9 * 10) + 3`. When we do `493 % 10`, the `(4 * 100)` and `(9 * 10)` parts have a remainder of 0, leaving only the `3`.

The same is true for base 13. The number **493** is **"2BC"** in base 13, which is:
`(2 * 13²) + (11 * 13¹) + 12`

When you calculate `493 % 13`:

- `(2 * 13²) % 13` is `0`.
- `(11 * 13¹) % 13` is `0`.
- This leaves only the `12`, which is our right-most digit ("C").

The modulo operator is a mathematical tool to isolate the value in the "ones" place for any given base.

#### 2. Why `num //= 13` Moves to the Next Digit

The floor division operator (`//`) divides and then rounds down, effectively "chopping off" the right-most digit you just found.

When we calculate `493 // 13`, the result is `37`. This `37` represents the rest of the number: `(2 * 13¹) + 11`. We have successfully removed the "C" digit and can now repeat the process on `37` to find the next digit, "B".

The `while` loop in the optimal solution uses these two operators together to cleanly deconstruct the number from right to left.
