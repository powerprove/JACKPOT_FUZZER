'''
    conf.py
    
'''

import ConfigParser
import optparse
import os
import sys

VERSION = "TEST - 0.1v"

default_config = "./.Jackrc"

pluginFileName = "/plugins"
commandFileName = "/commands"

class ConfClass(object):

    optparser = optparse.OptionParser(add_help_option = False, version = False)

    initialised = False

    def __init__(self):
        if not ConfClass.initialised:
            self.optparser.add_option("-h", "--help", action = "store_true", default = False, 
                    help = "list all available options and their default values. Default values may be set in the configuration file (" + default_config + ")")

            ConfClass.initialised = True

    def set_usage(self, usage = None, version = None):
        if usage:
            self.optparser.set_usage(usage)

        if version:
            self.optparser.version = version


config = ConfClass()
