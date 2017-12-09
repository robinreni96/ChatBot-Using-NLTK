#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 21:41:44 2017

@author: robinreni
"""



import warnings
warnings.filterwarnings("ignore")  

import utils 

conf = utils.get_config()

DBHOST = conf["MySQL"]["server"] 
DBUSER = conf["MySQL"]["dbuser"]
DBNAME = conf["MySQL"]["dbname"]
DBCHARSET = conf["MySQL"]["dbcharset"]

def try_drop(cursor,table_name):
    SQL = 'DROP TABLE IF EXISTS ' + table_name
    print(SQL)
    cursor.execute(SQL)

print("Configuring Tables for database configuration: \n \tServer: {0} \n \tDB-User: {1} \n \tDB-Name: {2}".format(DBHOST,DBUSER, DBNAME))
print("\n** ALL EXISTING TABLES AND DATA WILL BE LOST **\n")

response = utils.query_yes_no("Continue?")

if response:
    
    
    charTypeShort = "VARCHAR(16) COLLATE utf8_general_ci"
    charTypeMedium = "VARCHAR(64) COLLATE utf8_general_ci"
    charTypeLong = "VARCHAR(768) COLLATE utf8_general_ci"
    
    print("Connecting to database...", end=" ")
    connection = utils.db_connection(DBHOST, DBUSER, DBNAME, DBCHARSET)
    cursor = connection.cursor()
    print("connected.")
    

    

        
    print("\nCreating sentences table:")
    try:
        try_drop(cursor, "sentences")
        SQL = 'CREATE TABLE sentences (hashid ' + charTypeShort + ' , sentence ' + charTypeLong + ' , result '+ charTypeLong +' ) '    
        print(SQL)
        cursor.execute(SQL)
    except Exception as e:
        print("\n** ERROR **", e)
        

        
   
        
    print("\nDone.")   
    
else:
    exit(0)