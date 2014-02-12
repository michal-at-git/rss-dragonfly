#!/usr/bin/python
# coding: utf-8

from PyQt4.QtGui import *
from Feed import Feed;

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
   
  def add(self, name, url, source):
    
    self.dbHandle.send('insert into feedList(name, addr, content) values (\''+name+'\',\''+url+'\', \''+source+'\')');
    self.refresh();
  
  def read(self,feedId):
    res = self.dbHandle.getSingleFeed(self.feedListItems[feedId]);
    return res;
    
  def remove(self, feed_id):
    self.dbHandle.send('delete from feedList where id='+str(self.feedListItems[feed_id]));
   
    self.refresh();
    
  
