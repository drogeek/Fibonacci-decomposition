import math as m
from itertools import chain, takewhile
import itertools as it

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


class FibonacciCache:
    def __init__(self):
        self.cache = [1,2]
    def get(self, value):
        if self.cache[-1] < value:
            self.cache.extend(get_fib_seq(value, self.cache[-2:]))
                
        min_idx_possible = int(m.log(SQRT5*value, PHI)) - min(3, value)
        return it.chain(self.cache[1:min_idx_possible], takewhile(lambda x: x <= value, self.cache[min_idx_possible:]))

def get_fib_seq(nbr, last_two=(1,2)):
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
