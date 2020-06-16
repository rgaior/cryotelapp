"""
    gridcontrol.py
    --------------
    This is the main module of Grid Control. Implements the UI and business logic.
"""

import sys
#import threading

import connection
import helper
#import openhwmon
#import polling
import serial
#import settings
sys.path.append('/ui/')
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication
from ui.mainwindow import Ui_MainWindow

# Define status icons (available in the resource file built with "pyrcc5"
ICON_RED_LED = ":/icons/led-red-on.png"
ICON_GREEN_LED = ":/icons/green-led-on.png"

class Control(QtWidgets.QMainWindow):
    """Create the UI, based on PyQt5.
    The UI elements are defined in "mainwindow.py" and resource file "resources_rc.py", created in QT Designer.

    To update "mainwindow.py":
        Run "pyuic5.exe --from-imports mainwindow.ui -o mainwindow.py"

    To update "resources_rc.py":
        Run "pyrcc5.exe resources.qrc -o resource_rc.py"

    Note: Never modify "mainwindow.py" or "resource_rc.py" manually.
    """

    def __init__(self):
        super().__init__()

        # Create the main window
        self.ui = Ui_MainWindow()
         # Set upp the UI
        self.ui.setupUi(self)
       # self.show()
        # Get a list of available serial ports (e.g. "COM1" in Windows)
        self.serial_ports = connection.get_serial_ports()
        self.ui.comboBox.addItems(self.serial_ports)
        self.setup_ui_logic()
        # Populate the "COM port" combo box with available serial ports
        #self.ui.comboBoxComPorts.addItems(self.serial_ports)


    def setup_ui_logic(self):
        """Define QT signal and slot connections and initializes UI values."""
        # Connect "Restart Communication" button
        self.ui.quitbutton.clicked.connect(QApplication.instance().quit)

if __name__ == "__main__":
    # Use a rewritten excepthook for displaying unhandled exceptions as a QMessageBox
  #  sys.excepthook = helper.excepthook

    # Create the QT application
    app = QtWidgets.QApplication(sys.argv)

    # Create the main window
    win = Control()

    # Set program version
    win.setWindowTitle("Control 0.0.0")

    # Show window
    win.show()

    # Disable window resizing
    win.setFixedSize(win.size())

    # Start QT application
    sys.exit(app.exec_())