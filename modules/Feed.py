#!/usr/bin/python
# coding: utf-8

import feedparser;
import StringIO;
import img;
from Source import Source;

class Feed:
  def __init__(self):
    self.url = '';
    self.src = '';

    

  def generateFromURL(self,url):
    self.url = url;
    handle = Source(self.url); 
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
      
  def generateFromSource(self, source):
    self.src = source;
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

