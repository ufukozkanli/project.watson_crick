import os, sys

from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__),'../src')))

import des
import blowfish
import time
import m
#from src import main



alg="DES" #"DES","BLOWFISH"

def test():
    default_usage=m.get_usage()
    total=0.0
    ram_total=0.0
    cpu_total=0.0
    n=200  
    for i in range(n):
        usage=m.get_usage()
        cpu_total=cpu_total+usage['CPU']-default_usage['CPU']    
        ram_total=cpu_total+usage['MEMUSED']-default_usage['MEMUSED']        
        #print("CPU:",cpu_total)
        #print("RAM:",ram_total)
        t0 = time.time()
        if alg=="DES":
            des.main()
        if alg=="BLOWFISH":
            blowfish.main()
        t1 = time.time()
        dif = t1-t0
        total=total+dif
        if i%50==0:
            print("N: %r" % i,(total/(i+1)))
    print("ALG:%r" % alg)
    print("Time(s):%r" % (total/n))
    print("CPU(%%):%r" % (cpu_total/n))
    print("RAM(MB):%r" % (ram_total/n/1000000))
test()
