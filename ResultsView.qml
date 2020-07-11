import QtQuick 2.12
import QtQuick.Controls 2.12

Item {
    property string result :  ""
    visible: true
    clip: true
    Rectangle{
        anchors.fill: parent
        color: "lightGray"
        border.color: "black"
        border.width: 1

    }

    Flickable {
        id: scrollView
        flickableDirection: Flickable.VerticalFlick
        anchors.fill: parent
        TextArea.flickable: TextArea{
            id:resultTextArea
            anchors.fill: parent
            placeholderText: "Results"
            text: result
            selectByMouse: true
            selectByKeyboard: true
            clip: false
            //readOnly: true
            font.pixelSize: 17

        }
        ScrollBar.vertical: ScrollBar{}
    }
    //onResultChanged: resultTextArea.text = result

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
