#!/usr/bin/python
# coding: utf-8


"""
Main class of RSS Dragonfly
"""

__version__ =  '1.1 - milestone 3' #/5

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

from string import lower
import urllib
from os import remove



    
class rss_dragonfly(Window):
  selected = False;
  def __init__(self, parent=None):
    super(rss_dragonfly, self).__init__(parent);
    self.drawWindow();
    
    self.dbHandle = DB();
    
    self.feedList = FeedList(self.feedListWidget, self.dbHandle);
    self.addFeedPopup = AddFeedDialog();
    

    
    #status singals
    
    self.rssContentView.loadFinished.connect(self.statusLoaded);
    self.connect(self.goButton, SIGNAL("clicked()"), self.readFeed);
    

    self.connect(self.addressInput, SIGNAL("returnPressed()"), self.readFeed);
    
    #	self.connect(self.fromFileButton, SIGNAL("clicked()"), self.fromFile)
    self.connect(self.closeButton, SIGNAL("clicked()"), self.quit)
    
    self.connect(self.addNewFeedButton, SIGNAL("clicked()"), self.addFeedPopup.exec_)
   

    self.feedListWidget.itemActivated.connect(self.listItemSelected);

    #	self.connect(self.reloadFeedsButton, SIGNAL("clicked()"), self.updateFeeds)
    self.rmFeedButton.setEnabled(False);
    self.connect(self.rmFeedButton, SIGNAL("clicked()"), self.rmFeed)

    
    #popUp
    
    #popUp signals:
    self.connect(self.addFeedPopup.send, SIGNAL("clicked()"), self.addFeed);
    self.connect(self.addFeedPopup.cancel, SIGNAL("clicked()"), self.addFeedPopup.close);

    
    
    
  def readFeed(self,url=False):
    if len(str(self.addressInput.text())) > 1:
      if self.selected != False:
	self.feedListWidget.setItemSelected(self.selected, False);
	self.selected = False;
      
      self.feedsrc = Feed();
      self.feedsrc.generateFromURL(str(self.addressInput.text()));
      self.rssContentView.setHtml(unicode(FeedBox.FeedBox.showFeeds(self.feedsrc.h1, self.feedsrc.content)));
      self.updateTitle(self.feedsrc.h1);
      self.rmFeedButton.setEnabled(False);

    elif url != False and (len(str(url)) > 1):
      self.feedsrc = Feed();
      self.feedsrc.generateFromURL(url);
      self.rssContentView.setHtml(unicode(FeedBox.FeedBox.showFeeds(self.feedsrc.h1, self.feedsrc.content)));
      self.updateTitle(self.feedsrc.h1);
      
  def addFeed(self):
    if(len(str(self.addFeedPopup.address.text()))>5 and len(self.addFeedPopup.name.text()) >2):
      self.readFeed(str(self.addFeedPopup.address.text()));
      self.feedList.add(str(self.addFeedPopup.name.text()), str(self.addFeedPopup.address.text()), self.feedsrc.src);
      self.addFeedPopup.close();
    
  def rmFeed(self):
    fromListId =  self.feedListWidget.indexFromItem(self.selected).row();
    self.feedList.remove(fromListId);
    self.rmFeedButton.setEnabled(False);

        
  def quit(self):
    rsssq.quit();
    
  def listItemSelected(self,selected):
    self.selected = selected;
    self.addressInput.clear();

    fromListId =  self.feedListWidget.indexFromItem(self.selected).row();
    source = self.feedList.read(fromListId);
    self.feedsrc = Feed();
    self.feedsrc.generateFromSource(source['src']);
    self.rssContentView.setHtml(unicode(FeedBox.FeedBox.showFeeds(self.feedsrc.h1, self.feedsrc.content)));
    self.updateTitle(self.feedsrc.h1);
    

    self.rmFeedButton.setEnabled(True);
    
    
  #temporary!!!
  def statusLoading(self):
    self.statusDisplay.setText(u"Ładowanie");
  def statusLoaded(self):
    self.statusDisplay.setText(u"Załadowano");

  
    
    
rsssq = QApplication(sys.argv)
rss_sq = rss_dragonfly() 
rss_sq.show()
rsssq.exec_()