import QtQuick
import QtQuick.Shapes

Item {
    id: root

    property var clockData

    property int hours: clockData.hours
    property int minutes: clockData.mins
    property int seconds: clockData.secs

    width: 400
    height: 400

    Rectangle {
        id: clockFace

        width: Math.min(root.width, root.height)
        height: width

        anchors.centerIn: parent

        radius: width / 2

        color: "white"
        border.width: 3
        border.color: "black"

        Repeater {
            model: 60

            Rectangle {
                width: index % 5 === 0 ? 3 : 1
                height: index % 5 === 0 ? 15 : 8

                color: "black"

                x: clockFace.width / 2 - width / 2
                y: 10

                transformOrigin: Item.Bottom

                rotation: index * 6
            }
        }

        Repeater {
            model: 12

            Text {
                text: index + 1

                font.pixelSize: 24
                font.bold: true

                color: "black"

                property real angle: (index + 1) * 30 - 90
                property real radiusFromCenter: clockFace.width / 2 - 40

                x: clockFace.width / 2
                   + Math.cos(angle * Math.PI / 180) * radiusFromCenter
                   - width / 2

                y: clockFace.height / 2
                   + Math.sin(angle * Math.PI / 180) * radiusFromCenter
                   - height / 2
            }
        }

        Shape {
            id: hourHand

            width: clockFace.width
            height: clockFace.height

            anchors.centerIn: parent

            transformOrigin: Item.Center

            rotation: (root.hours + root.minutes / 60) * (360 / 12)

            ShapePath {
                strokeWidth: 6
                strokeColor: "black"

                startX: clockFace.width / 2
                startY: clockFace.height / 2

                PathLine {
                    x: clockFace.width / 2
                    y: clockFace.height / 2 - 80
                }
            }
        }

        Shape {
            id: minuteHand

            width: clockFace.width
            height: clockFace.height

            anchors.centerIn: parent

            transformOrigin: Item.Center

            rotation: root.minutes * 6 + root.seconds / 10

            ShapePath {
                strokeWidth: 4
                strokeColor: "black"

                startX: clockFace.width / 2
                startY: clockFace.height / 2

                PathLine {
                    x: clockFace.width / 2
                    y: clockFace.height / 2 - 115
                }
            }
        }

        Shape {
            id: secondHand

            width: clockFace.width
            height: clockFace.height

            anchors.centerIn: parent

            transformOrigin: Item.Center

            rotation: root.seconds * 6

            ShapePath {
                strokeWidth: 2
                strokeColor: "red"

                startX: clockFace.width / 2
                startY: clockFace.height / 2

                PathLine {
                    x: clockFace.width / 2
                    y: clockFace.height / 2 - 130
                }
            }
        }

        Rectangle {
            width: 12
            height: 12

            radius: 6

            color: "black"

            anchors.centerIn: parent
        }
    }
}
