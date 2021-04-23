import astropy.units as u
from astropy.coordinates import SkyCoord, AltAz, EarthLocation
from astropy.time import Time
import traceback

def EQ_AA(ra, dec, loc, time, debug=False):
    """ Convert EQ -> AltAz coordinates.
        - `ra` > Right ascention of the object in degrees.
        - `dec` > Declination of the object in degrees.
        - `loc` > An astropy `EarthLocation` object with the observers current location.
        - `time` > An astropy `Time` object with the time of the observation.
        - `debug`(False) > Whether or not to print additional debug infromation when an Exception occurs. """
    try:
        eq = SkyCoord(ra * u.deg, dec * u.deg)
        aa = AltAz(location=loc, obstime=time)
        return (eq.transform_to(aa), True)
    except Exception as _:
        if(debug): traceback.print_exc()
        return (SkyCoord(0, 0, unit='deg'), False) # Cannot use None to detect fault!


def EQ_AA_loc(ra, dec, lat, long, time, debug=False):
    """ Convert EQ -> AltAz coordinates without `astropy` objects.
        - `ra` > Right ascention of the object in degrees.
        - `dec` > Declination of the object in degrees.
        - `lat` > The latitude of where the observation occured in degrees.
        - 'long' > The longitude of where the observation occured in degrees.
        - `time` > A datetime string ("%Y-%m-%d %H:%M:%S") with the date & time of the observation.
        - `debug`(False) > Whether or not to print additional debug infromation when an Exception occurs. """
    # Get the location & time as astropy
    loc = _loc_to_astropy(lat, long, debug)
    if loc[1] == False: return (SkyCoord(0, 0, unit='deg'), False) # Cannot use None to detect fault!
    time = _time_to_astropy(time)

    # Use the current functions
    return EQ_AA(ra, dec, loc[0], time, debug)


def AA_EQ(alt, az, loc, time, debug=False):
    """ Convert AltAz -> EQ coordinates.
        - `alt` > Altitude of the object in degrees.
        - `az` > Azimuth of the object in degrees.
        - `loc` > An astropy `EarthLocation` object with the observers current location.
        - `time` > An astropy `Time` object with the time of the observation.
        - `debug`(False) > Whether or not to print additional debug infromation when an Exception occurs. """
    try:
        aa = SkyCoord(alt=alt * u.deg, az=az * u.deg, frame="altaz", location=loc, obstime=time)
        return (aa.icrs, True)
    except Exception as _:
        if(debug): traceback.print_exc()
        return (SkyCoord(0, 0, unit='deg'), False) # Cannot use None to detect fault!


def AA_EQ_loc(alt, az, lat, long, time, debug=False):
    """ Convert AltAz -> EQ coordinates without `astropy` objects.
        - `alt` > Altitude of the object in degrees.
        - `az` > Azimuth of the object in degrees.
        - `lat` > The latitude of where the observation occured in degrees.
        - 'long' > The longitude of where the observation occured in degrees.
        - `time` > A datetime string ("%Y-%m-%d %H:%M:%S") with the date & time of the observation.
        - `debug`(False) > Whether or not to print additional debug infromation when an Exception occurs. """
    # Get the location & time as astropy
    loc = _loc_to_astropy(lat, long, debug)
    if loc[1] == False: return (SkyCoord(0, 0, unit='deg'), False) # Cannot use None to detect fault!
    time = _time_to_astropy(time)

    # Use the current functions
    return AA_EQ(alt, az, loc[0], time, debug)    


def _loc_to_astropy(lat, long, debug=False):
    """ Helper function to convert a (lat, long)_pair to an astropy object """
    try:
        location = EarthLocation(lat=lat * u.deg, lon=long * u.deg, height=0 * u.m)
        return (location, True)
    except Exception as _:
        if(debug): traceback.print_exc()
        return (EarthLocation(0 * u.deg, 0 * u.deg, 0 * u.m), False)


def _time_to_astropy(string):
    """ Helper function to convert a datetime string ("%Y-%m-%d %H:%M:%S") to an astropy object """
    return Time(string)