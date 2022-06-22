from PySide import QtCore, QtGui
import sys
from ui import Ui_Form
from CalcEqualization import result


app = QtGui.QApplication(sys.argv)

#Create form and UI

Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

#Logic

def bp_0():
    ui.lineEdit.setText(ui.lineEdit.text() + "0")


def bp_1():
    ui.lineEdit.setText(ui.lineEdit.text() + "1")


def bp_2():
    ui.lineEdit.setText(ui.lineEdit.text() + "2")


def bp_3():
    ui.lineEdit.setText(ui.lineEdit.text() + "3")


def bp_4():
    ui.lineEdit.setText(ui.lineEdit.text() + "4")


def bp_5():
    ui.lineEdit.setText(ui.lineEdit.text() + "5")


def bp_6():
    ui.lineEdit.setText(ui.lineEdit.text() + "6")


def bp_7():
    ui.lineEdit.setText(ui.lineEdit.text() + "7")


def bp_8():
    ui.lineEdit.setText(ui.lineEdit.text() + "8")


def bp_9():
    ui.lineEdit.setText(ui.lineEdit.text() + "9")


def bp_10():
    if len(ui.lineEdit.text()) == 0:
        pass
    elif  len(ui.lineEdit.text()) != 1:
        if ui.lineEdit.text()[-1] != " " and ui.lineEdit.text()[-1] != ".":
            ui.lineEdit.setText(ui.lineEdit.text() + " + ")
    else:
        ui.lineEdit.setText(ui.lineEdit.text() + " + ")


def bp_11():
    if len(ui.lineEdit.text()) == 0 or len(ui.lineEdit.text()) == 1:
        ui.lineEdit.setText(ui.lineEdit.text() + " - ")
    else:
        if ui.lineEdit.text()[-1] != " " and ui.lineEdit.text()[-1] != ".":
            ui.lineEdit.setText(ui.lineEdit.text() + " - ")


def bp_12():
    if len(ui.lineEdit.text()) == 0:
        pass
    elif len(ui.lineEdit.text()) != 1:
        if ui.lineEdit.text()[-1] != " " and ui.lineEdit.text()[-1] != ".":
            ui.lineEdit.setText(ui.lineEdit.text() + " * ")
    else:
        ui.lineEdit.setText(ui.lineEdit.text() + " * ")


def bp_13():
    if len(ui.lineEdit.text()) == 0:
        pass
    elif len(ui.lineEdit.text()) != 1:
        if ui.lineEdit.text()[-1] != " " and ui.lineEdit.text()[-1] != ".":
            ui.lineEdit.setText(ui.lineEdit.text() + " / ")
    else:
        ui.lineEdit.setText(ui.lineEdit.text() + " / ")


def bp_14():
    ui.lineEdit.setText(ui.lineEdit.text() + " ( ")


def bp_15():
    ui.lineEdit.setText(ui.lineEdit.text() + " ) ")


def bp_16():
    if len(ui.lineEdit.text()) == 0:
        pass
    elif len(ui.lineEdit.text()) != 1:
        if ui.lineEdit.text()[-1] != " ":
            list = ui.lineEdit.text().split(" ")
            if len(list) == 1:
                if "." not in list[0]:
                    ui.lineEdit.setText(ui.lineEdit.text() + ".")
            else:
                if "." not in list[-1]:
                    ui.lineEdit.setText(ui.lineEdit.text() + ".")
    else:
        ui.lineEdit.setText(ui.lineEdit.text() + ".")


def bp_17():
    ui.lineEdit.setText("")


def bp_18():
    ui.lineEdit.setText(str(result(ui)))


def bp_19():
    if result(ui)[0] == "-" or result(ui) == "0":
        ui.lineEdit.setText("Sorry, it's impossible")
    else:
        ui.lineEdit.setText(str(pow(float(result(ui)), 1/2)))


def bp_20():
    ui.lineEdit.setText(str(pow(float(result(ui)), 2.0)))

def bp_21():
    if len(ui.lineEdit.text()) == 1:
        ui.lineEdit.setText("")
    elif len(ui.lineEdit.text()) != 0:
        if ui.lineEdit.text()[-1] != " ":
            ui.lineEdit.setText(ui.lineEdit.text()[0:-1])
        else:
            ui.lineEdit.setText(ui.lineEdit.text()[0:-3])


ui.pushButton_10.clicked.connect( bp_0 )
ui.pushButton.clicked.connect( bp_1 )
ui.pushButton_2.clicked.connect( bp_2 )
ui.pushButton_3.clicked.connect( bp_3 )
ui.pushButton_5.clicked.connect( bp_4 )
ui.pushButton_4.clicked.connect( bp_5 )
ui.pushButton_6.clicked.connect( bp_6 )
ui.pushButton_8.clicked.connect( bp_7 )
ui.pushButton_7.clicked.connect( bp_8 )
ui.pushButton_9.clicked.connect( bp_9 )
ui.pushButton_13.clicked.connect( bp_10 )
ui.pushButton_15.clicked.connect( bp_11 )
ui.pushButton_12.clicked.connect( bp_12 )
ui.pushButton_11.clicked.connect( bp_13 )
ui.pushButton_18.clicked.connect( bp_16 )
ui.pushButton_14.clicked.connect( bp_17 )
ui.pushButton_19.clicked.connect( bp_18 )
ui.pushButton_17.clicked.connect( bp_19 )
ui.pushButton_16.clicked.connect( bp_20 )
ui.pushButton_20.clicked.connect( bp_21 )
ui.pushButton_21.clicked.connect( bp_21 )

#Loop

sys.exit(app.exec_())
