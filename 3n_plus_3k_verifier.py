# Using a while loop to verify the Collatz conjecture
# research paper: The Real Algebraic Expression of the Collatz Conjecture
# created by Glenn Patrick King Ang 12/03/2021
# email: glenn.patrick.king.ang@outlook.com (preferred)
# email: glenn.p.ang@alumni.uts.edu.au (not affiliated, only an alumni)
# https://github.com/07231985


# ===================
# n starts at 1

# k can be set from 0 to 31, k = 32 to 39 does not work. possibly k = 32 onwards does not work
# k = 0; 3n+3**k = 3n+1
# k = 1; 3n+3

k = 0

# find_until = 1 or any positive integer > 0
# the value of find_until will be the last number that will be inputted in the loop as n
# n will always be set as an odd number
# example: 
# 	find_until = 100
# 	the last n = 99

find_until = 10000000

# ===================


missing_n = []

for x in range(1, find_until, 2):
    loop = 0
    previous_n = 0

    # n = 1 or any positive odd integer > 0
    # n = x that starts at 1 to find_until
    n = x

    iteration = 0

    while n > 0:

        previous_n = n
        if previous_n == 2 * 3 ** k:
            loop += 1
            print(f"==================== Infinite Loop:{loop} from n = {x}")
        if previous_n == 2 * 3 ** k and loop == 3:
            print("end loop")
            break
        elif n % 2 == 1:
            n = (3 * n) + 3 ** k
        elif n % 2 == 0:
            n = n / 2

        iteration += 1
        # print(int(n))

        if iteration == 1000000:
            missing_n.append(x)
            print(f"missing here on {x}")
            break

    print(f"Total steps for n = {x}: {iteration}")
    print(f"Missing n: {missing_n}\n")


print(f"\n==================== Algebraic expression: 3n + {3 ** k}")
print(f"Missing n: {missing_n}")