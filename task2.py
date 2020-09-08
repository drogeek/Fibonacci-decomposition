import math as m
from itertools import chain, takewhile
import itertools as it

SQRT5 = m.sqrt(5)
INV_SQRT5 = 1/SQRT5
PHI = (1+SQRT5)/2
PHI_PRIME = (1-SQRT5)/2

cache = {}

def get_max_fib(n):
    assert(n > 0)

    candidate = int(m.log(SQRT5*n, PHI))
    f_c = fib(candidate)
    if f_c == n:
        return (candidate, f_c)
    elif f_c < n:
        while f_c < n:
            f_c = fib(candidate+1)
        return (candidate, fib(candidate))
    else:
        while f_c > n:
            f_c = fib(candidate-1)
        return (candidate-1, f_c)


def decomposeFib(n):
    return fib_decompose(n)

class FunctionCache:
    def __init__(self, f):
        self.cache = {}
        self.f = f
    def get(self, key):
        if key not in self.cache:
            self.cache[key] = self.f(key)
        return self.cache[key]

class FibonacciCache:
    def __init__(self):
        self.cache = [1,2]
        self.cpt = 0
    def get(self, value):
        if self.cache[-1] < value:
            self.cpt += 1
            self.cache.extend(get_fib_seq(value, self.cache[-2:]))
                
        min_idx_possible = int(m.log(SQRT5*value, PHI)) - min(3, value)
        return it.chain(self.cache[1:min_idx_possible], takewhile(lambda x: x <= value, self.cache[min_idx_possible:]))

def get_fib_seq(nbr, last_two=(1,2)):
    prev, curr = last_two 
    while curr < nbr:
        tmp = curr
        curr += prev 
        prev = tmp 
        yield curr 

def fib_decompose(n, cache=None, fib_cache=None):
    result = set()
    if not fib_cache:
        fib_cache = FibonacciCache()
    if not cache:
        # generate a cache that will use fib_decompose if the value is not yet cached
        cache = FunctionCache(lambda x: fib_decompose(x, cache, fib_cache))
    if n <= 3:
        #print("cpt", fib_cache.cpt)
        result.add((n,))
    else:
        for fib_nbr in fib_cache.get(n):
            remain = n - fib_nbr 

            # skip solutions that require 1
            if remain < 2 :
                continue

            # get decompositions of the cached remain, computing it if it's not already in the cache
            decompositions = cache.get(remain)

            # add fib_nbr to the decompositions of the remaining, then sort each decompositions (to guarantee unicity), 
            # and add the decompositions to the final result if it's not already present
            for decomp in \
                map(
                    lambda x : tuple(sorted((x[0], *x[1]))), 
                    it.product([fib_nbr], decompositions)
                ):
                result.add(decomp)
        #print("cpt", fib_cache.cpt)
    return result


def fib(n):
    return int(INV_SQRT5*(m.pow(PHI, n+1) - m.pow(PHI_PRIME, n+1)))

if __name__ == "__main__":
    #assert([get_max_fib(n) for n in [fib(x) for x in range(1, 100)]] == [fib(x) for x in range(1,100)])
    #print(get_fib_seq(12))
    for decomp in decomposeFib(142):
        print(decomp)
        print(sum(decomp))
