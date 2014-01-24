#!/usr/bin/python
# coding: utf-8


"""
Main class of RSS Dragonfly
"""

__version__ =  '1.1 - milestone 1'

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
reload(sys)
sys.setdefaultencoding("utf-8");


sys.path.append('GUI/');
from window import *;
from addFeedDialog import *;

sys.path.append('modules/');
from feed_ruler import *
import feedBox;
from feed import feed;

import pop_ups
from string import lower
import urllib
from os import remove

    
class rss_dragonfly(window):
  def __init__(self, parent=None):
    super(rss_dragonfly, self).__init__(parent);
    self.drawWindow();
    
    self.addFeedPopup = addFeedDialog();


    
    self.connect(self.goButton, SIGNAL("clicked()"), self.readFeed);
    #	self.connect(self.fromFileButton, SIGNAL("clicked()"), self.fromFile)
    self.connect(self.closeButton, SIGNAL("clicked()"), self.quit)
    #	self.feedList.itemActivated.connect(self.readExistFeed)
    
    self.connect(self.addNewFeedButton, SIGNAL("clicked()"), self.addFeedPopup.exec_)
    #	self.connect(self.reloadFeedsButton, SIGNAL("clicked()"), self.updateFeeds)
    #	self.connect(self.rmFeedButton, SIGNAL("clicked()"), self.rmFeed)

    
    #popUp
    
    #popUp signals:
    self.connect(self.addFeedPopup.send, SIGNAL("clicked()"), self.addFeed);

    
    
    
  def readFeed(self):
    if len(self.addressInput.text()) > 1:
      feedsrc = feed(self.addressInput.text());
      feedsrc.generate();
      self.rssContentView.setHtml(unicode(feedBox.feedBox.showFeeds(feedsrc.h1, feedsrc.content)));
      self.updateTitle(feedsrc.h1);
      
      
  def addFeed(self):
    newFeed = feed(str(self.addFeedPopup.address.text()), str(self.addFeedPopup.name.text()));
    newFeed.add();
    self.addFeedPopup.close();
    
  def quit(self):
    rsssq.quit();
    

    

  
    
    
rsssq = QApplication(sys.argv)
rss_sq = rss_dragonfly() 
rss_sq.show()
rsssq.exec_()