def isWinner(x, nums):
    if not nums or x < 1:
        return None

    # Helper function to generate prime numbers using the Sieve of Eratosthenes
    def sieve_of_eratosthenes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    # Precompute primes up to the maximum number in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Precompute prime counts up to each number
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of primes in the current range
        prime_count = prime_counts[n]
        # Maria wins if the number of primes is odd, Ben wins if it's even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
