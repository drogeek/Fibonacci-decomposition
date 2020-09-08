from web_serv import fib_decompose, get_fib_seq
import itertools as it
import random
import numpy as np

def test_fib_decompose():
    given_answer = fib_decompose(11)
    expected_result = ( (2, 2, 2, 2, 3), (2, 2, 2, 5), (2, 3, 3, 3), (3, 3, 5), (3, 8) )
    for decomp in given_answer:
        assert decomp in expected_result 
    
    for decomp in expected_result:
        assert decomp in given_answer

    
    
    for i in np.random.randint(2,100,5):
        decompositions = fib_decompose(i)

        print("checking that there is no 1 in the decompositions".format(i))
        # check that there is no trace of number under 2 in the decompositions
        assert all(
            map(
                lambda x: x >= 2, 
                it.chain.from_iterable(decompositions)
            )
        )

        print("checking that decompositions sum to {}".format(i))
        # check that every decomposition sum to the value they should
        assert(all(
            map(
                lambda x: sum(x) == i, 
                decompositions
            )
        ))


def test_get_fib_seq():
    assert tuple(get_fib_seq(0)) == ()
    assert tuple(get_fib_seq(2)) == ()
    assert tuple(get_fib_seq(1)) == ()
    assert tuple(get_fib_seq(9,(2,3))) == (3,5,8)
