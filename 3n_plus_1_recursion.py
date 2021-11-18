# Creating a function called Collatz conjecture
# research paper: Deciphering the Collatz Conjecture Through Recursion
# created by Glenn Patrick King Ang 10/18/2021
# email: glenn.patrick.king.ang@outlook.com (preferred)
# email: glenn.p.ang@alumni.uts.edu.au (not affiliated, only an alumni)
# https://github.com/07231985


def Collatz_Conjecture(n, previous_n=0):
    if previous_n == 2 or n == 2:
        print("1")
        print("end recursive programming")

    else:
        previous_n = n

        if n % 2 == 1:
            n = (3 * n) + 1
        elif n % 2 == 0:
            n = n / 2

        print(int(n))

        Collatz_Conjecture(n, previous_n)


# n = 1 or any positive odd integer > 0
n = 1
Collatz_Conjecture(n)
