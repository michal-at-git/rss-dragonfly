#!/usr/bin/python
# coding: utf-8

class Settings:
  def __init__(self, dbHandle):
    self.db = dbHandle;
    
    
  
  
  def currentSettings(self):
    res = self.db.getSingleRow('settings');
    
    return {'theme' : res[1], 'startup' : res[2], 'startMinimalized' : res[3]}
    
  def saveSettings(self, settingsToken):
    query = 'update settings set theme = '+str(settingsToken['theme'])+', startUpdate = '+str(settingsToken['startup']) + ', startMinimalized = '+str(settingsToken['startMinimalized']) + ' where id = 1';
    self.db.send(query);