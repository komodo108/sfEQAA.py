# `sfEQAA.py`
Helper functions using `astropy` to convert between Equatiorial (ICRS) & Alt-Az coordinate systems.

This was made to be part of the **smart finder** software suite.

## Usage
### Programmatic
`sfEQAA.convert` exports functions that can be used to convert between coordinates easily.

To use them within your program, simply install this git repository under your python package manager (we recommend `pipenv`). An example of their usage is given below:
```py
import sfEQAA.convert as convert
import datetime

if __name__ == "__main__":
    aa = convert.EQ_AA_loc(0, 0, 0, 0, datetime.datetime.now())
    print(aa[0])
```

Please note that these functions return a tuple `(value, success)` as there is a problem with comparing to `None` within `astropy`. Therefore to check for success, you should first check if `val[1] == True`, then extract the value: `val = val[0]`.

Please refer to the source for documentation on the other functions

### Command line
`sfEQAA.py` can also be used as a command line tool to convert between coordinates.   

Before running please ensure that `astropy` is installed with `pip`. Or, run `pipenv sync` (install `pipenv` with `pip install pipenv`) to install `astropy` within a python virtual enviroment.

To see the arguments this program needs to recieve, please run the following:
```
pipenv run python sfEQAA.py -h
```