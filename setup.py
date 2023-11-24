from setuptools import setup

setup(
    name='signalnoise',
    version='0.1.0',
    description='Building',
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
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.11.6',
    ],
)
