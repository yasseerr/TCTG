# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine,QQmlContext,qmlRegisterType
from PySide2.QtCore import QObject

from tctg_manager import TCTG_Manager

import resources

#deployment configuration
#https://stackoverflow.com/questions/58035550/pyinstaller-and-qml-files
# application_path = (
#     sys._MEIPASS
#     if getattr(sys, "frozen", False)
#     else os.path.dirname(os.path.abspath(__file__))
# )

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    qmlRegisterType(TCTG_Manager, "TCTG", 1, 0, "TCTG_Manager")
    engine = QQmlApplicationEngine()
    #engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))
    engine.load("qrc:/main.qml")
    engine.rootContext()

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
