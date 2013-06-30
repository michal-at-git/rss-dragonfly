#!/usr/bin/python
#-*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from feed_ruler import *

class manage(QDialog):   
    def __init__(self, parent=None):
        super(manage, self).__init__(parent)
        
        core = QVBoxLayout();
        ch1 = QHBoxLayout()
        ch2 = QHBoxLayout();
        
        core.addLayout(ch1)
        core.addLayout(ch2)
        
        
        self.nazw = QLineEdit();
	self.adres = QLineEdit();
        
        labnaz = QLabel("Nazwa: ");
        labadr = QLabel("Adres: ");
        
        self.add = QPushButton("Dodaj");
        self.add.setFixedWidth(80)
        
        labadr.setFixedWidth(60)
        labnaz.setFixedWidth(60)
	self.nazw.setFixedWidth(200)
        self.adres.setFixedWidth(200)
        
        ch1.addWidget(labnaz)
        ch1.addWidget(self.nazw)
        
        ch2.addWidget(labadr)
        ch2.addWidget(self.adres)
        core.addWidget(self.add);
        
	self.setLayout(core)
	self.setWindowTitle(u"Dodaj nowy kanał RSS");
        self.setWindowIcon(QIcon('ikonka.png'))
	self.connect(self.add, SIGNAL("clicked()"), self.dodaj)
	self.exec_()

	
    def dodaj(self):
	test = feedr();
	test.feed_add(str(self.nazw.text()), str(self.nazw.text()))

	#c.feed_add("...", "http://")
	self.close();
	return True
