from greengraph.command import parser, do_the_thing

def test_save_maps():
    args = parser.parse_args(['--to','London','--from','Chicago','--save-maps'])
    assert args.save_png ==  True
    args = parser.parse_args(['--to','London','--from','Chicago'])
    assert args.save_png ==  False

def test_filename():
    args = parser.parse_args(['--to','London','--from','Chicago','--save-maps','-o','thefile'])
    assert args.filename == 'thefile'
