import Config as Conf
import Lib.Functions as Func
import pandas as pd 

BASE = Conf.base
RESPONSEXML = Conf.RESPONSEXML
MessageXML = Conf.MessageXML
URL = "/api/2.0/fo/asset/host/"
tag = Conf.TAG

timestampOut = Func.getIntervalString(Conf.TIMETOPURGE)
payload = Func.getJsonTagPayload(tag,timestampOut)
header = Func.getHeader(Conf.USERNAME,Conf.PASSWORD) 
REQUEST_URL = BASE + URL

#Getting a list of host that match the tag and interval
response = Func.postRequest(REQUEST_URL,payload,header)

if (response.ok != True):
  print("Failed to get response from API")
  exit()

with open(RESPONSEXML, "w") as f:
    f.write(response.text.encode("utf8").decode("ascii", "ignore"))
    f.close()

print("result of action can be found under the folder : " + RESPONSEXML)


HostsToPurge =Func.getAssetsToPurge(RESPONSEXML)

cols = ['ASSET_ID','ID','IP']
df = pd.DataFrame(HostsToPurge, columns=cols)
if (Conf.PURGE == True):
  id_list = df['ID'].tolist()
  idsString = Func.returnIdsAsString(id_list)
  payload = Func.getJsonPurgePayload(idsString)
  response = Func.postRequest(REQUEST_URL,payload,header)
  #Add exlode IP 10.225.100.150 
  if (response.ok != True):
    print("Failed to get response from API")
    exit()
  with open(MessageXML, "w") as f:
    f.write(response.text.encode("utf8").decode("ascii", "ignore"))
    f.close()
  text = Func.returnPurgeMessage(MessageXML)
  print(text)


