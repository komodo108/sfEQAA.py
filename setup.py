from setuptools import setup, find_packages

setup(
    name='sfEQAA.py',
    version='0.1.0',    
    description='Convert between equatorial (ra/dec) and alt-az coordinates',
    url='https://github.com/komodo108/sfEQAA.py',
    author='komodo108',
    author_email='p@ul.gr',
    packages=find_packages(exclude=['examples']),
    install_requires=['astropy',                     ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)