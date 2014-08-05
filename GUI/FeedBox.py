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
  global standard
  global lemon
  global violet
  global summer
  global monochromatic  
  global startCSS
  global theme
  theme = "0xfff"

  
  standard = """
  
  body, html { 
      color: #444;
      background-color: #fff;
      }
  
  header {
      background: #dfe9df;
      color: #005550;
      box-shadow: 0px 0px 9px #cdc;
      border-bottom: solid #ddd 1px;
  }
  h2 {
        color: #444;
    }
    
  img {
        border: double #005550 3px;

      }
  .pubDate {
    background: #dfe9df;
    color: #444;
    }
    
  """
  
  

  
  
  lemon = """
  
  body, html { 
      color: #363a74;
      background-color: #fff;
      }
  
  header {
      background: #f8f4dd;
      color: #00264c;
      box-shadow: 0px 0px 9px #dcc;
      border-bottom: solid #ddd 1px;
  }
  h2 {
      color: #363a74;
    }
    
  img {
      border: double #00264c 3px;

      }
  .pubDate {
      background: #f8f4dd;
      color: #363a74;

    }
    
  """
   
  violet = """
  
  body, html { 
      color: #363a74;
      background-color: #fff;
      }
  
  header {
      background: #520153;
      color: #fff;
      box-shadow: 0px 0px 9px #f08888;
      border-bottom: solid #ddd 1px;
  }
  h2 {
      color: #363a74;
    }
    
  img {
      border: double #00264c 3px;

      }
  .pubDate {
      background: #520153;
      color: #fff;
    }
    
  """
  summer = """
  
  body, html { 
      color: #363a74;
      background-color: #fff;
      }
  
  header {
      background: #4adbff;
      color: #fff;
      box-shadow: 0px 0px 9px #a2ff71;
      border-bottom: solid #ddd 1px;
  }
  h2 {
      color: #363a74;
    }
    
  img {
      border: double #00264c 3px;

      }
  .pubDate {
      background: #ffab71;
      color: #fff;
    }
    
  """
  
  monochromatic = """
  
  body, html { 
      color: #333;
      background-color: #fff;
      }
  
  header {
      background: #bbb;
      color: #333;
      box-shadow: 0px 0px 9px #777;
      border-bottom: solid #555 1px;
  }
  h2 {
      color: #333;
    }
    
  img {
      border: double #00264c 3px;

      }
  .pubDate {
      background: #ddd;
      color: #444;
    }
    
  """
  
  css = """
      body, html {margin: 0px;
      padding: 0px;
      font-size: 100%;
      font-family: sans-serif;
     }
      header {margin: 0px;
      display: table;
      padding: 0px;
      width: 100%;
      }
     
      h1 {margin-top: 20px;
      margin-bottom: 20px;
      margin-left: 20px;
      font-size: 200%;}
      
      h2 { font-size: 140%;
      margin: 0px;
      }
      img {max-width: 200px;
      float: left;
      margin: 10px;}
      
      article {width: 90%;
      margin: auto;
      margin-top: 5%;
      margin-bottom: 10%;
      display: table}
      
      .pubDate {display: table; 
      margin: 0px;
      font-style: italic;
      width: 100%;
      margin: auto;
      padding: 4px;
      }
      iframe {display: none}
    """;
    
    
  startCSS = """
       body, html {margin: 0px;
      padding: 0px;
      font-size: 100%;
      font-family: sans-serif;
      color: #fff;
      background-color: #0f7670;
      text-align: center;
      }
  
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
  def setTheme(themeID):
    themes = [standard, lemon, violet, summer, monochromatic];
    theme = themes[themeID]
    global css
    css = css +"""
    """+ theme
    
  @staticmethod
  def start():
    return """<!doctype html>
    <html>
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
    <h2>Version 1.2 beta</h2>
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
	<h1>Unable to load RSS feed</h1>
	</header>
	<article>
	<img src="""+img.error+""" alt="error" style="border: 0px;margin: 0px;"/>
	<p style="margin-left: 70px; padding: 0px;">Possible reasons:</p>
	<ul style="margin-left: 70px">
	<li>internet connection problem</li>
	<li>incorrectly typed web address</li>
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
	<h1>Unable to open RSS feed</h1>
	</header>
	<article>
	<img src="""+img.error+""" alt="error" style="border: 0px;margin: 0px;"/>
	<p style="margin-left: 70px; padding: 0px;">Possible reasons:</p>
	<ul style="margin-left: 70px">
	<li>downloaded content could not be RSS feed</li>
	<li>critical syntax error in RSS source</li>
	<li>unsupported tags</li>
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
	<h1>Unable to update RSS subscriptions</h1>
	</header>
	<article>
	<img src="""+img.error+""" alt="error" style="border: 0px;margin: 0px;"/>
	<p style="margin-left: 70px; padding: 0px;">Possible reasons:</p>
	<ul style="margin-left: 70px">
	<li>internet connection problem</li>
	<li>critical syntax error in RSS source</li>
	</ul></article>""";	
	  