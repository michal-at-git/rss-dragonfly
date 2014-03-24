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
      self.cursor.execute('select * from items where feed_id='+str(n[0]));
      n2 = self.cursor.fetchall();
      feeds = [];
      for x in n2:
	feeds.append({'id':x[0], 'feed_id':x[1], 'title':x[2], 'pubDate':x[3], 'description':x[4] });
	
      results.append({'id' : n[0], 'name' : n[1], 'addr' : n[2],'FeedTitle':n[3], 'content':feeds});    
      i += 1;
      
    return results;
    
  def getSingleSubscription(self, feedId):
    self.cursor.execute('select * from feedList where id='+str(feedId));
    n = self.cursor.fetchall();
    
    self.cursor.execute('select * from items where feed_id='+str(feedId));
    n2 = self.cursor.fetchall();
    feeds = [];
    for x in n2:
      feeds.append({'id':x[0], 'feed_id':x[1], 'title':x[2], 'pubDate':x[3], 'description':x[4] });
    
    return {'id' : n[0][0], 'name' : n[0][1], 'addr' : n[0][2], 'FeedTitle':n[0][3], 'content':feeds};  
    
    
  def getLastSubscription(self, feedId):
    #self.cursor.execute('select * from feedList where id='+str(feedId));
    #n = self.cursor.fetchall();
    
    self.cursor.execute('select * from items where feed_id='+feedId+' order by id asc limit 1');
    n2 = self.cursor.fetchall();
    feeds = False;
    for x in n2:
      feeds = {'id':x[0], 'feed_id':x[1], 'title':x[2], 'pubDate':x[3], 'description':x[4] };
    
    return feeds;    
    
    
    
  def lastID(self):
    self.cursor.execute('select id from feedList order by id desc');
    res = self.cursor.fetchall();
    
    return res[0][0];

    
