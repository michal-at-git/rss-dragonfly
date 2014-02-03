#!/usr/bin/python
# coding: utf-8

import sqlite3 as sqlite

class db:
  def __init__(self):
    self.dbHandle = sqlite.connect('dragonfly.db');
    with self.dbHandle:
      self.dbHandle.row_factory = sqlite.Row      
      self.cursor = self.dbHandle.cursor();
      
      
  def send(self, query):
    self.cursor.execute(query);
      
  def getFeedList(self):
    self.cursor.execute('select * from feedList');
    raw = self.cursor.fetchall();
    
    i=0
    results = [];
    for n in raw:
      results.append({'id' : n[0], 'name' : n[1], 'addr' : n[2]});    
      i += 1;
      
    return results;