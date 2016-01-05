from greengraph import Map
from mock import patch
from nose.tools import assert_equal
from nose.tools import assert_raises
from .colors import colors

import numpy as np

@patch('requests.get')
@patch('matplotlib.image.imread')
def test_map_init(mock_imread,mock_get):
    m = Map(10.,10.)
    mock_get.assert_called_with('http://maps.googleapis.com/maps/api/staticmap?',
                                 params={'style': 'feature:all|element:labels|visibility:off',
                                         'center': '10.0,10.0', 'zoom': 10,
                                         'maptype': 'satellite', 
                                         'sensor': 'false', 'size': '400x400'})
    m = Map(10.,10., satellite=False)
    mock_get.assert_called_with('http://maps.googleapis.com/maps/api/staticmap?',
                                 params={'style': 'feature:all|element:labels|visibility:off',
                                         'center': '10.0,10.0', 'zoom': 10,
                                         'sensor': 'false', 'size': '400x400'})
    m = Map(10.,10., sensor=True)
    mock_get.assert_called_with('http://maps.googleapis.com/maps/api/staticmap?',
                                 params={'style': 'feature:all|element:labels|visibility:off',
                                         'center': '10.0,10.0', 'zoom': 10,
                                         'maptype': 'satellite', 
                                         'sensor': 'true', 'size': '400x400'})
    m = Map(10.,10., size=(200,300))
    mock_get.assert_called_with('http://maps.googleapis.com/maps/api/staticmap?',
                                 params={'style': 'feature:all|element:labels|visibility:off',
                                         'center': '10.0,10.0', 'zoom': 10,
                                         'maptype': 'satellite', 
                                         'sensor': 'false', 'size': '200x300'})
    m = Map(10.,10., zoom=5)
    mock_get.assert_called_with('http://maps.googleapis.com/maps/api/staticmap?',
                                 params={'style': 'feature:all|element:labels|visibility:off',
                                         'center': '10.0,10.0', 'zoom': 5,
                                         'maptype': 'satellite', 
                                         'sensor': 'false', 'size': '400x400'})

def test_green_detection():
    #Colour RGB values taken from 500 colors list, http://cloford.com/resources/colours/500col.htm
    m = Map(10,10)
    trues = []
    for color in colors:
        pixel = np.array([[[color[0]/255.,color[1]/255.,color[2]/255.]]])
        m.pixels = pixel
        trues.append(m.green(1.1)[0,0])
    assert np.sum(trues) == 54

def test_green_count():
    vals = range(1,100)
    m = Map(10.,15.)
    for val in vals:
        pixels = ([[0.,1.,0.]] * val) + ([[1.,1.,1.]] * (100-val))
        pixels = np.array(pixels, dtype='float32')
        pixels = pixels.reshape(10,10,3)
        m.pixels = pixels
        assert_equal(m.count_green(), val)

@patch('matplotlib.image.imsave')
def test_green_save(mock_imsave):
    vals = range(1,100)
    m = Map(10.,20.)
    for val in vals:
        pixels = ([[0,1,0]] * val) + ([[0,0,0]] * (100-val))
        pixels = np.array(pixels)
        pixels = pixels.reshape(10,10,3)
        m.pixels = pixels
        m.show_green()
        assert np.array_equal(mock_imsave.call_args[0][1],pixels)
    assert_equal(mock_imsave.call_args[1], {'format':'png'})
