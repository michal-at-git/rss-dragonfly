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
from Window import *;
from AddFeedDialog import *;

sys.path.append('modules/');
import FeedBox;
from Feed import Feed;
from FeedList import FeedList;
from DB import DB;

import pop_ups
from string import lower
import urllib
from os import remove



    
class rss_dragonfly(Window):
  def __init__(self, parent=None):
    super(rss_dragonfly, self).__init__(parent);
    self.drawWindow();
    
    self.dbHandle = DB();
    
    self.feedList = FeedList(self.feedListWidget, self.dbHandle);
    self.addFeedPopup = AddFeedDialog();
    


    
    self.connect(self.goButton, SIGNAL("clicked()"), self.readFeed);
    #	self.connect(self.fromFileButton, SIGNAL("clicked()"), self.fromFile)
    self.connect(self.closeButton, SIGNAL("clicked()"), self.quit)
    #	self.feedList.itemActivated.connect(self.readExistFeed)
    
    self.connect(self.addNewFeedButton, SIGNAL("clicked()"), self.addFeedPopup.exec_)
   

    self.feedListWidget.itemActivated.connect(self.feedSelected);

    #	self.connect(self.reloadFeedsButton, SIGNAL("clicked()"), self.updateFeeds)
    self.rmFeedButton.setEnabled(False);
    self.connect(self.rmFeedButton, SIGNAL("clicked()"), self.rmFeed)

    
    #popUp
    
    #popUp signals:
    self.connect(self.addFeedPopup.send, SIGNAL("clicked()"), self.addFeed);
    self.connect(self.addFeedPopup.cancel, SIGNAL("clicked()"), self.addFeedPopup.close);

    
    
    
  def readFeed(self):
    if len(self.addressInput.text()) > 1:
      feedsrc = feed(self.addressInput.text());
      feedsrc.generate();
      self.rssContentView.setHtml(unicode(FeedBox.FeedBox.showFeeds(feedsrc.h1, feedsrc.content)));
      self.updateTitle(feedsrc.h1);
      
      
  def addFeed(self):
    newFeed = Feed(str(self.addFeedPopup.address.text()), str(self.addFeedPopup.name.text()));
    newFeed.add();
    self.addFeedPopup.close();
  def rmFeed(self):
    #self.feed_list.rmItem(selected.item());
    print self.feedListWidget.currentItem().text();
    
  def quit(self):
    rsssq.quit();
    
  def feedSelected(self,selected):

    print "opening feeds.. :)"
    self.rmFeedButton.setEnabled(True);

    

  
    
    
rsssq = QApplication(sys.argv)
rss_sq = rss_dragonfly() 
rss_sq.show()
rsssq.exec_()