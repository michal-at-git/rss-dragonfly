#!/usr/bin/python
# coding: utf-8 

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from threading import *
import sys;
import time;
import json;
import urllib2 as urllib;
import sqlite3 as sqlite;

class Updater(QWidget):
  def __init__(self, parent=None):
    super(Updater, self).__init__(parent);
    desktop = QDesktopWidget();
    self.setGeometry(((desktop.geometry().width()/2)-190),  ((desktop.geometry().height()/2)-100),0,0);
    self.setFixedSize(380,200);
    self.setWindowTitle("RSS Dragonfly updater");
    self.info = QLabel("");
    self.mainLayout = QHBoxLayout();
    self.mainLayout.addWidget(self.info);
    self.setLayout(self.mainLayout);
    
    self.toUpdate = QObject();
    self.actual = QObject();
    self.checking = QObject();
    
    self.setWindowIcon(QIcon("GUI/reload.png"));
    
    
    self.checkForUpdatesMessage();
    #if(self.checkForUpdatesMessage()):
    #self.thr = Thread(target=self.newVersionAvaibleMessg).start();
    ##else:
    self.thr = Thread(target=self.checkForUpdates);
    self.thr.start();


    #self.connect(self.updateButton, SIGNAL("clicked()"), self.checkForUpdatesMessage);
    
    self.connect(self.toUpdate, SIGNAL("triggered()"), self.newVersionAvaibleMessg);
    self.connect(self.actual, SIGNAL("triggered()"), self.usingActualMessg);
    self.connect(self.checking, SIGNAL("triggered()"), self.checkForUpdatesMessage);
    self.info.setOpenExternalLinks(True)
   
  def checkForUpdates(self):
    self.checking.emit(SIGNAL("triggered()"));
    time.sleep(1);
    
    infoFile = urllib.build_opener();
    useragent = {'User-Agent':'RSS_DragonflyUpdater'}
    request = urllib.Request('http://rss-dragonfly.michalt.pl/update/update.json', None ,useragent)
    infoFile = infoFile.open(request);
    self.updateInfo = json.loads(infoFile.read());
    db = sqlite.connect('dragonfly.db');
    with db:
      db.row_factory = sqlite.Row      
      cursor = db.cursor();
      cursor.execute('select version from dragonfly');
      result = cursor.fetchall()[0][0];
    if result < self.updateInfo['current_version']:
      self.toUpdate.emit(SIGNAL("triggered()"));
    else:
      self.actual.emit(SIGNAL("triggered()"));

    
    
    
  def checkForUpdatesMessage(self):
    self.info.setText("checking for updates")



  def usingActualMessg(self):
    self.info.setText("You are using actual version of RSS Dragonfly");
    
  def newVersionAvaibleMessg(self):
    self.info.setText("RSS Dragonfly "+str(self.updateInfo['current_version'])+" is avaible<br/> <a href=\""+self.updateInfo['update_link']+"\">download</a>");


  
  def runRSSDragonfly(self):
    import os;
    os.system("./rss-dragonfly.py")








app = QApplication(sys.argv)

updater = Updater();
updater.show();
app.exec_();