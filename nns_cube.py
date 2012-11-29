import math

def nns_cube( S, q ):
    '''
        Params:
            S: set of all points (list of tuples)
            q: point to find nearest neighbor in S for (tuple)
    '''
    n = len(S)
    d = len(q)
    psi = math.log( math.log (n))
    alpha = determine_alpha( psi, n, d )

    return find_p_hat( S, q, alpha )


def find_p_hat (S, q, alpha ):
    d = len(q)
    p_hat = None
    for p in S:
        j = 0
        dist_max = 0

        while True:
            # we've checked all the dimensions! all good!
            if j == d:
                p_hat = p
                alpha = 2 * dist_max
                break

            # gotta check this dimension
            dist = abs(p[j] - q[j])
            # check that point is in the box
            if dist > alpha / 2:
                break
            # check if this is the dimension of maximal distance thus far
            if dist > dist_max:
                dist_max = dist

            # increment the dimension
            j = j + 1

    if p_hat:
        print(str.format("{}", p_hat))
        return p_hat

    else:
        print( str.format( "Box too small at alpha = {}", alpha ))
        return find_p_hat( S, q, alpha * 2 )


def determine_alpha( psi, n, d ):
    return (psi / n)**(1/d)
