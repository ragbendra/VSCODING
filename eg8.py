# python program to recover the password of the mobile
import itertools
import time


# Define the possible digits (0-9)
digits = '0123456789'

# Generate all possible 6-digit combinations
combinations = itertools.product(digits, repeat=6)

# Initialize a counter for the number of attempts
attempts = 0

# Start a timer
start_time = time.time()

# Iterate over the combinations
for combination in combinations:
    password = ''.join(combination)
    attempts += 1
    print(f"Attempt {attempts}: {password}")
    # Simulate a delay to mimic the time it takes to try a password
    time.sleep(0.1)

    # If you want to stop the program after a certain number of attempts, uncomment the following line
    # if attempts >= 100000: break

# Print the elapsed time
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2f} seconds")