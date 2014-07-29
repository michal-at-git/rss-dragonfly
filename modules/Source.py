#!/usr/bin/python
# coding: utf-8

import pycurl;
import cStringIO;
from DB import DB;
from System import System;

class Source:
  
  def __init__(self):
    self.system = System("UNIX");
    source = False;
    
  def fromURL(self, url):
    try:
      self.url = url;
      handle = pycurl.Curl();
      buff = cStringIO.StringIO();
      
      handle.setopt(handle.URL, str(self.url));
      handle.setopt(handle.WRITEFUNCTION, buff.write);
      handle.setopt(handle.CONNECTTIMEOUT, 7);    
      handle.setopt(handle.TIMEOUT, 12);
      handle.setopt(handle.USERAGENT, self.system.useragent);
      handle.perform();
      
      self.source = buff.getvalue();
      buff.close();
    except:
      self.source = False;
    return self.source;

  def fromFile(self, path):
    rssFile = open(path, 'r');
    self.source = rssFile.read();    
    rssFile.close();
    return self.source;
    

