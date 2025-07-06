# Question

Write a function `fizz_buzz_sum` to find the sum of all multiples of 3 or 5 below a target value.

For example, if the target value was 10, the multiples of 3 or 5 below 10 are 3, 5, 6, and 9.

Because 3 + 5 + 6 + 9 = 23, our function would return 23.

# Thinking

- We could create two helper functions "is multiple of three" and "is multiple of five" and then
  return the list of factors.
- Some multiples may be a multiple of both 3 and 5 - in those cases, the helper functions will
  return duplicate numbers - for example, if the number is 16, one of the factors will be 15.
- This could be a dynamic programming problem, because each subsequent call to this function will
  comprise all previously solved instances. For example - if the user or system called
  `fizz_buzz_sum(10)` and then subsequently calls `fizz_buzz_sum(11)`, we can use the result of
  `fizz_buzz_sum(10)` and then only check new factors. However, this is maybe a bad example, because
  11 is a prime number.

