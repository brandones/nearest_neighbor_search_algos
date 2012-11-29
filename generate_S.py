import random
from pprint import pprint

def generate_S( n, d, writeout = True ):

    S = []
    for i in range(n):
        S.append( tuple(random.random() for dim in range(d)) )
    
    if writeout:
        with open( "rand_pts.txt", "w" ) as outfile:
            pprint(S, outfile)

    return S
