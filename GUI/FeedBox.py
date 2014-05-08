#!/usr/bin/python
# coding: utf-8

"""
FeedBox 
"""


__version__ =  '1.1' 
import sys;
reload(sys);
sys.setdefaultencoding("utf-8");

import img;
import logo;

class FeedBox(object):
  global css
  global startCSS
  css = """
      body, html {margin: 0px;
      padding: 0px;
      font-size: 100%;
      font-family: sans-serif;
      color: #444;
      background-color: #fff;}
      header {margin: 0px;
      display: table;
      padding: 0px;
      background: #dfe9df;
      color: #005550;
      width: 100%;
      box-shadow: 0px 0px 9px #cdc;
      border-bottom: solid #ddd 1px;
      }
      h1 {margin-top: 20px;
      margin-bottom: 20px;
      margin-left: 20px;
      font-size: 200%;}
      
      h2 { font-size: 140%;
      color: #444;
      margin: 0px;
      }
      img {max-width: 200px;
      border: double #005550 3px;
      float: left;
      margin: 10px;}
      
      article {width: 90%;
      margin: auto;
      margin-top: 5%;
      margin-bottom: 10%;}
      .pubDate {display: table; 
      margin: 0px;
      font-style: italic;
      background: #dfe9df;
      width: 100%;
      margin: auto;
      padding: 4px;
      }
    """;
  startCSS = """
       body, html {margin: 0px;
      padding: 0px;
      font-size: 100%;
      font-family: sans-serif;
      color: #fff;
      background-color: #0f7670;
      text-align: center;}
      
      
      header {margin: 0px;
      display: table;
      padding: 0px;
      background-color:#dfe9df;
      width: 100%;
      height: 260px;
        color: #005550;
	text-shadow: 2px 2px 0px #fff;
      }
      h1 {margin-top: 20px;
      margin-bottom: 20px;
      margin-left: 20px;
      font-size: 200%;}
      
      h2 { font-size: 140%;
      margin: 0px;
      margin-top: 7%;
      }
      
      img {margin-top: 100px;}
    
  """;
  @staticmethod
  def start():
    return """<!doctype html>
    <head>
    <meta charset="utf-8" />
    <style>
	"""+startCSS+"""
    </style>
    </head>
    <body>
    <header>
    <img src=\""""+logo.icon+"""\" alt="logo"/>
    <h1>RSS Dragonfly</h1>
    </header>
    <h2>Wersja 1.1</h2>
    </body>
    </html>
    """
  @staticmethod
  def showFeeds(h1, content):
    return """<!doctype html>
    <head>
    <meta charset="utf-8"/>
    <title> </title>
    <style>"""+css+"""</style>
    </head>
    <body>
    <header>
    <h1>"""+h1+"""</h1>
    </header>
    <article>
    """+content+"""
    </article>
    </body>
    </html> 
    """
  @staticmethod
  def downloadError():
    return """<!doctype html>
	<head>
	<meta charset="utf-8"/>
	<title> </title>
	<style>"""+css+"""</style>
	</head>
	<header>
	<h1>Nie udało się załadować kanału RSS</h1>
	</header>
	<article>
	<img src="""+img.error+""" alt="error" style="border: 0px;margin: 0px;"/>
	<p style="margin-left: 70px; padding: 0px;">Prawdopodobne przyczyny:</p>
	<ul style="margin-left: 70px">
	<li>problem z połączeniem sieciowym</li>
	<li>niepoprawnie wpisany adres</li>
	</ul></article>""";
  @staticmethod
  def parseError():
    return """<!doctype html>
	<head>
	<meta charset="utf-8"/>
	<title> </title>
	<style>"""+css+"""</style>
	</head>
	<header>
	<h1>Nie udało się odczytać kanału RSS</h1>
	</header>
	<article>
	<img src="""+img.error+""" alt="error" style="border: 0px;margin: 0px;"/>
	<p style="margin-left: 70px; padding: 0px;">Prawdopodobne przyczyny:</p>
	<ul style="margin-left: 70px">
	<li>pobrana treść nie jest kanałem RSS</li>
	<li>poważny błąd składniowy w skrypcie kanału RSS</li>
	<li>nieobsługiwane znaczniki</li>
	</ul></article>""";
  @staticmethod
  def updateError():
    return """<!doctype html>
	<head>
	<meta charset="utf-8"/>
	<title> </title>
	<style>"""+css+"""</style>
	</head>
	<header>
	<h1>Nie udało się zaktualizować subskrypcji RSS</h1>
	</header>
	<article>
	<img src="""+img.error+""" alt="error" style="border: 0px;margin: 0px;"/>
	<p style="margin-left: 70px; padding: 0px;">Prawdopodobne przyczyny:</p>
	<ul style="margin-left: 70px">
	<li>problem z połączeniem sieciowym</li>
	<li>poważny błąd składniowy w skrypcie kanału RSS</li>
	</ul></article>""";	