#!/usr/bin/python
# coding: utf-8

"""
Feed
"""


__version__ =  '1.1' 


import feedparser;
import StringIO;
import img;
from Source import Source;
import time;

class Feed:  
  def __init__(self, source, origin = "web"):
    self.url = False;
    self.handle = False; 
    self.source = False;
    self.feedTitle = False;
    self.title = [];
    self.pubDate = [];
    self.description = [];
    self.content = "";
    
    
    self.source = source;
    parsedSrc = feedparser.parse(self.source);
    tLength = len(parsedSrc.entries);
    self.feedTitle = (parsedSrc.feed.title).replace("'", "&#39;");

    #here I'm trying to fix the problem with error from feedparser but...
    #with some versions it works, with another not...
    for i in range(0, tLength):
      self.title.append((parsedSrc.entries[i].title).replace("'", "&#39;"));
      try:
	self.pubDate.append(time.strftime("%d.%m.%Y %H:%M",parsedSrc.entries[i].published_parsed));
      except AttributeError:
	try:
	  self.pubDate.append(time.strftime("%d.%m.%Y %H:%M",parsedSrc.entries[i].updated_parsed));
	except AttributeError:
	  try:
	    self.pubDate.append(time.strftime("%d.%m.%Y %H:%M",parsedSrc.entries[i].created_parsed));
	  except AttributeError:
	    try:
	      self.pubDate.append(time.strftime("%d.%m.%Y %H:%M",parsedSrc.entries[i].date));	      
	    except AttributeError:
	      self.pubDate.append("unreadable date");
	  

      self.description.append((parsedSrc.entries[i].description).replace("'", "&#39;"));
      
      
      
  def toHTML(self):
    length = len(self.title);
    for i in range(0, length):
      self.content += """<article><h2>"""+self.title[i]+"""</h2>
      <div class=\"pubDate\">"""+self.pubDate[i]+"""</div>
      <div class=\"description\">"""+self.description[i]+"""</div></article>
      """;
    return self.content;