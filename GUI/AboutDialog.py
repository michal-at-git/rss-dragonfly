#!/usr/bin/python
# coding: utf-8

import sys;
reload(sys);
sys.setdefaultencoding("utf-8");

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AboutDialog(QDialog):
  def __init__(self, parent=None):
    super(AboutDialog, self).__init__(parent);
    about = """<p valign="middle"><img src="GUI/ikonka.png" alt="" /> <b>RSS Dragonfly 1.1 alpha</b></p>
    <p><b>Wykorzystane komponenty:</b></p>
    - <a href="http://www.riverbankcomputing.co.uk/software/pyqt/intro">PyQt4</a><br/>
    - <a href="https://pypi.python.org/pypi/pysqlite">PySQLite3</a><br/>
    - <a href="http://pycurl.sourceforge.net/">PycURL</a><br/>
    <p>Licencja: GPL v3 </p>
    <p>Strona projektu: <a href="http://michalt.pl/projekty/rss-dragonfly/">michalt.pl/projekty/rss-dragonfly/</a></p>""";
    mainLayout = QVBoxLayout();
    mainLabel = QLabel(about);
    
    mainLayout.addWidget(mainLabel);
    self.setLayout(mainLayout);
    self.setWindowTitle("O RSS Dragonfly");
    self.setMinimumWidth(400);
    self.setMaximumWidth(400);

    self.setMinimumHeight(300);
    self.setMaximumHeight(300);