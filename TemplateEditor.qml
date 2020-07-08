import QtQuick 2.0
import QtQuick.Controls 2.12

Item {
    property alias currentText: textArea.text
    visible: true
    clip: true
    Rectangle{
        anchors.fill: parent
        //color: Qt.lightGray
        border.color: "black"
        border.width: 1
    }

    Flickable {
        id: scrollView
        flickableDirection: Flickable.VerticalFlick
        anchors.fill: parent
        TextArea.flickable: TextArea {
            id: textArea
            anchors.fill: parent
            selectByMouse: true
            selectByKeyboard: true
            text: "the name is : {{name}} \n the children are : \n{%for child in childes%}\n another one : {{child}} {%endfor%}"
        }
        ScrollBar.vertical: ScrollBar{}
    }


}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}D{i:1}D{i:3;anchors_x:73;anchors_y:28}
}
##^##*/
