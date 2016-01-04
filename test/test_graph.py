from greengraph.graph import Greengraph
from nose.tools import assert_equal
from nose.tools import assert_almost_equal
from nose.tools import assert_raises

graph = Greengraph('London', 'Chiacago')

def test_geolocate():
    start, end = (graph.geolocate(graph.start), graph.geolocate(graph.end))
    true_start = (51.507351, -0.127759)
    true_end = (41.878103, -87.629798)
    points = zip(start,true_start) + zip(end,true_end)
    for point, true_point in points:
        assert_almost_equal(point, true_point, 3)

def test_coodinates():
    with assert_raises(ValueError):
        graph.location_sequence((100.,0.),(45.,45.),20)
    with assert_raises(ValueError):
        graph.location_sequence((-100.,0.),(45.,45.),20)
