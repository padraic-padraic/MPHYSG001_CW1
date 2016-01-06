from greengraph.command import parser, do_the_thing, process
from mock import mock_open, patch

def test_save_maps():
    args = parser.parse_args(['--to','London','--from','Chicago','--save-maps'])
    assert args.save_png ==  True
    args = parser.parse_args(['--to','London','--from','Chicago'])
    assert args.save_png ==  False

def test_filename():
    args = parser.parse_args(['--to','London','--from','Chicago','--save-maps','-o','thefile'])
    assert args.filename == 'thefile'

m = mock_open()

@patch('matplotlib.pyplot.show')
@patch('matplotlib.pyplot.savefig')
@patch('matplotlib.pyplot.plot')
@patch('greengraph.Greengraph.green_between')
def test_do_the_thing(mock_green_between,mock_plot, mock_savefig,mock_show):
    args = parser.parse_args(['--to','London','--from','Chicago','--steps','1'])
    do_the_thing(args)
    mock_green_between.assert_called_with(1)

@patch('matplotlib.pyplot.show')
@patch('matplotlib.pyplot.savefig')
@patch('matplotlib.pyplot.plot')
@patch('greengraph.Map.show_green',return_value='Test')
@patch('greengraph.Map.count_green')
@patch('matplotlib.image.imread')
@patch('requests.get')
@patch('greengraph.Greengraph.location_sequence',return_value=[(10.,10.),(11.,11.)])
@patch('greengraph.Greengraph.geolocate', return_value=(10.,10))
def test_do_the_thing_with_save(mock_geolocate,mock_location_sequence, mock_get,mock_imread,mock_count_green,mock_show_green,mock_plot, mock_savefig,mock_show):
    args = parser.parse_args(['--to','London','--from','Chicago','--save-maps','--steps','1'])
    with patch('__builtin__.open',m,create=True):
        do_the_thing(args)
    assert m.called == True
    mock_location_sequence.assert_called_with((10.,10.),(10.,10.),1)
    assert mock_count_green.called == True
    assert mock_show_green.called == True

@patch('greengraph.command.do_the_thing')
@patch('greengraph.command.parser.parse_args',return_value='test')
def test_process(mock_parse, mock_thing):
    process()
    assert mock_parse.called == True
    mock_thing.assert_called_with('test')
