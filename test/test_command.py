from greengraph.command import parser, is_fltstring
# from nose.tools import assert_raises

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
