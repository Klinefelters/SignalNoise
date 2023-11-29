from setuptools import setup

setup(
    name='signalnoise',
    version='0.1.0',
    description='A TK GUI that allows the user to simulate noise filtering for signals',
    url='https://github.com/klinefelters/SignalNoise',
    author='Steven Klinefelter',
    author_email='klinefelters@etown.edu',
    license='MIT',
    packages=['signalnoise'],
    install_requires=[
        'mpi4py',
        'matplotlib',
        'scipy',
        'numpy'
    ],

    classifiers=[
        'Development Status :: 1 - Testing',
        'Programming Language :: Python :: 3.11.x',
        'Programming Language :: Python :: 3.10.x',
        'Programming Language :: Python :: 3.9.x',
        'Programming Language :: Python :: 3.8.x',
    ],
)
