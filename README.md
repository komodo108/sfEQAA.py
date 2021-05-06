# `sfEQAA.py`
Helper functions using `astropy` to convert between Equatiorial (ICRS) & Alt-Az coordinate systems.

This was made to be part of the **smart finder** software suite.

## Usage
### Programmatic
`sfEQAA` exports functions that can be used to convert between coordinates easily.

To use them within your program, simply install this git repository under your python package manager (we recommend `pipenv`). An example of their usage is given below:
```py
import sfEQAA
import datetime

if __name__ == "__main__":
    aa = sfEQAA.EQ_AA(0, 0, 0, 0, datetime.datetime.utcnow())
    print(aa[0]) if aa[1] else print(":(")
```

Please note that these functions return a tuple `(value, success)` as there is a problem with comparing to `None` within `astropy`. Therefore to check for success, you should first check if `val[1] == True`, then extract the value: `val = val[0]`.

Please note that the time one provides **must** be in UTC. Please also note `astropy` returns `0 <= az <= 360`, `-90 <= alt <= 90` & `0 <= ra <= 360`, `-90 <= dec <= 90`.

### Command line
`sfEQAA.py` can also be used as a command line tool to convert between coordinates.   

Before running please ensure that `astropy` is installed with `pip`. Or, run `pipenv sync` (install `pipenv` with `pip install pipenv`) to install `astropy` within a python virtual enviroment.

To see the arguments this program needs to recieve, please run the following:
```
pipenv run python sfEQAA.py -h
```

## Changelog
- `1.2` (06/05/2021):
    - Added license notice into `README.md`.
    - [Closed #1](https://github.com/komodo108/sfEQAA.py/issues/1):
        - All times given to `sfEQAA` must be in UTC, changed `time` parameter to type `datetime` to support this.
        - Updated `sfEQAA.py` command line script to automatically get timezone from system.
- `1.1` (05/05/2021):
    - Removed `EQ_AA_loc` & `AA_EQ_loc` in favor of not allowing developers to input their own `EarthLocation` & `Time` objects and instead use the provided helper functions.
    - Removed unneccessary `convert` submodule, imports are now `import sfEQAA`.
    - Looked into a bug causing coordinates to be off from those seen in stellarium [see #1](https://github.com/komodo108/sfEQAA.py/issues/1). Will continue investigating.
    - Updated documentation.
    - Add changelog.
    - Add Apache License.
- `1.0` (23/04/2021): Initial Release

## License
Apache 2.0.
