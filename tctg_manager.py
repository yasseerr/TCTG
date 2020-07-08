
from PySide2.QtCore import QObject,Signal,Slot

class TCTG_Manager(QObject):
    
    def __init__(self):
        QObject.__init__(self)
        self.nmbr= 0

    @Slot(str,str,result=str)
    def render(self, template,values):
        print(values)
        return "every thing is rendered dont worry"
