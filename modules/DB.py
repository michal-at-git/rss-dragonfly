#!/usr/bin/python
# coding: utf-8

import sqlite3 as sqlite

class DB:
  def __init__(self):
    self.dbHandle = sqlite.connect('dragonfly.db');
    with self.dbHandle:
      self.dbHandle.row_factory = sqlite.Row      
      self.cursor = self.dbHandle.cursor();
      
      
  def send(self, query):
    self.cursor.execute(query);
    self.dbHandle.commit();
  def getFeedList(self):
    self.cursor.execute('select * from feedList');
    raw = self.cursor.fetchall();
    
    i=0
    results = [];
    for n in raw:
      results.append({'id' : n[0], 'name' : n[1], 'addr' : n[2]});    
      i += 1;
      
    return results;
    
  def getSingleFeed(self, feedId):
    self.cursor.execute('select * from feedList where id='+str(feedId));
    n = self.cursor.fetchall();
    
    return {'id' : n[0][0], 'name' : n[0][1], 'addr' : n[0][2], 'src':n[0][3]};    
