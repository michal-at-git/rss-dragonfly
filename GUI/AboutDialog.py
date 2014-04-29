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
    self.closeButton = QPushButton("Zamknij");
    self.closeButton.setFixedWidth(100);
    
    
    header = """<img src="GUI/ikonka.png" alt="" style="float: left" /> <p style="float: left; margin: 4px"><b>RSS Dragonfly wersja 1.1 beta</b></p> 
    <p style="float: left; margin: 4px">(c) 2013-2014</p>""";
    
    about = """<p><b>Wykorzystane komponenty:</b></p>
    - <a href="http://www.riverbankcomputing.co.uk/software/pyqt/intro">PyQt4</a><br/>
    - <a href="https://pypi.python.org/pypi/pysqlite">PySQLite3</a><br/>
    - <a href="http://pycurl.sourceforge.net/">PycURL</a><br/>
    <p>Strona projektu: <a href="http://michalt.pl/projekty/rss-dragonfly/">michalt.pl/projekty/rss-dragonfly/</a></p>""";
    
    headerLabel = QLabel(header);

    
    mainLayout = QVBoxLayout();
    aboutLabel = QLabel(about);
    aboutLabel.setMargin(15);
    tabs.addTab(aboutLabel, "O programie");
    tabs.addTab(license, "Licencja");
    headerLabel.setFixedHeight(80);
    mainLayout.addWidget(headerLabel);
    mainLayout.addWidget(tabs);
    mainLayout.addWidget(self.closeButton, 0, Qt.AlignRight);
    self.setLayout(mainLayout);
    
   
    
    self.setWindowTitle("O RSS Dragonfly");

    self.setFixedSize(430, 390);
