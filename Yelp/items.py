# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 23:14:30 2016

@author: Ryan
"""

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field  



class YelpItem(Item):  
    restId = Field()  
    stars = Field()  
    date = Field()  
    user = Field()
    review = Field()
    location=Field()
    useful=Field()
    photourl=Field()
    cool=Field()
    funny=Field()
    title=Field()
    feedback=Field()
    
class RestItem(Item):  
    name = Field()  
    location=Field()
    reviews=Field()
    stars=Field()
    samplereviews=Field()
    price=Field()
    test=Field()
    street=Field()
    locality=Field()
    region=Field()
    postcode=Field()
    url=Field()
    opentime=Field()
    
    
class FeedBackItem(Item):
    useful=Field()
    funny=Field()
    cool=Field()


class OpenTimeItem(Item):
    Sun=Field()
    Mon=Field()
    Tue=Field()
    Wed=Field()
    Thu=Field()
    Fri=Field()
    Sat=Field()


class UserInfor(Item):
    name=Field()
    friends=Field()
    reviews=Field()
    location=Field()
    


class UrlItem(Item):
      url=Field()
      stars=Field()
      restId=Field()
    