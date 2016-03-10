#!/usr/bin/python
#-*- coding: utf-8 -*-

import yaml
from voluptuous import Schema, Required

schema = Schema({
    Required('tardis_config_version'): str # Notice how easily we can put astropy.Quantity here!
})

# Correct config
conf1 = """
tardis_config_version: v1.0
"""

# Wrong type
conf2 = """
tardis_config_version: 1.0
"""

# Required constraint not met
conf3 = """
foo: bar
"""

confs = [conf1, conf2, conf3]

def validate_confs():
    for conf in confs:
        try:
            schema(yaml.load(conf))
            print "Pass"
        except Exception as e:
            print "Fail (%s)" % str(e)


validate_confs()
