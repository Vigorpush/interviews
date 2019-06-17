# -*- coding: utf-8 -*-
# PC Browser Deploy Helper
# Writing in python, PYQT and QT
# Pre-Requisite: Chocolatey (PC software package manager) installed in your PC
from PyQt5 import QtCore, QtGui, QtWidgets
import GetBroswers


# from PyQt5.QtGui import QDesktopServices
# from PyQt5.QtCore import QUrl
# import subprocess
# import qdarkstyle
# import time
# from PyQt5.QtCore import QThread, QThreadPool
# https://nikolak.com/pyqt-threading-tutorial/
# https://martinfitzpatrick.name/article/multithreading-pyqt-applications-with-qthreadpool/
# class YourThreadName(QThread):
#
#     def __init__(self):
#         QThread.__init__(self)
#
#     def __del__(self):
#         self.wait()
#
#     def run(self):
#         time.sleep(100)
#         pass
#         # your logic here


class Uimainwindow(object):
    dict = {'chrome': '', 'ff': '', 'opera': '', 'ie': ''}

    ielist = ['ie9', 'ie10', 'ie11']
    chromelist = []
    fflist = []
    operalist = []

    ieradiolist = []
    chromeradiolist = []
    ffradiolist = []
    operaradiolist = []

    option = ''

    def _set_browser_dict(self, str):

        browsertype = str.split(' ')[0].lower()

        if browsertype == 'google':
            del self.dict['chrome']
            self.dict['chrome'] = str.split(' ')[-1].lower()
        elif browsertype == 'mozilla' or browsertype == 'firefox':
            del self.dict['ff']
            self.dict['ff'] = str.split(' ')[-1].lower()
        elif browsertype == 'opera':
            del self.dict['opera']
            self.dict['opera'] = str.split(' ')[-1].lower()
        elif browsertype == 'ie':
            del self.dict['ie']
            if str.split(' ')[-1].lower() == '11':
                self.dict['ie'] = '11'
            elif str.split(' ')[-1].lower() == '10':
                self.dict['ie'] = '10'
            elif str.split(' ')[-1].lower() == '9':
                self.dict['ie'] = '9'

    def download_last(self):
        self.plainTextEdit.appendPlainText('choco install googlechrome -f -y -r --ignore-checksums')
        self.plainTextEdit.appendPlainText('choco install firefox -f -y -r --ignore-checksums')
        self.plainTextEdit.appendPlainText('choco install opera -f -y -r --ignore-checksums')
        self.plainTextEdit.appendPlainText('choco install ie11 -f -y -r --ignore-checksums')
        # choco upgrade firefox
        self.plainTextEdit.appendPlainText('choco upgrade googlechrome -y -r -f ')
        self.plainTextEdit.appendPlainText('choco upgrade firefox -y -r -f ')
        self.plainTextEdit.appendPlainText('choco upgrade opera -y -r -f ')

    def chrome_downloader(self):
        if self.dict['chrome'].lower() == '':
            pass
        else:
            command = 'choco install googlechrome --version ' + self.dict['chrome'].replace("\n",
                                                                                            "") + ' -f -y -r --ignore-checksums'

            self.plainTextEdit.appendPlainText(command)

    def ff_downloader(self):
        if self.dict['ff'].lower() == '':
            pass
        else:
            command = 'choco install firefox --version ' + self.dict['ff'].replace("\n",
                                                                                   "") + ' -f -y -r --ignore-checksums'
            self.plainTextEdit.appendPlainText(command)

    def opera_downloader(self):
        if self.dict['opera'].lower() == '':
            pass
        else:
            command = 'choco install opera --version ' + self.dict['opera'].replace("\n",
                                                                                    "") + ' -f -y -r --ignore-checksums'
            self.plainTextEdit.appendPlainText(command)

    def ie_downloader(self):
        if self.dict['ie'].lower() == '':
            pass
        else:
            command = 'choco install ie' + self.dict['ie'].replace("\n", "") + ' -f -y -r --ignore-checksums'
            self.plainTextEdit.appendPlainText(command)

    def fetching_browser_lists(self):
        self.get_chrome_version()
        self.get_opera_version()
        self.get_ff_version()
        self.ielist = ['ie9', 'ie10', 'ie11']

    def get_opera_version(self):
        infile = open('opera.txt', 'r')

        for line in infile:
            self.operalist.append(line)

    def get_ff_version(self):
        infile = open('ff.txt', 'r')

        for line in infile:
            self.fflist.append(line)

    def get_chrome_version(self):
        infile = open('chrome.txt', 'r')

        for line in infile:
            self.chromelist.append(line)

    def setup_upper(self, MainWindow):
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.OptionPannel = QtWidgets.QHBoxLayout()
        self.OptionPannel.setSpacing(6)
        self.OptionPannel.setObjectName("OptionPannel")
        self.OptionA = QtWidgets.QVBoxLayout()
        self.OptionA.setSpacing(6)
        self.OptionA.setObjectName("OptionA")
        self.Enhance = QtWidgets.QRadioButton(self.centralWidget)
        self.Enhance.setObjectName("Enhance")
        self.OptionA.addWidget(self.Enhance)
        self.Degration = QtWidgets.QRadioButton(self.centralWidget)
        self.Degration.setObjectName("Degration")
        self.OptionA.addWidget(self.Degration)
        self.OptionPannel.addLayout(self.OptionA)
        self.OptionB = QtWidgets.QVBoxLayout()
        self.OptionB.setSpacing(6)
        self.OptionB.setObjectName("OptionB")
        self.Latest = QtWidgets.QRadioButton(self.centralWidget)
        self.Latest.setObjectName("Latest")
        self.OptionB.addWidget(self.Latest)
        self.Custom = QtWidgets.QRadioButton(self.centralWidget)
        self.Custom.setObjectName("Custom")
        self.OptionB.addWidget(self.Custom)
        self.OptionPannel.addLayout(self.OptionB)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setReadOnly(True)
        self.OptionPannel.addWidget(self.plainTextEdit)
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.OptionPannel.addWidget(self.line)
        self.Refresh = QtWidgets.QPushButton(self.centralWidget)
        self.Refresh.setMinimumSize(QtCore.QSize(0, 0))
        self.Refresh.setMaximumSize(QtCore.QSize(100, 100))
        self.Refresh.setIconSize(QtCore.QSize(16, 16))
        self.Refresh.setObjectName("Refresh")

        self.ExecutingButton = QtWidgets.QPushButton(self.centralWidget)
        self.ExecutingButton.setMinimumSize(QtCore.QSize(180, 100))
        self.ExecutingButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ExecutingButton.setIconSize(QtCore.QSize(16, 16))
        self.ExecutingButton.setObjectName("ExecutingButton")
        self.OptionPannel.addWidget(self.ExecutingButton)
        self.OptionPannel.addWidget(self.Refresh)

        self.Help = QtWidgets.QPushButton(self.centralWidget)
        self.Help.setMinimumSize(QtCore.QSize(0, 0))
        self.Help.setMaximumSize(QtCore.QSize(100, 100))
        self.Help.setIconSize(QtCore.QSize(16, 16))
        self.Help.setObjectName("Help")
        self.OptionPannel.addWidget(self.Help)

        self.verticalLayout_2.addLayout(self.OptionPannel)
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.BrowserSelectRegion = QtWidgets.QHBoxLayout()
        self.BrowserSelectRegion.setSpacing(6)
        self.BrowserSelectRegion.setObjectName("BrowserSelectRegion")

    def setup_middle(self, MainWindow):
        self.fetching_browser_lists()

        self.Chrome = QtWidgets.QVBoxLayout()
        self.Chrome.setSpacing(6)
        self.Chrome.setObjectName("Chrome")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -3, 122, 323))
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 157, 195))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        for chrome in self.chromelist:
            radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
            radio.setObjectName(chrome)
            self.verticalLayout.addWidget(radio)
            self.chromeradiolist.append(radio)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.Chrome.addWidget(self.scrollArea)
        self.BrowserSelectRegion.addLayout(self.Chrome)
        self.FF = QtWidgets.QVBoxLayout()
        self.FF.setSpacing(6)
        self.FF.setObjectName("FF")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 157, 195))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        for ff in self.fflist:
            radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
            radio.setObjectName(ff)
            self.verticalLayout_3.addWidget(radio)
            self.ffradiolist.append(radio)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.FF.addWidget(self.scrollArea_2)
        self.BrowserSelectRegion.addLayout(self.FF)
        self.Opera = QtWidgets.QVBoxLayout()
        self.Opera.setSpacing(6)
        self.Opera.setObjectName("Opera")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 157, 195))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        for opera in self.operalist:
            radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_3)
            radio.setObjectName(opera)
            self.verticalLayout_4.addWidget(radio)
            self.operaradiolist.append(radio)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.Opera.addWidget(self.scrollArea_3)
        self.BrowserSelectRegion.addLayout(self.Opera)

        self.IE = QtWidgets.QVBoxLayout()
        self.IE.setSpacing(6)
        self.IE.setObjectName("IE")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 157, 195))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ie11_radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_4)
        self.ie11_radioButton.setObjectName("IE11")
        self.verticalLayout_5.addWidget(self.ie11_radioButton)
        self.ie10_radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_4)
        self.ie10_radioButton.setObjectName("IE10")
        self.verticalLayout_5.addWidget(self.ie10_radioButton)
        self.ie9_radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_4)
        self.ie9_radioButton.setObjectName("IE9")
        self.verticalLayout_5.addWidget(self.ie9_radioButton)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.IE.addWidget(self.scrollArea_4)
        self.BrowserSelectRegion.addLayout(self.IE)
        self.verticalLayout_2.addLayout(self.BrowserSelectRegion)

    def setup_lower(self, MainWindow):
        # self.plainTextEdit.appendPlainText("Loading ie Pannal  ... ")

        self.infopannel = QtWidgets.QWidget(self.centralWidget)
        self.infopannel.setMinimumSize(QtCore.QSize(0, 60))

        self.infopannel.setObjectName("infopannel")
        self.softwareinfoPannel = QtWidgets.QHBoxLayout(self.infopannel)
        self.softwareinfoPannel.setContentsMargins(0, 0, 0, 0)
        self.softwareinfoPannel.setSpacing(1)
        self.softwareinfoPannel.setObjectName("softwareinfoPannel")
        self.Author = QtWidgets.QWidget(self.infopannel)
        self.Author.setEnabled(True)
        self.Author.setMinimumSize(QtCore.QSize(2, 22))
        self.Author.setObjectName("Author")
        self.Auther = QtWidgets.QVBoxLayout(self.Author)
        # self.Auther.setContentsMargins(11, 11, 11, 11)
        self.Auther.setSpacing(6)
        self.Auther.setObjectName("Auther")
        self.NAME = QtWidgets.QLabel(self.Author)
        self.NAME.setObjectName("NAME")
        self.Auther.addWidget(self.NAME)
        self.softwareinfoPannel.addWidget(self.Author)
        self.Version = QtWidgets.QVBoxLayout()
        self.Version.setSpacing(6)
        self.Version.setObjectName("Version")
        self.VERSION = QtWidgets.QLabel(self.infopannel)
        self.VERSION.setObjectName("VERSION")
        self.Version.addWidget(self.VERSION)
        self.softwareinfoPannel.addLayout(self.Version)
        self.Email = QtWidgets.QVBoxLayout()
        self.Email.setSpacing(6)
        self.Email.setObjectName("Email")
        self.EMAIL = QtWidgets.QLabel(self.infopannel)
        self.EMAIL.setObjectName("EMAIL")
        self.Email.addWidget(self.EMAIL)
        self.softwareinfoPannel.addLayout(self.Email)
        self.Donate = QtWidgets.QVBoxLayout()
        self.Donate.setSpacing(6)
        self.Donate.setObjectName("Donate")
        self.URL = QtWidgets.QLabel(self.infopannel)
        self.URL.setObjectName("URL")
        self.Donate.addWidget(self.URL)
        self.softwareinfoPannel.addLayout(self.Donate)
        self.verticalLayout_2.addWidget(self.infopannel)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setEnabled(True)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

    def setup_ui(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 500)
        self.setup_upper(MainWindow)
        self.setup_middle(MainWindow)
        self.setup_lower(MainWindow)
        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "PC Browser Deploy Helper v0.31"))

        self.Enhance.setText(_translate("main_window", "Enhancement"))
        self.Degration.setText(_translate("main_window", "Degration"))
        self.Latest.setText(_translate("main_window", "Keep Update"))
        self.Custom.setText(_translate("main_window", "Custom"))

        self.Help.setText(_translate("main_window", "Help"))
        self.ExecutingButton.setText(_translate("main_window", "Deploy"))
        self.Refresh.setText(_translate("main_window", "Check for\n"
                                                       "Updates"))

        i = 0
        for radioElement in self.chromeradiolist:
            radioElement.setText(_translate("main_window", self.chromelist[i]))
            helper = lambda i: (lambda: self._set_browser_dict(self.chromelist[i]))
            self.chromeradiolist[i].clicked.connect(helper(i))
            i = i + 1

        j = 0
        for radioElement in self.ffradiolist:
            radioElement.setText(_translate("main_window", self.fflist[j]))
            helper = lambda j: (lambda: self._set_browser_dict(self.fflist[j]))
            self.ffradiolist[j].clicked.connect(helper(j))
            j = j + 1

        n = 0
        for radioElement in self.operaradiolist:
            radioElement.setText(_translate("main_window", self.operalist[n]))
            helper = lambda n: (lambda: self._set_browser_dict(self.operalist[n]))
            self.operaradiolist[n].clicked.connect(helper(n))

            n = n + 1

        self.ie11_radioButton.setText(_translate("main_window", "IE 11"))
        self.ie10_radioButton.setText(_translate("main_window", "IE 10"))
        self.ie9_radioButton.setText(_translate("main_window", "IE 9"))
        self.ie11_radioButton.clicked.connect(lambda: self._set_browser_dict(self.ie11_radioButton.text()))
        self.ie10_radioButton.clicked.connect(lambda: self._set_browser_dict(self.ie10_radioButton.text()))
        self.ie9_radioButton.clicked.connect(lambda: self._set_browser_dict(self.ie9_radioButton.text()))

        self.ExecutingButton.clicked.connect(lambda: self._execution_action())
        self.Refresh.clicked.connect(lambda: self._refresh_action())
        self.Enhance.clicked.connect(lambda: self._option_action("Enhance"))
        self.Degration.clicked.connect(lambda: self._option_action("Degration"))
        self.Latest.clicked.connect(lambda: self._option_action("Latest"))
        self.Custom.clicked.connect(lambda: self._option_action("Custom"))
        self.Help.clicked.connect(lambda: self._help_action())

        self.NAME.setText(_translate("main_window", "Author: Vigor Zang"))
        self.VERSION.setText(_translate("main_window", "Version: 0.31"))
        self.EMAIL.setText('<a href="mailto:vigorzjw@gmail.com">Email Vigor</a>')
        self.EMAIL.setOpenExternalLinks(True)
        self.URL.setText('URL:<a href="https://www.linkedin.com/in/vigorz/">Vigor Push</a>')
        self.URL.setOpenExternalLinks(True)

        self.plainTextEdit.appendPlainText(
            "Make sure you installed choco on your PC (Click Help to get the instruction)")
        self.plainTextEdit.appendPlainText("1. Select Option")
        self.plainTextEdit.appendPlainText("2. Select Browser version, and press 'deploy' button ")
        self.plainTextEdit.appendPlainText("3. Copy the command generated, and paste it in cmd as admin")
        self.plainTextEdit.appendPlainText("4. Run the command, and wait")

    def _help_action(self):
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(
            "::Pre-Requisite: Chocolatey (A PC software package manager) installed in your PC")
        self.plainTextEdit.appendPlainText(
            "::Run following command with Admin in CMD.exe")
        self.plainTextEdit.appendPlainText(
            '@"%SystemRoot%\System32\WindowsPowerShell\\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\\bin"'.replace(
                "\n", ""))

    def _option_action(self, opt):
        self.plainTextEdit.clear()
        if opt.lower() == 'enhance':
            self.plainTextEdit.appendPlainText("Progressive enhancement Development Mode\n\n"
                                               "Now, Select the base version")
        elif opt.lower() == 'degration':
            self.plainTextEdit.appendPlainText(
                "Graceful Degradation Development Mode (it lets you start to working on the latest version) \n\n"
                "Now, Click Deploy to get command")
        elif opt.lower() == 'latest':
            self.plainTextEdit.appendPlainText(
                "Latest Development Mode, it gonna updates your browser to latest version\n\n"
                "Now, Click Deploy to get command")
        elif opt.lower() == 'custom':
            self.plainTextEdit.appendPlainText("Custom Development Mode\n\n"
                                               "Now, Select the version")
        self.option = opt.lower()

    def _refresh_action(self):
        self.plainTextEdit.clear()
        xhr = GetBroswers.GetBrowser()
        # self.plainTextEdit.appendPlainText("Start To Fetching Chrome Version ... ")
        xhr.get_chrome()
        # self.plainTextEdit.appendPlainText("Start To Fetching firefox Version ... ")
        xhr.get_ff()
        # self.plainTextEdit.appendPlainText("Start To Fetching opera Version ... ")
        xhr.get_opera()
        # self.plainTextEdit.appendPlainText("Start To Fetching IE Version ... ")
        xhr.get_ie()
        self.plainTextEdit.appendPlainText("Fetching Browser Version Successfully ")
        self.plainTextEdit.appendPlainText(
            "But You still need to restart this app to get the updated version lists -- Vigor")

    def _execution_action(self):
        # thread = YourThreadName()
        # thread.run()
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(":: Run the following command in Command Prompt as administrator")
        if self.option == 'custom':
            self.chrome_downloader()
            self.ff_downloader()
            self.opera_downloader()
            self.ie_downloader()
        elif self.option == 'enhance':
            self.chrome_downloader()
            self.ff_downloader()
            self.opera_downloader()
            self.ie_downloader()
        elif self.option == 'degration':
            self.download_last()
        elif self.option == 'latest':
            self.download_last()
        else:
            self.chrome_downloader()
            self.ff_downloader()
            self.opera_downloader()
            self.ie_downloader()

        self.plainTextEdit.appendPlainText(":: Copy Run the above command in Command Prompt as administrator")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow = QtWidgets.QMainWindow()
    app.setWindowIcon(QtGui.QIcon('logo.png'))
    ui = Uimainwindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
