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
        ch3 = QHBoxLayout();
        
        core.addLayout(ch1)
        core.addLayout(ch2)
        core.addLayout(ch3)

        
        self.nazw = QLineEdit();
	self.adres = QLineEdit();
        
        labnaz = QLabel("Nazwa: ");
        labadr = QLabel("Adres: ");
        
        self.add = QPushButton("Dodaj");
        self.cancel = QPushButton("Anuluj");
        
        self.add.setFixedWidth(80)
        self.cancel.setFixedWidth(90)
        
        labadr.setFixedWidth(60)
        labnaz.setFixedWidth(60)
	self.nazw.setFixedWidth(200)
        self.adres.setFixedWidth(200)
        
        ch1.addWidget(labnaz)
        ch1.addWidget(self.nazw)
        
        ch2.addWidget(labadr)
        ch2.addWidget(self.adres)
        ch3.addWidget(self.add);
        ch3.addWidget(self.cancel)
        
	self.setLayout(core)
	self.setWindowTitle(u"Dodaj nowy kanał RSS");
        self.setWindowIcon(QIcon('ikonka.png'))
	self.connect(self.add, SIGNAL("clicked()"), self.dodaj)
	self.connect(self.cancel, SIGNAL("clicked()"), self.close)

	self.exec_()


    def dodaj(self):
	test = feedr();
	test.feed_add(str(unicode(self.nazw.text())), str(self.adres.text()))

	#c.feed_add("...", "http://")
	self.close();
	return True
	