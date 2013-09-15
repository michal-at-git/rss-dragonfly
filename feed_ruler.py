#!/usr/bin/python
#-*- coding: utf-8 -*-


#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")


from xml.dom import minidom
#from os import *
import re
import urllib
from string import lower

class feedr():
  def __init__(self):
    
    self.flist = {}
    try:
      rss = minidom.parse('feeds.xml')
      self.feeds = rss.childNodes
	
      for i in self.feeds[0].getElementsByTagName("feed"):
	self.flist[i.getElementsByTagName("name")[0].childNodes[0].toxml()] = i.getElementsByTagName("addr")[0].childNodes[0].toxml() 

      
      
    except:
      x = open("feeds.xml", "w");
      x.write(u'<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n<feedlist>\n</feedlist>');
      x.close();
    #finally:
      #x.close();
  def feed_add(self, name, addr):
    try:
      urllib.urlopen(addr)
      if re.compile("^[0-9a-ząćęłŁśźż\- ]+[0-9a-ząćęłśźż\- ]$").match(lower(name)):
	update = self.feeds[0].toxml("utf-8");
	update = """<?xml version=\"1.0\" encoding=\"UTF-8\"?>
	"""+update[0:len(update)-11]+"""    <feed>
      <addr>"""+addr+"""</addr>
      <name>"""+name+"""</name>
    </feed>
  </feedlist>""";
	feedlistfile = open('feeds.xml', 'w')
	feedlistfile.write(update);
	feedlistfile.close()
	#name+".xml"
    except: None
      
  def feed_rm(self,name):
    x = open("feeds.xml", "r")
    txt = x.read();
    print "RMRMR>",name #DEBUG
    rm = """    <feed>
      <addr>"""+self.flist[u""+str(name).encode('Utf-8')]+"""</addr>
      <name>"""+name+"""</name>
    </feed>"""
    print rm #DEBUG
    txt = txt.replace(rm, "");
    print "\n********\n",txt #DEBUG

    x.close();
    x = open("feeds.xml", "w")
    x.write(txt);
    x.close();
  def feed_is(self): 
    # może kiedyś to się przyda? ;)
    self.li = []
    for i in listdir("feeds/"):
	  
	  if (re.compile(u"\w+.xml$").match(i)): self.li.append(i)
	
