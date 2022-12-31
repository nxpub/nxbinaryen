import cffi

from scripts.utils import preprocess_header, BINARYEN_C_HEADER_PATH, BINARYEN_ROOT

BINARYEN_C_SOURCE = """
#include <binaryen-c.h>
"""

ffi = cffi.FFI()
ffi.cdef(preprocess_header(BINARYEN_C_HEADER_PATH, strip_deprecated=True))
ffi.set_source(
    module_name='nxbinaryen.binaryen',
    source=BINARYEN_C_SOURCE,
    libraries=['binaryen', 'stdc++'],
    # To make a static library libbinaryen.a
    # cmake . -DBUILD_STATIC_LIB=1 -DBUILD_TESTS=0 -DBUILD_TOOLS=0
    # cmake --build . -j`nproc`
    library_dirs=[str(BINARYEN_ROOT / 'lib')],
    include_dirs=[str(BINARYEN_ROOT), str(BINARYEN_ROOT / 'src')],
)


if __name__ == '__main__':
    ffi.compile(verbose=True)
