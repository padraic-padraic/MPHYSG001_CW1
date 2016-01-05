from greengraph.command import parser, is_fltstring, do_the_thing
from mock import mock_open,patch

def test_argtypes():
    args = parser.parse_args(['--to','London','--from','10'])
    assert is_fltstring(args.end)
    args = parser.parse_args(['--to','10','--from','Chicago'])
    assert is_fltstring(args.start)

def test_save_maps():
    args = parser.parse_args(['--to','London','--from','Chicago','--save-maps'])
    assert args.save_png ==  True
    args = parser.parse_args(['--to','London','--from','Chicago'])
    assert args.save_png ==  False


@patch('greengraph.Map.count_green')
@patch('greengraph.Map.show_green', return_value='test')
@patch('requests.get')
@patch('matplotlib.image.imread')
@patch('matplotlib.pyplot.plot')
@patch('matplotlib.pyplot.show')
@patch('matplotlib.pyplot.savefig')
def test_process(mock_save, mock_show, mock_plot,mock_imread, mock_get, mock_show_green, mock_count_green):
    args = parser.parse_args(['--to','London','--from','Chicago'])
    do_the_thing(args)
    assert mock_save.called
    assert mock_show.called
    assert mock_plot.called
    # assert mock_geocode.called
    args = parser.parse_args(['--to','London','--from','Texas','--save-maps'])
    m = mock_open()
    with patch('__main__.open', m, create=True):
        do_the_thing(args)
    assert mock_show_green.called
    assert mock_count_green.called
