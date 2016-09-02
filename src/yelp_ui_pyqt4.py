#!/usr/bin/python

from PyQt4 import QtCore, QtGui
import sys
import json
import re
from Interface_Recommended_Results import obtain_list

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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1122, 672)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.rest_table = QtGui.QTableWidget(self.centralwidget)
        self.rest_table.setGeometry(QtCore.QRect(20, 250, 710, 371))
        self.rest_table.setObjectName(_fromUtf8("rest_table"))
        self.rest_table.setColumnCount(18)
        self.rest_table.setRowCount(10)
        self.rest_table.setHorizontalHeaderLabels(["City","Review Count","Name","Type","ID","Address","State", "Stars","Categories"])
        self.user_select_button = QtGui.QPushButton(self.centralwidget)
        self.user_select_button.setGeometry(QtCore.QRect(450, 90, 121, 28))
        self.user_select_button.setObjectName(_fromUtf8("user_select_button"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 281, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.user_box = QtGui.QTextEdit(self.centralwidget)
        self.user_box.setGeometry(QtCore.QRect(120, 90, 291, 31))
        self.user_box.setObjectName(_fromUtf8("user_box"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 72, 15))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.rest_name = QtGui.QTextEdit(self.centralwidget)
        self.rest_name.setGeometry(QtCore.QRect(190, 140, 291, 31))
        self.rest_name.setObjectName(_fromUtf8("rest_name"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.stars_box = QtGui.QComboBox(self.centralwidget)
        self.stars_box.setGeometry(QtCore.QRect(120, 180, 141, 31))
        self.stars_box.setObjectName(_fromUtf8("stars_box"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 190, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.category_box = QtGui.QComboBox(self.centralwidget)
        self.category_box.setGeometry(QtCore.QRect(490, 180, 191, 31))
        self.category_box.setEditable(False)
        self.category_box.setObjectName(_fromUtf8("category_box"))
        self.user_pic = QtGui.QLabel(self.centralwidget)
        self.user_pic.setGeometry(QtCore.QRect(760, 270, 321, 321))
        self.user_pic.setScaledContents(True)
        self.user_pic.setObjectName(_fromUtf8("user_pic"))
        self.word_count_pic = QtGui.QLabel(self.centralwidget)
        self.word_count_pic.setGeometry(QtCore.QRect(750, 20, 351, 221))
        self.word_count_pic.setScaledContents(True)
        self.word_count_pic.setObjectName(_fromUtf8("word_count_pic"))
        self.find_rest_button = QtGui.QPushButton(self.centralwidget)
        self.find_rest_button.setGeometry(QtCore.QRect(530, 140, 171, 28))
        self.find_rest_button.setObjectName(_fromUtf8("find_rest_button"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.user_select_button.setText(_translate("MainWindow", "Select User", None))
        self.label.setText(_translate("MainWindow", "Yelp Recommender", None))
        self.label_2.setText(_translate("MainWindow", "User ID:", None))
        self.label_3.setText(_translate("MainWindow", "Restaurant Name:", None))
        self.label_4.setText(_translate("MainWindow", "Stars:", None))
        self.label_5.setText(_translate("MainWindow", "Category:", None))
        #self.user_pic.setPixmap(QtGui.QPixmap('../picture/13916.png'))
        self.find_rest_button.setText(_translate("MainWindow", "Find Restaruants", None))

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        star_list=["1 Star and above",
                   "2 Stars and above",
                   "3 Stars and above",
                   "4 stars and above",
                   "5 Stars and above"]
        for star in star_list:
            self.stars_box.addItem(star)
        category_list=["Chinese",
                       "Italian",
                       "American (Traditional)",
                       "American (New)",
                       "Bars",
                       "Pizza",
                       "Vegetarian"]
        for category in category_list:
            self.category_box.addItem(category)
        self.user_select_button.clicked.connect(self.ChangeUser)
        self.find_rest_button.clicked.connect(self.findRest)

    def DisplayRest(self, rest_out_list):
        rest_table_list=[]
        for rest in rest_out_list:
            temp_list=[]
            for key in rest.keys():
                key_str=key.encode("ascii","ignore")
                if( type(rest[key]) == unicode ):
                    content=rest[key].encode("ascii","ignore")
                    temp_list.append(content)
                elif( key_str!='longitude' and key_str!='latitude' and type(rest[key]) in [int, float] ):
                    content=str(rest[key])
                    temp_list.append(content)
                elif( key_str=='categories'):
                    for item in rest[key]:
                        item_str=item.encode("ascii","ignore")
                        temp_list.append(item_str)
            rest_table_list.append(temp_list)

        self.rest_table.clearContents()
        for row in range(10):
            for column in range(18):
                try:
                    newitem = QtGui.QTableWidgetItem(rest_table_list[row][column])
                    self.rest_table.setItem(row, column, newitem)
                except:
                    pass

    def ShowPic(self, user_id):
        pic=QtGui.QPixmap('../picture/'+str(user_id)+'lay1.png')
        wc_pic=QtGui.QPixmap('../picture/'+str(user_id)+'.png')
        self.user_pic.setPixmap(pic)
        self.word_count_pic.setPixmap(wc_pic)

    def ChangeUser(self):
        user=int(self.user_box.toPlainText())
        user_rest_list=obtain_list(user)
        file1=open("rest_pitt.json")
        rest_list=[]
        for line in file1.readlines():
            rest_list.append(json.loads(line))
        rest_out_list=[]
        for rest in rest_list:
            rest_id=rest[unicode("business_id")].decode("ascii","ignore")
            if( rest_id in user_rest_list ):
                rest_out_list.append(rest)

        self.DisplayRest(rest_out_list)
        self.ShowPic(user)

    def findRest(self):
        file1=open("rest_pitt.json")
        rest_list=[]
        for line in file1.readlines():
            rest_list.append(json.loads(line))
        filter_stars=self.stars_box.currentIndex()+1
        filter_category=unicode(self.category_box.currentText())
        filter_name=str(self.rest_name.toPlainText())

        count=0
        rest_out_list=[]
        for rest in rest_list:
            if(count<10):
                rest_name=rest[unicode("name")].encode('ascii', 'ignore')
                rest_stars=rest[unicode("stars")]
                rest_category=rest[unicode("categories")]
                match=re.search(filter_name, rest_name)
                if( match and rest_stars>=filter_stars and (filter_category in rest_category)):
                    rest_out_list.append(rest)
                    count+=1

        self.DisplayRest(rest_out_list)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
