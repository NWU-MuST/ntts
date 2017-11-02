#!/usr/bin/env python
from __future__ import division

import sys
import numpy as np

if __name__ == "__main__":
    a = np.loadtxt(sys.stdin, dtype=np.int)
    #print a, len(a)
    
    comps = [[0, 1], [0, 2], [1, 2]]
    
    for comp in comps:
        #print "PRIM", comp[0]*2, comp[1]*2
        n1 = len(np.where(a[:,comp[0]*2] == 1)[0])
        n2 = len(np.where(a[:,comp[1]*2] == 1)[0])
        assert n1 == n2
        E_ov =  n1 * (n2 / len(a))
        E_ovp = E_ov / n1 * 100.0

        i1 = set(np.where(a[:,comp[0]*2] == 1)[0])
        i2 = set(np.where(a[:,comp[1]*2] == 1)[0])
        A_ov = len(i1.intersection(i2))
        A_ovp = A_ov / n1 * 100.0

        print "Listeners (columns)", comp
        print "PRIM chance", E_ov, "/", n1, E_ovp, "%"
        print "PRIM actual", A_ov, "/", n1, A_ovp, "%"
        print

    for comp in comps:
        c1 = a[:,comp[0]*2] + a[:,comp[0]*2+1]
        c2 = a[:,comp[1]*2] + a[:,comp[1]*2+1]
        n1 = len(np.where(c1 == 1)[0])
        n2 = len(np.where(c2 == 1)[0])
        #print "ALL", n1, n2, len(a)

        E_ov =  n1 * (n2 / len(a))

        i1 = set(np.where(c1 == 1)[0])
        i2 = set(np.where(c2 == 1)[0])
        E_ovp = E_ov / len(i1.union(i2)) * 100.0
        A_ov = len(i1.intersection(i2))
        A_ovp = A_ov / len(i1.union(i2)) * 100.0

        print "Listeners (columns)", comp
        print "ALL chance", E_ov, "/", len(i1.union(i2)), E_ovp, "%"
        print "ALL actual", A_ov, "/", len(i1.union(i2)), A_ovp, "%"
        print
