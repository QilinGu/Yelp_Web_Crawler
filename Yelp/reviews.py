# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 23:41:33 2016

@author: Ryan
"""


import json  
import codecs 
import urllib2
 

from bs4 import BeautifulSoup  

import unicodedata
import HTMLParser  



from items import YelpItem 
from items import FeedBackItem
from items import UserInfor


htmlparser = HTMLParser.HTMLParser()



def is_ascii(s):
	return all(ord(c) < 128 for c in s) 
 
 
def clean_parsed_string(string):
	if len(string) > 0:
		ascii_string = string
		if is_ascii(ascii_string) == False:
			ascii_string = unicodedata.normalize('NFKD', ascii_string).encode('ascii', 'ignore')
		return ascii_string
	else:
		return None
    
def get_parsed_string(tag):
    
    return_string = ''
    raw_string=''
    extracted_list=tag.find('div','review-content').p.get_text()

    if len(extracted_list) > 0:
        for strr in extracted_list:
            raw_string = raw_string+strr.strip()
        if raw_string is not None:
            return_string = htmlparser.unescape(raw_string)
    return return_string

      
def delete(strr):
     
    strr = [item.strip('\n').strip() for item in strr if str(strr)]
    
    return strr

      
def du (strr):
    strr=strr[3:]
    strr=strr[:-2]
    return strr 
     
def escape(string):
    esii=string.strip()
    esii=esii.replace("\n","")
    esii=esii.replace('"', r'\"')
    esii=esii.replace("'",r"\'")
    #esii=esii.encode('ascii','ignore')
    return esii         


def convertf(str):
    str=str.replace(" ","")
    str=str[5:]
    str=str[:-4]
    return str
 
Rname="aaa.json"

def parse(url,start,end,location,state):  
       
       page = urllib2.urlopen(url) 
       contents = page.read() 
       soup = BeautifulSoup(contents)
       
       

       rawname=soup.find('div',class_='biz-page-header-left').find('h1').get_text()

       restname=rawname.strip()
       restname=escape(restname)
       

       

       
       for tag in soup.find_all('div', class_='review review--with-sidebar')[1:]: 
               item=YelpItem()
               item3=UserInfor()
               item2=FeedBackItem()
               
               
               
               date=tag.find(attrs={"itemprop":"datePublished"}).get("content")
               time=int(date.split("-")[0])
             
               if (time<start or time>end):
                   continue
                   
               
               
               
               item['date'] =date
               
               
               
               
               
               
               item['stars']=tag.find(attrs={"itemprop":"ratingValue"}).get("content")
               
               review=[]
               review.append(escape(tag.find('div','review-content').find(attrs={"itemprop":"description"}).get_text()))
               item['review']=review
               
               

                            
               item2['useful']=tag.find('a',class_='ybtn ybtn--small useful js-analytics-click').find('span',class_='count').get_text() 
               item2['funny']=tag.find('a',class_='ybtn ybtn--small funny js-analytics-click').find('span',class_='count').get_text()
               item2['cool']=tag.find('a',class_='ybtn ybtn--small cool js-analytics-click').find('span',class_='count').get_text()
               item['feedback']=dict(item2)
               
                            
               item3['name']=tag.find('li',class_='user-name').a.get_text()
               item3['friends']=tag.find('li',class_='friend-count responsive-small-display-inline-block').b.get_text()
               item3['reviews']=tag.find('li',class_='review-count responsive-small-display-inline-block').b.get_text()
               item3['location']=tag.find('li',class_='user-location responsive-hidden-small').b.get_text()
               item['user']= dict(item3)
             
               loc_name=location+""+state
               
               
               filename='result/reviewinfor/'+loc_name+'/'+restname+'.json'
               
            
               
         
               file = codecs.open(filename, mode="a", encoding='utf-8')             
               line = json.dumps(dict(item)) + '\n'  
               file.write(line.decode("unicode_escape"))

       if soup.find(attrs={"rel":"next"}):
           url= soup.find(attrs={"rel":"next"}).get('href') 
           parse(url,start,end,location,state)



                
if __name__ == '__main__':       
    parse()    
    exit()
     

