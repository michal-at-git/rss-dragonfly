#!/usr/bin/python
# coding: utf-8

from PyQt4.QtGui import *

class FeedList():
  def __init__(self, feedListWidget, dbHandle):
    self.feedListWidget = feedListWidget;
    self.dbHandle = dbHandle;
    self.refresh();
    
  def refresh(self):
    self.feedListWidget.clear();
    self.feedListItems = [];
    
    itemlist = self.dbHandle.getFeedList();
    for item in itemlist:
      self.feedListWidget.addItem(item['name']);
      self.feedListItems.append(item['id']);
   
  def add(self, name, url):
    self.dbHandle.send('insert into feedList(name, addr) values (\''+name+'\',\''+url+'\')');
    self.refresh();
    
  def remove(self, feed_id):
    self.dbHandle.send('delete from feedList where id='+str(self.feedListItems[feed_id]));
   
    self.refresh();
