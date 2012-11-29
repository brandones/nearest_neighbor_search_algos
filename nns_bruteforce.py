from pprint import pprint

def nns_bruteforce( S, q ):
    '''Measure distance d from q to each point p in S and return
        the p minimizing d.

    Arguments:
    S -- the set of points we are considering (list of tuples)
    q -- the point we want to find the nearest neighbor to
    '''
    p_hat = None
    min_dist = float("Inf")
    for p in S:
        dist = norm( p, q )
        if dist < min_dist:
            p_hat = p
            min_dist = dist

    return p_hat



def norm( p, q ):
    '''Return the 2-norm of p and q treated as vectors.'''
    return sum((p[i] - q[i])**2 for i in range(len(p)))**(1/2)
