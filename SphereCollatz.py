#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
    # <your code>

    v = 1
    min = 0
    max = 0
    if i <= j:
        min = i
        max = j
    else:
        min = j
        max = i

    if (max >> 1) >= min:
        min = max >> 1

    if min<=99999 and (max>=200000 and max<=299999): #first cache loop
        v=383
        maxc = collatz_eval(200000, max)
        if maxc > v:
            v = maxc
        assert v >= 383

    elif min<=99999 and (max>=300000 and max<=399999): #second cache loop
        v=443
        assert v == 443

    elif min<=99999 and (max>=400000 and max<=499999): #third cache loop
        v=443
        maxc = collatz_eval(400000, max)
        if maxc > v:
            v = maxc
        assert v >= 443

    elif min<=99999 and (max>=500000 and max<=599999): #fourth cache loop
        v=449
        maxc = collatz_eval(500000, max)
        if maxc > v:
            v = maxc
        assert v >= 449

    elif min<=99999 and (max>=600000 and max<=899999): #fifth cache loop
        v=470
        assert v == 470

    elif min<=99999 and (max>=900000 and max<=999999): #sixth cache loop
        v=470
        maxc = collatz_eval(900000, max)
        if maxc > v:
            v = maxc
        assert v >= 470

    elif (min>=100000 and min<=199999) and (max>=300000 and max<=399999): #seventh cache loop
        v=443
        assert v == 443

    elif (min>=100000 and min<=199999) and (max>=400000 and max<=499999): #eigth cache loop
        v=443
        maxc = collatz_eval(400000, max)
        if maxc > v:
            v = maxc
        assert v >= 443

    elif (min>=100000 and min<=199999) and (max>=500000 and max<=599999): #nineth cache loop
        v=449
        maxc = collatz_eval(500000, max)
        if maxc > v:
            v = maxc
        assert v >= 449

    elif (min>=100000 and min<=199999) and (max>=600000 and max<=899999): #tenth cache loop
        v=470
        assert v == 470

    elif (min>=100000 and min<=199999) and (max>=900000 and max<=999999): #eleventh cache loop
        v=470
        maxc = collatz_eval(900000, max)
        if maxc > v:
            v = maxc
        assert v >= 470

    elif (min>=200000 and min<=299999) and (max>=400000 and max<=499999): #twelveth cache loop
        v=441
        minc = collatz_eval(min, 299999)
        if minc > 441: #441 is  cache value of 300000-399999
            v = minc
        maxc = collatz_eval(400000, max)
        if maxc > v:
            v = maxc
        assert v >= 441

    elif (min>=200000 and min<=299999) and (max>=500000 and max<=599999): #thirteenth cache loop
        v = 449
        maxc = collatz_eval(500000, max)
        if maxc > v:
            v = maxc
        assert v >= 449

    elif (min>=200000 and min<=299999) and (max>=600000 and max<=899999): #fourteenth cache loop
        v = 470
        assert v == 470

    elif (min>=200000 and min<=299999) and (max>=900000 and max<=999999): #fifteenth cache loop
        v = 470
        maxc = collatz_eval(900000, max)
        if maxc > v:
            v = maxc
        assert v >= 470

    elif (min>=300000 and min<=399999) and (max>=500000 and max<=599999): #sixteenth cache loop
        v = 449
        maxc = collatz_eval(500000, max)
        if maxc > v:
            v = maxc
        assert v >= 449

    elif (min>=300000 and min<=399999) and (max>=600000 and max<=899999): #seventeenth cache loop
        v = 470
        assert v == 470

    elif (min>=300000 and min<=399999) and (max>=900000 and max<=999999): #eighteenth cache loop
        v = 470
        maxc = collatz_eval(900000, max)
        if maxc > v:
            v = maxc
        assert v >= 470

    elif (min>=400000 and min<=499999) and (max>=600000 and max<=899999): #nineteenth cache loop
        v = 470
        assert v == 470

    elif (min>=400000 and min<=499999) and (max>=900000 and max<=999999): #twentieth cache loop
        v = 470
        maxc = collatz_eval(900000, max)
        if maxc > v:
            v = maxc
        assert v >= 470

    elif (min>=500000 and min<=599999) and (max>=700000 and max<=799999): #twenty-first cache loop
        v = 447
        minc = collatz_eval(min, 599999)
        if minc > 447: #447 is  cache value of 600000-699999
            v = minc
        maxc = collatz_eval(700000, max)
        if maxc > v:
            v = maxc
        assert v >= 447

    elif (min>=500000 and min<=599999) and (max>=800000 and max<=899999): #twenty-second cache loop
        v = 468
        minc = collatz_eval(min, 599999)
        if minc > 468: #447 is  cache value of 700000-799999
            v = minc
        maxc = collatz_eval(800000, max)
        if maxc > v:
            v = maxc
        assert v >= 468

    elif (min>=500000 and min<=599999) and (max>=900000 and max<=999999): #twenty-third cache loop
        v = 468
        minc = collatz_eval(min, 599999)
        if minc > 468: #468 is  cache value of 700000-799999
            v = minc
        maxc = collatz_eval(900000, max)
        if maxc > v:
            v = maxc
        assert v >= 468

    elif (min>=600000 and min<=699999) and (max>=800000 and max<=899999): #twenty-fourth cache loop
        v = 468
        assert v == 468

    elif (min>=600000 and min<=699999) and (max>=900000 and max<=999999): #twenty-fifth cache loop
        v = 468
        maxc = collatz_eval(900000, max)
        if maxc > v:
            v = maxc
        assert v >= 468

    elif (min>=700000 and min<=799999) and (max>=900000 and max<=999999): #twenty-sixth cache loop
        v = 450
        minc = collatz_eval(min, 799999)
        if minc > 450: #450 is  cache value of 800000-899999
            v = minc
        maxc = collatz_eval(900000, max)
        if maxc > v:
            v = maxc
        assert v >= 450

    else:
        for k in range(min, max + 1):
            c = 1
            l = k
            while l > 1:
                if(l%2 == 0):
                    l = l >> 1
                    c = c + 1
                else:
                    l = ((l << 1) + l + 1) >> 1
                    c = c + 2
            if c > v:
                v = c
    
    assert v > 0
    return v

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)












#!/usr/bin/env python

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To run the program
    % python RunCollatz.py < RunCollatz.in > RunCollatz.out
    % chmod ugo+x RunCollatz.py
    % RunCollatz.py < RunCollatz.in > RunCollatz.out

To document the program
    % pydoc -w Collatz
"""

# -------
# imports
# -------

import sys

# from Collatz import collatz_solve

# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)