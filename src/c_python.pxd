# Copyright (c) 2006-2010 Filip Wasilewski <http://filipwasilewski.pl/>
# See COPYING for license details.

cdef extern from "Python.h":

    ctypedef int Py_intptr_t

    ctypedef struct _typeobject:
        pass
    ctypedef struct PyObject:
        _typeobject* ob_type
        #pass
