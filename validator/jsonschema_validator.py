#!/usr/bin/python
#-*- coding: utf-8 -*-

import yaml
import jsonschema

schema = """
type: object
properties:
  tardis_config_version:
    type: string
    description: Version of the configuration file
required:
    - tardis_config_version
"""

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
            jsonschema.validate(yaml.load(conf), yaml.load(schema))
            print "Pass"
        except Exception as e:
            print "Fail (%s)" % str(e)


validate_confs()
