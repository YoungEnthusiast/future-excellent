import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPainter
from PyQt5.QtCore import QByteArray, QDateTime, QBuffer, QIODevice
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from adminform import Ui_AdminForm
from receipt import Ui_ReceiptForm
from inherstudedit import StudEdit
import sqlite3
from sqlite3 import Error

class InherAdmin(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AdminForm()
        self.ui.setupUi(self)
        self.stud_edit = StudEdit()
        self.receipt = Receipt()
        self.displayUsers()
        self.displayClasses()
        self.ui.class_edit_lineEdit.hide()
        self.ui.form_master_edit_lineEdit.hide()
        self.ui.class_update_btn.hide()
        self.ui.class_add_lineEdit.hide()
        self.ui.class_save_btn.hide()
        self.ui.form_master_lineEdit.hide()
        self.ui.user_save_btn.hide()
        self.ui.username_label.hide()
        self.ui.password_label.hide()
        self.ui.class_edit_label.hide()
        self.ui.form_master_edit_label.hide()
        self.ui.class_add_label.hide()
        self.ui.form_master_add_label.hide()
        self.ui.username_lineEdit.hide()
        self.ui.password_lineEdit.hide()
        self.ui.principal_edit_lineEdit.hide()
        self.ui.headmaster_edit_lineEdit.hide()
        self.ui.principal_update_btn.hide()
        self.ui.headmaster_update_btn.hide()
        self.ui.session_lineEdit.hide()
        self.ui.session_label.hide()
        self.ui.next_term_lineEdit.hide()
        self.ui.next_term_label.hide()
        self.ui.mgmt_update_btn.hide()
        self.ui.fees_label.hide()
        self.ui.fees_lineEdit.hide()
        self.ui.fees_lineEdit2.hide()
        self.ui.fees_lineEdit3.hide()
        self.ui.fees_lineEdit4.hide()
        self.ui.prin_browse_btn.hide()
        self.ui.head_browse_btn.hide()
        self.ui.class_sig_browse_btn.hide()
        self.ui.class_edit_btn.clicked.connect(self.showEditClass)
        self.ui.class_update_btn.clicked.connect(self.editClass)
        self.ui.class_delete_btn.clicked.connect(self.deleteClass)
        self.ui.add_new_btn.clicked.connect(self.showAddClass)
        self.ui.class_save_btn.clicked.connect(self.saveClass)
        self.ui.stud_edit_btn.clicked.connect(self.showEditStud)
        self.stud_edit.ui.update_btn.clicked.connect(self.editStud)
        self.stud_edit.ui.browse_btn.clicked.connect(self.browseImage)
        self.ui.stud_del_btn.clicked.connect(self.deleteStud)
        self.ui.user_add_btn.clicked.connect(self.showAddUser)
        self.ui.user_save_btn.clicked.connect(self.saveUser)
        self.ui.user_delete_btn.clicked.connect(self.deleteUser)
        self.ui.class_comboBox2.currentTextChanged.connect(self.displayStuds)
        #Generates Current Date
        self.stud_edit.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.ui.principal_edit_btn.clicked.connect(self.showEditPrin)
        self.ui.headmaster_edit_btn.clicked.connect(self.showEditHead)
        self.ui.mgmt_edit_btn.clicked.connect(self.showEditMgmt)
        self.ui.principal_update_btn.clicked.connect(self.editPrin)
        self.ui.headmaster_update_btn.clicked.connect(self.editHead)
        self.ui.mgmt_update_btn.clicked.connect(self.editMgmt)
        self.ui.paid_btn.clicked.connect(self.setPaid)
        self.ui.not_paid_btn.clicked.connect(self.setNotPaid)
        self.ui.prin_browse_btn.clicked.connect(self.browsePrinSig)
        self.ui.head_browse_btn.clicked.connect(self.browseHeadSig)
        self.ui.class_sig_browse_btn.clicked.connect(self.browseClassSig)

    def displayUsers(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        query = cur.execute("SELECT * FROM t_users ORDER BY username")
        rows = cur.fetchall()
        users = ["Select a user"]
        self.ui.user_comboBox.clear()
        for row in rows:
            users.append(row[0])
        self.ui.user_comboBox.addItems(users)
        con.close()

    def showAddUser(self):
        self.ui.user_save_btn.show()
        self.ui.username_label.show()
        self.ui.password_label.show()
        self.ui.username_lineEdit.show()
        self.ui.password_lineEdit.show()

    def saveUser(self):
        username = self.ui.username_lineEdit.text()
        password = self.ui.password_lineEdit.text()
        cmd = "INSERT INTO t_users(username, password) VALUES(?, ?)"
        try:
            con = sqlite3.connect("futuredb.db")
            con.execute("PRAGMA foreign_keys = 1")
            cur = con.cursor()
            cur.execute(cmd, (username, password, ))
            con.commit()
            QMessageBox.information(self, 'Adding User', username + " added successfully", QMessageBox.Ok)
            self.displayUsers()
        except Error:
            QMessageBox.critical(self, 'Adding User',"ERROR: "+ username + " already exists", QMessageBox.Ok)
        finally:
            con.close()
            self.ui.class_add_lineEdit.clear()

    def deleteUser(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        username = self.ui.user_comboBox.currentText()
        cmd = "DELETE FROM t_users WHERE username = ?"
        if username == "Select a user":
            QMessageBox.critical(self, 'Deleting User', "ERROR: Please select a user to delete", QMessageBox.Ok)
        else:
            buttonReply = QMessageBox.warning(self, 'Deleting User', "WARNING: Deleting this user means the user will not be able to use the system again. Do you still wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                cur.execute(cmd, (username,))
                con.commit()
                self.displayUsers()
                con.close()

    def showAddClass(self):
        self.ui.class_add_lineEdit.show()
        self.ui.class_save_btn.show()
        self.ui.class_add_label.show()
        self.ui.form_master_add_label.show()
        self.ui.form_master_lineEdit.show()

    def showEditClass(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        class_name = self.ui.class_comboBox.currentText()
        cmd1 = "SELECT * FROM t_classes WHERE class_name = ?"
        cur.execute(cmd1, (class_name,))
        row = cur.fetchone()
        if row == None:
            QMessageBox.critical(self, "Editing Class", "ERROR: Please select a class to edit", QMessageBox.Ok)
        elif row[2] == None:
            self.ui.class_edit_lineEdit.show()
            self.ui.class_edit_lineEdit.setText(row[0])
            self.ui.class_update_btn.show()
            self.ui.class_edit_label.show()
            self.ui.form_master_edit_label.show()
            self.ui.form_master_edit_lineEdit.show()
            self.ui.form_master_edit_lineEdit.setText(row[1])
            self.ui.class_sig_browse_btn.show()
            pixmap = QPixmap()
            #pixmap.loadFromData(QByteArray.fromBase64(row[2]))
            self.ui.master_sig_label.setPixmap(QPixmap(pixmap))
        else:
            self.ui.class_edit_lineEdit.show()
            self.ui.class_edit_lineEdit.setText(row[0])
            self.ui.class_update_btn.show()
            self.ui.class_edit_label.show()
            self.ui.form_master_edit_label.show()
            self.ui.form_master_edit_lineEdit.show()
            self.ui.form_master_edit_lineEdit.setText(row[1])
            self.ui.class_sig_browse_btn.show()
            self.ui.master_sig_label.show()
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray.fromBase64(row[2]))
            self.ui.master_sig_label.setPixmap(QPixmap(pixmap))

    def browseClassSig(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', 'Image Files (*.png *.jpg *gif)')
        image_path = file_name[0]
        pixmap = QPixmap(image_path)
        self.ui.master_sig_label.setPixmap(QPixmap(pixmap))

    def editClass(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        old_class = self.ui.class_comboBox.currentText()
        new_class = self.ui.class_edit_lineEdit.text()
        new_master = self.ui.form_master_edit_lineEdit.text()
        buff = QBuffer()
        buff.open(QIODevice.WriteOnly)
        pixmap = QPixmap(self.ui.master_sig_label.pixmap())
        pixmap.save(buff, "PNG")
        binary_img = buff.data().toBase64().data()

        cmd1 = "SELECT class_name FROM t_classes WHERE class_name = ?"
        try:
            cur.execute(cmd1, (old_class,))
            row = cur.fetchone()
            if old_class == "Select a class":
                QMessageBox.critical(self, 'Editing Class', "ERROR: Please select a class to edit", QMessageBox.Ok)
            else:
                cmd2 = "UPDATE t_classes SET class_name = ?, form_master = ?, sig = ? WHERE class_name = ?"
                cur.execute(cmd2, (new_class, new_master, binary_img, old_class,))
                con.commit()
                QMessageBox.information(self, "Class Modification", "Class modified successfully", QMessageBox.Ok)
                self.ui.class_edit_lineEdit.hide()
                self.ui.class_update_btn.hide()
                self.ui.class_edit_label.hide()
                self.ui.form_master_edit_label.hide()
                self.ui.form_master_edit_lineEdit.hide()
                self.ui.master_sig_label.hide()
                self.ui.class_sig_browse_btn.hide()
                self.displayClasses()
        except Error:
            QMessageBox.critical(self, "Editing Class","ERROR: "+ new_class + " already exists", QMessageBox.Ok)
        finally:
            con.close()

    def deleteClass(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        class_name = self.ui.class_comboBox.currentText()
        cmd = "DELETE FROM t_classes WHERE class_name = ?"
        if class_name == "Select a class":
            QMessageBox.critical(self, 'Deleting Class', "ERROR: Please select a class to delete", QMessageBox.Ok)
        else:
            buttonReply = QMessageBox.warning(self, 'Deleting Class', "WARNING: Deleting this class will delete all pupils/students in it. Do you still wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                cur.execute(cmd, (class_name,))
                con.commit()
                self.displayClasses()
                con.close()

    def saveClass(self):
        new_save_class = self.ui.class_add_lineEdit.text()
        new_form_master = self.ui.form_master_lineEdit.text()
        cmd = "INSERT INTO t_classes(class_name, form_master) VALUES(?, ?)"
        try:
            con = sqlite3.connect("futuredb.db")
            con.execute("PRAGMA foreign_keys = 1")
            cur = con.cursor()
            cur.execute(cmd, (new_save_class, new_form_master,))
            con.commit()
            QMessageBox.information(self, 'Adding Class', new_save_class + " added successfully", QMessageBox.Ok)
            self.displayClasses()
        except Error:
            QMessageBox.critical(self, 'Adding Class',"ERROR: "+ new_save_class + " already exists", QMessageBox.Ok)
        finally:
            con.close()

    def displayClasses(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        query = cur.execute('SELECT * FROM t_classes ORDER BY class_name')
        rows = cur.fetchall()
        classes = ["Select a class"]
        self.ui.class_comboBox.clear()
        self.ui.class_comboBox2.clear()
        for row in rows:
            classes.append(row[0])
        self.ui.class_comboBox.addItems(classes)
        self.ui.class_comboBox2.addItems(classes)
        con.commit()
        con.close()

    def displayStuds(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox2.currentText()
        cmd = "SELECT * FROM t_studs WHERE stud_class = ? ORDER BY admission_no"
        cur.execute(cmd, (classes_combo,))
        rows = cur.fetchall()
        adm_nos = ["Select an admission number"]
        self.ui.stud_name_comboBox.clear()
        for row in rows:
            adm_nos.append(row[0])
        self.ui.stud_name_comboBox.addItems(adm_nos)
        con.close()

    def showEditStud(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        admission_no = self.ui.stud_name_comboBox.currentText()
        cmd1 = "SELECT * FROM t_studs WHERE admission_no = ?"
        cur.execute(cmd1, (admission_no,))
        row = cur.fetchone()
        if row == None:
            QMessageBox.critical(self, "Editing Pupil/Student", "ERROR: Please select a pupil/student to edit", QMessageBox.Ok)
        else:
            self.stud_edit.showMaximized()
            self.stud_edit.ui.admission_edit.setText(row[0])
            self.stud_edit.ui.name_edit.setText(row[1])
            self.stud_edit.ui.date_edit.setText(row[2])
            self.stud_edit.ui.class_comboBox.setCurrentText(row[3])
            self.stud_edit.ui.sch_fees_edit.setText(row[4])
            self.stud_edit.ui.sex_edit.setText(row[5])
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray.fromBase64(row[6]))
            self.stud_edit.ui.image_label.setPixmap(QPixmap(pixmap))
            self.stud_edit.ui.address_lineEdit.setText(row[7])
            self.stud_edit.ui.parent_no_lineEdit.setText(row[8])

    def browseImage(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', 'Image Files (*.png *.jpg *gif)')
        image_path = file_name[0]
        pixmap = QPixmap(image_path)
        self.stud_edit.ui.image_label.setPixmap(QPixmap(pixmap))

    def editStud(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        var_admission_no = self.ui.stud_name_comboBox.currentText()
        new_admission_no = self.stud_edit.ui.admission_edit.text()
        new_stud_name = self.stud_edit.ui.name_edit.text()
        new_dob = self.stud_edit.ui.date_edit.text()
        new_class = self.stud_edit.ui.class_comboBox.currentText()
        new_sch_fees = self.stud_edit.ui.sch_fees_edit.text()
        new_sex = self.stud_edit.ui.sex_edit.text()
        buff = QBuffer()
        buff.open(QIODevice.WriteOnly)
        pixmap = QPixmap(self.stud_edit.ui.image_label.pixmap())
        pixmap.save(buff, "PNG")
        binary_img = buff.data().toBase64().data()
        new_address = self.stud_edit.ui.address_lineEdit.text()
        new_parent_no = self.stud_edit.ui.parent_no_lineEdit.text()
        modified_date = self.stud_edit.ui.dateTimeEdit.text()
        cmd2 = "SELECT * FROM t_studs WHERE admission_no = ?"
        try:
            cur.execute(cmd2, (var_admission_no,))
            row = cur.fetchone()
            cmd3 = "UPDATE t_studs SET admission_no = ?, stud_name = ?, date_of_birth = ?, stud_class = ?, fees =?, sex = ?, photo = ?, address = ?, parent_no =?, modified_date = ? WHERE admission_no = ?"
            cur.execute(cmd3, (new_admission_no, new_stud_name, new_dob, new_class, new_sch_fees, new_sex, binary_img, new_address, new_parent_no, modified_date, var_admission_no,))
            con.commit()
            QMessageBox.information(self, "Pupil/Student Modification", "Pupil/Student's details modified successfully", QMessageBox.Ok)
            self.displayClasses()
        except Error:
            QMessageBox.critical(self, "Editing Pupil/Student","ERROR: "+ new_admission_no + " already exists", QMessageBox.Ok)
        finally:
            con.close()
            self.stud_edit.close()

    def deleteStud(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no = self.ui.stud_name_comboBox.currentText()
        cmd = "DELETE FROM t_studs WHERE admission_no = ?"
        if stud_no == "Select an admission number":
            QMessageBox.critical(self, 'Deleting Pupil/Student', "ERROR: Please select a pupil/student to delete", QMessageBox.Ok)
        else:
            buttonReply = QMessageBox.warning(self, "Deleting Pupil/Student", "WARNING: Deleting this pupil/student will delete all his/her record in the system. Do you still wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                cur.execute(cmd, (stud_no,))
                con.commit()
                self.displayClasses()
                con.close()

    def showEditPrin(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        cmd1 = "SELECT * FROM t_senior_users WHERE role = 'principal'"
        cur.execute(cmd1)
        row = cur.fetchone()
        if row == None:
            self.ui.principal_edit_lineEdit.show()
            self.ui.principal_update_btn.show()
        elif row[5] == None:
            self.ui.principal_edit_lineEdit.show()
            self.ui.principal_edit_lineEdit.setText(row[1])
            self.ui.prin_browse_btn.show()
            pixmap = QPixmap()
            #pixmap.loadFromData(QByteArray.fromBase64(row[5]))
            self.ui.prin_sig_label.setPixmap(QPixmap(pixmap))
            self.ui.principal_update_btn.show()
        else:
            self.ui.principal_edit_lineEdit.show()
            self.ui.principal_edit_lineEdit.setText(row[1])
            self.ui.prin_browse_btn.show()
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray.fromBase64(row[5]))
            self.ui.prin_sig_label.setPixmap(QPixmap(pixmap))
            self.ui.principal_update_btn.show()

    def browsePrinSig(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', 'Image Files (*.png *.jpg *gif)')
        image_path = file_name[0]
        pixmap = QPixmap(image_path)
        self.ui.prin_sig_label.setPixmap(QPixmap(pixmap))

    def editPrin(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        new_principal = self.ui.principal_edit_lineEdit.text()
        buff = QBuffer()
        buff.open(QIODevice.WriteOnly)
        pixmap = QPixmap(self.ui.prin_sig_label.pixmap())
        pixmap.save(buff, "PNG")
        binary_img = buff.data().toBase64().data()

        cmd1 = "SELECT * FROM t_senior_users WHERE role = 'principal'"
        try:
            row = cur.fetchone()
            cmd2 = "UPDATE t_senior_users SET role = 'principal', name = ?, sig = ? WHERE role = 'principal'"
            cur.execute(cmd2, (new_principal, binary_img,))
            con.commit()
            QMessageBox.information(self, "Principal Modification", "Principal modified successfully", QMessageBox.Ok)
        except Error as e:
            QMessageBox.critical(self, "Editing Principal", str(e), QMessageBox.Ok)
        finally:
            con.close()

    def showEditHead(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        cmd1 = "SELECT * FROM t_senior_users WHERE role = 'headmaster'"
        cur.execute(cmd1)
        row = cur.fetchone()
        if row == None:
            self.ui.headmaster_edit_lineEdit.show()
            self.ui.headmaster_update_btn.show()
        elif row[5] == None:
            self.ui.headmaster_edit_lineEdit.show()
            self.ui.headmaster_edit_lineEdit.setText(row[1])
            self.ui.head_browse_btn.show()
            pixmap = QPixmap()
            #pixmap.loadFromData(QByteArray.fromBase64(row[5]))
            self.ui.head_sig_label.setPixmap(QPixmap(pixmap))
            self.ui.headmaster_update_btn.show()
        else:
            self.ui.headmaster_edit_lineEdit.show()
            self.ui.headmaster_edit_lineEdit.setText(row[1])
            self.ui.head_browse_btn.show()
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray.fromBase64(row[5]))
            self.ui.head_sig_label.setPixmap(QPixmap(pixmap))
            self.ui.headmaster_update_btn.show()

    def browseHeadSig(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', 'Image Files (*.png *.jpg *gif)')
        image_path = file_name[0]
        pixmap = QPixmap(image_path)
        self.ui.head_sig_label.setPixmap(QPixmap(pixmap))

    def editHead(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        new_headmaster = self.ui.headmaster_edit_lineEdit.text()
        buff = QBuffer()
        buff.open(QIODevice.WriteOnly)
        pixmap = QPixmap(self.ui.head_sig_label.pixmap())
        pixmap.save(buff, "PNG")
        binary_img = buff.data().toBase64().data()

        cmd1 = "SELECT * FROM t_senior_users WHERE role = 'headmaster'"
        try:
            row = cur.fetchone()
            cmd2 = "UPDATE t_senior_users SET role = 'headmaster', name = ?, sig = ? WHERE role = 'headmaster'"
            cur.execute(cmd2, (new_headmaster, binary_img,))
            con.commit()
            QMessageBox.information(self, "Headmaster Modification", "Headmaster modified successfully", QMessageBox.Ok)
        except Error as e:
            QMessageBox.critical(self, "Editing Headmaster", str(e), QMessageBox.Ok)
        finally:
            con.close()

    def showEditMgmt(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        cmd1 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
        cur.execute(cmd1)
        row = cur.fetchone()
        if row == None:
            self.ui.session_lineEdit.show()
            self.ui.session_label.show()
            self.ui.next_term_label.show()
            self.ui.next_term_lineEdit.show()
            self.ui.mgmt_update_btn.show()
        else:
            self.ui.session_lineEdit.show()
            self.ui.session_lineEdit.setText(row[2])
            self.ui.session_label.show()
            self.ui.next_term_label.show()
            self.ui.fees_label.show()
            self.ui.next_term_lineEdit.show()
            self.ui.next_term_lineEdit.setText(row[3])
            self.ui.fees_lineEdit.show()
            self.ui.fees_lineEdit2.show()
            self.ui.fees_lineEdit3.show()
            self.ui.fees_lineEdit4.show()
            self.ui.fees_lineEdit.setText(row[4])
            self.ui.fees_lineEdit2.setText(row[6])
            self.ui.fees_lineEdit3.setText(row[7])
            self.ui.fees_lineEdit4.setText(row[8])
            self.ui.mgmt_update_btn.show()

    def editMgmt(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        new_session = self.ui.session_lineEdit.text()
        new_term = self.ui.next_term_lineEdit.text()
        new_fees = self.ui.fees_lineEdit.text()
        new_fees2 = self.ui.fees_lineEdit2.text()
        new_fees3 = self.ui.fees_lineEdit3.text()
        new_fees4 = self.ui.fees_lineEdit4.text()
        cmd1 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
        try:
            row = cur.fetchone()
            cmd2 = "UPDATE t_senior_users SET role = 'mgmt', session = ?, term_begins = ?, fees = ?, fees2 = ?, fees3 = ?, fees4 = ? WHERE role = 'mgmt'"
            cur.execute(cmd2, (new_session, new_term, new_fees, new_fees2, new_fees3, new_fees4,))
            con.commit()
            QMessageBox.information(self, "Session and Term Modification", "Modified successfully", QMessageBox.Ok)
        except Error as e:
            QMessageBox.critical(self, "Session and Term Modification", str(e), QMessageBox.Ok)
        finally:
            con.close()

    def setPaid(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        try:
            cmd1 = "UPDATE t_studs SET fees = 'Paid'"
            cur.execute(cmd1,)
            con.commit()
            QMessageBox.information(self, "Fees Management", "All Pupils/Students's changed to 'Paid'", QMessageBox.Ok)
        except Error as e:
            QMessageBox.critical(self, "Fees Management", str(e), QMessageBox.Ok)
        finally:
            con.close()

    def setNotPaid(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        try:
            cmd1 = "UPDATE t_studs SET fees = 'Owing'"
            cur.execute(cmd1,)
            con.commit()
            QMessageBox.information(self, "Fees Management", "All Pupils/Students's changed to 'Owing'", QMessageBox.Ok)
        except Error as e:
            QMessageBox.critical(self, "Fees Management", str(e), QMessageBox.Ok)
        finally:
            con.close()

    def browseReceiverSig(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', 'Image Files (*.png *.jpg *gif)')
        image_path = file_name[0]
        pixmap = QPixmap(image_path)
        self.ui.receiver_sig_label.setPixmap(QPixmap(pixmap))

    def editReceiver(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        buff = QBuffer()
        buff.open(QIODevice.WriteOnly)
        pixmap = QPixmap(self.ui.receiver_sig_label.pixmap())
        pixmap.save(buff, "PNG")
        binary_img = buff.data().toBase64().data()

        cmd1 = "SELECT * FROM t_senior_users WHERE role = 'receiver'"
        try:
            row = cur.fetchone()
            cmd2 = "UPDATE t_senior_users SET role = 'receiver', sig = ? WHERE role = 'receiver'"
            cur.execute(cmd2, (binary_img,))
            con.commit()
            QMessageBox.information(self, "Receiver Modification", "Reciever's signature modified successfully", QMessageBox.Ok)
        except Error as e:
            QMessageBox.critical(self, "Editing receiver", str(e), QMessageBox.Ok)
        finally:
            con.close()

    def printReceipts(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        admission_no1 = self.ui.adm_no_lineEdit.text()
        admission_no2 = self.ui.adm_no_lineEdit_2.text()
        admission_no3 = self.ui.adm_no_lineEdit_3.text()
        admission_no4 = self.ui.adm_no_lineEdit_4.text()
        admission_no5 = self.ui.adm_no_lineEdit_5.text()
        admission_no6 = self.ui.adm_no_lineEdit_6.text()
        if admission_no1 == "" and admission_no2 == "" and admission_no3 == "" and admission_no4 == "" and admission_no5 == "" and admission_no6 == "":
            QMessageBox.critical(self, "Generating Receipt", "ERROR: Please fill in an admission number before generating", QMessageBox.Ok)
        else:
            try:
                cmd1 = "SELECT * FROM t_studs WHERE admission_no = ?"
                cur.execute(cmd1, (admission_no1,))
                row = cur.fetchone()
                if row == None:
                    pass
                else:
                    self.receipt.ui.name_label.setText(str(row[1]))
                    self.receipt.ui.amount_label.setText(str(row[4]))
                    self.receipt.ui.amount_label_2.setText(str(row[4]))
                cmd2 = "SELECT * FROM t_studs WHERE admission_no = ?"
                cur.execute(cmd2, (admission_no2,))
                row = cur.fetchone()
                if row == None:
                    pass
                else:
                    self.receipt.ui.name2_label.setText(str(row[1]))
                    self.receipt.ui.amount2_label.setText(str(row[4]))
                    self.receipt.ui.amount2_label_2.setText(str(row[4]))
                cmd3 = "SELECT * FROM t_studs WHERE admission_no = ?"
                cur.execute(cmd3, (admission_no3,))
                row = cur.fetchone()
                if row == None:
                    pass
                else:
                    self.receipt.ui.name3_label.setText(str(row[1]))
                    self.receipt.ui.amount3_label.setText(str(row[4]))
                    self.receipt.ui.amount3_label_2.setText(str(row[4]))
                cmd4 = "SELECT * FROM t_studs WHERE admission_no = ?"
                cur.execute(cmd4, (admission_no4,))
                row = cur.fetchone()
                if row == None:
                    pass
                else:
                    self.receipt.ui.name4_label.setText(str(row[1]))
                    self.receipt.ui.amount4_label.setText(str(row[4]))
                    self.receipt.ui.amount4_label_2.setText(str(row[4]))
                cmd5 = "SELECT * FROM t_studs WHERE admission_no = ?"
                cur.execute(cmd5, (admission_no5,))
                row = cur.fetchone()
                if row == None:
                    pass
                else:
                    self.receipt.ui.name5_label.setText(str(row[1]))
                    self.receipt.ui.amount5_label.setText(str(row[4]))
                    self.receipt.ui.amount5_label_2.setText(str(row[4]))
                cmd6 = "SELECT * FROM t_studs WHERE admission_no = ?"
                cur.execute(cmd6, (admission_no6,))
                row = cur.fetchone()
                if row == None:
                    pass
                else:
                    self.receipt.ui.name6_label.setText(str(row[1]))
                    self.receipt.ui.amount6_label.setText(str(row[4]))
                    self.receipt.ui.amount6_label_2.setText(str(row[4]))
                cmd7 = "SELECT * FROM t_senior_users WHERE role = 'receiver'"
                cur.execute(cmd7)
                row = cur.fetchone()
                pixmap = QPixmap()
                pixmap.loadFromData(QByteArray.fromBase64(row[5]))
                self.receipt.ui.receiver_sig_label.setPixmap(QPixmap(pixmap))
                self.receipt.ui.receiver2_sig_label.setPixmap(QPixmap(pixmap))
                self.receipt.ui.receiver3_sig_label.setPixmap(QPixmap(pixmap))
                self.receipt.ui.receiver4_sig_label.setPixmap(QPixmap(pixmap))
                self.receipt.ui.receiver5_sig_label.setPixmap(QPixmap(pixmap))
                self.receipt.ui.receiver6_sig_label.setPixmap(QPixmap(pixmap))
                self.printPDF()
            except Error as e:
                QMessageBox.critical(self, "Saving Score", str(e), QMessageBox.Ok)
            except TypeError as e:
                QMessageBox.critical(self, "Saving Score", str(e), QMessageBox.Ok)
            finally:
                con.close()

    def print_widget(self, widget, filename):
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        printer.setOutputFileName(filename)
        painter = QtGui.QPainter(printer)
        # start scale
        xscale = printer.pageRect().width() * 1.0 / widget.width()
        yscale = printer.pageRect().height() * 1.0 / widget.height()
        scale = min(xscale, yscale)
        painter.translate(printer.paperRect().center())
        painter.scale(scale, scale)
        painter.translate(-widget.width() / 2, -widget.height() / 2)
        # end scale
        widget.render(painter)
        painter.end()

    def printPDF(self):
        fn, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Export PDF", None, "PDF files (.pdf);;All Files()"
        )
        if fn:
            if QtCore.QFileInfo(fn).suffix() == "":
                fn += ".pdf"
            #print_widget(self.label, fn)
            self.print_widget(self.receipt, fn)

class Receipt(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ReceiptForm()
        self.ui.setupUi(self)
        #Generates Current Date
        self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.ui.dateTimeEdit.hide()
        self.ui.print_date_label.setText(self.ui.dateTimeEdit.text())
        self.ui.print_date_label_2.setText(self.ui.dateTimeEdit.text())
        self.ui.print_date_label_3.setText(self.ui.dateTimeEdit.text())
        self.ui.print_date_label_4.setText(self.ui.dateTimeEdit.text())
        self.ui.print_date_label_5.setText(self.ui.dateTimeEdit.text())
        self.ui.print_date_label_6.setText(self.ui.dateTimeEdit.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = InherAdmin()
    widget.show()
    sys.exit(app.exec_())
