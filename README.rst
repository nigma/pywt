Important
=========

**We're moving! The new home for the project is https://github.com/PyWavelets.**

Thanks everyone for starring, forking and following this repository on Github.

The PyWavelets project has a new home and maintainers.

Please go to https://github.com/PyWavelets/pywt and follow the development and new releases there.

PyWavelets - Discrete Wavelet Transform in Python
=================================================

PyWavelets is a free Open Source wavelet transform software for Python_
programming language. It is written in Python, Cython and C for a mix of easy
and powerful high-level interface and the best performance.

PyWavelets is very easy to start with and use, and currently is capable of:

  * 1D and 2D Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
  * 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
  * 1D and 2D Wavelet Packet decomposition and reconstruction
  * Approximating wavelet and scaling functions
  * Over seventy built-in wavelet filters and custom wavelets supported
  * Single and double precision calculations
  * Results compatibility with Matlab Wavelet Toolbox (tm)

.. image::
    https://secure.travis-ci.org/rgommers/pywt.png?branch=master
    :alt: Build Status
    :target: https://secure.travis-ci.org/rgommers/pywt


Requirements
------------

PyWavelets is a package for the Python programming language. It requires:

 - Python_ 2.6 or 2.7
 - numpy_ numeric array module

Download
--------

The most recent *development* version can be found on GitHub at
https://github.com/nigma/pywt.

Latest release, including source and binary package for Windows, is available
for download from the `Python Package Index`_.

Install
-------

In order to build PyWavelets from source, a working C compiler (GCC or MSVC)
and a recent version of Cython_ is required.

 - To install PyWavelets open shell prompt and type ``pip install PyWavelets``
   or ``easy_install PyWavelets``.

 - To build and install from source, navigate to downloaded PyWavelets source
   code directory and type ``python setup.py install``.

 - The `in-development version`_ of PyWavelets can be installed with
   ``pip install PyWavelets==dev`` or ``easy_install PyWavelets==dev``.

Prebuilt Windows binaries and source code packages are also
available from `Python Package Index`_.

Binary packages for several Linux distributors are maintained by Open Source
community contributors. Query your Linux package manager tool
for `python-wavelets`, `python-pywt` or similar package name.

Documentation
-------------

Documentation with detailed examples and links to more resources is available
online at http://www.pybytes.com/pywavelets/ and
http://pywavelets.readthedocs.org.

For more usage examples see the `demo`_ directory in the source package.

Contributing
------------

PyWavelets started in 2006 as an academic project for a master thesis
on `Analysis and Classification of Medical Signals using Wavelet Transforms`
and is maintained by its `original developer`_.

All contributions including bug reports, bug fixes, new feature implementations
and documentation improvements are welcome.

Go and fork on `GitHub`_ today!

Python 3
--------

Python 3 development branch is at https://github.com/nigma/pywt/tree/py-3.
Check out the `changelog <https://github.com/nigma/pywt/commits/py-3>`_ for
info. Currently the code and examples are ported to work on Python 2.7 and 3.2
from the same codebase.

Contact
-------

Use `GitHub Issues`_ or `PyWavelets discussions group`_ to post your
comments or questions.

License
-------

PyWavelets is a free Open Source software released under the MIT license.

Commercial Support
------------------

For information on commercial support and development email me at en@ig.ma.


.. _Cython: http://cython.org/
.. _demo: https://github.com/nigma/pywt/tree/master/demo
.. _GitHub: https://github.com/nigma/pywt
.. _GitHub Issues: https://github.com/nigma/pywt/issues
.. _in-development version: https://github.com/nigma/pywt/tarball/develop#egg=PyWavelets-dev
.. _numpy: http://numpy.scipy.org/
.. _original developer: http://en.ig.ma
.. _Python: http://python.org/
.. _Python Package Index: http://pypi.python.org/pypi/PyWavelets/
.. _PyWavelets discussions group: http://groups.google.com/group/pywavelets

