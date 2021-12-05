# Using a while loop for the Collatz conjecture
# research paper: The Real Algebraic Expression of the Collatz Conjecture
# created by Glenn Patrick King Ang 10/23/2021
# email: glenn.patrick.king.ang@outlook.com (preferred)
# email: glenn.p.ang@alumni.uts.edu.au (not affiliated, only an alumni)
# https://github.com/07231985


# ===================
# n = -1 or any negative odd integer < 0

n = -1

# k can be set from 0 to 31, k = 32 to 39 does not work. possibly k = 32 onwards does not work
# k = 0; 3n-3**k = 3n-1
# k = 1; 3n-3

k = 31

# ===================

previous_n = 0
loop = 0

while n < 0:

    previous_n = n
    if previous_n == -2 * 3 ** k:
        loop += 1
        print(f"==================== Infinite Loop:{loop} for n = {n}")
        print(f"==================== Algebraic expression: 3n - {3**k}")
    if previous_n == -2 * 3 ** k and loop == 3:
        print("end loop")
        break
    elif n % 2 == 1:
        n = (3 * n) - 3 ** k
    elif n % 2 == 0:
        n = n / 2

    print(int(n))
