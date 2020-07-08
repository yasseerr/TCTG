import QtQuick 2.12
import QtQuick.Controls 2.12

Item {
    property string result :  ""
    visible: true

    Rectangle{
        anchors.fill: parent
        color: "lightGray"
        border.color: "black"
        border.width: 1

    }

    TextArea{
        id:resultTextArea
        anchors.fill: parent
        placeholderText: "Results"
        text: result
        readOnly: true
    }
    //onResultChanged: resultTextArea.text = result

}
