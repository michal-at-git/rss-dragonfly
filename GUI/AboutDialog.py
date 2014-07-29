#!/usr/bin/python
# coding: utf-8

import sys;
import gpl;
reload(sys);
sys.setdefaultencoding("utf-8");

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AboutDialog(QDialog):
  def __init__(self, parent=None):
    super(AboutDialog, self).__init__(parent);
    tabs = QTabWidget();
    license = QTextBrowser();
    license.setText(gpl.license);
    self.closeButton = QPushButton("Close");
    self.closeButton.setFixedWidth(100);
    
    
    header = """<img src="GUI/ikonka.png" alt="" style="float: left" /> <p style="float: left; margin: 4px"><b>RSS Dragonfly version 1.2 (alpha)</b></p> 
    <p style="float: left; margin: 4px">(c) 2013-2014</p>""";
    
    about = """<p><b>Used modules:</b></p>
    - <a href="http://www.riverbankcomputing.co.uk/software/pyqt/intro">PyQt4</a><br/>
    - <a href="https://pypi.python.org/pypi/pysqlite">PySQLite3</a><br/>
    - <a href="http://pycurl.sourceforge.net/">PycURL</a><br/>
    - <a href="https://pypi.python.org/pypi/feedparser">Feedparser</a><br/>
    <p><b>Your Qt version:</b> """+QT_VERSION_STR+"""</p>
    <p>RSS Dragonfly website: <a href="http://rss-dragonfly.michalt.pl/">http://rss-dragonfly.michalt.pl/</a></p>
    """;
    
    headerLabel = QLabel(header);

    
    mainLayout = QVBoxLayout();
    aboutLabel = QLabel(about);
    aboutLabel.setMargin(15);
    aboutLabel.setOpenExternalLinks(True);
    tabs.addTab(aboutLabel, "About...");
    tabs.addTab(license, "License");
    headerLabel.setFixedHeight(80);
    mainLayout.addWidget(headerLabel);
    mainLayout.addWidget(tabs);
    mainLayout.addWidget(self.closeButton, 0, Qt.AlignRight);
    self.setLayout(mainLayout);
    
   
    self.setWindowIcon(QIcon('GUI/ikonka.png'));    
    self.setWindowTitle("About RSS Dragonfly");

    self.setFixedSize(430, 390);
