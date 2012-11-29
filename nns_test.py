import nns_bruteforce
import nns_cube
import generate_S
import unittest

infile = open( "testfile.txt", "r" )
knownS = eval( infile.read() )
infile.close()
q = (0.5, 0.5, 0.5)
known_p_hat = (0.38321316864282096, 0.5309492170673772, 0.49778067887287725)

class test_bruteforce( unittest.TestCase ):
    '''Test class for nns_bruteforce.py'''
    def setUp( self ):
        '''Get result of nns_bruteforce with our test data'''
        self.result = nns_bruteforce.nns_bruteforce( knownS, q)

    def test_vs_known( self ):
        '''self.result should equal our known value'''
        self.assertEqual( self.result, known_p_hat ) 

class test_cube( unittest.TestCase ):
    '''Test class for nns_cube.py'''
    def setUp( self ):
        '''Get result of nns_bruteforce with our test data'''
        self.result = nns_cube.nns_cube( knownS, q )

    def test_vs_known( self ):
        '''self.result should equal our known value'''
        self.assertEqual( self.result, known_p_hat ) 

    def test_vs_bruteforce( self ):
        '''self.result should equal the value obtained from the bruteforce method'''
        bf_result = nns_bruteforce.nns_bruteforce( knownS, q)
        self.assertEqual( self.result, bf_result )



if __name__ == '__main__':
    unittest.main()
