from greengraph import Map
from mock import MagicMock, patch
from nose.tools import assert_equal
from nose.tools import assert_raises

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

# def test