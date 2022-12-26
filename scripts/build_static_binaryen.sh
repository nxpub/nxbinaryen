cd ../binaryen
make clean
cmake . -DBUILD_STATIC_LIB=1 -DBUILD_TESTS=0 -DBUILD_TOOLS=0
cmake --build . -j`nproc`