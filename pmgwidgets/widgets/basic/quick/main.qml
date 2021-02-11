import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

ApplicationWindow {
    visible: true
    width: 640
    height: 240
    title: qsTr("PyQt5 love QML")
    color: "whitesmoke"
    menuBar: MenuBar {
        Menu {
            title: qsTr("File")
            MenuItem {
                text: qsTr("&Open")
                onTriggered: console.log("Open action triggered");
            }
            MenuItem {
                text: qsTr("Exit")
                onTriggered: Qt.quit();

            }
        }
    }
    ColumnLayout{
        GridLayout {
            id:grid1
            anchors.top: parent.top
            anchors.left: parent.left
            anchors.right: parent.right
            // anchors.bottom: parent.bottom
            anchors.margins: 9

            columns: 4
            rows: 4
            rowSpacing: 10
            columnSpacing: 10

            Text {
                text: qsTr("First number")
            }

            // Input field of the first number
            TextField {
                id: firstNumber
                text: qsTr("123")
            }

            Text {
                text: qsTr("Second number")
            }

            // Input field of the second number
            TextField {
                id: secondNumber
            }

            Button {
                height: 40
                Layout.fillWidth: true
                text: qsTr("Sum numbers")

                Layout.columnSpan: 2

                onClicked: {
                    // Invoke the calculator slot to sum the numbers
                    calculator.sum(firstNumber.text, secondNumber.text)
                }
            }

            Text {
                text: qsTr("Result")
            }

            // Here we see the result of sum
            Text {
                id: sumResult
            }

            Button {
                height: 40
                Layout.fillWidth: true
                text: qsTr("Subtraction numbers")

                Layout.columnSpan: 2

                onClicked: {
                    // Invoke the calculator slot to subtract the numbers
                    calculator.sub(firstNumber.text, secondNumber.text)
                }
            }

            Text {
                text: qsTr("Result")
            }

            // Here we see the result of subtraction
            Text {
                id: subResult
            }
        }
        GridLayout {
            id: grid
            columns: 3
            anchors.top: grid1.bottom
            anchors.left: parent.left
            anchors.margins: 9
            Text { text: "Three"; font.bold: true; }
            Text { text: "words"; color: "red" }
            Text { text: "in"; font.underline: true }
            Text { text: "a"; font.pixelSize: 20 }
            Text { text: "row"; font.strikeout: true }
            Button {id:button1; text:qsTr("click me to calculate"); onClicked:{calculator.sum(123,456)}}
        }
    }

    // Here we take the result of sum or subtracting numbers
    Connections {
        target: calculator
 
        // Sum signal handler
        onSumResult: {
            // sum was set through arguments=['sum']
            sumResult.text = sum
        }

        // Subtraction signal handler
        onSubResult: {
            // sub was set through arguments=['sub']
            subResult.text = sub
        }
    }
}

