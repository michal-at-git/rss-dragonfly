#!/usr/bin/python
# coding: utf-8

import sys;
reload(sys);
sys.setdefaultencoding("utf-8");


class FeedBox(object):
  global css
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
  @staticmethod
  def start():
    return """<!doctype html>
    <head>
    <meta charset="utf-8" />
    <style>
	"""+css+"""
    </style>
    </head>
    <body>
    <header>
    <h1>Witaj w RSS Dragonfly</h1>
    </header>
    <h2>Wersja 1.1 milestone 4</h2>
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