# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtQuick


class EditorManager(QObject):
    def __init__(self):
        self.templateText = ""
        self.valuesText = ""

