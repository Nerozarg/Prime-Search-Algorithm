from numpy import prod


# Finds primes, x equals how many loops
def prime(x):
    primes = {
        1: True,
        2: True,
        3: True,
        5: True
        }
    listOfPrimes, nextBase, primePosInList_next = primeHelper(primes, x)
    return primeRemoveMultiplesAll(primes, listOfPrimes, nextBase, primePosInList_next)


# Deletes all multiples of all primes
def primeRemoveMultiplesAll(primes, listOfPrimes, nextBase, primePosInList):
    state = True
    while state:
        state = primeRemoveMultiples(primes, listOfPrimes, nextBase, primePosInList)
        primePosInList += 1
    return primeDictToList(primes)


# Deletes all multiples of a single prime
def primeRemoveMultiples(primes, listOfPrimes, nextBase, primePosInList):
    if listOfPrimes[primePosInList]**2 > nextBase:
        # Unable to remove any more multiples
        return False
    for i in range(primePosInList, len(listOfPrimes)):
        valueToRemove = listOfPrimes[primePosInList]*listOfPrimes[i]
        if valueToRemove <= nextBase:
            try:
                del primes[valueToRemove]
            except Exception:
                # Expected, since listOfPrimes contains deleted non primes
                pass
        else:
            # Able to remove multiples
            return True


# Returns sorted, low to high, prime list
def primeDictToList(primes):
    return sorted(list(dict.keys(primes)))


# Main function Helper
def primeHelper(primes, loops):
    loop = 0
    listOfPrimes = primeDictToList(primes)
    primesInBase = [listOfPrimes[1], listOfPrimes[2]]

    while True:
        currentBase = prod(primesInBase)
        nextBase = currentBase * listOfPrimes[len(primesInBase)+1]

        # Make potential primes
        for base in range(currentBase, nextBase, currentBase):
            for prime in listOfPrimes[:len(listOfPrimes)]:
                if prime in primesInBase:
                    continue
                primes[base+prime] = True

        # Delete next prime multiples
        listOfPrimes = primeDictToList(primes)
        primeRemoveMultiples(primes, listOfPrimes, nextBase, len(primesInBase)+1)
        listOfPrimes = primeDictToList(primes)

        # End section
        loop += 1
        if loop >= loops:
            return listOfPrimes, nextBase, len(primesInBase)+2
        primesInBase.append(listOfPrimes[len(primesInBase)+1])


print(prime(4))
