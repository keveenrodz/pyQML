import QtQuick 2.6
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

ApplicationWindow {
    flags: Qt.FramelessWindowHint //Dont show the menu bar
    visible: true
    title: qsTr("Clock")
    color: "transparent"

    Clock {
    id: clock
    width: parent.width
    height: parent.height
}

}


