#!/usr/bin/python

# coding: utf-8

import sys;
reload(sys);
sys.setdefaultencoding("utf-8")


from PyQt4.QtGui import *
from PyQt4.QtCore import *

class SettingsDialog(QDialog):
  def __init__(self, prefToken, parent=None):
    super(SettingsDialog, self).__init__(parent);

    
    
    self.closeButton = QPushButton("Close");
    self.saveButton = QPushButton("Save");
    self.themeLabel = QLabel("Theme: ");
    self.themeOptions = QComboBox();
    self.themeOptions.addItems(["standard", "lemon", "violet", "summer", "mono"]);
    self.themeOptions.setCurrentIndex(prefToken['theme']);

    
    self.startUpLabel = QLabel("Update feeds at startup <i>(slow start)</i>: ");
    self.startUpCheckBox = QCheckBox();
    self.startMinimalizedLabel = QLabel("Start minimalized: ");
    self.startMinimalizedCheckBox = QCheckBox();

 
    self.startUpCheckBox.setChecked(prefToken["startup"]);
    self.startMinimalizedCheckBox.setChecked(prefToken["startMinimalized"]);
   
    
    
 
    
    self.connect(self.closeButton, SIGNAL("clicked()"), self.close);
    
    
    self.mainLayout = QVBoxLayout();
    self.headerLayout = QHBoxLayout();
    self.line1Layout = QHBoxLayout();
    self.line2Layout = QHBoxLayout();
    self.line3Layout = QHBoxLayout();

    self.footerLayout = QHBoxLayout();
    
    self.header = QLabel("<h1>Settings</h1>");
   
    
    
    self.headerLayout.addWidget(self.header);
    
    self.line1Layout.addWidget(self.themeLabel);
    self.line1Layout.addWidget(self.themeOptions, 0, Qt.AlignRight);

    self.line2Layout.addWidget(self.startUpLabel);
    self.line2Layout.addWidget(self.startUpCheckBox, 0, Qt.AlignRight);    
    
    
    
    self.line3Layout.addWidget(self.startMinimalizedLabel);
    self.line3Layout.addWidget(self.startMinimalizedCheckBox, 0, Qt.AlignRight);       
    
    
    
    self.footerLayout.addWidget(self.saveButton);    
    self.footerLayout.addWidget(self.closeButton);
    
    
    self.mainLayout.addLayout(self.headerLayout); 
    self.mainLayout.addLayout(self.line1Layout);
    self.mainLayout.addLayout(self.line2Layout);
    self.mainLayout.addLayout(self.line3Layout);   
    self.mainLayout.addLayout(self.footerLayout);
  
    
    
    self.setLayout(self.mainLayout);

    self.setWindowTitle("Settings");
    self.setFixedSize(420, 170);


  def getSettingsArray(self):
    checkBox = {2 : 1, 0 : 0};
    theme = self.themeOptions.currentIndex();
    startup = checkBox[self.startUpCheckBox.checkState()];
    startMinimalized = checkBox[self.startMinimalizedCheckBox.checkState()];
    
    return {'theme' : theme, 'startup' : startup, 'startMinimalized' : startMinimalized}