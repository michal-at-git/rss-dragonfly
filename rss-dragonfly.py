#!/usr/bin/python
# coding: utf-8


"""
Main class of RSS Dragonfly
"""
#TODO REFRESH SCREEN ON UPDATE SELECTED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#TODO update titlebar

__version__ =  '1.1 - milestone 4' #/5

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
reload(sys)
sys.setdefaultencoding("utf-8");


sys.path.append('GUI/');
from Window import *;
from AddFeedDialog import *;
from AboutDialog import *;

sys.path.append('modules/');
import FeedBox;
from Feed import Feed;
from FeedList import FeedList;
from Source import Source;
from DB import DB;


    
class rss_dragonfly(Window):
  selected = False;
  def __init__(self, parent=None):
    super(rss_dragonfly, self).__init__(parent);
    self.drawWindow();
    
    self.database = DB();
    self.feedList = FeedList(self.feedListWidget, self.database);
    self.addFeedPopup = AddFeedDialog();
    self.aboutDialog = AboutDialog();

    
    self.connect(self.aboutButton, SIGNAL("clicked()"), self.aboutDialog.exec_);

    
    self.connect(self.goButton, SIGNAL("clicked()"), self.readFromAddrBar);
    

    self.connect(self.addressInput, SIGNAL("returnPressed()"), self.readFromAddrBar);
    
    self.connect(self.closeButton, SIGNAL("clicked()"), self.quit)
    
    self.connect(self.addNewFeedButton, SIGNAL("clicked()"), self.addFeedPopup.exec_)
   

    self.feedListWidget.itemActivated.connect(self.listItemSelected);

    self.connect(self.reloadFeedsButton, SIGNAL("clicked()"), self.updateAllFeeds);
    self.connect(self.reloadOneFeedButton, SIGNAL("clicked()"), self.updateSelectedFeed);

    
    self.connect(self.rmFeedButton, SIGNAL("clicked()"), self.rmFeed)
    self.connect(self.saveFromAddrButton, SIGNAL("clicked()"), self.saveOpened);
    
    #popUp
    
    #popUp signals:
    self.connect(self.addFeedPopup.send, SIGNAL("clicked()"), self.addFeed);
    self.connect(self.addFeedPopup.cancel, SIGNAL("clicked()"), self.addFeedPopup.close);
    
    self.reloadOneFeedButton.setDisabled(True);
    self.rmFeedButton.setDisabled(True);
    self.saveFromAddrButton.setDisabled(True);
    
    
    
  def readFromAddrBar(self):
    if len(str(self.addressInput.text())) > 1:
      if self.selected != False:
	
	#double disabling selected element?
	#print self.selected;

	#self.feedListWidget.setItemSelected(self.selected, False);
	self.selected = False;
      
      source = Source();
      source = source.fromURL(str(self.addressInput.text()));
      if(source != False):
	try:
	  feed = Feed(source);      
	  self.rssContentView.setHtml(unicode(FeedBox.FeedBox.showFeeds(feed.feedTitle, feed.toHTML())));
	  self.updateTitle(feed.feedTitle);
	  self.rmFeedButton.setEnabled(False);
	  self.reloadOneFeedButton.setEnabled(False);
	  self.feedListWidget.clearSelection();
	  self.saveFromAddrButton.setEnabled(True);
	  self.addFeedPopup.name.setText(feed.feedTitle);
	  

	except:
	  self.rssContentView.setHtml(unicode(FeedBox.FeedBox.parseError()));
	  self.updateTitle("Nie udało się odczytać kanału RSS");
	  
      else:
	self.rssContentView.setHtml(unicode(FeedBox.FeedBox.downloadError()));
	self.updateTitle("Nie udało się załadować kanału RSS");
	
      
  def addFeed(self):
    if(len(str(self.addFeedPopup.address.text()))>5 and len(self.addFeedPopup.name.text()) >2):
      source = Source();
      source = source.fromURL(str(self.addFeedPopup.address.text()))
      if(source != False):
	try:
	  feed = Feed(source);
	  self.feedList.add(feed, self.addFeedPopup.name.text(), self.addFeedPopup.address.text());
	except:
	  self.rssContentView.setHtml(unicode(FeedBox.FeedBox.parseError()));
	  self.updateTitle("Nie udało się odczytać kanału RSS");
      else:
	self.rssContentView.setHtml(unicode(FeedBox.FeedBox.downloadError()));
	self.updateTitle("Nie udało się załadować kanału RSS");	
	
      self.addFeedPopup.name.clear();
      self.addFeedPopup.address.clear();
      self.addFeedPopup.close();
    
  def rmFeed(self):
    #fromListId =  self.feedListWidget.indexFromItem(self.selected).row();
    self.feedList.remove(self.selected);
    self.rmFeedButton.setEnabled(False);
    self.reloadOneFeedButton.setEnabled(False);

        
  def quit(self):
    rsssq.quit();
    
  def listItemSelected(self,selected):
    self.addressInput.clear();

    self.selected =  self.feedListWidget.indexFromItem(selected).row();
    
    html = self.feedList.getSingleSubscriptionToHTML(self.selected);
    feedSingle = self.feedList.getSingleSubscription(self.selected);
    self.rssContentView.setHtml(unicode(FeedBox.FeedBox.showFeeds(feedSingle['FeedTitle'], html)));
    self.updateTitle(feedSingle['FeedTitle']);
    

    self.rmFeedButton.setEnabled(True);
    self.reloadOneFeedButton.setEnabled(True);
    self.saveFromAddrButton.setEnabled(False);

    

    
  def saveOpened(self):
    self.addFeedPopup.address.setText(self.addressInput.text());
    
    self.addFeedPopup.exec_();
    
    
  def updateAllFeeds(self):
    try:
      self.feedList.updateAll(Feed,Source);
      self.feedListWidget.clearSelection();
    except:
      self.rssContentView.setHtml(unicode(FeedBox.FeedBox.updateError()));
      self.updateTitle("Nie udało się zaktualizować subskrypcji RSS"); 
    
    
    self.rmFeedButton.setEnabled(False);
    self.reloadOneFeedButton.setEnabled(False);

  
  def updateSelectedFeed(self):
    try:
      self.feedList.updateSelectedFeed(self.selected, Feed, Source);
    except:
      self.rssContentView.setHtml(unicode(FeedBox.FeedBox.updateError()));
      self.updateTitle("Nie udało się zaktualizować subskrypcji RSS");
    
    
rsssq = QApplication(sys.argv)
rss_sq = rss_dragonfly() 
rss_sq.show()
rsssq.exec_()