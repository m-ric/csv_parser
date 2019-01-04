from setuptools import setup

setup(
    name='csvparser',
    version='0.1',
    url='https://github.com/m-ric/csv_parser',
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["src/csvparser_build.py:ffi"], # "filename:global"
    install_requires=["cffi>=1.0.0"],
)