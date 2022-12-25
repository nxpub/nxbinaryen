# nxbinaryen
Python Bindings for Binaryen

### TODOs:
* Review the layout (split regions)
* Add test coverage, verify

### Problems:
* num-params aren't reduced (degradation)
* wrong ptr wrapping (see TypeExpand, TypeBuilderBuildAndDispose)
* cffi vs overflow in LiteralFloat32Bits, LiteralFloat64Bits (see tests)
* github action doesn't work properly