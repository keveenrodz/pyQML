import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    # app = QGuiApplication(sys.argv)
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load('main.qml')
    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
