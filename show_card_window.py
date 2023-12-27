# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\show_card_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_show_card_window(object):
    def setupUi(self, show_card_window):
        show_card_window.setObjectName("show_card_window")
        show_card_window.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(show_card_window)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 801, 661))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.deck_button = QtWidgets.QPushButton(self.frame)
        self.deck_button.setGeometry(QtCore.QRect(220, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.deck_button.setFont(font)
        self.deck_button.setAutoFillBackground(False)
        self.deck_button.setObjectName("deck_button")
        self.add_button = QtWidgets.QPushButton(self.frame)
        self.add_button.setGeometry(QtCore.QRect(330, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.stat_button = QtWidgets.QPushButton(self.frame)
        self.stat_button.setGeometry(QtCore.QRect(490, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stat_button.setFont(font)
        self.stat_button.setObjectName("stat_button")
        self.dark_mode_radio_button = QtWidgets.QRadioButton(self.frame)
        self.dark_mode_radio_button.setGeometry(QtCore.QRect(680, 50, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.dark_mode_radio_button.setFont(font)
        self.dark_mode_radio_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dark_mode_radio_button.setChecked(False)
        self.dark_mode_radio_button.setObjectName("dark_mode_radio_button")
        self.deck_name_label = QtWidgets.QLabel(self.frame)
        self.deck_name_label.setGeometry(QtCore.QRect(290, 110, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deck_name_label.setFont(font)
        self.deck_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.deck_name_label.setObjectName("deck_name_label")
        self.new_deck_label = QtWidgets.QLabel(self.frame)
        self.new_deck_label.setGeometry(QtCore.QRect(160, 200, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_deck_label.setFont(font)
        self.new_deck_label.setObjectName("new_deck_label")
        self.to_review_label = QtWidgets.QLabel(self.frame)
        self.to_review_label.setGeometry(QtCore.QRect(160, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.to_review_label.setFont(font)
        self.to_review_label.setObjectName("to_review_label")
        self.learning_Label = QtWidgets.QLabel(self.frame)
        self.learning_Label.setGeometry(QtCore.QRect(160, 240, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.learning_Label.setFont(font)
        self.learning_Label.setObjectName("learning_Label")
        self.new_entry_label = QtWidgets.QLabel(self.frame)
        self.new_entry_label.setGeometry(QtCore.QRect(260, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_entry_label.setFont(font)
        self.new_entry_label.setObjectName("new_entry_label")
        self.learnig_entry_label_2 = QtWidgets.QLabel(self.frame)
        self.learnig_entry_label_2.setGeometry(QtCore.QRect(260, 240, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.learnig_entry_label_2.setFont(font)
        self.learnig_entry_label_2.setObjectName("learnig_entry_label_2")
        self.to_review_entry_label = QtWidgets.QLabel(self.frame)
        self.to_review_entry_label.setGeometry(QtCore.QRect(260, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.to_review_entry_label.setFont(font)
        self.to_review_entry_label.setObjectName("to_review_entry_label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(460, 230, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        show_card_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(show_card_window)
        QtCore.QMetaObject.connectSlotsByName(show_card_window)

    def retranslateUi(self, show_card_window):
        _translate = QtCore.QCoreApplication.translate
        show_card_window.setWindowTitle(_translate("show_card_window", "Anki-RecallHub"))
        self.deck_button.setText(_translate("show_card_window", "Decks"))
        self.add_button.setText(_translate("show_card_window", "Add Flash Card"))
        self.stat_button.setText(_translate("show_card_window", "Stats"))
        self.dark_mode_radio_button.setText(_translate("show_card_window", "Dark Mode"))
        self.deck_name_label.setText(_translate("show_card_window", "Deck Name "))
        self.new_deck_label.setText(_translate("show_card_window", "New:"))
        self.to_review_label.setText(_translate("show_card_window", "To Review:"))
        self.learning_Label.setText(_translate("show_card_window", "Learning:"))
        self.new_entry_label.setText(_translate("show_card_window", "0"))
        self.learnig_entry_label_2.setText(_translate("show_card_window", "0"))
        self.to_review_entry_label.setText(_translate("show_card_window", "0"))
        self.pushButton.setText(_translate("show_card_window", "Show Cards"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    show_card_window = QtWidgets.QMainWindow()
    ui = Ui_show_card_window()
    ui.setupUi(show_card_window)
    show_card_window.show()
    sys.exit(app.exec_())
