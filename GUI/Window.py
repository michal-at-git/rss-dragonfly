#!/usr/bin/python
# coding: utf-8

"""
Window front-end class 
"""
__version__ =  '1.1 - milestone 1'
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
    
    #self.status = QString(u'<div style=\"margin-left: 300%; color: blue;\">załadowano</div>');
    self.statusDisplay = QLabel(u'załadowano...');
    
    self.feedListWidget = QListWidget()
  

    
    
    self.feedListWidget.setMinimumWidth(200);
    

    #layouts
      
    self.mainLayout = QVBoxLayout();
    self.topLinLayout = QHBoxLayout();
    self.midLinLayout = QHBoxLayout();
    self.listLayout = QVBoxLayout();
    #self.listButtLayout = QHBoxLayout(); #chyba do usunięcia
    
  
    #</DEFINITIONS>
    
    self.addNewFeedButton.setIcon(QIcon("GUI/plus.png"));
    self.reloadFeedsButton.setIcon(QIcon("GUI/reload.png"));
    self.reloadOneFeedButton.setIcon(QIcon("GUI/reload_one.png"));
    self.rmFeedButton.setIcon(QIcon("GUI/minus.png"));
    #setting tooltips
    self.addNewFeedButton.setToolTip(u"Dodaj do listy nowy kanał RSS");
    self.reloadFeedsButton.setToolTip(u"Zaktualizuj kanały RSS");
    self.rmFeedButton.setToolTip(u"Usuń z listy kanał RSS");
    #self.fromFileButton.setToolTip(u"Załaduj z pliku kanał RSS"); #w tym wydaniu zablokowany
    
   

    
    
    
    #setting layouts
    

    
    self.mainLayout.addLayout(self.topLinLayout);
    self.mainLayout.addLayout(self.midLinLayout);
    self.mainLayout.addWidget(self.statusDisplay);
    
    self.topLinLayout.addWidget(self.addNewFeedButton);
    self.topLinLayout.addWidget(self.reloadFeedsButton);
    self.topLinLayout.addWidget(self.reloadOneFeedButton);

    self.topLinLayout.addWidget(self.rmFeedButton);
    #self.topLinLayout.addWidget(self.fromFileButton); # w tym wydaniu zablokowany
    
    self.topLinLayout.addWidget(self.addressInput);
    self.topLinLayout.addWidget(self.goButton);
    self.topLinLayout.addWidget(self.closeButton);
    
    self.midLinLayout.addLayout(self.listLayout);
    
    self.listLayout.addWidget(self.feedListWidget);
    #self.listLayout.addLayout(self.listButtLayout); #ten layout chyba do usunięcia
    #self.listButtLayout.addWidget(self.addNewFeedButton);
    #self.listButtLayout.addWidget(self.reloadFeedsButton);
    #self.listButtLayout.addWidget(self.rmFeedButton);
    
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

    