#!/usr/bin/python
# coding: utf-8


"""
Main class of RSS Dragonfly
"""


__version__ =  '1.2' 

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
reload(sys)
sys.setdefaultencoding("utf-8");


sys.path.append('GUI/');
from Window import *;
from AddFeedDialog import *;
from EditFeedDialog import *;
from AboutDialog import *;
from SettingsDialog import *
from Tray import Tray;

sys.path.append('modules/');
import FeedBox;
from Feed import Feed;
from FeedList import FeedList;
from Source import Source;
from DB import DB;
from Settings import Settings;

from threading import *
   
class rss_dragonfly(Window):
  selected = False;
  def __init__(self, parent=None):
    super(rss_dragonfly, self).__init__(parent);
    self.drawWindow();
    
    self.database = DB();
    self.feedList = FeedList(self.feedListWidget, self.database);
    self.addFeedPopup = AddFeedDialog();
    self.editFeedDialog = EditFeedDialog();
    self.aboutDialog = AboutDialog();
    self.settings = Settings(self.database);
    self.settingsDialog = SettingsDialog(self.settings.currentSettings());

    
    self.connect(self.aboutAction, SIGNAL("triggered()"), self.aboutDialog.exec_);
    self.connect(self.importAction, SIGNAL("triggered()"), self.fromFile);
    self.connect(self.settingsAction, SIGNAL("triggered()"), self.displaySettings);
    
    self.connect(self.settingsDialog.saveButton, SIGNAL("clicked()"), self.saveSettings);

    
    self.connect(self.goButton, SIGNAL("clicked()"), self.readFromAddrBar);
    

    self.connect(self.addressInput, SIGNAL("returnPressed()"), self.readFromAddrBar);
    
    self.connect(self.quitAction, SIGNAL("triggered()"), self.quit)
    
    self.connect(self.addNewFeedButton, SIGNAL("clicked()"), self.addFeedPopup.exec_)
   

    self.feedListWidget.itemActivated.connect(self.listItemSelected);
    
    self.feedListWidget.setContextMenuPolicy(Qt.CustomContextMenu);
    self.connect(self.feedListWidget, SIGNAL("customContextMenuRequested(const QPoint &)"), self.listMenu);
    

    self.connect(self.reloadFeedsButton, SIGNAL("clicked()"), self.updateAllFeeds);
    
    # context menu form list
    self.connect(self.updateItemAction, SIGNAL("triggered()"), self.updateSelectedFeed);
    self.connect(self.deleteItemAction, SIGNAL("triggered()"), self.rmFeed);
    self.connect(self.editItemAction, SIGNAL("triggered()"), self.editFeed);
    self.connect(self.checkUpdatesAction, SIGNAL("triggered()"), self.checkForUpdates);
    
    self.connect(self.rmFeedButton, SIGNAL("clicked()"), self.rmFeed)
    self.connect(self.saveFromAddrButton, SIGNAL("clicked()"), self.saveOpened);
    
    #popUp
    
    #popUp signals:
    self.connect(self.addFeedPopup.send, SIGNAL("clicked()"), self.addFeed);
    self.connect(self.addFeedPopup.cancel, SIGNAL("clicked()"), self.cancel);
    self.connect(self.aboutDialog.closeButton, SIGNAL("clicked()"), self.aboutDialog.close);
    self.connect(self.editItemAction, SIGNAL("clicked()"), self.editFeed);
    self.connect(self.editFeedDialog.save, SIGNAL("clicked()"), self.editFeedSubmit);
    
    

    
    self.rmFeedButton.setDisabled(True);
    self.saveFromAddrButton.setDisabled(True);
    
  def start(self, tray):
    startDB = DB();
    settings = Settings(startDB);
    settings = settings.currentSettings();

    FeedBox.FeedBox.setTheme(settings['theme']); 
    
    if(settings['startMinimalized']):
      tray.minimalization();
    if(settings['startup']):
      self.updateAllFeeds();


  def listMenu(self, point):
    currentItem = self.feedListWidget.currentItem()
    if currentItem:
      self.selected = self.feedListWidget.indexFromItem(currentItem).row()
      #self.listItemSelected(currentItem)
      self.listItemMenu.exec_(QCursor.pos());
    
  def readFromAddrBar(self):
    if len(str(self.addressInput.text())) > 1:
      if self.selected != False:
	
	self.selected = False;
      
      source = Source();
      source = source.fromURL(str(self.addressInput.text()));
      if(source != False):
	try:
	  feed = Feed(source);  
	  self.rssContentView.setHtml(unicode(FeedBox.FeedBox.showFeeds(feed.feedTitle, feed.toHTML())));
	  self.updateTitle(str(feed.feedTitle).replace("&#39;", "'"));
	  self.rmFeedButton.setEnabled(False);
	  #self.reloadOneFeedButton.setEnabled(False);
	  self.saveFromAddrButton.setEnabled(True);
	  self.addFeedPopup.name.setText(feed.feedTitle);
	  

	except:
	  self.rssContentView.setHtml(unicode(FeedBox.FeedBox.parseError()));
	  self.updateTitle("Unable to load RSS feed");

      else:
	self.rssContentView.setHtml(unicode(FeedBox.FeedBox.downloadError()));
	self.updateTitle("Unable to load RSS feed");
      self.feedListWidget.clearSelection();

      
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
	  self.updateTitle("Unable to load RSS feed");
      else:
	self.rssContentView.setHtml(unicode(FeedBox.FeedBox.downloadError()));
	self.updateTitle("Unable to load RSS feed");	
	
      self.addFeedPopup.name.clear();
      self.addFeedPopup.address.clear();
      self.addFeedPopup.close();
      
  def editFeed(self):
    feed = self.feedList.getSingleSubscription(self.selected);
    self.editFeedDialog.setWindowTitle(u"Edit feed | "+feed['name']);
    self.editFeedDialog.name.setText(feed['name']);
    self.editFeedDialog.address.setText(feed['addr']);
    
    feedSingle = self.feedList.getSingleSubscription(self.selected);

    self.editFeedDialog.exec_();
  
  def editFeedSubmit(self):
    try:
      name = self.editFeedDialog.name.text();
      address = self.editFeedDialog.address.text();
      self.feedList.editSelectedFeed(self.selected, str(name), str(address), Feed, Source);
      self.editFeedDialog.close();
      self.feedListWidget.setCurrentRow(self.selected)
      self.listItemSelected(self.feedListWidget.currentItem())
    except:
      self.rssContentView.setHtml(unicode(FeedBox.FeedBox.updateError()));
      self.updateTitle("Unable to update RSS feed"); 
      
  def rmFeed(self):
    self.feedList.remove(self.selected);
    self.rmFeedButton.setEnabled(False);

        
  def quit(self):
    rsssq.quit();
    
  def listItemSelected(self,selected):
    self.addressInput.clear();
    self.selected =  self.feedListWidget.indexFromItem(selected).row();
    
    html = self.feedList.getSingleSubscriptionToHTML(self.selected);
    feedSingle = self.feedList.getSingleSubscription(self.selected);
    self.rssContentView.setHtml(unicode(FeedBox.FeedBox.showFeeds(feedSingle['FeedTitle'], html)));
    self.updateTitle(feedSingle['FeedTitle'].replace("&#39;", "'"));
    

    self.rmFeedButton.setEnabled(True);
    self.saveFromAddrButton.setEnabled(False);

    

    
  def saveOpened(self):
    self.addFeedPopup.address.setText(self.addressInput.text());    
    self.addFeedPopup.exec_();
  

    
  def updateAllFeeds(self):
    try:
      self.feedList.updateAll(Feed,Source);
            
      if(self.selected):      
	#updating content on screen
	html = self.feedList.getSingleSubscriptionToHTML(self.selected);
	feedSingle = self.feedList.getSingleSubscription(self.selected);
	self.rssContentView.setHtml(unicode(FeedBox.FeedBox.showFeeds(feedSingle['FeedTitle'], html)));
	self.updateTitle(feedSingle['FeedTitle'].replace("&#39;", "'"));
    except:
      self.rssContentView.setHtml(unicode(FeedBox.FeedBox.updateError()));
      self.updateTitle("Unable to update RSS feed"); 
    
    
    self.rmFeedButton.setEnabled(False);
    #self.reloadOneFeedButton.setEnabled(False);

  
  def updateSelectedFeed(self):
    try:
      self.feedList.updateSelectedFeed(self.selected, Feed, Source);
      
      #updating content on screen
      html = self.feedList.getSingleSubscriptionToHTML(self.selected);
      feedSingle = self.feedList.getSingleSubscription(self.selected);
      self.rssContentView.setHtml(unicode(FeedBox.FeedBox.showFeeds(feedSingle['FeedTitle'], html)));
      self.updateTitle(feedSingle['FeedTitle'].replace("&#39;", "'"));
      
    except:
      self.rssContentView.setHtml(unicode(FeedBox.FeedBox.updateError()));
      self.updateTitle("Unable to update RSS feed");
  
 
  
  def cancel(self):
    self.addFeedPopup.name.clear();
    self.addFeedPopup.address.clear();
    self.addFeedPopup.close();
    
  def fromFile(self):
    rssFile = QFileDialog.getOpenFileName(self, 'rss', '*.rss');
    source = Source();
    
    self.saveFromAddrButton.setEnabled(False);
    self.addressInput.clear();
    self.feedListWidget.clearSelection();
    try:
      feed = Feed(source.fromFile(str(rssFile)), "file");
      self.updateTitle(str(feed.feedTitle).replace("&#39;", "'"));
      self.rssContentView.setHtml(unicode(FeedBox.FeedBox.showFeeds(feed.feedTitle, feed.toHTML())));
    except:
      self.rssContentView.setHtml(unicode(FeedBox.FeedBox.parseError()));
      self.updateTitle("Unable to open RSS feed");

   
    
  def displaySettings(self):
    self.settingsDialog.exec_()
    
  def saveSettings(self):
    
    self.settings.saveSettings(self.settingsDialog.getSettingsArray());
    settings = self.settings.currentSettings()
    FeedBox.FeedBox.setTheme(settings['theme']);     
    self.settingsDialog.close();
    if (self.selected):
      self.listItemSelected(self.feedListWidget.currentItem());
    else:
      self.rssContentView.setHtml(unicode(FeedBox.FeedBox.start()));
      self.setWindowTitle("RSS Dragonfly");
      self.addressInput.clear();
      self.saveFromAddrButton.setEnabled(False);
      self.feedListWidget.clearSelection();
      

  def checkForUpdates(self):
    self.check = Thread(target=self.runUpdater).start();

  def runUpdater(self):
    import os;
    os.system("./updater.py")
    
rsssq = QApplication(sys.argv)
rss_sq = rss_dragonfly() 

  

rss_sq.show()
tray = Tray(rss_sq, rsssq);

rss_sq.start(tray);

rsssq.exec_()