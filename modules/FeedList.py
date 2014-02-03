#!/usr/bin/python
# coding: utf-8

from PyQt4.QtGui import *

class FeedList(QWidget):
  def __init__(self, feedListWidget, dbHandle):
    self.feedListWidget = feedListWidget;
    self.dbHandle = dbHandle;
    self.refresh();
  def refresh(self):
    itemlist = self.dbHandle.getFeedList();
    
    for item in itemlist:
      self.feedListWidget.addItem(item['name']);
    
