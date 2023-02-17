import sys
# from PyQt5.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QStackedLayout, QMainWindow, QTabWidget, \
    QApplication
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

from welcome_tab import WelcomeTab
from student_roster_tab import StudentRosterTab


stylesheet = """
    QTabBar {
        background-color: gray;
        color: white;
    }

    QTabBar::tab:selected {
        background-color: #FF0000;
    }

    QTabBar::tab:!selected {
        background-color: gray;
    }
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the size and position of the main window
        self.setGeometry(350, 100, 1210, 755)

        self.canvas = QWidget()
        self.setCentralWidget(self.canvas)

        # Create a tab control
        self.tab_widget = QTabWidget(self)

        # Set the style for the active tab
        self.tab_widget.setStyleSheet(stylesheet)

        # Set the size of the tab control to fill the main window
        self.tab_widget.setGeometry(0, 0, 1210, 755)

        # Set the window title
        self.setWindowTitle("SHRO SUITE v3 - 2023")

        # Set the font properties of the tab names
        font = QFont("Segoe UI", 12)
        self.tab_widget.setFont(font)

        # Add the Welcome tab to the tab control
        self.tab_widget.addTab(WelcomeTab(), "Welcome")

        # Add the other tabs to the tab control
        self.tab_widget.addTab(StudentRosterTab(), "Student Roster")
        self.tab_widget.addTab(QWidget(), "Receipt Creator")
        self.tab_widget.addTab(QWidget(), "Wisely Request")
        self.tab_widget.addTab(QWidget(), "Inventory Control")
        self.tab_widget.addTab(QWidget(), "FFB Documents")
        self.tab_widget.addTab(QWidget(), "Staff Directory")
        self.tab_widget.addTab(QWidget(), "Prize Vault")
        self.tab_widget.addTab(QWidget(), "SHRO Training")
        self.tab_widget.addTab(QWidget(), "Student Fine")

        # Set the tab control as the central widget for the main window
        self.setCentralWidget(self.tab_widget)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())