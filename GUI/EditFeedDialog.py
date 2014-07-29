#!/usr/bin/python
# coding: utf-8

import sys;
reload(sys);
sys.setdefaultencoding("utf-8")


from PyQt4.QtGui import *
from PyQt4.QtCore import *

class EditFeedDialog(QDialog):
  def __init__(self, parent=None):
    super(EditFeedDialog, self).__init__(parent);
  

    self.name = QLineEdit();
    self.address = QLineEdit();
    self.save = QPushButton("Save");
    self.cancel = QPushButton("Cancel");
    
    mainLayout = QVBoxLayout();
    line1 = QHBoxLayout();
    line2 = QHBoxLayout();
    line3 = QHBoxLayout();
    
    nameLabel = QLabel("Name: ");
    addressLabel = QLabel("Address: ");
    
    
    mainLayout.addLayout(line1);
    mainLayout.addLayout(line2);
    mainLayout.addLayout(line3);
    
    line1.addWidget(nameLabel);
    line1.addWidget(self.name);
    line2.addWidget(addressLabel);
    line2.addWidget(self.address);
    
    line3.addWidget(self.save);
    line3.addWidget(self.cancel);
    
    self.connect(self.cancel, SIGNAL("clicked()"), self.close);

    self.setWindowIcon(QIcon('GUI/ikonka.png'));
    self.setLayout(mainLayout);
    self.setWindowTitle(u"Edit feed | "+self.name.text());
    self.setGeometry(400, 180, 350,80);
    self.setMaximumWidth(500);
    self.setMaximumHeight(100);
