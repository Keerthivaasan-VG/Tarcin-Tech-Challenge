def bounded_sieve(n, max_ops):
    primes = []
    ops = 0
    if n < 2:
        return primes, ops

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for multiple in range(p * 2, n + 1, p):
                ops += 1
                if ops > max_ops:
                    return primes, ops
                sieve[multiple] = False
    return primes, ops

print(bounded_sieve(20, 50))
