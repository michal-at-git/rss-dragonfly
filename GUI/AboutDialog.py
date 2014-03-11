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
    about = """<p valign="middle"><img src="GUI/ikonka.png" alt="" /> <b>RSS Dragonfly 1.1</b></p>""";
    mainLayout = QVBoxLayout();
    mainLabel = QLabel(about);
    
    mainLayout.addWidget(mainLabel);
    self.setLayout(mainLayout);
    self.setWindowTitle("O RSS Dragonfly");