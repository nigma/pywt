#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import pywt

data = range(16)
wavelet = "db4"
level = 2
mode = "cpd"

print("original data:")
print(data)

# dec = [cA(n-1) cD(n-1) cD(n-2) ... cD(2) cD(1)]
dec = pywt.wavedec(data, wavelet, mode, level)

print("decomposition:")

print("cA{0}".format(len(dec) - 1))
print(" ".join("{0:.3f}".format(val) for val in dec[0]))

for i,d in enumerate(dec[1:]):
    print("cD{0}:".format(len(dec) - 1 - i))
    print(" ".join("{0:.3f}".format(val) for val in d))

print()
print("reconstruction:")

print(" ".join("{0:.3f}".format(val) for val in pywt.waverec(dec, wavelet, mode)))
