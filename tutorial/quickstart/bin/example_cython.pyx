def primes(int n) -> list[int]:
    cdef int i, j
    result = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)
    return result
