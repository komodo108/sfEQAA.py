import argparse, sys
from datetime import datetime
import sfEQAA.convert as convert

def exit(message, debug):
    """ Exits the program with an error message.
        Additionally informs the user to set the `--debug` flag to get more information """
    print("Error: " + message)
    if(not debug): print("For more information on this error, try setting the --debug flag")
    sys.exit(1)

def parse():
    """ Parse command line arguments for `sfEQAA.py` """
    parse = argparse.ArgumentParser(prog="sfEQAA.py", description="Convert between equatorial (ra/dec) and alt-az coordinates")
    parse.add_argument("lat", metavar='latitude', type=float, nargs=1, help="Latitude of the observer (decimal degrees)")
    parse.add_argument("long", metavar='longitude', type=float, nargs=1, help="Longitude of the observer (decimal degrees)")
    parse.add_argument("date", type=lambda d: datetime.strptime(d, "%d/%m/%Y"), nargs=1, help="Date of the observation (d/m/Y)")
    parse.add_argument("time", type=lambda t: datetime.strptime(t, "%H:%M:%S"), nargs=1, help="Time of the observation in 24-hour format (H:M:S)")
    parse.add_argument("--debug", action='store_true', help="Print out additional error information")
    subsparsers = parse.add_subparsers(dest="mode", help="Mode of operation")
    subsparsers.required = True

    # Need ra, dec 
    eqparser = subsparsers.add_parser("eq", help="Equatorial (Ra/Dec) -> Alt-Az")
    eqparser.add_argument('ra', metavar='right ascension', type=float, nargs=1, help="Right ascension of the observation (decimal degrees)")
    eqparser.add_argument('dec', metavar='declination', type=float, nargs=1, help="Declination of the observation (decimal degrees)")
    eqparser.set_defaults(mode="eq")

    # Need alt, az
    azparser = subsparsers.add_parser("altaz", help="Alt-Az -> Equatorial (Ra/Dec)")
    azparser.add_argument('alt', metavar='altitude', type=float, nargs=1, help="Altitude of the observation (decimal degrees)")
    azparser.add_argument('az', metavar='azimuth', type=float, nargs=1, help="Azimuth of the observation (decimal degrees)")
    azparser.set_defaults(mode="aa")

    # Get the arguments and parse them
    return parse.parse_args()

if __name__ == "__main__":
    """ Command line interface for `sfEQAA.py`. """
    # Parse command line arguments
    args = parse()
    debug = args.debug

    # Need to convert the time back into a string
    time = str(args.date[0].strftime("%Y-%m-%d")) + " " + str(args.time[0].strftime("%H:%M:%S"))

    # Now parse the eq / alt-az arguments & convert using our convertion functions
    if(args.mode == "eq"):
        aa = convert.EQ_AA_loc(args.ra[0], args.dec[0], args.lat[0], args.long[0], time, debug)
        if not aa[1]: exit("Couldn't convert from these equatorial coordinates!", debug)
        else: aa = aa[0]
    else:
        eq = convert.AA_EQ_loc(args.alt[0], args.az[0], args.lat[0], args.long[0], time, debug)
        if not eq[1]: exit("Couldn't convert from these alt-az coordinates!", debug)
        else: eq = eq[0]

    # Finally print out the converted coordinates as degrees
    if(args.mode == "eq"): print(aa.alt.degree, aa.az.degree)
    else: print(eq.ra.degree, eq.dec.degree)