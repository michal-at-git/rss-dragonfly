#!/usr/bin/python
# coding: utf-8

import pycurl;
import cStringIO;
from DB import DB;

class Source:
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
      handle.setopt(handle.USERAGENT, "Mozilla/5.0 (compatible; Python; RSS Dragonfly) RSS_Dragonfly/1.1_pre-alpha");
      handle.perform();
      
      self.source = buff.getvalue();
      buff.close();
    except:
      self.source = False;
      
    return self.source;
  #v 1.2  
  #def fromFile(self, fname):
    #0;

