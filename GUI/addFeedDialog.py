#!/usr/bin/python
# coding: utf-8

import sys;
reload(sys);
sys.setdefaultencoding("utf-8")


from PyQt4.QtGui import *
from PyQt4.QtCore import *

class addFeedDialog(QDialog):
  def __init__(self, parent=None):
    super(addFeedDialog, self).__init__(parent);
  

    self.name = QLineEdit();
    self.address = QLineEdit();
    self.send = QPushButton("Dodaj");
    self.cancel = QPushButton("Anuluj");
    
    mainLayout = QVBoxLayout();
    line1 = QHBoxLayout();
    line2 = QHBoxLayout();
    line3 = QHBoxLayout();
    
    nameLabel = QLabel("Nazwa: ");
    addressLabel = QLabel("Adres: ");
    
    
    mainLayout.addLayout(line1);
    mainLayout.addLayout(line2);
    mainLayout.addLayout(line3);
    
    line1.addWidget(nameLabel);
    line1.addWidget(self.name);
    line2.addWidget(addressLabel);
    line2.addWidget(self.address);
    
    line3.addWidget(self.send);
    line3.addWidget(self.cancel);
    

    self.setLayout(mainLayout);
    self.setWindowTitle(u"Dodaj nowy kanał RSS");
    self.setGeometry(400, 180, 350,80);
