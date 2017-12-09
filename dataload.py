#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:56:18 2017

@author: robinreni
"""

import pandas as pd

blogdata= pd.read_csv("techcrunch.csv")
global column
column=[]
column=blogdata.columns.tolist()

global wholelist
wholelist={}
for i in column:
    wholelist[i]=blogdata[i].values.tolist()
global catt
catt=[]

global content
content=[]



def checkcontent(con):
    name=[]
    l=[]
    for i in con:
        for j in column:
            l=wholelist[j]
            for k in range(len(l)):
                string=str(l[k])
                name=string.strip().split()
                if i in name:
                    print("BOT>> ",blogdata.loc[k,catt[0]])
            return("BOT>> Content Displayed")
    else:
        return("Sorry The Required Content is not avilable")




def result(content_list):
    if content_list[0]=='show':
       content_list.remove('show')
    elif content_list[0]=='Show':
       content_list.remove('Show')
    for i in content_list:
        if i in column:
            catt.append(i)
            content_list.remove(i)
    result=checkcontent(content_list)
    return(result)
    