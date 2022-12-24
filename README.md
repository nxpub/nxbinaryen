# nxbinaryen
Python Bindings for Binaryen

### TODOs:
* Add enums w/ cached values
* Review the layout (split regions)

### Problems:
* num-params aren't reduced (degradation)
* wrong ptr wrapping (see TypeExpand, TypeBuilderBuildAndDispose)
* cffi vs overflow in LiteralFloat32Bits, LiteralFloat64Bits (see tests)