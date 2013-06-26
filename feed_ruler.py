#!/usr/bin/python
#-*- coding: utf-8 -*-



from xml.dom import minidom


class feedr():
  def __init__(self):
    
    self.flist = {}
    try:
      rss = minidom.parse('feeds.xml')
      feeds = rss.childNodes
	
      for i in feeds[0].getElementsByTagName("feed"):
	self.flist[i.getElementsByTagName("name")[0].childNodes[0].toxml()] = i.getElementsByTagName("addr")[0].childNodes[0].toxml() 

      
      
    except:
      x = open("feeds.xml", "w");
      x.write('<?xml version=\"1.0\"?>\n<feedlist>\n</feedlist>');
      x.close();
    #finally:
      #x.close();
      
   

#class feed_list(feedr):
  #def __init__(self):
    #print feedr().flist
    
  #def insert(self):
    #0
  #def delete(self):
    #0
    
    
