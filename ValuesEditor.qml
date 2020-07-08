import QtQuick 2.12
import QtQuick.Controls 2.12

Item {
    visible: true
    property alias currentText: textArea.text
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
        TextArea.flickable: TextArea{
            id: textArea
            anchors.fill: parent
            selectByMouse: true
            selectByKeyboard: true
            placeholderText: "Values in YAML"
            text: "name : awesome\nchildes :\n - cool\n - smart\n - fantastic"
        }
        ScrollBar.vertical: ScrollBar{}
    }
}
