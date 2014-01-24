#!/usr/bin/python
# coding: utf-8

import feedparser;
import StringIO;
import img;
from db import *;
from source import source;

class feed:
  def __init__(self, url, name = False):
    
    
    self.url = url;
    
    
    #name for add() method
    self.name = name;
    

  def generate(self):
    
    handle = source(self.url); 
    self.src = handle.getSource();
    
    try:
      if(self.src):
	parsedSrc = feedparser.parse(self.src); #IO - very experimental!!!
	self.h1 =  parsedSrc.feed.title;
	self.content = ' ';
	i = 0;
	
	tLength = len( parsedSrc.entries);
	
	for i in range(0, (tLength-1)):
	  self.content += "<article><h2>"+parsedSrc.entries[i].title+"""</h2>
	  <div class=\"pubDate\">"""+parsedSrc.entries[i].published+"""</div>
	  <div class=\"description\">"""+parsedSrc.entries[i].description+"""</div></article>
	  """;
      else:
	self.h1 = 'Nie udało się załadować kanału RSS';
	self.content = """<article><h2>Nie udało się załadować kanału RSS</h2>
	<img src=\""""+img.error+"""\" alt="error" style="border: 0px;margin: 0px;"/>
	<p style="margin-left: 70px; padding: 0px;">Nie udało się załadować kanału RSS. Prawdopodobne przyczyny:</p>
	<ul style="margin-left: 70px">
	  <li>problem z połączeniem sieciowym</li>
	  <li>niepoprawnie wpisany adres</li>
	</ul></article>""";	  
	    
	
	
    except:
      self.h1 = 'Nie udało się załadować kanału RSS';
      self.content = """<article><h2>Nie udało się odczytać kanału RSS</h2>
      <img src=\""""+img.error+"""\" alt="error" style="border: 0px;margin: 0px;"/>
      <p style="margin-left: 70px;">Nie udało się odczytać kanału RSS. Prawdopodobne przyczyny:</p>
      <ul style="margin-left: 70px;">
      	<li>pobrana treść nie jest kanałem RSS</li>
	<li>poważny błąd składniowy w skrypcie kanału RSS</li>
	<li>nieobsługiwane znaczniki</li>
      </ul></article>""";

      
  def add(self):
    from db import db;
    
    if(len(self.url) > 0 and len(self.name)>0):
      query = "insert into feedList(name, addr) values ('"+self.name+"', '"+self.url+"');";

      try:
	database = db();
	database.send(query);
	
      except:
	print "adding feed into database failed"
      
