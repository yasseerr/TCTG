import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.12

Window {
    id: mainWindow
    title: qsTr("Hello World")
    width: 640
    height: 480
    visible: true

    GridLayout {
        id: gridLayout
        anchors.fill: parent

        TemplateEditor {
            id: templateEditor
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.preferredHeight: 100;
            Layout.preferredWidth: 100;
        }

        TextArea {
            id: valuesEditor
            placeholderText: "#yaml text"
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.preferredHeight: 100;
            Layout.preferredWidth: 100;
        }

        TextArea {
            id: results
            enabled: false
            placeholderText: "Results"
            Layout.preferredHeight: 100
            Layout.preferredWidth: 100
            Layout.fillHeight: true
            Layout.fillWidth: true
            Layout.column: 0
            Layout.row: 1
        }

        GridLayout {
            id: gridLayout1
            Layout.preferredHeight: 100
            Layout.preferredWidth: 100
            Layout.fillHeight: true
            Layout.fillWidth: true
        }

    }
    Component.onCompleted: {
        mainWindow.setTitle("TCTG")
        gridLayout.anchors.margins = 10
    }

}

/*##^##
Designer {
    D{i:1;anchors_height:100;anchors_width:100;anchors_x:150;anchors_y:190}
}
##^##*/
