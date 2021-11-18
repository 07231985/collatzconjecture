# n = 1 or any positive odd integer > 0
# research paper: Deciphering the Collatz Conjecture Through Recursion
# created by Glenn Patrick King Ang 10/18/2021
# email: glenn.patrick.king.ang@outlook.com (preferred)
# email: glenn.p.ang@alumni.uts.edu.au (not affiliated, only an alumni)
# https://github.com/07231985


n = 1
previous_n = 0


def n_plus_1(n_recursion, previous_n_recursion=0):
    if previous_n_recursion == 2 or n_recursion == 2:
        return n_recursion
    else:
        previous_n_recursion = n_recursion
        if n_recursion % 2 == 1:
            n_recursion = n_recursion + 1
        elif n_recursion % 2 == 0:
            n_recursion = n_recursion / 2

        return n_plus_1(n_recursion, previous_n_recursion)


while n > 0 and previous_n != 2:

    previous_n = n

    if previous_n == 2:
        print("end while loop for 2n + recursion at 1")
        break
    elif n % 2 == 1:
        n = (2 * n) + n_plus_1(n)
    elif n % 2 == 0:
        n = n / 2

    print(f"While loop for 2n + recursion (n+1): {int(n)}")
