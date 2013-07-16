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
    
    #disable all buttons
    self.addButt.setEnabled(False)
    self.relButt.setEnabled(False)
    self.rmButt.setEnabled(False)

    
    #tooltips
    self.addButt.setToolTip(u"Dodaj do listy nowy kanał RSS")
    self.relButt.setToolTip(u"Odśwież zaznaczony kanał")
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
    self.addButt.setEnabled(True)
    self.relButt.setEnabled(True)
    self.rmButt.setEnabled(True)
    
    
    
  def fromFile(self):
    feedFile = QFileDialog.getOpenFileName(self, '', '*.rss')
    self.readFeed(feedFile);
    

  def addFeed(self):
    element = pop_ups.manage()
    source = urllib.urlopen(str(element.adres.text()));  #element adres z pop_pups
    target = open(u"feeds/"+lower(str(element.nazw.text())).replace(" ", "")+".rss", "w") #nazw - pop_ups
    target.write(source.read())
    target.close()
    
    self.feedList.clear();
    for i in feedr().flist: self.feedList.addItem(i);  #feedr() <-> feed_ruler
    
  def rmFeed(self):
    remove("feeds/"+lower(str(self.feedList.selectedItems()[0].text()).replace(" ", ""))+".rss");
    feedr().feed_rm(str(self.feedList.selectedItems()[0].text()));
    
    self.feedList.clear()
    
    for i in feedr().flist: self.feedList.addItem(i);
    

    
    
    
    
#=====================================================================
#@@@@@@@	STARY MODEL			@@@@@@@@@@@@@@@@@@@@@@
#=====================================================================



class rss_squirrel_OLD(QDialog):
    def __init__(self, parent=None):
        super(rss_squirrel_OLD, self).__init__(parent)
        
        self.start();
        self.widok.setText("<h1>Witaj w RSS Squirrel!!!</h1>");
            

    def start(self):
      
        self.widok = QTextBrowser()
        self.adres = QLineEdit()
        self.przejdz = QPushButton(u'Otwórz');
        self.zpliku = QPushButton(u'z pliku');
        self.zamknij = QPushButton(u'Zamknij');
        self.dodaj = QPushButton();
        self.dodaj.setIcon(QIcon("plus.png"))
        self.odsw = QPushButton();
        self.odsw.setIcon(QIcon("reload.png"));
        self.usun = QPushButton();
        self.usun.setIcon(QIcon("minus.png"))

        self.lista = QListWidget();
        
        
        
        
        
        for i in feedr().flist:

	  self.lista.addItem(i);


        
        layout = QVBoxLayout()
        linlayout = QHBoxLayout();
	linlayoutcont = QHBoxLayout();
        listlayout = QVBoxLayout();
	addrem = QHBoxLayout();

        	
        layout.addLayout(linlayout);
	layout.addLayout(linlayoutcont)

	linlayoutcont.addLayout(listlayout)

        linlayout.addWidget(self.zpliku)
        linlayout.addWidget(self.zamknij)
        linlayout.addWidget(self.adres)
        linlayout.addWidget(self.przejdz)
        
        self.lista.setMaximumWidth(200)
        listlayout.addWidget(self.lista)

        listlayout.addLayout(addrem)
        
        addrem.addWidget(self.dodaj);
        addrem.addWidget(self.odsw);
        addrem.addWidget(self.usun);

                
        linlayoutcont.addWidget(self.widok);



        
        
        self.setLayout(layout)
	self.setGeometry(400, 180, 600,500)
        self.setWindowTitle("RSS Squirrel")
        self.setWindowIcon(QIcon('ikonka.png'))

	self.connect(self.przejdz, SIGNAL("clicked()"), self.run)
	self.connect(self.zpliku, SIGNAL("clicked()"), self.filerss)
	self.connect(self.zamknij, SIGNAL("clicked()"), rsssq.quit)
	self.lista.itemActivated.connect(self.openfeed)
	self.connect(self.dodaj, SIGNAL("clicked()"), self.update_add)
	self.connect(self.usun, SIGNAL("clicked()"), self.update_rm)


    def openfeed(self, lista):
      self.run("feeds/"+lower(str(lista.text())).replace(" ", "")+".rss")

    def run(self, adr=None):
     
      try:

	if (adr == None):
	  x = nut(self.adres.text());
	else: x=nut(adr)

	self.widok.setText("<h1>"+x.frss.feed.title+"</h1>");
	i = 0;
	self.setWindowTitle(x.frss.feed.title+" | RSS Squirrel")
	for n in x.frss.entries:
	  self.widok.append("<h2>"+x.frss.entries[i].title+"</h2>");
	  self.widok.append("<i>"+x.frss.entries[i].published+"</i>");
	  self.widok.append(x.frss.entries[i].description);
	  i += 1

      except:
	self.widok.setText("<h1>"+u'Nie można załadować kanału rss'+"</h1>")
	self.setWindowTitle(u"Nie można załadować kanału rss | RSS Squirrel")
    def filerss(self):
       
       plik = QFileDialog.getOpenFileName(self, '', '.')
       self.run(plik);
    def update_add(self):
       dod = pop_ups.manage()
       zrodlo = urllib.urlopen(str(dod.adres.text()));
       cel = open(u"feeds/"+lower(str(dod.nazw.text())).replace(" ", "")+".rss", "w")
       cel.write(zrodlo.read())
       cel.close()
       
       self.lista.clear()
       for i in feedr().flist: self.lista.addItem(i);
       
    def update_rm(self):

    
       remove("feeds/"+lower(str(self.lista.selectedItems()[0].text()).replace(" ", ""))+".rss");

       feedr().feed_rm(str(self.lista.selectedItems()[0].text()));
       self.lista.clear()
       for i in feedr().flist: self.lista.addItem(i);
rsssq = QApplication(sys.argv)
rss_sq = rss_squirrel() #rss_sq = _rss_squirrel() #można przełączyć na tryb testowy
rss_sq.show()
rsssq.exec_()