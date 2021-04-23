#!/usr/bin/env python
import sfEQAA.convert as convert
import datetime

if __name__ == "__main__":
    aa = convert.EQ_AA_loc(0, 0, 0, 0, datetime.datetime.now())
    print(aa[0])