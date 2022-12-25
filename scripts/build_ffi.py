import cffi

from scripts.utils import preprocess_header, BINARYEN_C_HEADER_PATH

BINARYEN_C_SOURCE = """
#include <binaryen-c.h>
"""

ffi = cffi.FFI()
ffi.cdef(preprocess_header(BINARYEN_C_HEADER_PATH, strip_deprecated=True))
ffi.set_source(
    module_name='nxbinaryen.binaryen',
    source=BINARYEN_C_SOURCE,
    libraries=['binaryen'],
    # TODO: Static build? Seems pretty big (53 mb w/ BUILD_LLVM_DWARF, 50 mb w/o)
    # cmake . -DBUILD_STATIC_LIB=1 -DBUILD_TESTS=0 -DBUILD_TOOLS=0
    # cmake --build . -j XX
)


if __name__ == '__main__':
    ffi.compile(verbose=True)
