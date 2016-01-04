from datetime import datetime
from greengraph import Greengraph, Map
from matplotlib import pyplot as plt

import argparse

def default_filename():
    return datetime.now().strftime('%H%M%S-%d%m%Y')

parser = argparse.ArgumentParser(description='A tool for calculating the amount of green between two places.')
parser.add_argument("-t", "--to", help="Starting location", required=True, 
                    dest='start', type=str)
parser.add_argument("-f", "--from", help="Ending location", required=True,
                    dest='end', type=str)
parser.add_argument("-o", "--out", help="Output filename", type=str, 
                    dest='fname', default=default_filename())
parser.add_argument("--save-maps", dest='save_png',
                    help="Save the amount of green at each step",
                    action='store_true')
parser.add_argument("-s", "--steps", dest='steps', help="Number of steps", type=int, 
                    default=20)

def process():
    args = parser.parse_args()
    graph = Greengraph(args.start, args.end)
    if args.save_png:
        points = graph.location_sequence(graph.geolocate(graph.start),
                                         graph.geolocate(graph.end),
                                         args.steps)
        green = []
        for n, point in enumerate(points):
            _m = Map(*point)
            green.append(_m.count_green())
            with open(args.fname+'_'+str(n)+'.png','w') as f:
                f.write(_m.show_green(green[n]))
    else:
        green = graph.green_between(args.steps)
    plt.plot(graph.green_between(args.steps))
    plt.show()
    plt.savefig(args.fname+'.png')