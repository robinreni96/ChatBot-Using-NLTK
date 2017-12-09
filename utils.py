#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 21:23:29 2017

@author: robinreni
"""

import sys
import configparser
import os
import datetime
import pymysql   

class ConfigFileAccessError(Exception):
    pass

def fileexists(CONFIGFILE):
    return(os.path.isfile(CONFIGFILE) )


def get_config():
    
    CONFIGFILE = "./config/config.ini"
    
    Config = configparser.ConfigParser()
    
    config = {}   
    if fileexists(CONFIGFILE):
        Config.read(CONFIGFILE)
        for section in Config.sections():

            subdict = {}
            options = Config.options(section)
            for option in options:
                key = option
                val = Config.get(section,option)
                
                subdict[option] = Config.get(section,option)
                      
            config[section] = subdict
   
    else:
        raise ConfigFileAccessError(CONFIGFILE)

    return config

def query_yes_no(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
            
 
def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i  
                      
def db_connection(host, user, dbname, charset = "utf8mb4"):
   
   
    
    connection = pymysql.connect(host = host
                                , user = user
                                , password = 'password'
                                , db = dbname
                                , charset = charset
                                , cursorclass=pymysql.cursors.DictCursor)
    
    return connection

def db_connectionID(cursor):
    cursor.execute('SELECT connection_id()', (None))
    value = cursor.fetchone()["connection_id()"]
    return(value)

def timestamp_string():
    timestamp_string = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    return(timestamp_string)