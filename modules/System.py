#!/usr/bin/python
# coding: utf-8

class System():
  def __init__(self, platform=False):
    if(platform == "UNIX"):
      self.unix();
    elif (platform == "NT"):
      self.nt();
    else:
      self.legacy();

  def unix(self):
    import os;
    osId = os.uname();
    osIdLen = len(osId);
    self.useragent = "Mozilla/5.0 ("+osId[0]+" "+osId[osIdLen-1]+") RSS_Dragonfly/1.2-";
    self.confPath = "~/.rss-dragonfly";
    print self.useragent;
    
    return 0;
    
    
  def nt(self):
    import sys;
    self.useragent = "Mozilla/5.0 ("+str(sys.platform)+") RSS_Dragonfly/1.2";
    print self.useragent;
    return 0;
  
  def legacy(self):
    self.useragent = "Mozilla/5.0 (other) RSS_Dragonfly/1.2";    
    return 0;