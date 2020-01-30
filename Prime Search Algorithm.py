from numpy import prod


class Prime:
    # Variables
        # (Dict) primes
        # (Arr) listOfPrimes
        # (Arr) primesInBase
        # (Int) currentBase
        # (Int) nextBase
        # (Int) loop
    def __init__(self):
        self.primes = {
            1: True,
            2: True,
            3: True,
            5: True
            }
        self.loop = 0
        self.listOfPrimes = self.primeDictToList()
        self.primesInBase = [self.listOfPrimes[1], self.listOfPrimes[2]]

    # Returns Prime Dictionary as Array
    def primeDictToList(self):
        return sorted(list(dict.keys(self.primes)))

    # Deletes all multiples of a single prime
    def primeRemoveMultiples(self, primePosInList):
        if self.listOfPrimes[primePosInList]**2 > self.nextBase:
            # Unable to remove any more multiples
            return False
        for i in range(primePosInList, len(self.listOfPrimes)):
            valueToRemove = self.listOfPrimes[primePosInList]*self.listOfPrimes[i]
            if valueToRemove <= self.nextBase:
                try:
                    del self.primes[valueToRemove]
                except Exception:
                    # Expected, since listOfPrimes contains deleted non primes
                    pass
            else:
                # Able to remove multiples
                return True

    # Deletes all multiples of all primes
    def primeRemoveMultiplesAll(self, primePosInList):
        state = True
        while state:
            state = self.primeRemoveMultiples(primePosInList)
            primePosInList += 1
        return self.primeDictToList()

    # Main Search Function
    def primeSearch(self, loops):
        while True:
            self.currentBase = prod(self.primesInBase)
            self.nextBase = self.currentBase * self.listOfPrimes[len(self.primesInBase)+1]

            # Make potential primes
            for base in range(self.currentBase, self.nextBase, self.currentBase):
                for prime in self.listOfPrimes[:len(self.listOfPrimes)]:
                    if prime in self.primesInBase:
                        continue
                    self.primes[base+prime] = True

            # Delete next prime multiples
            self.listOfPrimes = self.primeDictToList()
            self.primeRemoveMultiples(len(self.primesInBase)+1)
            self.listOfPrimes = self.primeDictToList()

            # End section
            self.loop += 1
            if self.loop >= loops:
                self.listOfPrimes = self.primeRemoveMultiplesAll(len(self.primesInBase)+2)
                return self.listOfPrimes
            self.primesInBase.append(self.listOfPrimes[len(self.primesInBase)+1])


PSO = Prime()

print("Prime array: " + str(PSO.primeSearch(4)))
print("Prime dictionary: " + str(PSO.primes))
print("Primes in base: " + str(PSO.primesInBase))
print("Current base: " + str(PSO.currentBase))
print("Next base: " + str(PSO.nextBase))
print("Loop: " + str(PSO.loop))

# Currently unable to continue search, because all line constructing non primes are removed
