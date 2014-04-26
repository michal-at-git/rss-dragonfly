#!/usr/bin/python
# coding: utf-8

import feedparser;
import StringIO;
import img;
from Source import Source;

class Feed:  
  def __init__(self, source):
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
    tLength = len( parsedSrc.entries);
    self.feedTitle = (parsedSrc.feed.title).replace("'", "&#39;");
	
    for i in range(0, (tLength-1)):
      self.title.append((parsedSrc.entries[i].title).replace("'", "&#39;"));
      self.pubDate.append(parsedSrc.entries[i].published);
      self.description.append((parsedSrc.entries[i].description).replace("'", "&#39;"));
      
      
##STWORZYĆ WYJĄTKI I REAKCJE NA PODSTAWIE KODÓW Z cURL'a!!!
      
  def toHTML(self):
    length = len(self.title)-1;
    for i in range(0, length):
      self.content += """<article><h2>"""+self.title[i]+"""</h2>
      <div class=\"pubDate\">"""+self.pubDate[i]+"""</div>
      <div class=\"description\">"""+self.description[i]+"""</div></article>
      """;
    return self.content;