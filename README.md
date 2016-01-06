# Greengraph Package: Assessment for PHYSGQ01 [![Build Status](https://travis-ci.org/padraic-padraic/MPHYSG001_CW1.svg?branch=master)](https://travis-ci.org/padraic-padraic/MPHYSG001_CW1)

Greengraph is a package that allows you to calculate the amount of green space between two places. 

This package provides two classes

1. `greengraph.Map`
    This package takes a latitute/longitude pair, fetches a google map for the area and calculate the number of green pixels present.
2. `greengraph.Greengraph`
   This package takes a pair of start and end locations, in plain text or coordinates, and uses the Map class to calculate the amount of green at each step between the two points.

The package also provides a command line interface, `greengraph`, installed alongside the module by `python setup.py install`.

```
usage: greengraph [-h] -t START -f END [-o FNAME] [--save-maps] [-s STEPS]

A tool for calculating the amount of green between two places.

optional arguments:
  -h, --help            show this help message and exit
  -t START, --to START  Starting location
  -f END, --from END    Ending location
  -o FNAME, --out FNAME
                        Output filename
  --save-maps           Save the amount of green at each step
  -s STEPS, --steps STEPS
                        Number of steps
```
