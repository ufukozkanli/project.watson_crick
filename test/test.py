import os, sys

from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__),'../src')))

import des
import blowfish
#from src import main




def test():
    import time
    total=0.0
    n=1000
    for i in range(n):
        t0 = time.time()
        des.main()
        #blowfish.main()
        t1 = time.time()
        dif = t1-t0
        total=total+dif
        if i%50==0:
            print("%r" % (total/(i+1)))
    print("%r" % (total/n))
test()
