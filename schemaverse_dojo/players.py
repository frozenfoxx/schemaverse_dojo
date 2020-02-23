""" Player loading and handling """

import configparser
import sys

class Players(object):
    """ Player-handling Object """

    def __init__(self, playersconf_location, environment):
        self.playersconf_location = playersconf_location
        self.environment = environment
        self.players = {}

    def load_players(self):
        """ Load players """

        playersconf = configparser.ConfigParser()

        print("[+] Reading players configuration file")
        try:
            playersconf.read(self.playersconf_location)
        except Exception as e:
            sys.exit("Unable to read playersconf file, does it exist?")

        print("[+] Loading players")
        try:
            for key in playersconf[environment]:
                self.players[key] = playersconf[environment][key]
        except Exception as e:
            sys.exit("Unable to read config file, does it exist?")

        return self.players
