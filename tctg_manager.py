
from PySide2.QtCore import QObject,Signal,Slot

import yaml
from yaml.error import YAMLError
from jinja2 import Environment, PackageLoader, select_autoescape,Template,TemplateError

#jinjaEnv = Environment()

class TCTG_Manager(QObject):

    templateError = Signal()
    yamlError = Signal()
    
    def __init__(self):
        QObject.__init__(self)
        self.nmbr= 0

    @Slot(str,str,result=str)
    def render(self, template_str,values):
        valuesDict = dict()
        try:
            valuesDict = yaml.load(values)
            print(valuesDict)
        except YAMLError as e :
            self.yamlError.emit()
            return str(e)

        rendered = "nothing rendered"
        try:
            the_template = Template(template_str)
            rendered  = the_template.render(valuesDict)
            print(rendered)
        except Exception as e:
            self.templateError.emit()
            return str(e)
        print(values)
        return rendered
        #return "every thing is rendered dont worry"
