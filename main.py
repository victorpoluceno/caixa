import sys

import SimpleHTTPServer
import SocketServer

import threading 

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *


PORT = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
t = threading.Thread(target=httpd.serve_forever)
t.start()

app = QApplication(sys.argv)
web = QWebView()
web.load(QUrl("http://localhost:8000/index.html"))
web.show()
sys.exit(app.exec_())

t.join()
