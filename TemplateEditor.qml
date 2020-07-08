import QtQuick 2.0
import QtQuick.Controls 2.12

Item {
    property alias currentText: textArea.text
    visible: true
    Rectangle{
        anchors.fill: parent
        //color: Qt.lightGray
        border.color: "black"
        border.width: 1
    }
    TextArea {
        id: textArea
        anchors.fill: parent
        placeholderText: qsTr("Text Area")
    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}D{i:1}D{i:3;anchors_x:73;anchors_y:28}
}
##^##*/
