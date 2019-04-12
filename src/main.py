#!/usr/bin/env python
# -*- coding: utf-8 -*-

import common_methods
import retweet_core
import follower_management
import config
import logging

if __name__ == '__main__':
    CONFIG = config.Config()
    
    logging.basicConfig(level = logging.getLevelName(CONFIG.general['log_level']))

    logging.debug("Bot started")

    API = retweet_core.api_login(CONFIG.twitter_keys)

    logging.debug("Logged in")

    retweet_core.retweet(API, CONFIG.query_objects)
    follower_management.manage_followers(API, CONFIG)

