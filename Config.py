
import pandas as pd 
import Lib.Functions as Func
import os

df = pd.read_xml('config.xml')
configList = df.iloc[0].to_list()

USERNAME = configList[1]
PASSWORD = configList[2]
TAG = configList[3]
TIMETOPURGE = configList[4]
PURGE = configList[5]
##Start Detection
base = configList[0]
###Change the environment POD

RESPONSEXML = os.path.join("Requests","Response.xml")
MessageXML = os.path.join("Requests","Message.xml")
