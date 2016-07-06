#! /usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url='http://www.hscode.net/Home/OrderTrackData'
trackid=input('Enter trackid:')
if len(trackid)<1:  trackid='WSEA015203646'

payload={'txtOrderNo':trackid}

r=requests.post(url,data=payload)

print ('\n','\tRetrieve track log for:',trackid)
print ('\tRetrieve status:',r.status_code)

soup= BeautifulSoup(r.text,"html.parser")
if soup.find('li',class_='finished')!=None:
    print ('\tCurrent state:',soup.find('li',class_='finished').find(class_='info').string.strip())
else:
    ali=soup.find('li',class_='passed active')
    print ('\tCurrent state:',ali.find(class_='info').string.strip())
    print ('\tTime:',ali.find(class_='day').string.strip(),ali.find(class_='time').string.strip())



#litags=soup.find_all('li')
#for litag in litags:
#    print (litag['class'],888888888888888)
#    print (type(litag['class']),9999999999)
#    if len(litag['class'])>1: status=litag['class'][0]+' '+litag['class'][1]
#    else: status=litag['class'][0]
#    print (status+':',str(litag.contents[5].contents[0]).strip())
#new_file=open(trackid+'.html','w')
#new_file.write(r.text)
#new_file.close()
