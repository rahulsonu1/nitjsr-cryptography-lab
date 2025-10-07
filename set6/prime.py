def is_prime_division(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


import random
def is_prime_fermat(n, k=5):
    if n <= 1: return False
    for _ in range(k):
        a = random.randint(2, n-2)
        if pow(a, n-1, n) != 1:
            return False
    return True


import random
def is_prime_mr(n, k=5):
    if n < 2: return False
    r, d = 0, n-1
    while d % 2 == 0:
        r += 1; d //= 2
    for _ in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x in (1, n-1): continue
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n-1: break
        else:
            return False
    return True


n=843
print(is_prime_division(n))
print(is_prime_fermat(n))
print(is_prime_mr(n))