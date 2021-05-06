#!/usr/bin/env python
import sfEQAA
import datetime

if __name__ == "__main__":
    aa = sfEQAA.EQ_AA(0, 0, 0, 0, datetime.datetime.utcnow())
    print(aa[0]) if aa[1] else print(":(")
    