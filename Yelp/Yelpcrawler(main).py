# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 23:31:25 2016

@author: Ryan
"""

import reviews
import restaurant
import geturl
import json
import os.path



def crawlreviews(location,state,starttime, endtime):
        urlset=[]
        data = []
        loc_name=location+""+state
        filename='result/urldata/%s.json' %loc_name
        
        outputfile='result/reviewinfor/%s' %loc_name
        
        
        if not os.path.exists(outputfile):
            os.makedirs(outputfile)

        with open(filename) as f:
            for line in f:
                data.append(json.loads(line))
        
        
        for i in range(len(data)):
            urlset.append(data[i]["url"])
            
    
        for url in urlset:
            print url
            reviews.parse(url,starttime,endtime,location,state)




def crawlrest(location,state):
        urlset=[]
        data = []
        
        loc_name=location+""+state
        filename='result/urldata/%s.json' %loc_name
        
        with open(filename) as f:
            for line in f:
                data.append(json.loads(line))
        
        
        for i in range(len(data)):
            urlset.append(data[i]["url"])
            
    
        for url in urlset:
            restaurant.restparse(url,location,state)


#get the url from the specific city
geturl.searchurl('charlottesville','VA')



# parameter: location ,startime, endtime. 	You can search all reviews on all restaurants in that specific city
crawlreviews('charlottesville','VA',2014,2017) 


#paramter location. You can get all the restaurants information in that specific city
crawlrest('charlottesville','VA')