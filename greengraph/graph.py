from greengraph.google_map import Map

import numpy as np
import geopy

class Greengraph(object):
    """Class which """
    def __init__(self, start, end):
        """Initialise the Greengraph with a <start> and <end> location."""
        self.start = start
        self.end = end
        self.geocoder = geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

    def geolocate(self, place):
        """Return the Google geocode of a given place name."""
        return self.geocoder.geocode(place,exactly_one=False)[0][1]

    def location_sequence(self, start,end,steps):
        """Break the distance between the <start> and <end> locations into <steps> steps."""
        if abs(start[0]) > 90. or abs(end[0]) > 90. or abs(start[1]) >180. or abs(end[1])>180.:
            raise ValueError('Invalid coordinates')
        lats = np.linspace(start[0], end[0], steps)
        longs = np.linspace(start[1],end[1], steps)
        return np.vstack([lats, longs]).transpose()

    def green_between(self, steps):
        """Return the amount of green in each of the <steps> steps."""
        return [Map(*location).count_green()
                for location in self.location_sequence(
                self.geolocate(self.start),
                self.geolocate(self.end),
                steps)]
                