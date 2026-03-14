# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTimeEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(700, 480)
        Main.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        Main.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.gridLayout_2 = QGridLayout(self.mainPage)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.leftColumn = QVBoxLayout()
        self.leftColumn.setObjectName(u"leftColumn")
        self.leftColumn.setContentsMargins(3, 3, 3, 3)
        self.passwordsList = QListWidget(self.mainPage)
        self.passwordsList.setObjectName(u"passwordsList")
        font = QFont()
        font.setPointSize(10)
        self.passwordsList.setFont(font)

        self.leftColumn.addWidget(self.passwordsList)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.addButton = QPushButton(self.mainPage)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/resources/icons/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addButton.setIcon(icon)
        self.addButton.setIconSize(QSize(17, 17))

        self.buttonsLayout.addWidget(self.addButton)

        self.removeButton = QPushButton(self.mainPage)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/icons/minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.removeButton.setIcon(icon1)
        self.removeButton.setIconSize(QSize(17, 17))

        self.buttonsLayout.addWidget(self.removeButton)

        self.buttonsHorizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.buttonsHorizontalSpacer)

        self.mainSettingButton = QPushButton(self.mainPage)
        self.mainSettingButton.setObjectName(u"mainSettingButton")
        self.mainSettingButton.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/icons/gear.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mainSettingButton.setIcon(icon2)
        self.mainSettingButton.setIconSize(QSize(17, 17))

        self.buttonsLayout.addWidget(self.mainSettingButton)


        self.leftColumn.addLayout(self.buttonsLayout)


        self.mainLayout.addLayout(self.leftColumn)

        self.rightColumn = QStackedWidget(self.mainPage)
        self.rightColumn.setObjectName(u"rightColumn")
        self.selectedPasswordRightColumn = QWidget()
        self.selectedPasswordRightColumn.setObjectName(u"selectedPasswordRightColumn")
        self.verticalLayout_6 = QVBoxLayout(self.selectedPasswordRightColumn)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.passwordEnter = QLineEdit(self.selectedPasswordRightColumn)
        self.passwordEnter.setObjectName(u"passwordEnter")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordEnter.sizePolicy().hasHeightForWidth())
        self.passwordEnter.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.passwordEnter.setFont(font1)
        self.passwordEnter.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordEnter.setClearButtonEnabled(True)

        self.verticalLayout_6.addWidget(self.passwordEnter)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.submitPasswordButton = QPushButton(self.selectedPasswordRightColumn)
        self.submitPasswordButton.setObjectName(u"submitPasswordButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.submitPasswordButton.sizePolicy().hasHeightForWidth())
        self.submitPasswordButton.setSizePolicy(sizePolicy1)
        self.submitPasswordButton.setMaximumSize(QSize(16777215, 16777215))
        self.submitPasswordButton.setBaseSize(QSize(0, 0))
        self.submitPasswordButton.setFont(font1)
        self.submitPasswordButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_4.addWidget(self.submitPasswordButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.correctLabel = QLabel(self.selectedPasswordRightColumn)
        self.correctLabel.setObjectName(u"correctLabel")
        self.correctLabel.setFont(font1)

        self.verticalLayout_6.addWidget(self.correctLabel)

        self.wrongLabel = QLabel(self.selectedPasswordRightColumn)
        self.wrongLabel.setObjectName(u"wrongLabel")
        self.wrongLabel.setFont(font1)

        self.verticalLayout_6.addWidget(self.wrongLabel)

        self.successRateLabel = QLabel(self.selectedPasswordRightColumn)
        self.successRateLabel.setObjectName(u"successRateLabel")
        self.successRateLabel.setFont(font1)

        self.verticalLayout_6.addWidget(self.successRateLabel)

        self.lastAttemptLabel = QLabel(self.selectedPasswordRightColumn)
        self.lastAttemptLabel.setObjectName(u"lastAttemptLabel")
        self.lastAttemptLabel.setFont(font1)

        self.verticalLayout_6.addWidget(self.lastAttemptLabel)

        self.reminderLabel = QLabel(self.selectedPasswordRightColumn)
        self.reminderLabel.setObjectName(u"reminderLabel")
        self.reminderLabel.setFont(font1)

        self.verticalLayout_6.addWidget(self.reminderLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.hintButton = QPushButton(self.selectedPasswordRightColumn)
        self.hintButton.setObjectName(u"hintButton")
        font2 = QFont()
        font2.setPointSize(11)
        self.hintButton.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/icons/resources/icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.hintButton.setIcon(icon3)
        self.hintButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.hintButton)

        self.currentPasswordSettingsButton = QPushButton(self.selectedPasswordRightColumn)
        self.currentPasswordSettingsButton.setObjectName(u"currentPasswordSettingsButton")
        self.currentPasswordSettingsButton.setIcon(icon2)
        self.currentPasswordSettingsButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.currentPasswordSettingsButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.rightColumn.addWidget(self.selectedPasswordRightColumn)
        self.noSelectRightColumn = QWidget()
        self.noSelectRightColumn.setObjectName(u"noSelectRightColumn")
        self.verticalLayout_5 = QVBoxLayout(self.noSelectRightColumn)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.noSelectRightColumn)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.verticalLayout_5.addWidget(self.label)

        self.rightColumn.addWidget(self.noSelectRightColumn)
        self.editPageRightColumn = QWidget()
        self.editPageRightColumn.setObjectName(u"editPageRightColumn")
        self.verticalLayout_2 = QVBoxLayout(self.editPageRightColumn)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.editHint = QPlainTextEdit(self.editPageRightColumn)
        self.editHint.setObjectName(u"editHint")
        self.editHint.setFont(font1)

        self.verticalLayout_2.addWidget(self.editHint)

        self.editTime = QTimeEdit(self.editPageRightColumn)
        self.editTime.setObjectName(u"editTime")
        self.editTime.setFont(font1)

        self.verticalLayout_2.addWidget(self.editTime)

        self.editReminderNoReminders = QRadioButton(self.editPageRightColumn)
        self.editReminderNoReminders.setObjectName(u"editReminderNoReminders")
        self.editReminderNoReminders.setFont(font1)

        self.verticalLayout_2.addWidget(self.editReminderNoReminders)

        self.editReminderAfterStart = QRadioButton(self.editPageRightColumn)
        self.editReminderAfterStart.setObjectName(u"editReminderAfterStart")
        self.editReminderAfterStart.setFont(font1)

        self.verticalLayout_2.addWidget(self.editReminderAfterStart)

        self.editReminderEveryday = QRadioButton(self.editPageRightColumn)
        self.editReminderEveryday.setObjectName(u"editReminderEveryday")
        self.editReminderEveryday.setFont(font1)

        self.verticalLayout_2.addWidget(self.editReminderEveryday)

        self.editReminderWeek = QRadioButton(self.editPageRightColumn)
        self.editReminderWeek.setObjectName(u"editReminderWeek")
        self.editReminderWeek.setFont(font1)

        self.verticalLayout_2.addWidget(self.editReminderWeek)

        self.editReminderMonth = QRadioButton(self.editPageRightColumn)
        self.editReminderMonth.setObjectName(u"editReminderMonth")
        self.editReminderMonth.setFont(font1)

        self.verticalLayout_2.addWidget(self.editReminderMonth)

        self.editConfirmButton = QPushButton(self.editPageRightColumn)
        self.editConfirmButton.setObjectName(u"editConfirmButton")
        self.editConfirmButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.editConfirmButton)

        self.editCancelButton = QPushButton(self.editPageRightColumn)
        self.editCancelButton.setObjectName(u"editCancelButton")
        self.editCancelButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.editCancelButton)

        self.rightColumn.addWidget(self.editPageRightColumn)

        self.mainLayout.addWidget(self.rightColumn)

        self.mainLayout.setStretch(0, 2)
        self.mainLayout.setStretch(1, 4)

        self.gridLayout_2.addLayout(self.mainLayout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.mainPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_7 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBoxAutostart = QCheckBox(self.settingsPage)
        self.checkBoxAutostart.setObjectName(u"checkBoxAutostart")
        self.checkBoxAutostart.setFont(font1)

        self.verticalLayout_3.addWidget(self.checkBoxAutostart)

        self.checkBoxTray = QCheckBox(self.settingsPage)
        self.checkBoxTray.setObjectName(u"checkBoxTray")
        self.checkBoxTray.setFont(font1)
        self.checkBoxTray.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBoxTray)

        self.checkBoxStartMinimized = QCheckBox(self.settingsPage)
        self.checkBoxStartMinimized.setObjectName(u"checkBoxStartMinimized")
        self.checkBoxStartMinimized.setFont(font1)

        self.verticalLayout_3.addWidget(self.checkBoxStartMinimized)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.retunSettingsButton = QPushButton(self.settingsPage)
        self.retunSettingsButton.setObjectName(u"retunSettingsButton")
        self.retunSettingsButton.setFont(font1)

        self.verticalLayout_7.addWidget(self.retunSettingsButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.settingsPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout.addWidget(self.label_3)

        self.infoSettingsButton = QPushButton(self.settingsPage)
        self.infoSettingsButton.setObjectName(u"infoSettingsButton")
        sizePolicy1.setHeightForWidth(self.infoSettingsButton.sizePolicy().hasHeightForWidth())
        self.infoSettingsButton.setSizePolicy(sizePolicy1)
        self.infoSettingsButton.setFont(font1)

        self.horizontalLayout.addWidget(self.infoSettingsButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.settingsPage)
        self.addPasswordPage = QWidget()
        self.addPasswordPage.setObjectName(u"addPasswordPage")
        self.gridLayout_3 = QGridLayout(self.addPasswordPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addPasswordInput = QLineEdit(self.addPasswordPage)
        self.addPasswordInput.setObjectName(u"addPasswordInput")
        self.addPasswordInput.setFont(font1)
        self.addPasswordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.addPasswordInput.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.addPasswordInput)

        self.addPasswordInputConfirm = QLineEdit(self.addPasswordPage)
        self.addPasswordInputConfirm.setObjectName(u"addPasswordInputConfirm")
        self.addPasswordInputConfirm.setFont(font1)
        self.addPasswordInputConfirm.setEchoMode(QLineEdit.EchoMode.Password)
        self.addPasswordInputConfirm.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.addPasswordInputConfirm)

        self.addPasswordHint = QPlainTextEdit(self.addPasswordPage)
        self.addPasswordHint.setObjectName(u"addPasswordHint")
        self.addPasswordHint.setFont(font2)

        self.verticalLayout.addWidget(self.addPasswordHint)

        self.label_2 = QLabel(self.addPasswordPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.addPasswordRemiderTime = QTimeEdit(self.addPasswordPage)
        self.addPasswordRemiderTime.setObjectName(u"addPasswordRemiderTime")
        self.addPasswordRemiderTime.setFont(font1)

        self.verticalLayout.addWidget(self.addPasswordRemiderTime)

        self.addPasswordRadioButtonNoReminders = QRadioButton(self.addPasswordPage)
        self.addPasswordRadioButtonNoReminders.setObjectName(u"addPasswordRadioButtonNoReminders")
        self.addPasswordRadioButtonNoReminders.setFont(font1)
        self.addPasswordRadioButtonNoReminders.setChecked(True)

        self.verticalLayout.addWidget(self.addPasswordRadioButtonNoReminders)

        self.addPasswordRadioButtonAfterStart = QRadioButton(self.addPasswordPage)
        self.addPasswordRadioButtonAfterStart.setObjectName(u"addPasswordRadioButtonAfterStart")
        self.addPasswordRadioButtonAfterStart.setFont(font1)

        self.verticalLayout.addWidget(self.addPasswordRadioButtonAfterStart)

        self.addPasswordRadioButtonEveryday = QRadioButton(self.addPasswordPage)
        self.addPasswordRadioButtonEveryday.setObjectName(u"addPasswordRadioButtonEveryday")
        self.addPasswordRadioButtonEveryday.setFont(font1)

        self.verticalLayout.addWidget(self.addPasswordRadioButtonEveryday)

        self.addPasswordRadioButtonWeek = QRadioButton(self.addPasswordPage)
        self.addPasswordRadioButtonWeek.setObjectName(u"addPasswordRadioButtonWeek")
        self.addPasswordRadioButtonWeek.setFont(font1)

        self.verticalLayout.addWidget(self.addPasswordRadioButtonWeek)

        self.addPasswordRadioButtonMonth = QRadioButton(self.addPasswordPage)
        self.addPasswordRadioButtonMonth.setObjectName(u"addPasswordRadioButtonMonth")
        self.addPasswordRadioButtonMonth.setFont(font1)

        self.verticalLayout.addWidget(self.addPasswordRadioButtonMonth)

        self.addPasswordConfirmButton = QPushButton(self.addPasswordPage)
        self.addPasswordConfirmButton.setObjectName(u"addPasswordConfirmButton")
        self.addPasswordConfirmButton.setFont(font1)

        self.verticalLayout.addWidget(self.addPasswordConfirmButton)

        self.addPasswordCancelButton = QPushButton(self.addPasswordPage)
        self.addPasswordCancelButton.setObjectName(u"addPasswordCancelButton")
        self.addPasswordCancelButton.setFont(font1)

        self.verticalLayout.addWidget(self.addPasswordCancelButton)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.addPasswordPage)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Remember your passwords", None))
        self.addButton.setText("")
        self.removeButton.setText("")
        self.mainSettingButton.setText("")
        self.passwordEnter.setPlaceholderText(QCoreApplication.translate("Main", u"Enter password", None))
        self.submitPasswordButton.setText(QCoreApplication.translate("Main", u"Submit", None))
        self.correctLabel.setText(QCoreApplication.translate("Main", u"Correct: ", None))
        self.wrongLabel.setText(QCoreApplication.translate("Main", u"Wrong: ", None))
        self.successRateLabel.setText(QCoreApplication.translate("Main", u"Success rate:", None))
        self.lastAttemptLabel.setText(QCoreApplication.translate("Main", u"Last attempt: ", None))
        self.reminderLabel.setText(QCoreApplication.translate("Main", u"Reminder: ", None))
        self.hintButton.setText(QCoreApplication.translate("Main", u"Hint", None))
        self.currentPasswordSettingsButton.setText("")
        self.label.setText(QCoreApplication.translate("Main", u"Select or add password", None))
        self.editReminderNoReminders.setText(QCoreApplication.translate("Main", u"No reminders", None))
        self.editReminderAfterStart.setText(QCoreApplication.translate("Main", u"After start", None))
        self.editReminderEveryday.setText(QCoreApplication.translate("Main", u"Everyday", None))
        self.editReminderWeek.setText(QCoreApplication.translate("Main", u"Once a week", None))
        self.editReminderMonth.setText(QCoreApplication.translate("Main", u"Once a month", None))
        self.editConfirmButton.setText(QCoreApplication.translate("Main", u"Confirm", None))
        self.editCancelButton.setText(QCoreApplication.translate("Main", u"Cancel", None))
#if QT_CONFIG(tooltip)
        self.checkBoxAutostart.setToolTip(QCoreApplication.translate("Main", u"Requires admin privileges (Task Scheduler)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxAutostart.setText(QCoreApplication.translate("Main", u"Autostart on boot", None))
        self.checkBoxTray.setText(QCoreApplication.translate("Main", u"Minimize to tray instead of closing", None))
        self.checkBoxStartMinimized.setText(QCoreApplication.translate("Main", u"Start minimized", None))
        self.retunSettingsButton.setText(QCoreApplication.translate("Main", u"Return", None))
        self.label_3.setText(QCoreApplication.translate("Main", u"https://github.com/xEska1337/remember-your-passwords", None))
        self.infoSettingsButton.setText(QCoreApplication.translate("Main", u"Info", None))
        self.addPasswordInput.setPlaceholderText(QCoreApplication.translate("Main", u"Password", None))
        self.addPasswordInputConfirm.setPlaceholderText(QCoreApplication.translate("Main", u"Confirm password", None))
        self.addPasswordHint.setPlaceholderText(QCoreApplication.translate("Main", u"Hint", None))
        self.label_2.setText(QCoreApplication.translate("Main", u"Reminder", None))
        self.addPasswordRadioButtonNoReminders.setText(QCoreApplication.translate("Main", u"No reminders", None))
        self.addPasswordRadioButtonAfterStart.setText(QCoreApplication.translate("Main", u"After start", None))
        self.addPasswordRadioButtonEveryday.setText(QCoreApplication.translate("Main", u"Everyday", None))
        self.addPasswordRadioButtonWeek.setText(QCoreApplication.translate("Main", u"Once a week", None))
        self.addPasswordRadioButtonMonth.setText(QCoreApplication.translate("Main", u"Once a month", None))
        self.addPasswordConfirmButton.setText(QCoreApplication.translate("Main", u"Add", None))
        self.addPasswordCancelButton.setText(QCoreApplication.translate("Main", u"Cancel", None))
    # retranslateUi

