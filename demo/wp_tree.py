#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pprint

from pywt import WaveletPacket

wp = WaveletPacket(range(16), 'db2', maxlevel=3)

pprint.pprint([node.path for node in wp.get_leaf_nodes(decompose=False)])
pprint.pprint([node.path for node in wp.get_leaf_nodes(decompose=True)])

coeffs = [(node.path, node.data) for node in wp.get_leaf_nodes(decompose=True)]
pprint.pprint(coeffs)

wp2 = WaveletPacket(None, 'db2', maxlevel=3)
for path, data in coeffs:
    wp2[path] = data

pprint.pprint([node.path for node in wp2.get_leaf_nodes(decompose=False)])
pprint.pprint(wp2.reconstruct())
