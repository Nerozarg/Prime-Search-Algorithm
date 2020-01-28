from numpy import prod


# Finds primes, x equals how many loops
def prime(x):
    primes = {
        1: True,
        2: True,
        3: True,
        5: True
        }
    loop, nextBase = primeHelper(primes, x)
    return dictPrimeList(primes, loop, nextBase)


# Removes non prime integers through a pattern
def blackPrimeList(primes, baseValue, primesList, nextBase, main=True):
    for i in range(baseValue, len(primesList)):
        testing = primesList[baseValue]*primesList[i]
        if testing > nextBase:
            break
        try:
            del primes[testing]
        except Exception:
            pass
        if main:
            blackPrimeList(primes, i+1, primesList, nextBase, False)


# Creates a sorted array from Object
def dictPrimeList(primes, loop, nextBase):
    primesList = [1, 2, 3, 5]
    primesLen = nextBase
    for x in range(5, primesLen, 2):
        if not x == 5:
            try:
                if primes[x]:
                    primesList.append(x)
            except Exception:
                pass
    return primesList


# Main function Helper
def primeHelper(primes, loops):
    loop = 0
    primesList = dictPrimeList(primes, loop, 30)
    baseValue = [primesList[1], primesList[2]]

    while True:
        currentBase = prod(baseValue)
        nextBase = currentBase * primesList[len(baseValue)+1]

        # Last prime appended during prior run
        for x in range(len(primes)-1, -1, -1):
            if primesList[x] < currentBase:
                lastPosition = x
                break

        # Make potential primes
        for base in range(currentBase, nextBase, currentBase):
            for prime in primesList[:lastPosition+1]:
                if prime in baseValue:
                    continue
                primes[base+prime] = True

        # Correct potential primes
        primesList = dictPrimeList(primes, loop, nextBase)
        blackPrimeList(primes, len(baseValue)+1, primesList, nextBase)
        primesList = dictPrimeList(primes, loop, nextBase)

        # End section
        loop += 1
        if loop >= loops:
            return loop, nextBase
        baseValue.append(primesList[len(baseValue)+1])


# test
# print(prime(4))
