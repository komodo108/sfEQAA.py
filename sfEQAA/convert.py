import astropy.units as u
from astropy.coordinates import SkyCoord, AltAz, EarthLocation
from astropy.time import Time
from typing import Tuple
import traceback, datetime

def EQ_AA(ra: float, dec: float, lat: float, long: float, time: datetime, debug = False) -> Tuple[SkyCoord, bool]:
    """ Convert EQ -> AltAz coordinates without `astropy` objects.
        - `ra` -> Right ascention of the object in degrees.
        - `dec` -> Declination of the object in degrees.
        - `lat` -> The latitude of where the observation occured in degrees.
        - `long` -> The longitude of where the observation occured in degrees.
        - `time` -> A datetime string ("%Y-%m-%d %H:%M:%S") with the date & time of the observation.
        - `debug`(False) -> Whether or not to print additional debug infromation when an Exception occurs.

        `returns` <- A `SkyCoord` with the same coordinates in the AltAz Frame. """
    # Get the location & time as astropy
    loc = _loc_to_astropy(lat, long, debug)
    if loc[1] == False: return (SkyCoord(0, 0, unit='deg'), False) # Cannot use None to detect fault!
    time = _time_to_astropy(time)

    # Convert
    try:
        eq = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame='icrs')
        aa = AltAz(location=loc[0], obstime=time)
        return (eq.transform_to(aa), True)
    except Exception as _:
        if(debug): traceback.print_exc()
        return (SkyCoord(0, 0, unit='deg'), False) # Cannot use None to detect fault!


def AA_EQ(alt: float, az: float, lat: float, long: float, time: datetime, debug = False) -> Tuple[SkyCoord, bool]:
    """ Convert AltAz -> EQ coordinates without `astropy` objects.
        - `alt` -> Altitude of the object in degrees.
        - `az` -> Azimuth of the object in degrees.
        - `lat` -> The latitude of where the observation occured in degrees.
        - `long` -> The longitude of where the observation occured in degrees.
        - `time` -> A datetime string ("%Y-%m-%d %H:%M:%S") with the date & time of the observation.
        - `debug`(False) -> Whether or not to print additional debug infromation when an Exception occurs.
        
        `returns` <- A `SkyCoord` with the same coordinates in the ICRS EQ Frame. """
    # Get the location & time as astropy
    loc = _loc_to_astropy(lat, long, debug)
    if loc[1] == False: return (SkyCoord(0, 0, unit='deg'), False) # Cannot use None to detect fault!
    time = _time_to_astropy(time)

    # Convert
    try:
        aa = SkyCoord(alt=alt * u.deg, az=az * u.deg, frame="altaz", location=loc[0], obstime=time)
        return (aa.icrs, True)
    except Exception as _:
        if(debug): traceback.print_exc()
        return (SkyCoord(0, 0, unit='deg'), False) # Cannot use None to detect fault!


def _loc_to_astropy(lat: float, long: float, debug = False) -> Tuple[EarthLocation, bool]:
    """ Helper function to convert a (lat, long)_pair to an astropy object """
    try:
        location = EarthLocation(lat=lat * u.deg, lon=long * u.deg, height=0 * u.m)
        return (location, True) # Cannot use None to detect fault!
    except Exception as _:
        if(debug): traceback.print_exc()
        return (EarthLocation(0 * u.deg, 0 * u.deg, 0 * u.m), False) # Cannot use None to detect fault!


def _time_to_astropy(time: datetime) -> Time:
    """ Helper function to convert a datetime string ("%Y-%m-%d %H:%M:%S") to an astropy object """
    return Time(time)