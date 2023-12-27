# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\select_image_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImgSelectWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 820)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_window_frame = QtWidgets.QFrame(self.centralwidget)
        self.add_window_frame.setGeometry(QtCore.QRect(10, 0, 1041, 801))
        self.add_window_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_window_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_window_frame.setObjectName("add_window_frame")
        self.flash_card_options = QtWidgets.QComboBox(self.add_window_frame)
        self.flash_card_options.setGeometry(QtCore.QRect(146, 30, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.flash_card_options.setFont(font)
        self.flash_card_options.setAutoFillBackground(False)
        self.flash_card_options.setDuplicatesEnabled(False)
        self.flash_card_options.setFrame(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        #self.flash_card_options.setCurrentFont(font)
        self.flash_card_options.addItem("Image Occlusion")
        self.flash_card_options.addItem("Basic")
        self.flash_card_options.addItem("Basic (and Reversed card)")
        self.flash_card_options.setObjectName("flash_card_options")
        self.Deck_Options = QtWidgets.QComboBox(self.add_window_frame)
        self.Deck_Options.setGeometry(QtCore.QRect(600, 30, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Deck_Options.setFont(font)
        self.Deck_Options.setAutoFillBackground(False)
        self.Deck_Options.setDuplicatesEnabled(False)
        self.Deck_Options.setFrame(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        #self.Deck_Options.setCurrentFont(font)
        self.Deck_Options.setObjectName("Deck_Options")
        self.deck_label = QtWidgets.QLabel(self.add_window_frame)
        self.deck_label.setGeometry(QtCore.QRect(550, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.deck_label.setFont(font)
        self.deck_label.setObjectName("deck_label")
        self.flashcard_type_label = QtWidgets.QLabel(self.add_window_frame)
        self.flashcard_type_label.setGeometry(QtCore.QRect(10, 30, 136, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.flashcard_type_label.setFont(font)
        self.flashcard_type_label.setObjectName("flashcard_type_label")
        self.groupBox = QtWidgets.QGroupBox(self.add_window_frame)
        self.groupBox.setGeometry(QtCore.QRect(20, 90, 991, 71))
        self.groupBox.setObjectName("groupBox")
        self.setting_button = QtWidgets.QToolButton(self.groupBox)
        self.setting_button.setGeometry(QtCore.QRect(10, 20, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\images\setting_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_button.setIcon(icon)
        self.setting_button.setObjectName("setting_button")
        self.bold_button = QtWidgets.QToolButton(self.groupBox)
        self.bold_button.setGeometry(QtCore.QRect(70, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bold_button.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\images\Bold_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bold_button.setIcon(icon1)
        self.bold_button.setObjectName("bold_button")
        self.italic_button = QtWidgets.QToolButton(self.groupBox)
        self.italic_button.setGeometry(QtCore.QRect(110, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.italic_button.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\images\Italic_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.italic_button.setIcon(icon2)
        self.italic_button.setObjectName("italic_button")
        self.underline_button = QtWidgets.QToolButton(self.groupBox)
        self.underline_button.setGeometry(QtCore.QRect(150, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.underline_button.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\images\\Underline_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.underline_button.setIcon(icon3)
        self.underline_button.setObjectName("underline_button")
        self.font_color_button = QtWidgets.QToolButton(self.groupBox)
        self.font_color_button.setGeometry(QtCore.QRect(380, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.font_color_button.setFont(font)
        self.font_color_button.setMouseTracking(True)
        self.font_color_button.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.font_color_button.setObjectName("font_color_button")
        self.highlight_button = QtWidgets.QToolButton(self.groupBox)
        self.highlight_button.setGeometry(QtCore.QRect(430, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.highlight_button.setFont(font)
        self.highlight_button.setMouseTracking(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\images\highlight_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.highlight_button.setIcon(icon4)
        self.highlight_button.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.highlight_button.setObjectName("highlight_button")
        self.bullete_button = QtWidgets.QToolButton(self.groupBox)
        self.bullete_button.setGeometry(QtCore.QRect(530, 20, 31, 31))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\images\\bullet_list_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bullete_button.setIcon(icon5)
        self.bullete_button.setObjectName("bullete_button")
        self.numbered_buttton = QtWidgets.QToolButton(self.groupBox)
        self.numbered_buttton.setGeometry(QtCore.QRect(570, 20, 31, 31))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\images\\numeric_list_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.numbered_buttton.setIcon(icon6)
        self.numbered_buttton.setObjectName("numbered_buttton")
        self.left_align_button = QtWidgets.QToolButton(self.groupBox)
        self.left_align_button.setGeometry(QtCore.QRect(620, 20, 31, 31))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(".\images\\left_align_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_align_button.setIcon(icon7)
        self.left_align_button.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.left_align_button.setObjectName("left_align_button")
        self.image_insert_button = QtWidgets.QToolButton(self.groupBox)
        self.image_insert_button.setGeometry(QtCore.QRect(770, 20, 31, 31))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(".\images\\attach_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.image_insert_button.setIcon(icon8)
        self.image_insert_button.setObjectName("image_insert_button")
        self.equation_button = QtWidgets.QToolButton(self.groupBox)
        self.equation_button.setGeometry(QtCore.QRect(860, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.equation_button.setFont(font)
        self.equation_button.setObjectName("equation_button")
        self.audio_button = QtWidgets.QToolButton(self.groupBox)
        self.audio_button.setGeometry(QtCore.QRect(810, 20, 31, 31))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(".\images\\mike_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.audio_button.setIcon(icon9)
        self.audio_button.setObjectName("audio_button")
        self.center_align_button = QtWidgets.QToolButton(self.groupBox)
        self.center_align_button.setGeometry(QtCore.QRect(660, 20, 31, 31))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(".\images\\center_align_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.center_align_button.setIcon(icon10)
        self.center_align_button.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.center_align_button.setObjectName("center_align_button")
        self.right_align_button = QtWidgets.QToolButton(self.groupBox)
        self.right_align_button.setGeometry(QtCore.QRect(700, 20, 31, 31))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(".\images\\right_align_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right_align_button.setIcon(icon11)
        self.right_align_button.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.right_align_button.setObjectName("right_align_button")
        self.font_style_combobox = QtWidgets.QFontComboBox(self.groupBox)
        self.font_style_combobox.setGeometry(QtCore.QRect(250, 20, 111, 31))
        self.font_style_combobox.setObjectName("font_style_combobox")
        self.font_size_spin = QtWidgets.QSpinBox(self.groupBox)
        self.font_size_spin.setGeometry(QtCore.QRect(200, 20, 42, 31))
        self.font_size_spin.setObjectName("font_size_spin")
        self.font_size_spin.setValue(8)
        self.select_image_button = QtWidgets.QPushButton(self.add_window_frame)
        self.select_image_button.setGeometry(QtCore.QRect(430, 260, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.select_image_button.setFont(font)
        self.select_image_button.setObjectName("select_image_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Add FlashCard", "Add FlashCard"))
        self.deck_label.setText(_translate("MainWindow", "Deck:"))
        self.flashcard_type_label.setText(_translate("MainWindow", "FlashCard Type:"))
        self.groupBox.setTitle(_translate("MainWindow", "ToolBox"))
        self.setting_button.setText(_translate("MainWindow", "..."))
        self.bold_button.setText(_translate("MainWindow", "B"))
        self.italic_button.setText(_translate("MainWindow", "I"))
        self.underline_button.setText(_translate("MainWindow", "U"))
        self.font_color_button.setText(_translate("MainWindow", "A"))
        self.highlight_button.setText(_translate("MainWindow", "H"))
        self.bullete_button.setText(_translate("MainWindow", "."))
        self.numbered_buttton.setText(_translate("MainWindow", "1"))
        self.left_align_button.setText(_translate("MainWindow", "l.ali"))
        self.image_insert_button.setText(_translate("MainWindow", "f"))
        self.equation_button.setText(_translate("MainWindow", "fx"))
        self.audio_button.setText(_translate("MainWindow", "adi"))
        self.center_align_button.setText(_translate("MainWindow", "r.ali"))
        self.right_align_button.setText(_translate("MainWindow", "c.ali"))
        self.select_image_button.setText(_translate("MainWindow", "Select Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ImgSelectWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
