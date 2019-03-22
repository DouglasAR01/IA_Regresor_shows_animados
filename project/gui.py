# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from core import CoreRegressors

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):

    def __init__(self):
        self.regressors = CoreRegressors()
        self.genres = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(20, 200, 300, 280))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.g1 = QtGui.QCheckBox(self.groupBox)
        self.g1.setGeometry(QtCore.QRect(60, 20, 70, 17))
        self.g1.setObjectName(_fromUtf8("g1"))
        self.g2 = QtGui.QCheckBox(self.groupBox)
        self.g2.setGeometry(QtCore.QRect(60, 50, 70, 17))
        self.g2.setObjectName(_fromUtf8("g2"))
        self.g3 = QtGui.QCheckBox(self.groupBox)
        self.g3.setGeometry(QtCore.QRect(60, 80, 70, 17))
        self.g3.setObjectName(_fromUtf8("g3"))
        self.g4 = QtGui.QCheckBox(self.groupBox)
        self.g4.setGeometry(QtCore.QRect(60, 110, 70, 17))
        self.g4.setObjectName(_fromUtf8("g4"))
        self.g5 = QtGui.QCheckBox(self.groupBox)
        self.g5.setGeometry(QtCore.QRect(60, 140, 70, 17))
        self.g5.setObjectName(_fromUtf8("g5"))
        self.g6 = QtGui.QCheckBox(self.groupBox)
        self.g6.setGeometry(QtCore.QRect(60, 170, 70, 17))
        self.g6.setObjectName(_fromUtf8("g6"))
        self.g7 = QtGui.QCheckBox(self.groupBox)
        self.g7.setGeometry(QtCore.QRect(60, 200, 70, 17))
        self.g7.setObjectName(_fromUtf8("g7"))
        self.g8 = QtGui.QCheckBox(self.groupBox)
        self.g8.setGeometry(QtCore.QRect(60, 230, 70, 17))
        self.g8.setObjectName(_fromUtf8("g8"))
        self.g13 = QtGui.QCheckBox(self.groupBox)
        self.g13.setGeometry(QtCore.QRect(160, 140, 70, 17))
        self.g13.setObjectName(_fromUtf8("g13"))
        self.g9 = QtGui.QCheckBox(self.groupBox)
        self.g9.setGeometry(QtCore.QRect(160, 20, 70, 17))
        self.g9.setObjectName(_fromUtf8("g9"))
        self.g12 = QtGui.QCheckBox(self.groupBox)
        self.g12.setGeometry(QtCore.QRect(160, 110, 70, 17))
        self.g12.setObjectName(_fromUtf8("g12"))
        self.g11 = QtGui.QCheckBox(self.groupBox)
        self.g11.setGeometry(QtCore.QRect(160, 80, 91, 17))
        self.g11.setObjectName(_fromUtf8("g11"))
        self.g10 = QtGui.QCheckBox(self.groupBox)
        self.g10.setGeometry(QtCore.QRect(160, 50, 70, 17))
        self.g10.setObjectName(_fromUtf8("g10"))
        self.g16 = QtGui.QCheckBox(self.groupBox)
        self.g16.setGeometry(QtCore.QRect(160, 230, 70, 17))
        self.g16.setObjectName(_fromUtf8("g16"))
        self.g14 = QtGui.QCheckBox(self.groupBox)
        self.g14.setGeometry(QtCore.QRect(160, 170, 70, 17))
        self.g14.setObjectName(_fromUtf8("g14"))
        self.g15 = QtGui.QCheckBox(self.groupBox)
        self.g15.setGeometry(QtCore.QRect(160, 200, 70, 17))
        self.g15.setObjectName(_fromUtf8("g15"))
        self.g17 = QtGui.QCheckBox(self.groupBox)
        self.g17.setGeometry(QtCore.QRect(110, 250, 70, 17))
        self.g17.setObjectName(_fromUtf8("g17"))
        self.genres.append(self.g1)
        self.genres.append(self.g2)
        self.genres.append(self.g3)
        self.genres.append(self.g4)
        self.genres.append(self.g5)
        self.genres.append(self.g6)
        self.genres.append(self.g7)
        self.genres.append(self.g8)
        self.genres.append(self.g9)
        self.genres.append(self.g10)
        self.genres.append(self.g11)
        self.genres.append(self.g12)
        self.genres.append(self.g13)
        self.genres.append(self.g14)
        self.genres.append(self.g15)
        self.genres.append(self.g16)
        self.genres.append(self.g17)

        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(325, 200, 155, 200))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.lbl_type = QtGui.QLabel(self.groupBox_2)
        self.lbl_type.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.lbl_type.setObjectName(_fromUtf8("lbl_type"))
        self.cb_types = QtGui.QComboBox(self.groupBox_2)
        self.cb_types.setGeometry(QtCore.QRect(20, 40, 115, 22))
        self.cb_types.setObjectName(_fromUtf8("cb_types"))
        self.cb_types.addItem("Movie")
        self.cb_types.addItem("Music")
        self.cb_types.addItem("ONA")
        self.cb_types.addItem("OVA")
        self.cb_types.addItem("Special")
        self.cb_types.addItem("TV")

        self.lbl_source = QtGui.QLabel(self.groupBox_2)
        self.lbl_source.setGeometry(QtCore.QRect(20, 80, 46, 13))
        self.lbl_source.setObjectName(_fromUtf8("lbl_source"))
        self.cb_sources = QtGui.QComboBox(self.groupBox_2)
        self.cb_sources.setGeometry(QtCore.QRect(20, 100, 115, 22))
        self.cb_sources.setObjectName(_fromUtf8("cb_sources"))
        self.cb_sources.addItem("4-Koma manga")
        self.cb_sources.addItem("Book")
        self.cb_sources.addItem("Card game")
        self.cb_sources.addItem("Digital manga")
        self.cb_sources.addItem("Game")
        self.cb_sources.addItem("Light novel")
        self.cb_sources.addItem("Manga")
        self.cb_sources.addItem("Music")
        self.cb_sources.addItem("Novel")
        self.cb_sources.addItem("Original")
        self.cb_sources.addItem("Other")
        self.cb_sources.addItem("Picture book")
        self.cb_sources.addItem("Radio")
        self.cb_sources.addItem("Visual novel")
        self.cb_sources.addItem("Web manga")

        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 100, 460, 100))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.lbl_popularity = QtGui.QLabel(self.groupBox_3)
        self.lbl_popularity.setGeometry(QtCore.QRect(10, 30, 145, 16))
        self.lbl_popularity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_popularity.setObjectName(_fromUtf8("lbl_popularity"))
        self.lbl_score = QtGui.QLabel(self.groupBox_3)
        self.lbl_score.setGeometry(QtCore.QRect(157, 30, 145, 13))
        self.lbl_score.setObjectName(_fromUtf8("lbl_score"))
        self.lbl_favorites = QtGui.QLabel(self.groupBox_3)
        self.lbl_favorites.setGeometry(QtCore.QRect(304, 30, 145, 13))
        self.lbl_favorites.setObjectName(_fromUtf8("lbl_favorites"))

        self.tbx_popularity = QtGui.QLineEdit(self.groupBox_3)
        self.tbx_popularity.setEnabled(False)
        self.tbx_popularity.setGeometry(QtCore.QRect(10, 50, 145, 20))
        self.tbx_popularity.setObjectName(_fromUtf8("tbx_popularity"))

        self.tbx_score = QtGui.QLineEdit(self.groupBox_3)
        self.tbx_score.setEnabled(False)
        self.tbx_score.setGeometry(QtCore.QRect(157, 50, 145, 20))
        self.tbx_score.setObjectName(_fromUtf8("tbx_score"))

        self.tbx_favorites = QtGui.QLineEdit(self.groupBox_3)
        self.tbx_favorites.setEnabled(False)
        self.tbx_favorites.setGeometry(QtCore.QRect(304, 50, 145, 20))
        self.tbx_favorites.setObjectName(_fromUtf8("tbx_favorites"))

        self.predict = QtGui.QPushButton(self.centralwidget)
        self.predict.setGeometry(QtCore.QRect(325, 405, 155, 40))
        self.predict.setObjectName(_fromUtf8("predict"))
        self.clear = QtGui.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(325, 450, 155, 25))
        self.clear.setObjectName(_fromUtf8("clear"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.lbl_date = QtGui.QLabel(self.groupBox_2)
        self.lbl_date.setGeometry(QtCore.QRect(20, 140, 115, 13))
        self.lbl_date.setObjectName(_fromUtf8("lbl_date"))
        self.spb_date = QtGui.QSpinBox(self.groupBox_2)
        self.spb_date.setGeometry(QtCore.QRect(20, 160, 115, 22))
        self.spb_date.setObjectName(_fromUtf8("date"))
        self.spb_date.setMinimum(1942)
        self.spb_date.setMaximum(2018)
        self.spb_date.setValue(2018)
        self.retranslateUi(MainWindow)

        #LOGICA DE LAS CONEXIONES
        self.clear.clicked.connect(lambda: self.Clear())
        self.predict.clicked.connect(lambda: self.Predict())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Predict(self):
        X = [self.spb_date.value(),self.cb_types.currentIndex(),self.cb_sources.currentIndex()]
        import numpy as np
        for checkbox_widget in self.genres:
            X.append(1 if checkbox_widget.isChecked() else 0)
        res = self.regressors.BGR_predict(np.array(X).reshape(1,-1))
        self.tbx_popularity.setText(str(np.abs(int(res[0,0]))))
        self.tbx_score.setText(str(np.abs(res[0,1].round(2))))
        self.tbx_favorites.setText(str(np.abs(int(res[0,2]))))

    def Clear(self):
        for checkbox_widget in self.genres:
            if checkbox_widget.isChecked():
                checkbox_widget.click()
        self.tbx_popularity.setText('0')
        self.tbx_favorites.setText('0')
        self.tbx_score.setText('0')

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Anime Genie", None))
        self.groupBox.setTitle(_translate("MainWindow", "Genres", None))
        self.g1.setText(_translate("MainWindow", "Romance", None))
        self.g2.setText(_translate("MainWindow", "Shoujo", None))
        self.g3.setText(_translate("MainWindow", "Ecchi", None))
        self.g4.setText(_translate("MainWindow", "Sports", None))
        self.g5.setText(_translate("MainWindow", "Sci-Fi", None))
        self.g6.setText(_translate("MainWindow", "Action", None))
        self.g7.setText(_translate("MainWindow", "Shounen", None))
        self.g8.setText(_translate("MainWindow", "Comedy", None))
        self.g13.setText(_translate("MainWindow", "Historical", None))
        self.g9.setText(_translate("MainWindow", "Fantasy", None))
        self.g12.setText(_translate("MainWindow", "Gore", None))
        self.g11.setText(_translate("MainWindow", "Supernatural", None))
        self.g10.setText(_translate("MainWindow", "Music", None))
        self.g16.setText(_translate("MainWindow", "Hentai", None))
        self.g14.setText(_translate("MainWindow", "Thriller", None))
        self.g15.setText(_translate("MainWindow", "Mistery", None))
        self.g17.setText(_translate("MainWindow", "Another(s)", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Aditional parameters", None))
        self.lbl_type.setText(_translate("MainWindow", "Type", None))
        self.lbl_source.setText(_translate("MainWindow", "Source", None))
        self.lbl_date.setText(_translate("MainWindow", "Predict based on year:", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Results", None))
        self.lbl_popularity.setText(_translate("MainWindow", "Popularity", None))
        self.lbl_score.setText(_translate("MainWindow", "Score", None))
        self.lbl_favorites.setText(_translate("MainWindow", "Favorites", None))
        self.predict.setText(_translate("MainWindow", "Predict!", None))
        self.clear.setText(_translate("MainWindow", "Clear", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
