#!/usr/bin/python
# coding: utf-8

"""
Window front-end class 
"""
__version__ =  '1.1 - milestone 3'
__name__ = 'window';

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
    
    #it works with QT 4.7 and newer.
    try:
      self.addressInput.setProperty("placeholderText", u"wpisz adres strony");
    except:
      0;
    self.goButton = QPushButton(u'Przejdź');
    #self.fromFileButton = QPushButton(u'z pliku'); # w tym wydaniu zablokowany
    self.closeButton = QPushButton(u'Zamknij');
    
    self.addNewFeedButton = QPushButton();
    self.reloadFeedsButton = QPushButton();
    self.reloadOneFeedButton = QPushButton();    
    self.rmFeedButton = QPushButton();
    self.saveFromAddrButton = QPushButton();
    self.aboutButton = QPushButton();

    self.statusDisplay = QLabel();
    
    self.feedListWidget = QListWidget()

    
    
    self.feedListWidget.setMinimumWidth(200);
    

    #layouts
      
    self.mainLayout = QVBoxLayout();
    self.topLinLayout = QHBoxLayout();
    self.midLinLayout = QHBoxLayout();
    self.listLayout = QVBoxLayout();
    self.listButtonsLayout = QHBoxLayout(); 
    
  
    #</DEFINITIONS>
    
    self.addNewFeedButton.setIcon(QIcon("GUI/plus.png"));
    self.reloadFeedsButton.setIcon(QIcon("GUI/reload.png"));
    self.reloadOneFeedButton.setIcon(QIcon("GUI/reload_one.png"));
    self.rmFeedButton.setIcon(QIcon("GUI/minus.png"));
    self.saveFromAddrButton.setIcon(QIcon("GUI/star.png"));
    self.aboutButton.setIcon(QIcon("GUI/ikonka.png"));


    #setting tooltips
    self.addNewFeedButton.setToolTip(u"Dodaj do listy nowy kanał RSS");
    self.reloadFeedsButton.setToolTip(u"Zaktualizuj kanały RSS");
    self.rmFeedButton.setToolTip(u"Usuń z listy kanał RSS");
    self.reloadOneFeedButton.setToolTip(u"Odśwież wybrany kanał RSS");
    self.goButton.setToolTip(u"Otwórz wybrany kanał RSS");
    self.closeButton.setToolTip(u"Zamknij program RSS Dragonfly");
    self.saveFromAddrButton.setToolTip(u"Zapisz kanał na liście");
    self.aboutButton.setToolTip(u"Informacja o programie");

   

    
    
    
    #setting layouts
    

    
    self.mainLayout.addLayout(self.topLinLayout);
    self.mainLayout.addLayout(self.midLinLayout);
    self.mainLayout.addWidget(self.statusDisplay);
    
    self.listButtonsLayout.addWidget(self.addNewFeedButton);
    self.listButtonsLayout.addWidget(self.rmFeedButton);
    self.listButtonsLayout.addWidget(self.reloadFeedsButton);
    self.listButtonsLayout.addWidget(self.reloadOneFeedButton);

    self.topLinLayout.addWidget(self.saveFromAddrButton);
    self.topLinLayout.addWidget(self.addressInput);
    self.topLinLayout.addWidget(self.goButton);
    self.topLinLayout.addWidget(self.closeButton);
    self.topLinLayout.addWidget(self.aboutButton);

    
    self.midLinLayout.addLayout(self.listLayout);
    
    self.listLayout.addLayout(self.listButtonsLayout);
    self.listLayout.addWidget(self.feedListWidget);
    
    
    self.midLinLayout.addWidget(self.rssContentView);

    self.setLayout(self.mainLayout);
    
    self.setGeometry(400, 180, 700,500);
    self.setWindowIcon(QIcon('GUI/ikonka.png'));
    self.setWindowTitle("RSS Dragonfly");
    self.rssContentView.setHtml(unicode(FeedBox.FeedBox.start()));
    
    self.setMinimumWidth(600);
    self.setMinimumHeight(400);

  def updateTitle(self, h1):
        self.setWindowTitle(unicode(h1+" | RSS Dragonfly"));

    