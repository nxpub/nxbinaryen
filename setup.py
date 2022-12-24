from setuptools import setup

setup(
    name='nxbinaryen',
    version='1.111.0',
    url='https://github.com/nxpub/nxbinaryen',
    author='NX Maintainer',
    author_email='support@nx.pub',
    description='Python Bindings for Binaryen',
    license='MIT License',
    license_files=('LICENSE',),
    zip_safe=False,
    include_package_data=True,
    setup_requires=['cffi>=1.13.2'],
    install_requires=['cffi>=1.13.2'],
    cffi_modules=['scripts/build_ffi.py:ffi'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
    ]
)
