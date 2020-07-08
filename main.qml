import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.12
import TCTG 1.0

Window {
    id: mainWindow
    title: qsTr("Hello World")
    width: 1280
    height: 960
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

        ValuesEditor {
            id: valuesEditor
            //placeholderText: "#yaml text"
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.preferredHeight: 100;
            Layout.preferredWidth: 100;
        }

        ResultsView {
            id: results
            Layout.preferredHeight: 100
            Layout.preferredWidth: 100
            Layout.fillHeight: true
            Layout.fillWidth: true
            Layout.column: 0
            Layout.row: 1
        }

        GridLayout {
            id: gridLayout1
            columns: 2
            Layout.alignment: Qt.AlignLeft | Qt.AlignTop
            Layout.preferredHeight: 100
            Layout.preferredWidth: 100
            Layout.fillHeight: true
            Layout.fillWidth: true

            Button {
                id: renderButton
                text: qsTr("Render")
                Layout.fillWidth: true
                flat: false
                onClicked: {
                    results.result = "it should be added "
                    results.result =  manager1.render(templateEditor.currentText,valuesEditor.currentText)
                }
            }

            Button {
                id: clearButton
                text: qsTr("Clear")
                Layout.fillWidth: true
                Layout.column: 0
                Layout.row: 1
            }
            Item {
                id: spacer1
                Layout.preferredWidth: 300
                Layout.fillWidth: true
                Layout.column: 1
                Layout.row: 0
                Layout.rowSpan: 2
            }
        }

    }
    Component.onCompleted: {
        mainWindow.setTitle("TCTG")
        gridLayout.anchors.margins = 10
    }
    TCTG_Manager{
        id: manager1
    }

}

/*##^##
Designer {
    D{i:1;anchors_height:100;anchors_width:100;anchors_x:150;anchors_y:190}
}
##^##*/
