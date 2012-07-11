#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import time, gc, sys
import pywt
import numpy
import pylab

if sys.platform == 'win32':
    clock = time.clock
else:
    clock = time.time

sizes = [
    20, 50, 100, 120, 150, 200, 250, 300, 400, 500, 600, 750,
    1000, 2000, 3000, 4000, 5000, 6000, 7500,
    10000, 15000, 20000, 25000, 30000, 40000, 50000, 75000,
    100000, 150000, 200000, 250000, 300000, 400000, 500000,
    600000, 750000, 1000000
]

wavelet_names = [
    'db1', 'db2', 'db3', 'db4', 'db5', 'db6', 'db7', 'db8', 'db9', 'db10',
    'sym10', 'coif1', 'coif2', 'coif3', 'coif4', 'coif5'
]

dtype = numpy.float64

wavelets = [pywt.Wavelet(n) for n in wavelet_names]
mode = pywt.MODES.zpd

times_dwt = [[] for i in range(len(wavelets))]
times_idwt = [[] for i in range(len(wavelets))]

repeat = 5

for j, size in enumerate(sizes):
    data = numpy.ones((size,), dtype)

    print("{0:>2}/{1:<3}{0:>9}".format(j+1, len(sizes), size), end="")

    for i, w in enumerate(wavelets):
        min_t1, min_t2 = 9999., 9999.
        for _ in range(repeat):
            t1 = clock()
            (a, d) = pywt.dwt(data, w, mode)
            t1 = clock() - t1
            min_t1 = min(t1, min_t1)

            t2 = clock()
            a0 = pywt.idwt(a, d, w, mode)
            t2 = clock() - t2
            min_t2 = min(t2, min_t2)

        times_dwt[i].append(min_t1)
        times_idwt[i].append(min_t2)
        print(".", end="")
    print()
    gc.collect()

for j, (times, name) in enumerate([(times_dwt, 'dwt'), (times_idwt, 'idwt')]):
    pylab.figure(j)
    pylab.title(name)

    for i, n in enumerate(wavelet_names):
        pylab.loglog(sizes, times[i], label=n)

    pylab.legend(loc='best')
    pylab.xlabel('len(x)')
    pylab.ylabel('time [s]')

pylab.show()
