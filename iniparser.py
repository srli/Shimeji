# -*- coding: utf-8 -*-
"""
Created on Sat May 24 23:39:20 2014

@author: sophie
"""
import os
import configparser

#file_ini = open()

config = configparser.ConfigParser()
config.read('Shimeji1.ini')
print(config['DEFAULT']['path'])     # -> "/path/name/"
config['DEFAULT']['path'] = '/.config/screenlets/Shimeji/default'    # update
config['DEFAULT']['default_message'] = 'Hey! help me!!'   # create

with open('Shimeji1.ini', 'w') as configfile:    # save
    config.write(configfile)