"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    sieve_size = number_of_primes * 10;
    primes = [] # Primes identified by the sieve
    terminations = [] # The first multiple of a prime at which the sieve has stopped
    sieve = [False for x in range(sieve_size)]
    sieve_start = 2
    while True:
        while len(sieve):
            if not sieve.pop(0):
                primes.append(sieve_start)
                terminations.append(sieve_start + 1 + run_sieve(sieve, (sieve_start * (sieve_start - 1)) - 1, sieve_start))
            
            sieve_start += 1

        if len(primes) >= number_of_primes:
            break
        else:
            sieve = [False for x in range(sieve_size)]
            for i in range(len(primes)):
                prime = primes[i]
                prev_term = terminations[i]
                terminations[i] = sieve_start + run_sieve(sieve, prev_term - sieve_start, prime)

    return primes[:number_of_primes]

"""Run over a sieve from a start index with a step, setting locations to true"""
def run_sieve(sieve, start_index, step):
    i = start_index
    while i < len(sieve):
        sieve[i] = True
        i += step
    return i

"""Utility Function for Debugging"""
def print_sieve(sieve_start, sieve):
    string = " ".join((str(i + sieve_start) if not x else "*" for i, x in enumerate(sieve)))
    print(string)

