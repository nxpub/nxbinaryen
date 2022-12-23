from setuptools import setup

setup(
    setup_requires=['cffi>=1.13.2'],
    install_requires=['cffi>=1.13.2'],
    cffi_modules=['./scripts/build_ffi.py:ffi'],
)
