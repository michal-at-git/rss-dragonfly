#!/usr/bin/python
# coding: utf-8

"""
Window front-end class 
"""
__version__ =  '1.2'
__name__ = 'Window';

from PyQt4.QtGui import *;
from PyQt4.QtCore import *;
from PyQt4.QtWebKit import *
import FeedBox;

import sys;
reload(sys);
sys.setdefaultencoding("utf-8");

class Window(QWidget):
  
  
  def drawWindow(self):  
    # <DEFINITIONS>
    self.rssContentView = QWebView();    
    self.addressInput = QLineEdit();
    self.addressInput.setFixedHeight(30);
    
    #it works with QT 4.7 and newer.
    try:
      self.addressInput.setProperty("placeholderText", u"enter feed address");
    except:
      0;
    self.goButton = QPushButton(u'Go');
    self.goButton.setFixedHeight(30)
   
    
    self.addNewFeedButton = QPushButton();
    self.reloadFeedsButton = QPushButton();
    #self.reloadOneFeedButton = QPushButton();    
    self.rmFeedButton = QPushButton();
    self.editFeedButton = QPushButton();
    
    self.saveFromAddrButton = QPushButton();
    self.menuButton = QPushButton( "RSS Dragonfly");

    
    self.feedListWidget = QListWidget();

    
    
    self.feedListWidget.setMinimumWidth(200);
    

    #layouts
      
    self.mainLayout = QVBoxLayout();
    self.topLinLayout = QHBoxLayout();
    self.midLinLayout = QHBoxLayout();
    self.listLayout = QVBoxLayout();
    self.listButtonsLayout = QHBoxLayout(); 
    
  
    #</DEFINITIONS>
    
    self.addNewFeedButton.setIcon(QIcon("GUI/plus.png"));
    self.addNewFeedButton.setIconSize(QSize(20,20));
    self.reloadFeedsButton.setIcon(QIcon("GUI/reload.png"));
    self.reloadFeedsButton.setIconSize(QSize(20,20));
    self.editFeedButton.setIcon(QIcon("GUI/edit.png"));
    self.editFeedButton.setIconSize(QSize(20,20));   
    self.rmFeedButton.setIcon(QIcon("GUI/minus.png"));
    self.rmFeedButton.setIconSize(QSize(20,20));
    self.saveFromAddrButton.setIcon(QIcon("GUI/star.png"));
    self.saveFromAddrButton.setIconSize(QSize(20,20));
    self.menuButton.setIcon(QIcon("GUI/ikonka.png"));
    self.menuButton.setIconSize(QSize(20,20));
    
    
    
    
    
    
    
    
    
    ##################################
    ###Dragonfly menu
    #################################
    self.aboutOption = QObject();    
    self.quitOption = QObject();
    self.importOption = QObject();
    self.settingsOption = QObject();
    self.checkUpdatesOption = QObject();

    
    self.importAction = QAction("&Import from file", self.importOption); 
    self.settingsAction = QAction("Se&ttings", self.settingsOption);    
    self.checkUpdatesAction = QAction("Check for &updates", self.checkUpdatesOption);

   
    self.aboutAction = QAction("&About", self.aboutOption);
    self.quitAction = QAction("&Quit", self.quitOption);
    self.dragonflyMenu = QMenu();
    self.dragonflyMenu.addAction(self.importAction);
    self.dragonflyMenu.addAction(self.settingsAction);
    self.dragonflyMenu.addAction(self.checkUpdatesAction);
    self.dragonflyMenu.addAction(self.aboutAction);
    self.dragonflyMenu.addAction(self.quitAction);
    
    self.menuButton.setMenu(self.dragonflyMenu);

    
    

    ### CONTEXT MENU FOR LIST ITEMS  
    
    self.listItemMenu= QMenu();

    self.editItemOption = QObject();
    self.updateItemOption = QObject();
    self.deleteItemOption = QObject();
    
    self.editItemAction = QAction(QIcon("GUI/edit.png"), "Edit selected item", self.editItemOption);
    self.updateItemAction = QAction(QIcon("GUI/reload.png"), "Update selected item", self.updateItemOption);
    self.deleteItemAction = QAction(QIcon("GUI/minus.png"), "delete", self.deleteItemOption);
    
    self.listItemMenu.addAction(self.editItemAction);
    self.listItemMenu.addAction(self.updateItemAction);
    self.listItemMenu.addAction(self.deleteItemAction)

    

    
    ###*****************************
    
    
    

    #setting tooltips
    self.addNewFeedButton.setToolTip(u"Add new RSS feed to list");
    self.reloadFeedsButton.setToolTip(u"Update feed list");
    self.rmFeedButton.setToolTip(u"Delete selected item from list");
    #self.reloadOneFeedButton.setToolTip(u"Update selected feed"); 
    self.goButton.setToolTip(u"Open feed");
    #self.closeButton.setToolTip(u"Quit from RSS Dragonfly");
    self.saveFromAddrButton.setToolTip(u"Save this feed to list");
    self.menuButton.setToolTip(u"Menu");
    self.menuButton.setFixedWidth(155);
   

    
    
    
    #setting layouts
    

    
    self.mainLayout.addLayout(self.topLinLayout);
    self.mainLayout.addLayout(self.midLinLayout);
    
    self.listButtonsLayout.addWidget(self.addNewFeedButton);
    self.listButtonsLayout.addWidget(self.rmFeedButton);
    #self.listButtonsLayout.addWidget(self.editFeedButton); # ZA DUŻO MIEJSCA POBIERA... TRZEBA ZROBIĆ COŚ Z WYMIARAMIII!!!!!!!!!!!  
    self.listButtonsLayout.addWidget(self.reloadFeedsButton);
    #self.listButtonsLayout.addWidget(self.reloadOneFeedButton);

    self.topLinLayout.addWidget(self.saveFromAddrButton);
    self.topLinLayout.addWidget(self.addressInput);
    self.topLinLayout.addWidget(self.goButton);
    #self.topLinLayout.addWidget(self.closeButton);
    self.topLinLayout.addWidget(self.menuButton);

    
    self.midLinLayout.addLayout(self.listLayout);
    
    self.listLayout.addLayout(self.listButtonsLayout);
    self.listLayout.addWidget(self.feedListWidget);
    
    
    self.midLinLayout.addWidget(self.rssContentView);

    self.setLayout(self.mainLayout);
    
    self.setGeometry(400, 180, 700,500);
    self.setWindowIcon(QIcon('GUI/ikonka.png'));
    self.setWindowTitle("RSS Dragonfly");
    self.rssContentView.setHtml(unicode(FeedBox.FeedBox.start()));
    
    self.setMinimumSize(600, 400);

  def updateTitle(self, h1):
        self.setWindowTitle(unicode(h1+" | RSS Dragonfly"));

    