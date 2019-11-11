# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:49:22 2019

@author: LOPEZPED
"""
from datetime import date
import datetime
import pandas as pd
import os
#import plotly.plotly as py
#import plotly.graph_objs as go

os.chdir(r"C:\Users\Lopezped\Desktop")

df= pd.read_csv('legislators.csv')
df["birthdate"]=pd.to_datetime(df["birthdate"])

year =date.today() - datetime.timedelta(days = 45*365)

dems = df.query("party == 'D'")
dems = dems[df.birthdate>year] 

repub = df.query("party=='R'")
repub = repub[repub.youtube_url.notnull()]
repub = repub [repub.twitter_id.notnull()] 


writer = pd.ExcelWriter("DataMade.xlsx",
                        engine="xlsxwriter")
#
df.to_excel(writer, "Original Data")
dems.to_excel(writer, "Democrats over 45")
repub.to_excel(writer, "Republicans with Social Media")

writer.save()