# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1102, 875)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_link = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_link.sizePolicy().hasHeightForWidth())
        self.groupBox_link.setSizePolicy(sizePolicy)
        self.groupBox_link.setObjectName("groupBox_link")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_link)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_10 = QtWidgets.QLabel(self.groupBox_link)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_link)
        self.label_12.setObjectName("label_12")
        self.gridLayout_7.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_link)
        self.label_11.setObjectName("label_11")
        self.gridLayout_7.addWidget(self.label_11, 1, 0, 1, 1)
        self.comboBox_port = QtWidgets.QComboBox(self.groupBox_link)
        self.comboBox_port.setObjectName("comboBox_port")
        self.comboBox_port.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_port, 0, 1, 1, 1)
        self.comboBox_baudrate = QtWidgets.QComboBox(self.groupBox_link)
        self.comboBox_baudrate.setObjectName("comboBox_baudrate")
        self.comboBox_baudrate.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_baudrate, 1, 1, 1, 1)
        self.comboBox_fs = QtWidgets.QComboBox(self.groupBox_link)
        self.comboBox_fs.setObjectName("comboBox_fs")
        self.comboBox_fs.addItem("")
        self.comboBox_fs.addItem("")
        self.comboBox_fs.addItem("")
        self.comboBox_fs.addItem("")
        self.comboBox_fs.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_fs, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_7)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_link)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBox_link)
        self.groupBox_filter0 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_filter0.sizePolicy().hasHeightForWidth())
        self.groupBox_filter0.setSizePolicy(sizePolicy)
        self.groupBox_filter0.setObjectName("groupBox_filter0")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_filter0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_notch_filter = QtWidgets.QCheckBox(self.groupBox_filter0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_notch_filter.sizePolicy().hasHeightForWidth())
        self.checkBox_notch_filter.setSizePolicy(sizePolicy)
        self.checkBox_notch_filter.setText("")
        self.checkBox_notch_filter.setChecked(True)
        self.checkBox_notch_filter.setObjectName("checkBox_notch_filter")
        self.gridLayout_3.addWidget(self.checkBox_notch_filter, 0, 1, 1, 1)
        self.checkBox_filter = QtWidgets.QCheckBox(self.groupBox_filter0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_filter.sizePolicy().hasHeightForWidth())
        self.checkBox_filter.setSizePolicy(sizePolicy)
        self.checkBox_filter.setText("")
        self.checkBox_filter.setChecked(True)
        self.checkBox_filter.setObjectName("checkBox_filter")
        self.gridLayout_3.addWidget(self.checkBox_filter, 1, 1, 1, 1)
        self.groupBox_notch = QtWidgets.QGroupBox(self.groupBox_filter0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_notch.sizePolicy().hasHeightForWidth())
        self.groupBox_notch.setSizePolicy(sizePolicy)
        self.groupBox_notch.setObjectName("groupBox_notch")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_notch)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem1, 2, 2, 1, 1)
        self.spinBox_notch_q_factor = QtWidgets.QSpinBox(self.groupBox_notch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_notch_q_factor.sizePolicy().hasHeightForWidth())
        self.spinBox_notch_q_factor.setSizePolicy(sizePolicy)
        self.spinBox_notch_q_factor.setMinimum(25)
        self.spinBox_notch_q_factor.setMaximum(40)
        self.spinBox_notch_q_factor.setProperty("value", 30)
        self.spinBox_notch_q_factor.setObjectName("spinBox_notch_q_factor")
        self.gridLayout_8.addWidget(self.spinBox_notch_q_factor, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_notch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 3, 0, 1, 1)
        self.comboBox_notch_freq = QtWidgets.QComboBox(self.groupBox_notch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_notch_freq.sizePolicy().hasHeightForWidth())
        self.comboBox_notch_freq.setSizePolicy(sizePolicy)
        self.comboBox_notch_freq.setObjectName("comboBox_notch_freq")
        self.comboBox_notch_freq.addItem("")
        self.comboBox_notch_freq.addItem("")
        self.gridLayout_8.addWidget(self.comboBox_notch_freq, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_notch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem3, 4, 0, 1, 1)
        self.gridLayout_8.setColumnStretch(0, 2)
        self.gridLayout_8.setColumnStretch(1, 2)
        self.gridLayout_8.setColumnStretch(2, 1)
        self.gridLayout_8.setRowStretch(0, 1)
        self.gridLayout_8.setRowStretch(1, 1)
        self.gridLayout_8.setRowStretch(2, 2)
        self.gridLayout_8.setRowStretch(3, 2)
        self.gridLayout_8.setRowStretch(4, 1)
        self.gridLayout_3.addWidget(self.groupBox_notch, 0, 0, 1, 1)
        self.groupBox_filter = QtWidgets.QGroupBox(self.groupBox_filter0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_filter.sizePolicy().hasHeightForWidth())
        self.groupBox_filter.setSizePolicy(sizePolicy)
        self.groupBox_filter.setObjectName("groupBox_filter")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_filter)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.groupBox_filter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.spinBox_filter_order = QtWidgets.QSpinBox(self.groupBox_filter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_filter_order.sizePolicy().hasHeightForWidth())
        self.spinBox_filter_order.setSizePolicy(sizePolicy)
        self.spinBox_filter_order.setMinimum(1)
        self.spinBox_filter_order.setMaximum(10)
        self.spinBox_filter_order.setProperty("value", 4)
        self.spinBox_filter_order.setObjectName("spinBox_filter_order")
        self.horizontalLayout_7.addWidget(self.spinBox_filter_order)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.groupBox_filter_setting = QtWidgets.QGroupBox(self.groupBox_filter)
        self.groupBox_filter_setting.setTitle("")
        self.groupBox_filter_setting.setObjectName("groupBox_filter_setting")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_filter_setting)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.groupBox_filter_freq = QtWidgets.QGroupBox(self.groupBox_filter_setting)
        self.groupBox_filter_freq.setObjectName("groupBox_filter_freq")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_filter_freq)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.spinBox_filter_low_freq = QtWidgets.QDoubleSpinBox(self.groupBox_filter_freq)
        self.spinBox_filter_low_freq.setDecimals(1)
        self.spinBox_filter_low_freq.setObjectName("spinBox_filter_low_freq")
        self.gridLayout_11.addWidget(self.spinBox_filter_low_freq, 1, 1, 1, 1)
        self.spinBox_filter_high_freq = QtWidgets.QDoubleSpinBox(self.groupBox_filter_freq)
        self.spinBox_filter_high_freq.setDecimals(1)
        self.spinBox_filter_high_freq.setObjectName("spinBox_filter_high_freq")
        self.gridLayout_11.addWidget(self.spinBox_filter_high_freq, 0, 1, 1, 1)
        self.label_low = QtWidgets.QLabel(self.groupBox_filter_freq)
        self.label_low.setObjectName("label_low")
        self.gridLayout_11.addWidget(self.label_low, 1, 0, 1, 1)
        self.label_high = QtWidgets.QLabel(self.groupBox_filter_freq)
        self.label_high.setObjectName("label_high")
        self.gridLayout_11.addWidget(self.label_high, 0, 0, 1, 1)
        self.gridLayout_11.setColumnStretch(0, 1)
        self.gridLayout_11.setColumnStretch(1, 2)
        self.gridLayout_13.addWidget(self.groupBox_filter_freq, 1, 1, 1, 1)
        self.widget_filter_type = QtWidgets.QWidget(self.groupBox_filter_setting)
        self.widget_filter_type.setObjectName("widget_filter_type")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_filter_type)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_low = QtWidgets.QRadioButton(self.widget_filter_type)
        self.radioButton_low.setObjectName("radioButton_low")
        self.horizontalLayout_3.addWidget(self.radioButton_low)
        self.radioButton_band = QtWidgets.QRadioButton(self.widget_filter_type)
        self.radioButton_band.setChecked(True)
        self.radioButton_band.setObjectName("radioButton_band")
        self.horizontalLayout_3.addWidget(self.radioButton_band)
        self.radioButton_high = QtWidgets.QRadioButton(self.widget_filter_type)
        self.radioButton_high.setObjectName("radioButton_high")
        self.horizontalLayout_3.addWidget(self.radioButton_high)
        self.gridLayout_13.addWidget(self.widget_filter_type, 0, 1, 1, 1)
        self.radioButton_filter = QtWidgets.QRadioButton(self.groupBox_filter_setting)
        self.radioButton_filter.setText("")
        self.radioButton_filter.setChecked(True)
        self.radioButton_filter.setObjectName("radioButton_filter")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_filter)
        self.gridLayout_13.addWidget(self.radioButton_filter, 1, 0, 1, 1)
        self.gridLayout_13.setColumnStretch(0, 1)
        self.gridLayout_13.setColumnStretch(1, 3)
        self.gridLayout_14.addLayout(self.gridLayout_13, 0, 0, 1, 1)
        self.groupBox_shortcut = QtWidgets.QGroupBox(self.groupBox_filter_setting)
        self.groupBox_shortcut.setObjectName("groupBox_shortcut")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_shortcut)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.radioButton_beta = QtWidgets.QRadioButton(self.groupBox_shortcut)
        self.radioButton_beta.setObjectName("radioButton_beta")
        self.buttonGroup.addButton(self.radioButton_beta)
        self.gridLayout_15.addWidget(self.radioButton_beta, 1, 2, 1, 1)
        self.radioButton_delta = QtWidgets.QRadioButton(self.groupBox_shortcut)
        self.radioButton_delta.setObjectName("radioButton_delta")
        self.buttonGroup.addButton(self.radioButton_delta)
        self.gridLayout_15.addWidget(self.radioButton_delta, 0, 0, 1, 1)
        self.radioButton_gamma = QtWidgets.QRadioButton(self.groupBox_shortcut)
        self.radioButton_gamma.setObjectName("radioButton_gamma")
        self.buttonGroup.addButton(self.radioButton_gamma)
        self.gridLayout_15.addWidget(self.radioButton_gamma, 2, 0, 1, 1)
        self.radioButton_mu = QtWidgets.QRadioButton(self.groupBox_shortcut)
        self.radioButton_mu.setObjectName("radioButton_mu")
        self.buttonGroup.addButton(self.radioButton_mu)
        self.gridLayout_15.addWidget(self.radioButton_mu, 2, 2, 1, 1)
        self.radioButton_theta = QtWidgets.QRadioButton(self.groupBox_shortcut)
        self.radioButton_theta.setObjectName("radioButton_theta")
        self.buttonGroup.addButton(self.radioButton_theta)
        self.gridLayout_15.addWidget(self.radioButton_theta, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem5, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem6, 2, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem7, 0, 1, 1, 1)
        self.radioButton_alpha = QtWidgets.QRadioButton(self.groupBox_shortcut)
        self.radioButton_alpha.setObjectName("radioButton_alpha")
        self.buttonGroup.addButton(self.radioButton_alpha)
        self.gridLayout_15.addWidget(self.radioButton_alpha, 0, 2, 1, 1)
        self.gridLayout_14.addWidget(self.groupBox_shortcut, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_filter_setting)
        self.gridLayout_9.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_filter, 1, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 9)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 2)
        self.verticalLayout_7.addLayout(self.gridLayout_3)
        self.verticalLayout_3.addWidget(self.groupBox_filter0)
        self.groupBox_channels = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_channels.sizePolicy().hasHeightForWidth())
        self.groupBox_channels.setSizePolicy(sizePolicy)
        self.groupBox_channels.setObjectName("groupBox_channels")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_channels)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_channel1 = QtWidgets.QCheckBox(self.groupBox_channels)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_channel1.sizePolicy().hasHeightForWidth())
        self.checkBox_channel1.setSizePolicy(sizePolicy)
        self.checkBox_channel1.setObjectName("checkBox_channel1")
        self.gridLayout.addWidget(self.checkBox_channel1, 0, 0, 1, 1)
        self.checkBox_channel2 = QtWidgets.QCheckBox(self.groupBox_channels)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_channel2.sizePolicy().hasHeightForWidth())
        self.checkBox_channel2.setSizePolicy(sizePolicy)
        self.checkBox_channel2.setObjectName("checkBox_channel2")
        self.gridLayout.addWidget(self.checkBox_channel2, 0, 1, 1, 1)
        self.checkBox_channel3 = QtWidgets.QCheckBox(self.groupBox_channels)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_channel3.sizePolicy().hasHeightForWidth())
        self.checkBox_channel3.setSizePolicy(sizePolicy)
        self.checkBox_channel3.setObjectName("checkBox_channel3")
        self.gridLayout.addWidget(self.checkBox_channel3, 1, 0, 1, 1)
        self.checkBox_channel4 = QtWidgets.QCheckBox(self.groupBox_channels)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_channel4.sizePolicy().hasHeightForWidth())
        self.checkBox_channel4.setSizePolicy(sizePolicy)
        self.checkBox_channel4.setObjectName("checkBox_channel4")
        self.gridLayout.addWidget(self.checkBox_channel4, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_channels)
        self.groupBox_visual = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_visual.sizePolicy().hasHeightForWidth())
        self.groupBox_visual.setSizePolicy(sizePolicy)
        self.groupBox_visual.setObjectName("groupBox_visual")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_visual)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_time = QtWidgets.QCheckBox(self.groupBox_visual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_time.sizePolicy().hasHeightForWidth())
        self.checkBox_time.setSizePolicy(sizePolicy)
        self.checkBox_time.setObjectName("checkBox_time")
        self.verticalLayout_5.addWidget(self.checkBox_time)
        self.checkBox_freq = QtWidgets.QCheckBox(self.groupBox_visual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_freq.sizePolicy().hasHeightForWidth())
        self.checkBox_freq.setSizePolicy(sizePolicy)
        self.checkBox_freq.setObjectName("checkBox_freq")
        self.verticalLayout_5.addWidget(self.checkBox_freq)
        self.checkBox_spectrogram = QtWidgets.QCheckBox(self.groupBox_visual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_spectrogram.sizePolicy().hasHeightForWidth())
        self.checkBox_spectrogram.setSizePolicy(sizePolicy)
        self.checkBox_spectrogram.setObjectName("checkBox_spectrogram")
        self.verticalLayout_5.addWidget(self.checkBox_spectrogram)
        self.checkBox_psd = QtWidgets.QCheckBox(self.groupBox_visual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_psd.sizePolicy().hasHeightForWidth())
        self.checkBox_psd.setSizePolicy(sizePolicy)
        self.checkBox_psd.setObjectName("checkBox_psd")
        self.verticalLayout_5.addWidget(self.checkBox_psd)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addWidget(self.groupBox_visual)
        self.groupBox_note = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_note.sizePolicy().hasHeightForWidth())
        self.groupBox_note.setSizePolicy(sizePolicy)
        self.groupBox_note.setObjectName("groupBox_note")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_note)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_msg = QtWidgets.QLabel(self.groupBox_note)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_msg.sizePolicy().hasHeightForWidth())
        self.label_msg.setSizePolicy(sizePolicy)
        self.label_msg.setText("")
        self.label_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_msg.setObjectName("label_msg")
        self.gridLayout_6.addWidget(self.label_msg, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_note)
        self.verticalLayout_3.setStretch(0, 7)
        self.verticalLayout_3.setStretch(1, 25)
        self.verticalLayout_3.setStretch(2, 5)
        self.verticalLayout_3.setStretch(3, 8)
        self.verticalLayout_3.setStretch(4, 5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.visualWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.visualWidget.sizePolicy().hasHeightForWidth())
        self.visualWidget.setSizePolicy(sizePolicy)
        self.visualWidget.setObjectName("visualWidget")
        self.horizontalLayout_2.addWidget(self.visualWidget)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 7)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1102, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EEG-4Channels-Viewer"))
        self.groupBox_link.setTitle(_translate("MainWindow", "Link"))
        self.label_10.setText(_translate("MainWindow", "COM Port:"))
        self.label_12.setText(_translate("MainWindow", "Sampling:"))
        self.label_11.setText(_translate("MainWindow", "Byte Rate:"))
        self.comboBox_port.setItemText(0, _translate("MainWindow", "COM3"))
        self.comboBox_baudrate.setItemText(0, _translate("MainWindow", "460800"))
        self.comboBox_fs.setItemText(0, _translate("MainWindow", "250"))
        self.comboBox_fs.setItemText(1, _translate("MainWindow", "500"))
        self.comboBox_fs.setItemText(2, _translate("MainWindow", "1000"))
        self.comboBox_fs.setItemText(3, _translate("MainWindow", "1500"))
        self.comboBox_fs.setItemText(4, _translate("MainWindow", "2000"))
        self.groupBox_filter0.setTitle(_translate("MainWindow", "Filter"))
        self.groupBox_notch.setTitle(_translate("MainWindow", "Notch Filter"))
        self.label_2.setText(_translate("MainWindow", "Q Factor:"))
        self.comboBox_notch_freq.setItemText(0, _translate("MainWindow", "50"))
        self.comboBox_notch_freq.setItemText(1, _translate("MainWindow", "60"))
        self.label.setText(_translate("MainWindow", "Frequency:"))
        self.groupBox_filter.setTitle(_translate("MainWindow", "Filter"))
        self.label_3.setText(_translate("MainWindow", "Order:"))
        self.label_low.setText(_translate("MainWindow", "Low:"))
        self.label_high.setText(_translate("MainWindow", "High:"))
        self.radioButton_low.setText(_translate("MainWindow", "Low"))
        self.radioButton_band.setText(_translate("MainWindow", "Band"))
        self.radioButton_high.setText(_translate("MainWindow", "High"))
        self.groupBox_shortcut.setTitle(_translate("MainWindow", "ShortCut"))
        self.radioButton_beta.setText(_translate("MainWindow", "Beta"))
        self.radioButton_delta.setText(_translate("MainWindow", "Delta"))
        self.radioButton_gamma.setText(_translate("MainWindow", "Gamma"))
        self.radioButton_mu.setText(_translate("MainWindow", "Mu"))
        self.radioButton_theta.setText(_translate("MainWindow", "Theta"))
        self.radioButton_alpha.setText(_translate("MainWindow", "Alpha"))
        self.groupBox_channels.setTitle(_translate("MainWindow", "Channels"))
        self.checkBox_channel1.setText(_translate("MainWindow", "Channel1"))
        self.checkBox_channel2.setText(_translate("MainWindow", "Channel2"))
        self.checkBox_channel3.setText(_translate("MainWindow", "Channel3"))
        self.checkBox_channel4.setText(_translate("MainWindow", "Channel4"))
        self.groupBox_visual.setTitle(_translate("MainWindow", "Visualization"))
        self.checkBox_time.setText(_translate("MainWindow", "Time Domain"))
        self.checkBox_freq.setText(_translate("MainWindow", "Frequency Domain"))
        self.checkBox_spectrogram.setText(_translate("MainWindow", "Spectrogram"))
        self.checkBox_psd.setText(_translate("MainWindow", "Power Spectral Density"))
        self.groupBox_note.setTitle(_translate("MainWindow", "Note"))