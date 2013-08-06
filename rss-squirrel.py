#!/usr/bin/python
#-*- coding: utf-8 -*-


from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from feedparser import *


from feed_ruler import *
import pop_ups
from string import lower
import urllib
from os import remove

class nut:
  def __init__(self, addr=None):
    
    self.addr = addr
    self.frss = parse(str(self.addr))  

   
    
class squirrelGUI(QDialog):
 def init(self):
    self.rssContentView = QTextBrowser();
    self.addr = QLineEdit();
    self.goButt = QPushButton(u'Otwórz');
    self.fromFileButt = QPushButton(u'z pliku');
    self.closeButt = QPushButton(u'Zamknij');
    self.addButt = QPushButton();
    self.relButt = QPushButton();
    self.rmButt = QPushButton();
    
    self.addButt.setIcon(QIcon("plus.png"))
    self.relButt.setIcon(QIcon("reload.png"))
    self.rmButt.setIcon(QIcon("minus.png"))
    
    #disable buttons
    self.rmButt.setEnabled(False)

    
    #tooltips
    self.addButt.setToolTip(u"Dodaj do listy nowy kanał RSS")
    self.relButt.setToolTip(u"Zaktualizuj kanały RSS")
    self.rmButt.setToolTip(u"Usuń z listy kanał RSS")
    self.fromFileButt.setToolTip(u"Załaduj z pliku kanał RSS")
    
    #list
    
    self.feedList = QListWidget()
    self.feedList.setMaximumWidth(200)
    for i in feedr().flist:
      self.feedList.addItem(i);
      
    #layouts
    
    mainLayout = QVBoxLayout();
    topLinLayout = QHBoxLayout();
    midLinLayout = QHBoxLayout();
    listLayout = QVBoxLayout();
    listButtLayout = QHBoxLayout();
    
    mainLayout.addLayout(topLinLayout);
    mainLayout.addLayout(midLinLayout);
    
    topLinLayout.addWidget(self.fromFileButt);
    topLinLayout.addWidget(self.closeButt);
    topLinLayout.addWidget(self.addr);
    topLinLayout.addWidget(self.goButt);
    
    midLinLayout.addLayout(listLayout);
    
    listLayout.addWidget(self.feedList);
    listLayout.addLayout(listButtLayout);
    listButtLayout.addWidget(self.addButt);
    listButtLayout.addWidget(self.relButt);
    listButtLayout.addWidget(self.rmButt);
    
    midLinLayout.addWidget(self.rssContentView);

    self.setLayout(mainLayout);
    self.setGeometry(400, 180, 600,500);
    self.setWindowIcon(QIcon('ikonka.png'));
    self.setWindowTitle("RSS Squirrel")
    
class rss_squirrel(squirrelGUI):
  def __init__(self, parent=None):
    super(rss_squirrel, self).__init__(parent)
    self.init()
    self.rssContentView.setText("<h1>Witaj w RSS Squirrel!!!</h1>");
    
    self.connect(self.goButt, SIGNAL("clicked()"), self.readFeed)
    self.connect(self.fromFileButt, SIGNAL("clicked()"), self.fromFile)
    self.connect(self.closeButt, SIGNAL("clicked()"), rsssq.quit)
    self.feedList.itemActivated.connect(self.readExistFeed)
    
    self.connect(self.addButt, SIGNAL("clicked()"), self.addFeed)
    self.connect(self.relButt, SIGNAL("clicked()"), self.updateFeeds)
    self.connect(self.rmButt, SIGNAL("clicked()"), self.rmFeed)
    
    
    
  def readFeed(self, link=None):
    try:
      if (link == None):
	x = nut(self.addr.text());
      else: x=nut(link);
      self.rssContentView.setText("<h1>"+x.frss.feed.title+"</h1>");
      i = 0;
      self.setWindowTitle(x.frss.feed.title+" | RSS Squirrel")
      
      for n in x.frss.entries:
	self.rssContentView.append("<h2>"+x.frss.entries[i].title+"</h2>");
	self.rssContentView.append("<i>"+x.frss.entries[i].published+"</i>");
	self.rssContentView.append(x.frss.entries[i].description);
	i += 1
	
    except:
      self.rssContentView.setText("<h1>"+u'Nie można załadować kanału rss'+"</h1>")
      self.setWindowTitle(u"Nie można załadować kanału rss | RSS Squirrel")
      
      
  def readExistFeed(self, FList):
    self.readFeed("feeds/"+lower(str(FList.text())).replace(" ", "")+".rss") #FList -> arg wysył z self.lista.itemActivated.connect(self.openfeed)

    #enabling buttons
    self.rmButt.setEnabled(True)
    
    
    
  def fromFile(self):
    feedFile = QFileDialog.getOpenFileName(self, '', '*.rss')
    self.readFeed(feedFile);
    

  def addFeed(self):
    element = pop_ups.manage()
    if (element.adres.text()):
      source = urllib.urlopen(str(element.adres.text()));  #element adres z pop_pups
      target = open(u"feeds/"+lower(str(element.label.text())).replace(" ", "")+".rss", "w") #nazw - pop_ups
      target.write(source.read())
      target.close()
      
      self.feedList.clear();
      i = 0; stop = False;
      for j in feedr().flist: 
	self.feedList.addItem(j);        #feedr() <-> feed_ruler
	if (stop == False and j != element.label.text()): 
	  i += 1
	else: stop = True
	
      self.feedList.item(i).setSelected(True);
      self.readExistFeed(self.feedList.selectedItems()[0])
      self.rmButt.setEnabled(True)

  def updateFeeds(self):
    for obj in feedr().flist:
      
      source = urllib.urlopen(feedr().flist[obj]);
      target = open(u"feeds/"+lower(obj).replace(" ", "")+".rss", "w")
      target.write(source.read())
      target.close()
      
      
  def rmFeed(self):
    remove("feeds/"+lower(str(self.feedList.selectedItems()[0].text()).replace(" ", ""))+".rss");
    feedr().feed_rm(str(self.feedList.selectedItems()[0].text()));
    
    self.feedList.clear()
    
    for i in feedr().flist: self.feedList.addItem(i);
    

    
    
    

rsssq = QApplication(sys.argv)
rss_sq = rss_squirrel() #rss_sq = _rss_squirrel() #można przełączyć na tryb testowy
rss_sq.show()
rsssq.exec_()