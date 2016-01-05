from greengraph.command import parser
from nose.tools import assert_raises

# def test_argtypes():
#     with assert_raises(TypeError):
#         args = parser.parse_args(['--to','London','--from','10'])
#     with assert_raises(TypeError):
#         args = parser.parse_args(['--to','10','--from','Chicago'])

def test_save_maps():
    args = parser.parse_args(['--to','London','--from','Chicago','--save-maps'])
    assert args.save_png ==  True
    args = parser.parse_args(['--to','London','--from','Chicago'])
    assert args.save_png ==  False
