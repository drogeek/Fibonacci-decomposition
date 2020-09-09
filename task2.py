import math as m
from itertools import chain, takewhile
import itertools as it
from utils import app, cache
from db import lookup_table, insert_into_db, conn

SQRT5 = m.sqrt(5)
INV_SQRT5 = 1/SQRT5
PHI = (1+SQRT5)/2
PHI_PRIME = (1-SQRT5)/2


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


class FunctionCache:
    def __init__(self, f, conn):
        self.conn = conn
        self.f = f

    @cache.memoize(timeout=5000)
    def get(self, key):
        value = lookup_table(key)
        if not value:
            #the additional tuple is a bit dirty…
            #but the fetchone method called in lookup_table
            #return a tuple, and this way it works in both cases
            value = (self.f(key),)
            insert_into_db(key, tuple(value[0]))
        return value[0]
    
    def __contains__(self, key):
        return lookup_table(key) != None
        
class FibonacciCache:
    def __init__(self):
        self.cache = [1,2]
    def get(self, value):
        if self.cache[-1] < value:
            self.cache.extend(get_fib_seq(value, self.cache[-2:]))
                
        min_idx_possible = int(m.log(SQRT5*value, PHI)) - min(3, value)
        return it.chain(self.cache[1:min_idx_possible], takewhile(lambda x: x <= value, self.cache[min_idx_possible:]))

def fib_decompose(n, cache=None):
    result = set()

    if not cache:
        cache = FunctionCache(lambda x: fib_decompose(x, cache), conn)
    # if it's already in the cache, why bother? Let's give it back!
    if n in cache:
        return cache.get(n)
    if n <= 3:
        result.add((n,))
    else:
        for fib_nbr in get_fib_seq(n):
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
    return result

@cache.memoize(timeout=1000)
def get_fib_seq(nbr, last_two=(1,2)):
    return tuple(get_fib_seq_gen(nbr, last_two))

def get_fib_seq_gen(nbr, last_two=(1,2)):
    prev, curr = last_two 
    while curr < nbr:
        yield curr 
        tmp = curr
        curr += prev 
        prev = tmp 


def fib(n):
    return int(INV_SQRT5*(m.pow(PHI, n+1) - m.pow(PHI_PRIME, n+1)))

if __name__ == "__main__":
    pass
    #for decomp in fib_decompose(142):
        #print(decomp)
