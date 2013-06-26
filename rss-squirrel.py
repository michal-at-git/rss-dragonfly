#!/usr/bin/python
#-*- coding: utf-8 -*-


from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from feedparser import *


from feed_ruler import * #EXPERIMENTAL!!!!!!


class nut:
  def __init__(self, addr=None):
    
    self.addr = addr
    self.frss = parse(str(self.addr))  
    
    
    
    
    
class rss_squirrel(QDialog):
    def __init__(self, parent=None):
        super(rss_squirrel, self).__init__(parent)
        
        self.start();
        self.widok.setText("<h1>Witaj w RSS Squirrel!!!</h1>");
            

    def start(self):
      
        self.widok = QTextBrowser()
        self.adres = QLineEdit()
        self.przejdz = QPushButton(u'Otwórz');
        self.zpliku = QPushButton(u'z pliku');
        self.zamknij = QPushButton(u'Zamknij');
        self.lista = QListWidget();
        
        
        
        
        
        for i in feedr().flist:
	  
	  self.lista.addItem(i);
        
        
        
        
        
        
        
        #void itemClicked (QListWidgetItem *) // WAZNY SYGNAL
        
        
        layout = QVBoxLayout()
        linlayout = QHBoxLayout();
        linlayout2 = QHBoxLayout();

        
        layout.addLayout(linlayout);

        linlayout.addWidget(self.zpliku)
        linlayout.addWidget(self.zamknij)
        
        layout.addWidget(self.lista);
        layout.addWidget(self.widok);

        layout.addLayout(linlayout2);


        linlayout2.addWidget(self.adres)
        linlayout2.addWidget(self.przejdz)
        
        self.setLayout(layout)
	self.setGeometry(400, 300, 420,500)
        self.setWindowTitle("RSS Squirrel")
        self.setWindowIcon(QIcon('ikonka.png'))
	
	self.connect(self.przejdz, SIGNAL("clicked()"), self.run)
	self.connect(self.zpliku, SIGNAL("clicked()"), self.filerss)
	self.connect(self.zamknij, SIGNAL("clicked()"), rsssq.quit)

	
	
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
	  self.widok.append(x.frss.entries[i].description);
	  i += 1
	  
      except:
	self.widok.setText("<h1>"+u'Nie można załadować kanału rss'+"</h1>")
	
    def filerss(self):
       
       plik = getOpenFileName(self, '', '.')
       self.run(plik);
        
rsssq = QApplication(sys.argv)
rss_sq = rss_squirrel()
rss_sq.show()
rsssq.exec_()
