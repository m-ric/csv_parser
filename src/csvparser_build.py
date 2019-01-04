#!/usr/bin/env python3

from cffi import FFI
import os

#libcsvparser_dir = os.path.expanduser('./')

ffi = FFI()

# cdef() expects a string listing the C types, functions and
# globals needed from Python. The string follows the C syntax.
with open(os.path.join(os.path.dirname(__file__), "csvparser_cffi.h")) as fp:
    ffi.cdef(fp.read())

# This describes the extension module "_pi_cffi" to produce.
ffi.set_source("csvparser_cffi",
    '#include "csvparser_cffi.h"',
    libraries=['csvparser'],
    library_dirs=[os.path.dirname(__file__)],
)

if __name__ == "__main__":
    ffi.compile(verbose=True)