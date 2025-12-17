# Sum of Number from 1 to 50 using Loop
# Using total=0 to make python remember the sum so far
total = 0
# Using range() to read number from 1 to 50 and we used n+1 to read 50
for numbers in range(1, 51):
    total += numbers
print(f"The sum of numbers from 1 to 50 is: {total}")