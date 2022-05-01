import sys
import os
from PySide2 import *
import csv
########################################################################
# IMPORT GUI FILE
from ui_teamPlayer import *


########################################################################


class MainApp(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.team = ''
        self.player = ''
        self.datafile_location = ''
        # self.setGeometry(650, 450, 900, 900)

        ################### Remove window tittle bar ######################
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setIcon()

        ################### Set main background to transparent ###################
        self.setAttribute(Qt.WA_TranslucentBackground)

        ################### Shadow effect style ###################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))

        ################### Appy shadow to central widget ###################
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #################### Set window Icon ###################
        # This icon and title will not appear on our app main window because we removed the title bar
        self.setWindowIcon(QIcon(u"icons/analysis.png"))

        ################### Set window tittle ###################
        self.setWindowTitle("ANOM")

        ################### Minimize window ###################
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())

        ################### Close window ###################
        self.ui.out.clicked.connect(lambda: self.close())
        self.ui.exit_button.clicked.connect(lambda: self.close())

        ################### Restore/Maximize window ###################
        self.ui.expand.clicked.connect(lambda: self.restore_or_maximize_window())

        # Function to Move window on mouse drag event on the tittle bar
        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################
            if self.isMaximized() == False:  # Not maximized
                # Move window only when window is normal size
                # ###############################################
                # if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    # Move window
                    self.move(self.pos() + e.globalPosition().toPoint() - self.clickPosition)
                    self.clickPosition = e.globalPosition().toPoint()
                    e.accept()

        # Add click event/Mouse move event/drag event to the top header to move the window
        self.ui.ToolBar.mouseMoveEvent = moveWindow

        # Left Menu toggle button
        self.ui.open_close_side_bar.clicked.connect(lambda: self.slideLeftMenu())

        # Left Choices buttons
        # Home Button
        self.ui.home_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
        # Time Button
        self.ui.upload_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.uplad_page))
        # Fourier Button
        self.ui.search_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.search_page))

        # seach Button
        self.ui.lineEdit_2.setPlaceholderText('Player Name')
        self.ui.lineEdit_3.setPlaceholderText('Team Name')

        self.ui.pushButton.clicked.connect(self.show_data)

        # Browse Button

        self.ui.browse_button.clicked.connect(self.browse_files)
        self.createWindow()

    ###############################################################
    # Browse file
    ###############################################################
    def browse_files(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\', "Excel files (*.csv *.xls *.xls)")
        self.ui.lineEdit.setText(fname[0])
        self.datafile_location = fname[0]

    def search_data(self):
        if self.datafile_location == '':
            return "Please Upload the Dataset First"
        with open(f'{self.datafile_location}', 'r') as f:
            reader = csv.reader(f)
            for i in reader:
                p = i[1]
                t = i[0]
                if self.player.strip() == str(p) and self.team.strip() == t:
                    return i[2]

        return "Not exist"

    def show_data(self):
        self.player = self.ui.lineEdit_2.text()
        self.team = self.ui.lineEdit_3.text()
        out = ''
        if self.player == '':
            out =  "Please Enter the Player Name"
        elif self.team == '':
            out =  "Please Enter the Team Name"
        elif self.datafile_location == '':
            out =  "Please Upload the Dataset First"
        elif self.search_data() == "Not exist":
            out = f"{self.player} is: {self.search_data()} "
        else:
            out = f"The NBA correlation of {self.player} is: {self.search_data()} "

        self.ui.show_nba.setText(out)


    ###############################################################
    # Update restore button icon on msximizing or minimizing window
    ###############################################################
    def restore_or_maximize_window(self):
        # If window is maxmized
        if self.isMaximized():
            self.showNormal()
            # Change Icon
            self.ui.expand.setIcon(QIcon(u"icons/assets/expand-arrows-free-icon-font.svg"))
        else:
            self.showMaximized()
            # Change Icon
            self.ui.expand.setIcon(QIcon(u"icons/minimize.png"))

    ########################################################################
    # Slide left menu function
    ########################################################################
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.left_body.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 210
            self.ui.open_close_side_bar.setIcon(QIcon(u"icons/left-arrow.png"))
            self.ui.sidebar_icon.setMaximumWidth(190)
            self.ui.open_close_side_bar.setMaximumWidth(100)
            self.ui.logo_name.setMaximumWidth(100)
            self.ui.Logo.setMaximumWidth(90)

        # If maximized
        else:
            # Restore menu
            newWidth = 0
            self.ui.logo_name.setMaximumWidth(0)
            self.ui.Logo.setMaximumWidth(0)
            self.ui.open_close_side_bar.setIcon(QIcon(u"icons/align-justify-free-icon-font.png"))
            self.ui.sidebar_icon.setMaximumWidth(40)



        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.left_body, b"maximumWidth")#Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    ########################################################################
    # show window
    ########################################################################
    def createWindow(self):
        self.show()
        sys.exit(self.app.exec())

    ########################################################################
    # set the application icon
    ########################################################################
    def setIcon(self):
        icon = QIcon('increasing.png')
        icon.addFile('../assets/increasing.png')
        self.setWindowIcon(icon)

    #######################################################################
    # Add mouse events to the window
    #######################################################################
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPosition().toPoint()
        # We will use this value to move the window

if __name__ == '__main__':
    app = MainApp()

    # app.geometry().center()