# Retweet Bot configuration module

import logging
import json
import os

class Config():
    """Attempts to load and set the defined configuration"""

    general = {}
    twitter_keys = {}
    follower_management = {}
    query_objects = {}

    def __init__(self):
        try:
            path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', "config", "config.json"))
            with open(path) as json_data_file:
                config_data = json.load(json_data_file)

            self.general = config_data['general']
            self.twitter_keys = config_data['twitter_keys']
            self.follower_management = config_data['follower_management']
            self.query_objects = config_data['query_objects']

        except Exception as err:
            logging.error("Failed to load config. Error: %s", err)
