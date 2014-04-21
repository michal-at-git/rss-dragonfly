#!/usr/bin/python
# coding: utf-8

from PyQt4.QtGui import *
from Feed import Feed;
from DB import DB;

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
   
  def add(self, feed, name, address):
    
    self.dbHandle.send('insert into feedList(name, addr, FeedTitle) values (\''+str(name)+'\',\''+str(address)+'\', \''+feed.feedTitle+'\')');
    
    size = (len(feed.title))-1;

    for i in range(0, size):
      self.dbHandle.send('insert into items(feed_id, title, pubDate, description) values ('+str(self.dbHandle.lastID())+',\''+feed.title[i].replace("'","&#39;")+'\', \''+feed.pubDate[i].replace("'","&#39;")+'\', \''+feed.description[i].replace("'","&#39;")+'\')');
    self.refresh();
    
  def remove(self, feed_id):
    self.dbHandle.send('delete from feedList where id='+str(self.feedListItems[feed_id]));
    self.dbHandle.send('delete from items where feed_id='+str(self.feedListItems[feed_id]));

    self.refresh();

  def getSingleSubscription(self, feed_id):
    feed = self.dbHandle.getSingleSubscription(self.feedListItems[feed_id]);
    return feed;

  def getSingleSubscriptionToHTML(self, feed_id):
    
    feed = self.dbHandle.getSingleSubscription(self.feedListItems[feed_id]);
    size = (len(feed['content']))-1;
    result = "";
    for i in range(0, size):
      result += """<article><h2>"""+feed['content'][i]['title']+"""</h2>
      <div class=\"pubDate\">"""+feed['content'][i]['pubDate']+"""</div>
      <div class=\"description\">"""+feed['content'][i]['description']+"""</div></article>
      """;
    return result;
    
  def updateAll(self, Feed, Source):
    print self.feedListItems;
    for feed_id in self.feedListItems:
      
      #deleting old feeds
      self.dbHandle.send('delete from items where feed_id='+str(feed_id));
      source = Source();

      feed_from_db = self.dbHandle.getSingleSubscription(feed_id);
      source = source.fromURL(str(feed_from_db['addr']));
      feed = Feed(source);
      size = (len(feed.title)-1);
    
      for i in range(0, size):
	self.dbHandle.send('insert into items(feed_id, title, pubDate, description) values ('+str(feed_id)+',\''+feed.title[i]+'\', \''+feed.pubDate[i]+'\', \''+feed.description[i]+'\')');
      
      
      
      
      
      
      
      
      
      
      
      
    
    #source = Source();
    #feed = Feed(source); 
    #this is featured method maybe for next release... ;/
    lastFeed = self.dbHandle.getLastSubscription(1); #NOT FINISHED!!!
    
    #size = (len(feed.title)-1);
    #print feed.title
    #for i in range(0, size):
      
      #print lastFeed['pubDate'];
      #print feed[i]['pubDate'];
      
      
    
      #if (5+5 == 10): #lastFeed['pubDate'] date > od higher than last from subscription     
	#self.dbHandle.send('insert into items(feed_id, title, pubDate, description) values...');
    
  
  #def update(self, feedId, feed):
    
    ##size = (len(feed.title)-1);
    #size = 2; #for test and demonstration
    #self.dbHandle.send('delete from items where feed_id='+str(feedId));
    
    ##for i in range(0, size):
      ##self.dbHandle.send('insert into items(feed_id, title, pubDate, description) values ('+str(feedId)+',\''+feed.title[i].replace("'","&#39;")+'\', \''+feed.pubDate[i].replace("'","&#39;")+'\', \''+feed.description[i].replace("'","&#39;")+'\')');
