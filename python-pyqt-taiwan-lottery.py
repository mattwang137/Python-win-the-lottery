#!/usr/bin/python3
#encoding:utf-8
__author__="Matt Wang"

'''
大樂透模擬器ver2.00 加上 PyQt 界面
輸入數量看要買多少張電腦選號
製作日期：27/06/2019
'''

import random
import sys
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QFont,QPalette
from PyQt4.QtCore import Qt

class Myapp(QtGui.QWidget):
    def __init__(self,parent=None):
        super(Myapp,self).__init__(parent)

        vlayout = QtGui.QVBoxLayout()

        hlayout1 = QtGui.QHBoxLayout()
        self.label1=QtGui.QLabel()
        self.label1.setText(u"大樂透期號: [ 108000047 ]")
        self.label1.setFont(QFont("Roman times",20,QFont.Bold))
        hlayout1.addWidget(self.label1)

        hlayout2 = QtGui.QHBoxLayout()
        self.label2=QtGui.QLabel()
        self.label2.setText(u"本期中獎號碼: [ 2 , 7 , 12 , 21 , 23 , 45 ]")
        self.label2.setFont(QFont("Roman times",20,QFont.Bold))
        self.label3=QtGui.QLabel()
        self.label3.setText(u"本期中獎特別號: [ 10 ]")
        self.label3.setFont(QFont("Roman times",20,QFont.Bold))
        hlayout2.addWidget(self.label2)
        hlayout2.addWidget(self.label3)

        hlayout3 = QtGui.QHBoxLayout()
        self.label4=QtGui.QLabel()
        self.label4.setText(u"請輸入要買多少張大樂透電腦選號: ")
        self.label4.setFont(QFont("Roman times",20,QFont.Bold))
        self.text1=QtGui.QLineEdit()
        hlayout3.addWidget(self.label4)
        hlayout3.addWidget(self.text1)

        hlayout4 = QtGui.QHBoxLayout()
        self.browser1 = QtGui.QTextBrowser()
        self.browser1.setFixedHeight(400)
        hlayout4.addWidget(self.browser1)

        hlayout5 = QtGui.QHBoxLayout()
        self.label5=QtGui.QLabel()
        self.label5.setText(u"結算: ")
        self.label5.setFont(QFont("Roman times",20,QFont.Bold))
        hlayout5.addWidget(self.label5)

        hlayout6 = QtGui.QHBoxLayout()
        self.browser2 = QtGui.QTextBrowser()
        hlayout6.addWidget(self.browser2)

        hlayout7 = QtGui.QHBoxLayout()
        self.bt1=QtGui.QPushButton(u"購買")
        self.bt1.setFont(QFont("Roman times",20,QFont.Bold))
        self.bt2=QtGui.QPushButton(u"清除")
        self.bt2.setFont(QFont("Roman times",20,QFont.Bold))
        hlayout7.addWidget(self.bt1)
        hlayout7.addWidget(self.bt2)

        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)
        vlayout.addLayout(hlayout3)
        vlayout.addLayout(hlayout4)
        vlayout.addLayout(hlayout5)
        vlayout.addLayout(hlayout6)
        vlayout.addLayout(hlayout7)
        self.setLayout(vlayout)

        # button event
        self.bt1.clicked.connect(self.buyTicket)
        self.bt2.clicked.connect(self.clear)

        color = QPalette()
        color.setColor(QPalette.WindowText,Qt.red)
        color.setColor(QPalette.Window,Qt.blue)
        self.label1.setAutoFillBackground(True)
        self.label1.setPalette(color)
        self.label2.setAutoFillBackground(True)
        self.label2.setPalette(color)
        self.label3.setAutoFillBackground(True)
        self.label3.setPalette(color)

    def buyTicket(self):

        self.browser1.clear()
        self.browser2.clear()

        count=int(self.text1.text())
        num=int(count)

        term=108000047
        win=[2,7,12,21,23,45]
        winS=10

        # hit of normal number

        total=0 #for total price you win

        for c in range(1,count+1):
            self.browser1.append(" ")
            # print(" ") #space
            own=random.sample(range(1,49),6)
            self.browser1.append("你的第 %d 張大樂透電腦選號: %s"%(c,own))


            hit=0
            for i in range(6):
                for j in range(6):
                    if (own[i]==win[j]):
                        hit+=1 #hit of normal number

            if (hit!=0):
                self.browser1.append("恭喜您！您中了 %d 個號碼"%hit)
            else:
                self.browser1.append("喔喔！您沒有中的號碼！")


            cs=0
            for i in range(6):

                if (own[i]==winS):
                    self.browser1.append("恭喜您！您中了本期的特別號！")
                    cs+=1 #hit of special number

            # how much do you win (hit & cs)


            if (hit==6):
                self.browser1.append("恭喜您！您中了本期的頭獎！獎金是: 301,272,731 元新台幣！")
                total+=301272731
            elif (hit==5 and cs==1):
                self.browser1.append("恭喜您！您中了本期的貳獎！獎金是: 798,313 元新台幣！")
                total+=798313
            elif (hit==5):
                self.browser1.append("恭喜您！您中了本期的參獎！獎金是: 39,987 元新台幣！")
                total+=39987
            elif (hit==4 and cs==1):
                self.browser1.append("恭喜您！您中了本期的肆獎！獎金是: 8,248 元新台幣！")
                total+=8248
            elif (hit==4):
                self.browser1.append("恭喜您！您中了本期的伍獎！獎金是: 2,000 元新台幣！")
                total+=2000
            elif (hit==3 and cs==1):
                self.browser1.append("恭喜您！您中了本期的陸獎！獎金是: 1,000 元新台幣！")
                total+=1000
            elif (hit==2 and cs==1):
                self.browser1.append("恭喜您！您中了本期的柒獎！獎金是: 400 元新台幣！")
                total+=400
            elif (hit==3):
                self.browser1.append("恭喜您！您中了本期的普獎！獎金是: 400 元新台幣！")
                total+=400
            else:
                self.browser1.append("這張彩卷沒有中獎喔！請再接再厲！")

        self.browser2.append("本次您總共買了 %d 張彩卷"%count)
        p=count*50
        self.browser2.append("一共花費了 %d 元新台幣"%p)
        self.browser2.append("總共贏得了 %d 元新台幣"%total)

    def clear(self):
        self.text1.clear()
        self.browser1.clear()
        self.browser2.clear()

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    w=Myapp()
    w.setGeometry(100,100,350,700)
    w.setWindowTitle(u"大樂透電腦選號模擬器 version 2.00")
    w.show()
    sys.exit(app.exec_())