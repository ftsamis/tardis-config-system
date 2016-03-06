#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Fotis Tsamis <ftsamis@gmail.com>
# This is a snippet for the first objective of the "config system" GSoC16 idea.

import re
import yaml

from astropy import units


def quantity_constructor(loader, node):
    '''A constructor for converting a value and a unit to
    an astropy.units.Quantity object.
    '''
    data = loader.construct_scalar(node)
    value_str, unit_str = data.split(None, 1)
    return float(value_str) * units.Unit(unit_str)

# Register the custom constructor to yaml
yaml.add_constructor('!quantity', quantity_constructor)

# This pattern matches a number (scientific notation supported) followed by
# one or more whitespace characters, followed by one or more characters, 
# including whitespace, which would be the unit.
pattern = re.compile(r'^-?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?\s+.+$')
yaml.add_implicit_resolver('!quantity', pattern)

def parse_test():
    print yaml.load("velocity: 15.03e-2 km/s")

if __name__ == '__main__':
    parse_test()
