# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:22:14 2016

@author: Ryan
"""

import json  
import codecs 
import urllib2 

import os.path
from bs4 import BeautifulSoup  

from items import UrlItem
  
 




def convertf(str):
    str=str.replace(" ","")
    str=str[5:]
    str=str[:-4]
    return str
  



def GetUrl(statr_url,location,state):           
        

         print statr_url
         page = urllib2.urlopen(statr_url) 
         contents = page.read() 
         soup = BeautifulSoup(contents)

         
         
         restaurant=soup.find_all('div',class_='search-result natural-search-result')
         
         loc_name=location+""+state
         Rname="result\urldata\%s.json" %loc_name
         
         
         item1=UrlItem()
        
         for rest in restaurant:
            
            infor=rest.find('a',class_='biz-name js-analytics-click')
            
            urlinfor=infor.get('href')
            url="http://www.yelp.com"+urlinfor
            
            
            restid=infor.find('span').get_text()
            
            if rest.find('div',class_='rating-large'):
                 stars=rest.find('div',class_='rating-large').find('i').get('title')
                 item1['stars']=stars
            
            item1['restId']=restid
            item1['url']=url
            

            file = codecs.open(Rname, mode="a", encoding='utf-8') 
            line = json.dumps(dict(item1)) + '\n'  
            file.write(line.decode("unicode_escape")) 
            
            
            
         if soup.find('a',class_='u-decoration-none next pagination-links_anchor'):
            url='http://www.yelp.com'+soup.find('a',class_='u-decoration-none next pagination-links_anchor').get('href')
            GetUrl(url,location,state)
      




def searchurl(location,state):
    print "start"
    loc_name=location+""+state
    statr_url="http://www.yelp.com/search?cflt=restaurants&find_loc="+location+"%2C+"+state
    filename='result/urldata/%s.json' %loc_name
    if  os.path.exists(filename)==True:
        print 'has exist'
        
    else:
        GetUrl(statr_url,location,state)
             
             
if __name__ == '__main__':
    searchurl()    
    exit() 


