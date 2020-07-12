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
            selectByMouse: true
            selectByKeyboard: true
            font.pixelSize: 15
            textFormat:  Text.RichText
            //placeholderText: "Values in YAML"
            //preeditText: ""
            //overwriteMode: true
            text: "name : awesome<br/>childes :<br/> - cool<br/> - smart<br/> - fantastic"
        }
        ScrollBar.vertical: ScrollBar{}
        onWidthChanged: {
            textArea.width = textArea.width>scrollView.width?textArea.width:scrollView.width
        }
        onHeightChanged: {textArea.height = textArea.height>scrollView.height?textArea.height:scrollView.height}
    }
    function updateHighlighting(richText){
        textArea.text = richText
    }
    function getPlainText(){
        return textArea.getText(0,textArea.length)
    }
    function loadText(t){
        textArea.text = t
    }
}
