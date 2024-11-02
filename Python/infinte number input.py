#wp to enter numbers while and find the sum of highest and lowest number entered by the user


numbers = []

max_attempts = 10  # Set the maximum number of attempts

print(f"Enter up to {max_attempts} numbers (enter 0 to end early):")

for _ in range(max_attempts):
    num = int(input())
    if num == 0:
        break
    numbers.append(num)

if numbers:
    highest = max(numbers)
    lowest = min(numbers)
    sum_high_low = highest + lowest
    print(f"The highest number is: {highest}")
    print(f"The lowest number is: {lowest}")
    print(f"The sum of the highest and lowest numbers is: {sum_high_low}")
    
else:
    print("No numbers were entered.")



