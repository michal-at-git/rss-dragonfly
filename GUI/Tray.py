#!/usr/bin/python

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore;

class Tray(QObject):
  

      
      
  def __init__(self,window,qapp, parent=None):
    super(Tray, self).__init__(parent);
    self.visible = True;
    self.window = window;
    self.tray = QSystemTrayIcon(QIcon("GUI/ikonka.png"), self.window);

    self.quitOption = QObject();
    self.updateAllOption = QObject();
    self.settingsOption = QObject();
    
    
    self.updateAllAction = QAction("&Update all feeds", self.updateAllOption); 
    self.settingsAction = QAction("Se&ttings", self.settingsOption);    
    self.quitAction = QAction("Quit", self.quitOption);
    
    
    self.trayMenu = QMenu();
    self.trayMenu.addAction(self.updateAllAction);
    self.trayMenu.addAction(self.settingsAction);
    self.trayMenu.addAction(self.quitAction);
    
    self.connect(self.quitAction, SIGNAL("triggered()"), self.close);
    self.connect(self.updateAllAction, SIGNAL("triggered()"), self.updateAll);
    self.connect(self.settingsAction, SIGNAL("triggered()"), self.settings);
    self.connect(self.tray, SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), self.iconActivated)

    
    self.tray.setContextMenu(self.trayMenu);
        
    self.tray.show();


 
    
  def close(self):
    self.window.quit();
    
  def settings(self):
    self.window.displaySettings();
    
  def updateAll(self):
    self.window.updateAllFeeds();
  
  
  def minimalization(self):
    if(self.visible):
      self.window.hide();
      self.visible = False;
    else:
      self.window.show();
      self.visible = True;
      
  def iconActivated(self, reason):
    if(reason == QSystemTrayIcon.Trigger):
      self.minimalization();
  def message(self,title, message):
    self.tray.showMessage(title, message, 10000);