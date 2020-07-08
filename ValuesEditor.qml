import QtQuick 2.12
import QtQuick.Controls 2.12

Item {
    visible: true
    property alias currentText: textArea.text

    Rectangle{
        anchors.fill: parent
        //color: Qt.lightGray
        border.color: "black"
        border.width: 1
    }

    TextArea{
        id: textArea
        anchors.fill: parent
        placeholderText: "Values in YAML"
    }
}
