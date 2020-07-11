# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Sat Jul 11 13:40:47 2020
#      by: The Resource Compiler for PySide2 (Qt v5.12.1)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x03\xdc\
i\
mport QtQuick 2.\
0\x0d\x0aimport QtQuic\
k.Controls 2.12\x0d\
\x0a\x0d\x0aItem {\x0d\x0a    p\
roperty alias cu\
rrentText: textA\
rea.text\x0d\x0a    vi\
sible: true\x0d\x0a   \
 clip: true\x0d\x0a   \
 Rectangle{\x0d\x0a   \
     anchors.fil\
l: parent\x0d\x0a     \
   //color: Qt.l\
ightGray\x0d\x0a      \
  border.color: \
\x22black\x22\x0d\x0a       \
 border.width: 1\
\x0d\x0a    }\x0d\x0a\x0d\x0a    F\
lickable {\x0d\x0a    \
    id: scrollVi\
ew\x0d\x0a        flic\
kableDirection: \
Flickable.Vertic\
alFlick\x0d\x0a       \
 anchors.fill: p\
arent\x0d\x0a        T\
extArea.flickabl\
e: TextArea {\x0d\x0a \
           id: t\
extArea\x0d\x0a       \
     anchors.fil\
l: parent\x0d\x0a     \
       selectByM\
ouse: true\x0d\x0a    \
        selectBy\
Keyboard: true\x0d\x0a\
            font\
.pixelSize: 15\x0d\x0a\
            text\
: \x22the name is :\
 {{name}} \x5cn the\
 children are : \
\x5cn{%for child in\
 childes%}\x5cn ano\
ther one : {{chi\
ld}} {%endfor%}\x22\
\x0d\x0a        }\x0d\x0a   \
     ScrollBar.v\
ertical: ScrollB\
ar{}\x0d\x0a    }\x0d\x0a\x0d\x0a \
   function load\
Text(t){\x0d\x0a      \
  textArea.text \
= t\x0d\x0a    }\x0d\x0a\x0d\x0a\x0d\x0a\
}\x0d\x0a\x0d\x0a/*##^##\x0d\x0aDe\
signer {\x0d\x0a    D{\
i:0;autoSize:tru\
e;height:480;wid\
th:640}D{i:1}D{i\
:3;anchors_x:73;\
anchors_y:28}\x0d\x0a}\
\x0d\x0a##^##*/\x0d\x0a\
\x00\x00\x1a\xce\
i\
mport QtQuick 2.\
12\x0d\x0aimport QtQui\
ck.Window 2.12\x0d\x0a\
import QtQuick.L\
ayouts 1.3\x0d\x0aimpo\
rt QtQuick.Contr\
ols 2.12\x0d\x0aimport\
 QtQuick.Dialogs\
 1.0\x0d\x0aimport TCT\
G 1.0\x0d\x0a\x0d\x0aApplica\
tionWindow {\x0d\x0a  \
  id: mainWindow\
\x0d\x0a    title: qsT\
r(\x22Hello World\x22)\
\x0d\x0a    width: 128\
0\x0d\x0a    height: 9\
60\x0d\x0a    visible:\
 true\x0d\x0a    menuB\
ar: MenuBar{\x0d\x0a\x0d\x0a\
        Menu {\x0d\x0a\
            titl\
e: qsTr(\x22&File\x22)\
\x0d\x0a            Ac\
tion { text: qsT\
r(\x22&New...\x22) }\x0d\x0a\
            Acti\
on {\x0d\x0a          \
      id: openSt\
ateAction\x0d\x0a     \
           text:\
 qsTr(\x22&Open Sta\
te...\x22)\x0d\x0a       \
         shortcu\
t: StandardKey.O\
pen\x0d\x0a           \
     onTriggered\
: {\x0d\x0a           \
         openSta\
teFileDialog.ope\
n()\x0d\x0a           \
     }\x0d\x0a        \
    }\x0d\x0a         \
   Action {\x0d\x0a   \
             id:\
 saveStateAction\
\x0d\x0a              \
  text: qsTr(\x22&S\
ave State\x22)\x0d\x0a   \
             sho\
rtcut: StandardK\
ey.Save\x0d\x0a       \
         onTrigg\
ered: {\x0d\x0a       \
             sav\
eStateFileDialog\
.open()\x0d\x0a       \
         }\x0d\x0a    \
        }\x0d\x0a     \
       Action { \
text: qsTr(\x22&Sav\
e Template\x22) }\x0d\x0a\
            Acti\
on { text: qsTr(\
\x22&Save Values\x22) \
}\x0d\x0a            A\
ction { text: qs\
Tr(\x22Save &As...\x22\
) }\x0d\x0a           \
 MenuSeparator {\
 }\x0d\x0a            \
Action { text: q\
sTr(\x22&Quit\x22) }\x0d\x0a\
        }\x0d\x0a     \
   Menu {\x0d\x0a     \
       title: qs\
Tr(\x22&Edit\x22)\x0d\x0a   \
         Action \
{ text: qsTr(\x22Cu\
&t\x22) }\x0d\x0a        \
    Action { tex\
t: qsTr(\x22&Copy\x22)\
 }\x0d\x0a            \
Action { text: q\
sTr(\x22&Paste\x22) }\x0d\
\x0a            Act\
ion { text: qsTr\
(\x22&Copy Results\x22\
) }\x0d\x0a        }\x0d\x0a\
        Menu {\x0d\x0a\
            titl\
e: qsTr(\x22&Tools\x22\
)\x0d\x0a            A\
ction { text: qs\
Tr(\x22&Render\x22) }\x0d\
\x0a            Act\
ion { text: qsTr\
(\x22&Clear\x22) }\x0d\x0a  \
          //Acti\
on { text: qsTr(\
\x22&Paste\x22) }\x0d\x0a   \
         //Actio\
n { text: qsTr(\x22\
&Copy Results\x22) \
}\x0d\x0a        }\x0d\x0a  \
      Menu {\x0d\x0a  \
          title:\
 qsTr(\x22&Help\x22)\x0d\x0a\
            Acti\
on { text: qsTr(\
\x22&About\x22) }\x0d\x0a   \
     }\x0d\x0a    }\x0d\x0a\x0d\
\x0a    GridLayout \
{\x0d\x0a        id: g\
ridLayout\x0d\x0a     \
   anchors.fill:\
 parent\x0d\x0a\x0d\x0a     \
   TemplateEdito\
r {\x0d\x0a           \
 id: templateEdi\
tor\x0d\x0a           \
 Layout.fillWidt\
h: true\x0d\x0a       \
     Layout.fill\
Height: true\x0d\x0a  \
          Layout\
.preferredHeight\
: 100;\x0d\x0a        \
    Layout.prefe\
rredWidth: 100;\x0d\
\x0a        }\x0d\x0a\x0d\x0a  \
      ValuesEdit\
or {\x0d\x0a          \
  id: valuesEdit\
or\x0d\x0a            \
//placeholderTex\
t: \x22#yaml text\x22\x0d\
\x0a            Lay\
out.fillWidth: t\
rue\x0d\x0a           \
 Layout.fillHeig\
ht: true\x0d\x0a      \
      Layout.pre\
ferredHeight: 10\
0;\x0d\x0a            \
Layout.preferred\
Width: 100;\x0d\x0a   \
     }\x0d\x0a\x0d\x0a      \
  ResultsView {\x0d\
\x0a            id:\
 results\x0d\x0a      \
      Layout.pre\
ferredHeight: 10\
0\x0d\x0a            L\
ayout.preferredW\
idth: 100\x0d\x0a     \
       Layout.fi\
llHeight: true\x0d\x0a\
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
Layout.column: 0\
\x0d\x0a            La\
yout.row: 1\x0d\x0a   \
     }\x0d\x0a\x0d\x0a      \
  GridLayout {\x0d\x0a\
            id: \
gridLayout1\x0d\x0a   \
         Layout.\
topMargin: 0\x0d\x0a  \
          Layout\
.leftMargin: 0\x0d\x0a\
            colu\
mns: 2\x0d\x0a        \
    Layout.align\
ment: Qt.AlignLe\
ft | Qt.AlignTop\
\x0d\x0a            La\
yout.preferredHe\
ight: 100\x0d\x0a     \
       Layout.pr\
eferredWidth: 10\
0\x0d\x0a            L\
ayout.fillHeight\
: true\x0d\x0a        \
    Layout.fillW\
idth: true\x0d\x0a\x0d\x0a  \
          Button\
 {\x0d\x0a            \
    id: renderBu\
tton\x0d\x0a          \
      text: qsTr\
(\x22Render\x22)\x0d\x0a    \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
    flat: false\x0d\
\x0a               \
 onClicked: {\x0d\x0a \
                \
   //results.res\
ult = \x22it should\
 be added \x22\x0d\x0a   \
                \
 results.result \
=  manager1.rend\
er(templateEdito\
r.currentText,va\
luesEditor.curre\
ntText)\x0d\x0a       \
         }\x0d\x0a    \
        }\x0d\x0a\x0d\x0a   \
         Button \
{\x0d\x0a             \
   id: clearButt\
on\x0d\x0a            \
    text: qsTr(\x22\
Clear\x22)\x0d\x0a       \
         Layout.\
fillWidth: true\x0d\
\x0a               \
 Layout.column: \
0\x0d\x0a             \
   Layout.row: 1\
\x0d\x0a              \
  onClicked: {\x0d\x0a\
                \
    //TODO add t\
he support for h\
tml highlighting\
\x0d\x0a              \
      var the_co\
de = valuesEdito\
r.getPlainText()\
;\x0d\x0a             \
       console.l\
og(the_code)\x0d\x0a  \
                \
   valuesEditor.\
updateHighlighti\
ng(manager1.high\
lightCode(the_co\
de,\x22YAML\x22))\x0d\x0a   \
             }\x0d\x0a\
            }\x0d\x0a \
           Butto\
n {\x0d\x0a           \
     id: saveTem\
plateButton\x0d\x0a   \
             tex\
t: qsTr(\x22Save Te\
mplate\x22)\x0d\x0a      \
          Layout\
.fillWidth: true\
\x0d\x0a              \
  Layout.column:\
 0\x0d\x0a            \
    Layout.row: \
2\x0d\x0a            }\
\x0d\x0a\x0d\x0a            \
Button {\x0d\x0a      \
          id: sa\
veValuesButton\x0d\x0a\
                \
text: qsTr(\x22Save\
 Values\x22)\x0d\x0a     \
           Layou\
t.fillWidth: tru\
e\x0d\x0a             \
   Layout.column\
: 0\x0d\x0a           \
     Layout.row:\
 3\x0d\x0a            \
}\x0d\x0a\x0d\x0a           \
 Button {\x0d\x0a     \
           id: c\
opyResultsButton\
\x0d\x0a              \
  text: qsTr(\x22Co\
py Results\x22)\x0d\x0a  \
              La\
yout.fillWidth: \
true\x0d\x0a          \
      Layout.col\
umn: 0\x0d\x0a        \
        Layout.r\
ow: 4\x0d\x0a         \
   }\x0d\x0a\x0d\x0a        \
    RoundButton \
{\x0d\x0a             \
   id: saveState\
Button\x0d\x0a        \
        text: qs\
Tr(\x22Save State\x22)\
\x0d\x0a              \
  Layout.fillWid\
th: true\x0d\x0a      \
          Layout\
.column: 0\x0d\x0a    \
            Layo\
ut.row: 5\x0d\x0a     \
           actio\
n: saveStateActi\
on\x0d\x0a\x0d\x0a          \
  }\x0d\x0a\x0d\x0a\x0d\x0a       \
     Item {\x0d\x0a   \
             id:\
 spacer1\x0d\x0a      \
          Layout\
.preferredWidth:\
 300\x0d\x0a          \
      Layout.fil\
lWidth: true\x0d\x0a  \
              La\
yout.column: 1\x0d\x0a\
                \
Layout.row: 0\x0d\x0a \
               L\
ayout.rowSpan: 2\
\x0d\x0a            }\x0d\
\x0a\x0d\x0a        }\x0d\x0a\x0d\x0a\
    }\x0d\x0a    Compo\
nent.onCompleted\
: {\x0d\x0a        mai\
nWindow.setTitle\
(\x22TCTG\x22)\x0d\x0a      \
  gridLayout.anc\
hors.margins = 1\
0\x0d\x0a    }\x0d\x0a\x0d\x0a    \
FileDialog {\x0d\x0a  \
      id: saveSt\
ateFileDialog\x0d\x0a \
       title: \x22P\
lease choose a f\
ile to save the \
state\x22\x0d\x0a        \
folder: shortcut\
s.home\x0d\x0a        \
selectExisting: \
false\x0d\x0a        m\
odality: Qt.Appl\
icationModal\x0d\x0a  \
      onAccepted\
: {\x0d\x0a           \
 console.log(\x22Yo\
u chose: \x22 + sav\
eStateFileDialog\
.fileUrls)\x0d\x0a    \
        manager1\
.saveState(templ\
ateEditor.curren\
tText,valuesEdit\
or.currentText,f\
ileUrl)\x0d\x0a       \
     //Qt.quit()\
\x0d\x0a        }\x0d\x0a   \
     onRejected:\
 {\x0d\x0a            \
console.log(\x22Can\
celed\x22)\x0d\x0a       \
     //Qt.quit()\
\x0d\x0a            ex\
itedProperly = f\
alse\x0d\x0a        }\x0d\
\x0a        //Compo\
nent.onCompleted\
: visible = true\
\x0d\x0a    }\x0d\x0a\x0d\x0a    F\
ileDialog {\x0d\x0a   \
     id: openSta\
teFileDialog\x0d\x0a  \
      title: \x22Pl\
ease choose a fi\
le to save the s\
tate\x22\x0d\x0a        f\
older: shortcuts\
.home\x0d\x0a        s\
electExisting: t\
rue\x0d\x0a        mod\
ality: Qt.Applic\
ationModal\x0d\x0a    \
    onAccepted: \
{\x0d\x0a            c\
onsole.log(\x22You \
chose: \x22 + saveS\
tateFileDialog.f\
ileUrls)\x0d\x0a      \
      var retLis\
t = manager1.ope\
nState(fileUrl)\x0d\
\x0a            tem\
plateEditor.load\
Text(retList[0])\
\x0d\x0a            va\
luesEditor.loadT\
ext(retList[1])\x0d\
\x0a            //Q\
t.quit()\x0d\x0a      \
  }\x0d\x0a        onR\
ejected: {\x0d\x0a    \
        console.\
log(\x22Canceled\x22)\x0d\
\x0a            //Q\
t.quit()\x0d\x0a      \
      exitedProp\
erly = false\x0d\x0a  \
      }\x0d\x0a       \
 //Component.onC\
ompleted: visibl\
e = true\x0d\x0a    }\x0d\
\x0a\x0d\x0a    TCTG_Mana\
ger{\x0d\x0a        id\
: manager1\x0d\x0a    \
    onYamlError:\
 console.log(\x22th\
e yaml is not pr\
operly formated\x22\
)\x0d\x0a        onTem\
plateError : con\
sole.log(\x22the te\
mplate is not we\
ll formated\x22)\x0d\x0a \
   }\x0d\x0a\x0d\x0a\x0d\x0a}\x0d\x0a\x0d\x0a/\
*##^##\x0d\x0aDesigner\
 {\x0d\x0a    D{i:1;an\
chors_height:100\
;anchors_width:1\
00;anchors_x:150\
;anchors_y:190}\x0d\
\x0a}\x0d\x0a##^##*/\x0d\x0a\
\x00\x00\x04K\
i\
mport QtQuick 2.\
12\x0d\x0aimport QtQui\
ck.Controls 2.12\
\x0d\x0a\x0d\x0aItem {\x0d\x0a    \
visible: true\x0d\x0a \
   property alia\
s currentText: t\
extArea.text\x0d\x0a  \
  clip: true\x0d\x0a  \
  Rectangle{\x0d\x0a  \
      anchors.fi\
ll: parent\x0d\x0a    \
    //color: Qt.\
lightGray\x0d\x0a     \
   border.color:\
 \x22black\x22\x0d\x0a      \
  border.width: \
1\x0d\x0a    }\x0d\x0a    Fl\
ickable {\x0d\x0a     \
   id: scrollVie\
w\x0d\x0a        flick\
ableDirection: F\
lickable.Vertica\
lFlick\x0d\x0a        \
anchors.fill: pa\
rent\x0d\x0a        Te\
xtArea.flickable\
: TextArea{\x0d\x0a   \
         id: tex\
tArea\x0d\x0a         \
   anchors.fill:\
 parent\x0d\x0a       \
     selectByMou\
se: true\x0d\x0a      \
      selectByKe\
yboard: true\x0d\x0a  \
          font.p\
ixelSize: 15\x0d\x0a  \
          //plac\
eholderText: \x22Va\
lues in YAML\x22\x0d\x0a \
           //pre\
editText: \x22\x22\x0d\x0a  \
          //over\
writeMode: true\x0d\
\x0a            tex\
t: \x22name : aweso\
me\x5cnchildes :\x5cn \
- cool\x5cn - smart\
\x5cn - fantastic\x22\x0d\
\x0a        }\x0d\x0a    \
    ScrollBar.ve\
rtical: ScrollBa\
r{}\x0d\x0a    }\x0d\x0a    \
function updateH\
ighlighting(rich\
Text){\x0d\x0a        \
textArea.text = \
richText\x0d\x0a    }\x0d\
\x0a    function ge\
tPlainText(){\x0d\x0a \
       return te\
xtArea.getText(0\
,textArea.length\
)\x0d\x0a    }\x0d\x0a    fu\
nction loadText(\
t){\x0d\x0a        tex\
tArea.text = t\x0d\x0a\
    }\x0d\x0a}\x0d\x0a\
\x00\x00\x03\x9a\
i\
mport QtQuick 2.\
12\x0d\x0aimport QtQui\
ck.Controls 2.12\
\x0d\x0a\x0d\x0aItem {\x0d\x0a    \
property string \
result :  \x22\x22\x0d\x0a  \
  visible: true\x0d\
\x0a    clip: true\x0d\
\x0a    Rectangle{\x0d\
\x0a        anchors\
.fill: parent\x0d\x0a \
       color: \x22l\
ightGray\x22\x0d\x0a     \
   border.color:\
 \x22black\x22\x0d\x0a      \
  border.width: \
1\x0d\x0a\x0d\x0a    }\x0d\x0a\x0d\x0a  \
  Flickable {\x0d\x0a \
       id: scrol\
lView\x0d\x0a        f\
lickableDirectio\
n: Flickable.Ver\
ticalFlick\x0d\x0a    \
    anchors.fill\
: parent\x0d\x0a      \
  TextArea.flick\
able: TextArea{\x0d\
\x0a            id:\
resultTextArea\x0d\x0a\
            anch\
ors.fill: parent\
\x0d\x0a            pl\
aceholderText: \x22\
Results\x22\x0d\x0a      \
      text: resu\
lt\x0d\x0a            \
selectByMouse: t\
rue\x0d\x0a           \
 selectByKeyboar\
d: true\x0d\x0a       \
     clip: false\
\x0d\x0a            //\
readOnly: true\x0d\x0a\
            font\
.pixelSize: 17\x0d\x0a\
\x0d\x0a        }\x0d\x0a   \
     ScrollBar.v\
ertical: ScrollB\
ar{}\x0d\x0a    }\x0d\x0a   \
 //onResultChang\
ed: resultTextAr\
ea.text = result\
\x0d\x0a\x0d\x0a}\x0d\x0a\x0d\x0a/*##^##\
\x0d\x0aDesigner {\x0d\x0a  \
  D{i:0;autoSize\
:true;height:480\
;width:640}\x0d\x0a}\x0d\x0a\
##^##*/\x0d\x0a\
"

qt_resource_name = b"\
\x00\x12\
\x0c\x87>\xbc\
\x00T\
\x00e\x00m\x00p\x00l\x00a\x00t\x00e\x00E\x00d\x00i\x00t\x00o\x00r\x00.\x00q\x00m\
\x00l\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
\x00\x10\
\x0c\xfd\x02\xdc\
\x00V\
\x00a\x00l\x00u\x00e\x00s\x00E\x00d\x00i\x00t\x00o\x00r\x00.\x00q\x00m\x00l\
\x00\x0f\
\x0aPF\x9c\
\x00R\
\x00e\x00s\x00u\x00l\x00t\x00s\x00V\x00i\x00e\x00w\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x01\
\x00\x00\x00*\x00\x00\x00\x00\x00\x01\x00\x00\x03\xe0\
\x00\x00\x00f\x00\x00\x00\x00\x00\x01\x00\x00#\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00@\x00\x00\x00\x00\x00\x01\x00\x00\x1e\xb2\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
