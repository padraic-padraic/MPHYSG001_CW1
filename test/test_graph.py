from greengraph import Greengraph

from itertools import combinations_with_replacement
from nose.tools import assert_almost_equal
from nose.tools import assert_raises
from mock import patch

graph =  Greengraph('London', 'Chiacago')

def test_geolocate():
    start, end = (graph.geolocate(graph.start), graph.geolocate(graph.end))
    true_start = (51.507351, -0.127759)
    true_end = (41.878103, -87.629798)
    points = zip(start,true_start) + zip(end,true_end)
    for point, true_point in points:
        assert_almost_equal(point, true_point, 3)

def test_geocoder():
    with assert_raises(ValueError):
        graph.geolocate('hjkbjhild') == None

def test_coodinates():
    with assert_raises(ValueError):
        graph.location_sequence((100.,0.),(45.,45.),20)
    with assert_raises(ValueError):
        graph.location_sequence((-100.,0.),(45.,45.),20)

def test_location_sequence():
    points = Greengraph.location_sequence(Greengraph('London','Texas'),
                                         (10.,10.), (20.,20.), 10)
    diffs = [points[i][0] - points[i-1][0] for i in range(1,10)]
    for diff1, diff2 in combinations_with_replacement(diffs, 2):
        assert_almost_equal(diff1, diff2)
    for diff in diffs:
        assert_almost_equal(diff, ((20.-10.)/9))

@patch('greengraph.google_map.Map.count_green')
@patch('greengraph.Greengraph.geolocate',return_value=(10.,10.))
def test_green_between(mock_geolocate,mock_map):
    Greengraph('10.,10.','20.,20.').green_between(2)
    assert mock_map.call_count == 2

def test_limits():
    with assert_raises(RuntimeError):
        while True:
            graph.geolocate('Lapland')