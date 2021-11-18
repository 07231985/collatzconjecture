# n = 1 or any positive odd integer > 0
# research paper: Deciphering the Collatz Conjecture Through Recursion
# created by Glenn Patrick King Ang 10/18/2021
# email: glenn.patrick.king.ang@outlook.com (preferred)
# email: glenn.p.ang@alumni.uts.edu.au (not affiliated, only an alumni)
# https://github.com/07231985

n = 1
previous_n = 0

while n > 0 and previous_n != 2:

    previous_n = n

    if previous_n == 2:
        print("1")
        print("end loop")
        break
    elif n % 2 == 1:
        n = n + 1
    elif n % 2 == 0:
        n = n / 2

    print(int(n))
