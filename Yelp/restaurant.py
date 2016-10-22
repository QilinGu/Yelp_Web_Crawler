# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 22:47:44 2016

@author: Ryan
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:22:14 2016

@author: Ryan
"""

import json  
import codecs 
import urllib2 
from bs4 import BeautifulSoup  
 


from items import RestItem 
from items import OpenTimeItem



def delete(strr):
     
    strr = [item.strip('\n').strip() for item in strr if str(strr)]
    
    return strr

      
def du (strr):
    strr=strr[3:]
    strr=strr[:-2]
    return strr      


def convertf(str):
    str=str.replace(" ","")
    str=str[5:]
    str=str[:-4]
    return str
def escape(string):
    esii=string.strip()
    esii=esii.replace("\n","")
    esii=esii.replace('"', r'\"')
    esii=esii.replace("'",r"\'")
    return esii         
       
    
def restparse(url,location,state): 
         
         page = urllib2.urlopen(url) 
         contents = page.read() 
         soup = BeautifulSoup(contents)


         rawname=soup.find('div',class_='biz-page-header-left').find('h1').get_text()
         name=rawname.strip()
         name=escape(name)

         title=soup.find('div',class_='top-shelf')    
         icon=soup.find('div','island summary')
         openhour=soup.find('div',class_='ywidget biz-hours').find('table').find('tbody').find_all('tr')
         
         
         item2=RestItem()
         
         
         item3=OpenTimeItem()
         
         #soup.find("meta", {"name":"City"})
         
         print name
 
         item2['name'] = name
         
         item2['street']=title.find(attrs={"itemprop":"streetAddress"}).get_text()          
         item2['locality']=title.find(attrs={"itemprop":"addressLocality"}).get_text()
         item2['region']=title.find(attrs={"itemprop":"addressRegion"}).get_text()
         item2['postcode']=title.find(attrs={"itemprop":"postalCode"}).get_text()
   
         item2['reviews']=title.find(attrs={"itemprop":"reviewCount"}).get_text()

         item2['stars']=title.find(attrs={"itemprop":"ratingValue"}).get('content')
        
         item2['url']=url
         
         price=icon.find('dd',class_='nowrap price-description').get_text()
         #str(icon.select('.//dd[@class="nowrap price-description"]/text()').extract())
         price=price.strip().replace(" ","")

         item2['price']=price

         for hour in openhour: 
                           
                #days=str(hour.select('.//th[@scope="row"]/text()').extract())
                days=hour.find(attrs={"scope":"row"}).get_text()
         
                if hour.find('td').find('span',class_='nowrap'):
                   start=hour.find('td').find('span',class_='nowrap').get_text()
                   item3[days]=start
                else:
                   item3[days]="Close"
         item2['opentime']=dict(item3) 
      
         loc_name=location+""+state
         
         
         filename='result/restinfor/'+loc_name+'.json'
         
        
         file = codecs.open(filename, mode="a", encoding='utf-8') 
         line = json.dumps(dict(item2)) + '\n'  
         file.write(line.decode("unicode_escape")) 
          
  
                  
if __name__ == '__main__':       
    restparse()    
    exit()      

 
        
