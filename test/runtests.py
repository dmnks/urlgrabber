#!/usr/bin/python

# quick script to run tests from source directory
# i.e. without having to install

import sys
import unittest
from os.path import dirname, join as joinpath

def main():
    dn = dirname(sys.argv[0])
    sys.path.insert(0, joinpath(dn,'..'))
    sys.path.insert(0, dn)
    import test_grabber, test_byterange
    suite = unittest.TestSuite( (test_grabber.suite(),test_byterange.suite()) )
    runner = unittest.TextTestRunner(descriptions=1,verbosity=2)
    runner.run(suite)
    
if __name__ == '__main__':
    main()