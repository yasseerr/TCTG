import QtQuick 2.12
import QtQuick.Controls 2.12

Item {
    visible: true
    property string result: ""

    Rectangle{
        anchors.fill: parent
        color: Qt.gray
        border.color: Qt.black
        border.width: 1
    }

    TextArea{
        anchors.fill: parent
        placeholderText: "Results"
        text: result
        readOnly: true
    }

}
