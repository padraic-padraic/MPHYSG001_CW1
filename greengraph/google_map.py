import numpy as np
import requests
from StringIO import StringIO
from matplotlib import image as img

class Map(object):
    """Class that stores a PNG image of a google map and calcualtes the amount of green present."""
    def __init__(self, lat, long, satellite=True,
                 zoom=10, size=(400, 400), sensor=False):
        """Define the map parameters, fetch it and save it."""
        base = "http://maps.googleapis.com/maps/api/staticmap?"
        params = dict(
            sensor=str(sensor).lower(),
            zoom=zoom,
            size="x".join(map(str, size)),
            center=",".join(map(str, (lat, long) )),
            style="feature:all|element:labels|visibility:off"
        )
        if satellite:
            params["maptype"] = "satellite"
        self.image = requests.get(base, params=params).content
        # Fetch our PNG image data
        self.pixels = img.imread(StringIO(self.image))
        # Parse our PNG image as a numpy array
    
    def green(self, threshold):
        """For a given pixel, determine if it's green based on <threshold>, and return a logical array over all pixels."""
        # Use NumPy to build an element-by-element logical array
        greener_than_red = self.pixels[:, :, 1] > threshold*self.pixels[:,:,0]
        greener_than_blue = self.pixels[:, :, 1] > threshold*self.pixels[:,:,2]
        green = np.logical_and(greener_than_red, greener_than_blue)
        return green

    def count_green(self, threshold = 1.1):
        """Count the number of green pixels"""
        return np.sum(self.green(threshold))

    def show_green(self, threshold = 1.1):
        """Save a PNG showing only the green spaces."""
        green = self.green(threshold)
        out = green[:, :, np.newaxis]*np.array([0, 1, 0])[np.newaxis,
                                                          np.newaxis, :]
        buffer = StringIO()
        result = img.imsave(buffer, out, format='png')
        return buffer.getvalue()
