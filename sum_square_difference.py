"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

sum_of_squares = 0
sum_ = 0

for x in range(0, 101):
    sum_of_squares += x ** 2
    sum_ += x

result = sum_of_squares - sum_

print(f"Sum of squares = {sum_of_squares}")
print(f"Squared sum = {sum_}")
print(f"Result of minus = {result}")
