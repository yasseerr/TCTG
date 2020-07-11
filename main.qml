import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.12
import QtQuick.Dialogs 1.0
import TCTG 1.0

ApplicationWindow {
    id: mainWindow
    title: qsTr("Hello World")
    width: 1280
    height: 960
    visible: true
    menuBar: MenuBar{

        Menu {
            title: qsTr("&File")
            Action { text: qsTr("&New...") }
            Action {
                id: openStateAction
                text: qsTr("&Open State...")
                shortcut: StandardKey.Open
                onTriggered: {
                    openStateFileDialog.open()
                }
            }
            Action {
                id: saveStateAction
                text: qsTr("&Save State")
                shortcut: StandardKey.Save
                onTriggered: {
                    saveStateFileDialog.open()
                }
            }
            Action { text: qsTr("&Save Template") }
            Action { text: qsTr("&Save Values") }
            Action { text: qsTr("Save &As...") }
            MenuSeparator { }
            Action { text: qsTr("&Quit") }
        }
        Menu {
            title: qsTr("&Edit")
            Action { text: qsTr("Cu&t") }
            Action { text: qsTr("&Copy") }
            Action { text: qsTr("&Paste") }
            Action { text: qsTr("&Copy Results") }
        }
        Menu {
            title: qsTr("&Tools")
            Action { text: qsTr("&Render") }
            Action { text: qsTr("&Clear") }
            //Action { text: qsTr("&Paste") }
            //Action { text: qsTr("&Copy Results") }
        }
        Menu {
            title: qsTr("&Help")
            Action { text: qsTr("&About") }
        }
    }

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
            Layout.topMargin: 0
            Layout.leftMargin: 0
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
                    //results.result = "it should be added "
                    results.result =  manager1.render(templateEditor.currentText,valuesEditor.currentText)
                }
            }

            Button {
                id: clearButton
                text: qsTr("Clear")
                Layout.fillWidth: true
                Layout.column: 0
                Layout.row: 1
                onClicked: {
                    //TODO add the support for html highlighting
                    var the_code = valuesEditor.getPlainText();
                    console.log(the_code)
                     valuesEditor.updateHighlighting(manager1.highlightCode(the_code,"YAML"))
                }
            }
            Button {
                id: saveTemplateButton
                text: qsTr("Save Template")
                Layout.fillWidth: true
                Layout.column: 0
                Layout.row: 2
            }

            Button {
                id: saveValuesButton
                text: qsTr("Save Values")
                Layout.fillWidth: true
                Layout.column: 0
                Layout.row: 3
            }

            Button {
                id: copyResultsButton
                text: qsTr("Copy Results")
                Layout.fillWidth: true
                Layout.column: 0
                Layout.row: 4
            }

            RoundButton {
                id: saveStateButton
                text: qsTr("Save State")
                Layout.fillWidth: true
                Layout.column: 0
                Layout.row: 5
                action: saveStateAction

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

    FileDialog {
        id: saveStateFileDialog
        title: "Please choose a file to save the state"
        folder: shortcuts.home
        selectExisting: false
        modality: Qt.ApplicationModal
        onAccepted: {
            console.log("You chose: " + saveStateFileDialog.fileUrls)
            manager1.saveState(templateEditor.currentText,valuesEditor.currentText,fileUrl)
            //Qt.quit()
        }
        onRejected: {
            console.log("Canceled")
            //Qt.quit()
            exitedProperly = false
        }
        //Component.onCompleted: visible = true
    }

    FileDialog {
        id: openStateFileDialog
        title: "Please choose a file to save the state"
        folder: shortcuts.home
        selectExisting: true
        modality: Qt.ApplicationModal
        onAccepted: {
            console.log("You chose: " + saveStateFileDialog.fileUrls)
            var retList = manager1.openState(fileUrl)
            templateEditor.loadText(retList[0])
            valuesEditor.loadText(retList[1])
            //Qt.quit()
        }
        onRejected: {
            console.log("Canceled")
            //Qt.quit()
            exitedProperly = false
        }
        //Component.onCompleted: visible = true
    }

    TCTG_Manager{
        id: manager1
        onYamlError: console.log("the yaml is not properly formated")
        onTemplateError : console.log("the template is not well formated")
    }


}

/*##^##
Designer {
    D{i:1;anchors_height:100;anchors_width:100;anchors_x:150;anchors_y:190}
}
##^##*/
