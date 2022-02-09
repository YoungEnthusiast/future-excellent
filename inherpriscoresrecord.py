import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import QDateTime, QByteArray
from prireport import Ui_PriReportForm
# from prireport2nd import Ui_PriReport2ndForm
# from prireport3rd import Ui_PriReport3rdForm

from priscoresrecord import Ui_PriScoreRecForm
# from priscoresrecord2nd import Ui_PriScoreRec2ndForm
# from priscoresrecord3rd import Ui_PriScoreRec3rdForm
from priscoreslist import Ui_PriScoreForm
# from priscoreslist2nd import Ui_PriScore2ndForm
# from priscoreslist3rd import Ui_PriScore3rdForm

import sqlite3
from sqlite3 import Error

class PriScoresRecord(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PriScoreRecForm()
        self.ui.setupUi(self)
        self.displayClasses()
        self.ui.class_comboBox.currentTextChanged.connect(self.displayStuds)
        self.ui.stud_adm_no_comboBox.currentTextChanged.connect(self.displayName)
        self.ui.stud_adm_no_comboBox.currentTextChanged.connect(self.displaySpinVals)

        self.ui.qur_score_btn.clicked.connect(self.saveEnglishScores)
        self.ui.qur_score_btn.clicked.connect(self.saveMathScores)
        self.ui.qur_score_btn.clicked.connect(self.saveIrsScores)
        self.ui.qur_score_btn.clicked.connect(self.saveCivicScores)
        self.ui.qur_score_btn.clicked.connect(self.saveComputerScores)
        self.ui.qur_score_btn.clicked.connect(self.saveBasicScores)
        self.ui.qur_score_btn.clicked.connect(self.saveQuantScores)
        self.ui.qur_score_btn.clicked.connect(self.saveVerbalScores)
        self.ui.qur_score_btn.clicked.connect(self.saveArabicScores)
        self.ui.qur_score_btn.clicked.connect(self.saveQurScores)
        self.ui.qur_score_btn.clicked.connect(self.saveAgricScores)
        self.ui.qur_score_btn.clicked.connect(self.savePheScores)
        self.ui.qur_score_btn.clicked.connect(self.saveCreativeScores)
        self.ui.qur_score_btn.clicked.connect(self.saveHandwiritingScores)

        self.ui.qur_score_btn.clicked.connect(self.computeTotAvg)

    def displayClasses(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        query = cur.execute('SELECT * FROM t_classes ORDER BY class_name')
        rows = cur.fetchall()
        classes = ["Select a class"]
        self.ui.class_comboBox.clear()
        for row in rows:
            classes.append(row[0])
        self.ui.class_comboBox.addItems(classes)
        con.commit()
        con.close()

    def displayStuds(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox.currentText()
        cmd = "SELECT * FROM t_studs WHERE stud_class = ? ORDER BY admission_no"
        cur.execute(cmd, (classes_combo,))
        rows = cur.fetchall()
        adm_nos = ["Select a pupil"]
        self.ui.stud_adm_no_comboBox.clear()
        for row in rows:
            adm_nos.append(row[0])
        self.ui.stud_adm_no_comboBox.addItems(adm_nos)
        con.close()

    def displayName(self):
        self.ui.name_label.setText("")
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no_combo = self.ui.stud_adm_no_comboBox.currentText()
        cmd = "SELECT * FROM t_studs WHERE admission_no = ?"
        cur.execute(cmd, (stud_no_combo,))
        row = cur.fetchone()
        if row == None:
            self.ui.name_label.setText("")
        else:
            self.ui.name_label.setText("Name: " + row[1])

    def displaySpinVals(self):
        self.ui.eng_c1_spin.setValue(0)
        self.ui.eng_c2_spin.setValue(0)
        self.ui.eng_ass_spin.setValue(0)
        self.ui.eng_att_spin.setValue(0)
        self.ui.eng_exam_spin.setValue(0)
        self.ui.math_c1_spin.setValue(0)
        self.ui.math_c2_spin.setValue(0)
        self.ui.math_ass_spin.setValue(0)
        self.ui.math_att_spin.setValue(0)
        self.ui.math_exam_spin.setValue(0)
        self.ui.irs_c1_spin.setValue(0)
        self.ui.irs_c2_spin.setValue(0)
        self.ui.irs_ass_spin.setValue(0)
        self.ui.irs_att_spin.setValue(0)
        self.ui.irs_exam_spin.setValue(0)
        self.ui.civic_c1_spin.setValue(0)
        self.ui.civic_c2_spin.setValue(0)
        self.ui.civic_ass_spin.setValue(0)
        self.ui.civic_att_spin.setValue(0)
        self.ui.civic_exam_spin.setValue(0)
        self.ui.computer_c1_spin.setValue(0)
        self.ui.computer_c2_spin.setValue(0)
        self.ui.computer_ass_spin.setValue(0)
        self.ui.computer_att_spin.setValue(0)
        self.ui.computer_exam_spin.setValue(0)
        self.ui.basic_c1_spin.setValue(0)
        self.ui.basic_c2_spin.setValue(0)
        self.ui.basic_ass_spin.setValue(0)
        self.ui.basic_att_spin.setValue(0)
        self.ui.basic_exam_spin.setValue(0)
        self.ui.quant_c1_spin.setValue(0)
        self.ui.quant_c2_spin.setValue(0)
        self.ui.quant_ass_spin.setValue(0)
        self.ui.quant_att_spin.setValue(0)
        self.ui.quant_exam_spin.setValue(0)
        self.ui.verbal_c1_spin.setValue(0)
        self.ui.verbal_c2_spin.setValue(0)
        self.ui.verbal_ass_spin.setValue(0)
        self.ui.verbal_att_spin.setValue(0)
        self.ui.verbal_exam_spin.setValue(0)
        self.ui.arabic_c1_spin.setValue(0)
        self.ui.arabic_c2_spin.setValue(0)
        self.ui.arabic_ass_spin.setValue(0)
        self.ui.arabic_att_spin.setValue(0)
        self.ui.arabic_exam_spin.setValue(0)
        self.ui.qur_c1_spin.setValue(0)
        self.ui.qur_c2_spin.setValue(0)
        self.ui.qur_ass_spin.setValue(0)
        self.ui.qur_att_spin.setValue(0)
        self.ui.qur_exam_spin.setValue(0)
        self.ui.agric_c1_spin.setValue(0)
        self.ui.agric_c2_spin.setValue(0)
        self.ui.agric_ass_spin.setValue(0)
        self.ui.agric_att_spin.setValue(0)
        self.ui.agric_exam_spin.setValue(0)
        self.ui.phe_c1_spin.setValue(0)
        self.ui.phe_c2_spin.setValue(0)
        self.ui.phe_ass_spin.setValue(0)
        self.ui.phe_att_spin.setValue(0)
        self.ui.phe_exam_spin.setValue(0)
        self.ui.creative_c1_spin.setValue(0)
        self.ui.creative_c2_spin.setValue(0)
        self.ui.creative_ass_spin.setValue(0)
        self.ui.creative_att_spin.setValue(0)
        self.ui.creative_exam_spin.setValue(0)
        self.ui.handwriting_c1_spin.setValue(0)
        self.ui.handwriting_c2_spin.setValue(0)
        self.ui.handwriting_ass_spin.setValue(0)
        self.ui.handwriting_att_spin.setValue(0)
        self.ui.handwriting_exam_spin.setValue(0)

        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        try:
            cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row != None and row[3] != None and row[4] != None and row[5] != None and row[6] != None and row[7] != None:
                self.ui.eng_c1_spin.setValue(row[3])
                self.ui.eng_c2_spin.setValue(row[4])
                self.ui.eng_ass_spin.setValue(row[5])
                self.ui.eng_att_spin.setValue(row[6])
                self.ui.eng_exam_spin.setValue(row[7])
            if row != None and row[9] != None and row[10] != None and row[11] != None and row[12] != None and row[13] != None:
                self.ui.math_c1_spin.setValue(row[9])
                self.ui.math_c2_spin.setValue(row[10])
                self.ui.math_ass_spin.setValue(row[11])
                self.ui.math_att_spin.setValue(row[12])
                self.ui.math_exam_spin.setValue(row[13])
            if row != None and row[15] != None and row[16] != None and row[17] != None and row[18] != None and row[19] != None:
                self.ui.irs_c1_spin.setValue(row[15])
                self.ui.irs_c2_spin.setValue(row[16])
                self.ui.irs_ass_spin.setValue(row[17])
                self.ui.irs_att_spin.setValue(row[18])
                self.ui.irs_exam_spin.setValue(row[19])
            if row != None and row[21] != None and row[22] != None and row[23] != None and row[24] != None and row[25] != None:
                self.ui.civic_c1_spin.setValue(row[21])
                self.ui.civic_c2_spin.setValue(row[22])
                self.ui.civic_ass_spin.setValue(row[23])
                self.ui.civic_att_spin.setValue(row[24])
                self.ui.civic_exam_spin.setValue(row[25])
            if row != None and row[27] != None and row[28] != None and row[29] != None and row[30] != None and row[31] != None:
                self.ui.computer_c1_spin.setValue(row[27])
                self.ui.computer_c2_spin.setValue(row[28])
                self.ui.computer_ass_spin.setValue(row[29])
                self.ui.computer_att_spin.setValue(row[30])
                self.ui.computer_exam_spin.setValue(row[31])
            if row != None and row[33] != None and row[34] != None and row[35] != None and row[36] != None and row[37] != None:
                self.ui.basic_c1_spin.setValue(row[33])
                self.ui.basic_c2_spin.setValue(row[34])
                self.ui.basic_ass_spin.setValue(row[35])
                self.ui.basic_att_spin.setValue(row[36])
                self.ui.basic_exam_spin.setValue(row[37])
            if row != None and row[39] != None and row[40] != None and row[41] != None and row[42] != None and row[43] != None:
                self.ui.quant_c1_spin.setValue(row[39])
                self.ui.quant_c2_spin.setValue(row[40])
                self.ui.quant_ass_spin.setValue(row[41])
                self.ui.quant_att_spin.setValue(row[42])
                self.ui.quant_exam_spin.setValue(row[43])
            if row != None and row[45] != None and row[46] != None and row[47] != None and row[48] != None and row[49] != None:
                self.ui.verbal_c1_spin.setValue(row[45])
                self.ui.verbal_c2_spin.setValue(row[46])
                self.ui.verbal_ass_spin.setValue(row[47])
                self.ui.verbal_att_spin.setValue(row[48])
                self.ui.verbal_exam_spin.setValue(row[49])
            if row != None and row[51] != None and row[52] != None and row[53] != None and row[54] != None and row[55] != None:
                self.ui.arabic_c1_spin.setValue(row[51])
                self.ui.arabic_c2_spin.setValue(row[52])
                self.ui.arabic_ass_spin.setValue(row[53])
                self.ui.arabic_att_spin.setValue(row[54])
                self.ui.arabic_exam_spin.setValue(row[55])
            if row != None and row[57] != None and row[58] != None and row[59] != None and row[60] != None and row[61] != None:
                self.ui.qur_c1_spin.setValue(row[57])
                self.ui.qur_c2_spin.setValue(row[58])
                self.ui.qur_ass_spin.setValue(row[59])
                self.ui.qur_att_spin.setValue(row[60])
                self.ui.qur_exam_spin.setValue(row[61])
            if row != None and row[63] != None and row[64] != None and row[65] != None and row[66] != None and row[67] != None:
                self.ui.agric_c1_spin.setValue(row[63])
                self.ui.agric_c2_spin.setValue(row[64])
                self.ui.agric_ass_spin.setValue(row[65])
                self.ui.agric_att_spin.setValue(row[66])
                self.ui.agric_exam_spin.setValue(row[67])
            if row != None and row[69] != None and row[70] != None and row[71] != None and row[72] != None and row[73] != None:
                self.ui.phe_c1_spin.setValue(row[69])
                self.ui.phe_c2_spin.setValue(row[70])
                self.ui.phe_ass_spin.setValue(row[71])
                self.ui.phe_att_spin.setValue(row[72])
                self.ui.phe_exam_spin.setValue(row[73])
            if row != None and row[75] != None and row[76] != None and row[77] != None and row[78] != None and row[79] != None:
                self.ui.creative_c1_spin.setValue(row[75])
                self.ui.creative_c2_spin.setValue(row[76])
                self.ui.creative_ass_spin.setValue(row[77])
                self.ui.creative_att_spin.setValue(row[78])
                self.ui.creative_exam_spin.setValue(row[79])
            if row != None and row[81] != None and row[82] != None and row[83] != None and row[84] != None and row[85] != None:
                self.ui.handwriting_c1_spin.setValue(row[81])
                self.ui.handwriting_c2_spin.setValue(row[82])
                self.ui.handwriting_ass_spin.setValue(row[83])
                self.ui.handwriting_att_spin.setValue(row[84])
                self.ui.handwriting_exam_spin.setValue(row[85])
        except Error as e:
            QMessageBox.critical(self, "Saving Score", str(e), QMessageBox.Ok)

    def saveEnglishScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        eng_c1 = self.ui.eng_c1_spin.value()
        eng_c2 = self.ui.eng_c2_spin.value()
        eng_ass = self.ui.eng_ass_spin.value()
        eng_att = self.ui.eng_att_spin.value()
        eng_exam = self.ui.eng_exam_spin.value()
        eng_total = eng_c1 + eng_c2 + eng_ass + eng_att + eng_exam
        cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_first(stud_no, score_class, eng_c1, eng_c2, eng_ass, eng_att, eng_exam, eng_total) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, eng_c1, eng_c2, eng_ass, eng_att, eng_exam, eng_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_first SET stud_no = ?, score_class = ?, eng_c1 = ?, eng_c2 = ?, eng_ass = ?, eng_att = ?, eng_exam = ?, eng_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, eng_c1, eng_c2, eng_ass, eng_att, eng_exam, eng_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveMathScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        math_c1 = self.ui.math_c1_spin.value()
        math_c2 = self.ui.math_c2_spin.value()
        math_ass = self.ui.math_ass_spin.value()
        math_att = self.ui.math_att_spin.value()
        math_exam = self.ui.math_exam_spin.value()
        math_total = math_c1 + math_c2 + math_ass + math_att + math_exam
        cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_first(stud_no, score_class, math_c1, math_c2, math_ass, math_att, math_exam, math_total) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, math_c1, math_c2, math_ass, math_att, math_exam, math_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_first SET stud_no = ?, score_class = ?, math_c1 = ?, math_c2 = ?, math_ass = ?, math_att = ?, math_exam = ?, math_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, math_c1, math_c2, math_ass, math_att, math_exam, math_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveIrsScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        irs_c1 = self.ui.irs_c1_spin.value()
        irs_c2 = self.ui.irs_c2_spin.value()
        irs_ass = self.ui.irs_ass_spin.value()
        irs_att = self.ui.irs_att_spin.value()
        irs_exam = self.ui.irs_exam_spin.value()
        irs_total = irs_c1 + irs_c2 + irs_ass + irs_att + irs_exam
        cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_first(stud_no, score_class, irs_c1, irs_c2, irs_ass, irs_att, irs_exam, irs_total) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, irs_c1, irs_c2, irs_ass, irs_att, irs_exam, irs_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_first SET stud_no = ?, score_class = ?, irs_c1 = ?, irs_c2 = ?, irs_ass = ?, irs_att = ?, irs_exam = ?, irs_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, irs_c1, irs_c2, irs_ass, irs_att, irs_exam, irs_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveCivicScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        civic_c1 = self.ui.civic_c1_spin.value()
        civic_c2 = self.ui.civic_c2_spin.value()
        civic_ass = self.ui.civic_ass_spin.value()
        civic_att = self.ui.civic_att_spin.value()
        civic_exam = self.ui.civic_exam_spin.value()
        civic_total = civic_c1 + civic_c2 + civic_ass + civic_att + civic_exam
        cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_first(stud_no, score_class, civic_c1, civic_c2, civic_ass, civic_att, civic_exam, civic_total) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, civic_c1, civic_c2, civic_ass, civic_att, civic_exam, civic_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_first SET stud_no = ?, score_class = ?, civic_c1 = ?, civic_c2 = ?, civic_ass = ?, civic_att = ?, civic_exam = ?, civic_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, civic_c1, civic_c2, civic_ass, civic_att, civic_exam, civic_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveComputerScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        computer_c1 = self.ui.computer_c1_spin.value()
        computer_c2 = self.ui.computer_c2_spin.value()
        computer_ass = self.ui.computer_ass_spin.value()
        computer_att = self.ui.computer_att_spin.value()
        computer_exam = self.ui.computer_exam_spin.value()
        computer_total = computer_c1 + computer_c2 + computer_ass + computer_att + computer_exam
        cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_first(stud_no, score_class, computer_c1, computer_c2, computer_ass, computer_att, computer_exam, computer_total) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, computer_c1, computer_c2, computer_ass, computer_att, computer_exam, computer_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_first SET stud_no = ?, score_class = ?, computer_c1 = ?, computer_c2 = ?, computer_ass = ?, computer_att = ?, computer_exam = ?, computer_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, computer_c1, computer_c2, computer_ass, computer_att, computer_exam, computer_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveBasicScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        basic_c1 = self.ui.basic_c1_spin.value()
        basic_c2 = self.ui.basic_c2_spin.value()
        basic_ass = self.ui.basic_ass_spin.value()
        basic_att = self.ui.basic_att_spin.value()
        basic_exam = self.ui.basic_exam_spin.value()
        basic_total = basic_c1 + basic_c2 + basic_ass + basic_att + basic_exam
        cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_first(stud_no, score_class, basic_c1, basic_c2, basic_ass, basic_att, basic_exam, basic_total) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, basic_c1, basic_c2, basic_ass, basic_att, basic_exam, basic_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_first SET stud_no = ?, score_class = ?, basic_c1 = ?, basic_c2 = ?, basic_ass = ?, basic_att = ?, basic_exam = ?, basic_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, basic_c1, basic_c2, basic_ass, basic_att, basic_exam, basic_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveQuantScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        quant_c1 = self.ui.quant_c1_spin.value()
        quant_c2 = self.ui.quant_c2_spin.value()
        quant_ass = self.ui.quant_ass_spin.value()
        quant_att = self.ui.quant_att_spin.value()
        quant_exam = self.ui.quant_exam_spin.value()
        quant_total = quant_c1 + quant_c2 + quant_ass + quant_att + quant_exam
        cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_first(stud_no, score_class, quant_c1, quant_c2, quant_ass, quant_att, quant_exam, quant_total) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, quant_c1, quant_c2, quant_ass, quant_att, quant_exam, quant_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_first SET stud_no = ?, score_class = ?, quant_c1 = ?, quant_c2 = ?, quant_ass = ?, quant_att = ?, quant_exam = ?, quant_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, quant_c1, quant_c2, quant_ass, quant_att, quant_exam, quant_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveVerbalScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        verbal_c1 = self.ui.verbal_c1_spin.value()
        verbal_c2 = self.ui.verbal_c2_spin.value()
        verbal_ass = self.ui.verbal_ass_spin.value()
        verbal_att = self.ui.verbal_att_spin.value()
        verbal_exam = self.ui.verbal_exam_spin.value()
        verbal_total = verbal_c1 + verbal_c2 + verbal_ass + verbal_att + verbal_exam
        cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_first(stud_no, score_class, verbal_c1, verbal_c2, verbal_ass, verbal_att, verbal_exam, verbal_total) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, verbal_c1, verbal_c2, verbal_ass, verbal_att, verbal_exam, verbal_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_first SET stud_no = ?, score_class = ?, verbal_c1 = ?, verbal_c2 = ?, verbal_ass = ?, verbal_att = ?, verbal_exam = ?, verbal_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, verbal_c1, verbal_c2, verbal_ass, verbal_att, verbal_exam, verbal_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveArabicScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        arabic_c1 = self.ui.arabic_c1_spin.value()
        arabic_c2 = self.ui.arabic_c2_spin.value()
        arabic_ass = self.ui.arabic_ass_spin.value()
        arabic_att = self.ui.arabic_att_spin.value()
        arabic_exam = self.ui.arabic_exam_spin.value()
        arabic_total = arabic_c1 + arabic_c2 + arabic_ass + arabic_att + arabic_exam
        cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_first(stud_no, score_class, arabic_c1, arabic_c2, arabic_ass, arabic_att, arabic_exam, arabic_total) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, arabic_c1, arabic_c2, arabic_ass, arabic_att, arabic_exam, arabic_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_first SET stud_no = ?, score_class = ?, arabic_c1 = ?, arabic_c2 = ?, arabic_ass = ?, arabic_att = ?, arabic_exam = ?, arabic_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, arabic_c1, arabic_c2, arabic_ass, arabic_att, arabic_exam, arabic_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveQurScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        qur_c1 = self.ui.qur_c1_spin.value()
        qur_c2 = self.ui.qur_c2_spin.value()
        qur_ass = self.ui.qur_ass_spin.value()
        qur_att = self.ui.qur_att_spin.value()
        qur_exam = self.ui.qur_exam_spin.value()
        qur_total = qur_c1 + qur_c2 + qur_ass + qur_att + qur_exam
        cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_first(stud_no, score_class, qur_c1, qur_c2, qur_ass, qur_att, qur_exam, qur_total) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, qur_c1, qur_c2, qur_ass, qur_att, qur_exam, qur_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_first SET stud_no = ?, score_class = ?, qur_c1 = ?, qur_c2 = ?, qur_ass = ?, qur_att = ?, qur_exam = ?, qur_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, qur_c1, qur_c2, qur_ass, qur_att, qur_exam, qur_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveAgricScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        agric_c1 = self.ui.agric_c1_spin.value()
        agric_c2 = self.ui.agric_c2_spin.value()
        agric_ass = self.ui.agric_ass_spin.value()
        agric_att = self.ui.agric_att_spin.value()
        agric_exam = self.ui.agric_exam_spin.value()
        agric_total = agric_c1 + agric_c2 + agric_ass + agric_att + agric_exam
        cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_first(stud_no, score_class, agric_c1, agric_c2, agric_ass, agric_att, agric_exam, agric_total) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, agric_c1, agric_c2, agric_ass, agric_att, agric_exam, agric_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_first SET stud_no = ?, score_class = ?, agric_c1 = ?, agric_c2 = ?, agric_ass = ?, agric_att = ?, agric_exam = ?, agric_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, agric_c1, agric_c2, agric_ass, agric_att, agric_exam, agric_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def savePheScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        phe_c1 = self.ui.phe_c1_spin.value()
        phe_c2 = self.ui.phe_c2_spin.value()
        phe_ass = self.ui.phe_ass_spin.value()
        phe_att = self.ui.phe_att_spin.value()
        phe_exam = self.ui.phe_exam_spin.value()
        phe_total = phe_c1 + phe_c2 + phe_ass + phe_att + phe_exam
        cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_first(stud_no, score_class, phe_c1, phe_c2, phe_ass, phe_att, phe_exam, phe_total) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, phe_c1, phe_c2, phe_ass, phe_att, phe_exam, phe_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_first SET stud_no = ?, score_class = ?, phe_c1 = ?, phe_c2 = ?, phe_ass = ?, phe_att = ?, phe_exam = ?, phe_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, phe_c1, phe_c2, phe_ass, phe_att, phe_exam, phe_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveCreativeScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        creative_c1 = self.ui.creative_c1_spin.value()
        creative_c2 = self.ui.creative_c2_spin.value()
        creative_ass = self.ui.creative_ass_spin.value()
        creative_att = self.ui.creative_att_spin.value()
        creative_exam = self.ui.creative_exam_spin.value()
        creative_total = creative_c1 + creative_c2 + creative_ass + creative_att + creative_exam
        cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_first(stud_no, score_class, creative_c1, creative_c2, creative_ass, creative_att, creative_exam, creative_total) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, creative_c1, creative_c2, creative_ass, creative_att, creative_exam, creative_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_first SET stud_no = ?, score_class = ?, creative_c1 = ?, creative_c2 = ?, creative_ass = ?, creative_att = ?, creative_exam = ?, creative_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, creative_c1, creative_c2, creative_ass, creative_att, creative_exam, creative_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveHandwiritingScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        handwriting_c1 = self.ui.handwriting_c1_spin.value()
        handwriting_c2 = self.ui.handwriting_c2_spin.value()
        handwriting_ass = self.ui.handwriting_ass_spin.value()
        handwriting_att = self.ui.handwriting_att_spin.value()
        handwriting_exam = self.ui.handwriting_exam_spin.value()
        handwriting_total = handwriting_c1 + handwriting_c2 + handwriting_ass + handwriting_att + handwriting_exam
        cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_first(stud_no, score_class, handwriting_c1, handwriting_c2, handwriting_ass, handwriting_att, handwriting_exam, handwriting_total) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, handwriting_c1, handwriting_c2, handwriting_ass, handwriting_att, handwriting_exam, handwriting_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_first SET stud_no = ?, score_class = ?, handwriting_c1 = ?, handwriting_c2 = ?, handwriting_ass = ?, handwriting_att = ?, handwriting_exam = ?, handwriting_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, handwriting_c1, handwriting_c2, handwriting_ass, handwriting_att, handwriting_exam, handwriting_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def computeTotAvg(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        cmd1 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
        cur.execute(cmd1, (stud_no,))
        row = cur.fetchone()
        if row == None:
            pass
        elif row[8] != None and row[14] != None and row[20] != None and row[26] != None and row[32] != None and row[38] != None and row[44] != None and row[50] != None and row[56] != None and row[62] != None and row[68] != None and row[74] != None and row[80] != None and row[86] != None:
            try:
                all_total = row[8] + row[14] + row[20] + row[26] + row[32] + row[38] + row[44] + row[50] + row[56] + row[62] + row[68] + row[74] + row[80] + row[86]
                avg = round((all_total/14), 4)
                cmd2 = "UPDATE t_pri_scores_first SET stud_no = ?, all_total = ?, avg = ?  WHERE stud_no = ?"
                cur.execute(cmd2, (stud_no, all_total, avg, stud_no,))
                con.commit()
                QMessageBox.information(self, "Saving Score",  "Pupil's scores saved successfully", QMessageBox.Ok)
            except Error as e:
                QMessageBox.critical(self, "Saving Score", str(e), QMessageBox.Ok)
            except TypeError as e:
                QMessageBox.critical(self, "Saving Score", str(e), QMessageBox.Ok)
            finally:
                con.close()

class PriScoresView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PriScoreForm()
        self.ui.setupUi(self)
        self.pri_report = PriReport()
        self.displayClasses()
        self.listStudsScores()
        self.ui.class_comboBox.currentTextChanged.connect(self.listClass)
        self.ui.class_comboBox.currentTextChanged.connect(self.displayStuds)
        self.ui.switch_back_btn.clicked.connect(self.listStudsScores)
        self.ui.report_gen_btn.clicked.connect(self.displayRadios)
        self.ui.report_gen_btn.clicked.connect(self.generatePriReport)
        self.ui.pdf_btn.clicked.connect(self.displayRadios)
        self.ui.pdf_btn.clicked.connect(self.generatePriReportPDF)
        self.ui.del_btn.clicked.connect(self.deleteStud)
        self.ui.stud_adm_no_comboBox.currentTextChanged.connect(self.displayName)

    def displayClasses(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        query = cur.execute('SELECT * FROM t_pri_scores_first ORDER BY score_class')
        self.ui.class_comboBox.clear()
        classes = ["Select a class"]
        rows = cur.fetchall()
        for row in rows:
            if row[2] not in classes:
                classes.append(row[2])
        self.ui.class_comboBox.addItems(classes)
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

    def listStudsScores(self):
        self.displayClasses()
        self.ui.tableWidget_2.hide()
        self.ui.tableWidget.setRowCount(0)
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        cmd = "SELECT * FROM t_pri_scores_first ORDER BY stud_no"
        cur.execute(cmd)
        rows = cur.fetchall()
        for row_number, row_data in enumerate(rows):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                it = QTableWidgetItem()
                it.setText(str(column_data))
                self.ui.tableWidget.setItem(row_number, column_number, it)
        self.ui.tableWidget.show()
        self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.ui.tableWidget.setColumnWidth(0,0)
        con.close()

    def listClass(self):
        self.ui.tableWidget.hide()
        self.ui.tableWidget_2.setRowCount(0)
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox.currentText()
        cmd = "SELECT * FROM t_pri_scores_first WHERE score_class = ? ORDER BY stud_no"
        cur.execute(cmd, (classes_combo,))
        rows = cur.fetchall()
        for row_number, row_data in enumerate(rows):
            self.ui.tableWidget_2.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                it = QTableWidgetItem()
                it.setText(str(column_data))
                self.ui.tableWidget_2.setItem(row_number, column_number, it)
        self.ui.tableWidget_2.show()
        self.ui.tableWidget_2.horizontalHeader().setDefaultSectionSize(180)
        self.ui.tableWidget_2.setColumnWidth(0,0)
        self.ui.class_comboBox.show()
        con.close()

    def displayStuds(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox.currentText()
        cmd = "SELECT * FROM t_pri_scores_first WHERE score_class = ? ORDER BY stud_no"
        cur.execute(cmd, (classes_combo,))
        rows = cur.fetchall()
        adm_nos = ["Select an admission number"]
        self.ui.stud_adm_no_comboBox.clear()
        for row in rows:
            adm_nos.append(row[1])
        self.ui.stud_adm_no_comboBox.addItems(adm_nos)
        con.close()

    def displayName(self):
        self.ui.name_label.setText("")
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no_combo = self.ui.stud_adm_no_comboBox.currentText()
        cmd = "SELECT * FROM t_studs WHERE admission_no = ?"
        cur.execute(cmd, (stud_no_combo,))
        row = cur.fetchone()
        if row == None:
            self.ui.name_label.setText("")
        else:
            self.ui.name_label.setText("Name: \n" + row[1])

    def deleteStud(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        if stud_no == "Select an admission number":
            QMessageBox.critical(self, "Deleting Pupil", "ERROR: Please select pupil's admission number before pressing delete", QMessageBox.Ok)
        elif stud_no == "":
            QMessageBox.critical(self, "Deleting Pupil", "ERROR: Please select a class and pupil's admission number before pressing delete", QMessageBox.Ok)
        else:
            cmd = "DELETE FROM t_pri_scores_first WHERE stud_no = ?"
            buttonReply = QMessageBox.warning(self, 'Deleting Pupil', "WARNING: Deleting will remove all the pupil's score records in the class. Do you still wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                cur.execute(cmd, (stud_no,))
                con.commit()
                self.displayStuds()
                con.close()

    def generatePriReport(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox.currentText()
        admission_no = self.ui.stud_adm_no_comboBox.currentText()
        cmd1 = "SELECT * FROM t_studs WHERE admission_no = ?"
        cur.execute(cmd1, (admission_no,))
        row = cur.fetchone()
        if row == None:
            QMessageBox.critical(self, "Printing Report", "ERROR: Please select a class and pupil's admission number before generating report", QMessageBox.Ok)
        else:
            self.pri_report.ui.name_label.setText(row[1])
            self.pri_report.ui.class_label.setText(row[3])
            self.pri_report.ui.sex_label.setText(row[5])
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray.fromBase64(row[6]))
            self.pri_report.ui.photo_label.setPixmap(QPixmap(pixmap))
            try:
                cmd3 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
                cur.execute(cmd3, (admission_no,))
                row = cur.fetchone()
                self.pri_report.ui.english_c1_label.setText(str(row[3]))
                self.pri_report.ui.english_c2_label.setText(str(row[4]))
                self.pri_report.ui.english_ass_label.setText(str(row[5]))
                self.pri_report.ui.english_att_label.setText(str(row[6]))
                self.pri_report.ui.english_exam_label.setText(str(row[7]))
                self.pri_report.ui.english_total_label.setText(str(row[8]))
                if row[8] < 40:
                    self.pri_report.ui.english_grade_label.setText("F")
                    self.pri_report.ui.english_remark_label.setText("Fail")
                elif row[8] >= 40 and row[8] < 46:
                    self.pri_report.ui.english_grade_label.setText("E")
                    self.pri_report.ui.english_remark_label.setText("Pass")
                elif row[8] >= 46 and row[8] < 50:
                    self.pri_report.ui.english_grade_label.setText("D")
                    self.pri_report.ui.english_remark_label.setText("Pass")
                elif row[8] >= 50 and row[8] < 60:
                    self.pri_report.ui.english_grade_label.setText("C")
                    self.pri_report.ui.english_remark_label.setText("Good")
                elif row[8] >= 60 and row[8] < 70:
                    self.pri_report.ui.english_grade_label.setText("B")
                    self.pri_report.ui.english_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.english_grade_label.setText("A")
                    self.pri_report.ui.english_remark_label.setText("Excellent")
                self.pri_report.ui.math_c1_label.setText(str(row[9]))
                self.pri_report.ui.math_c2_label.setText(str(row[10]))
                self.pri_report.ui.math_ass_label.setText(str(row[11]))
                self.pri_report.ui.math_att_label.setText(str(row[12]))
                self.pri_report.ui.math_exam_label.setText(str(row[13]))
                self.pri_report.ui.math_total_label.setText(str(row[14]))
                if row[14] < 40:
                    self.pri_report.ui.math_grade_label.setText("F")
                    self.pri_report.ui.math_remark_label.setText("Fail")
                elif row[14] >= 40 and row[14] < 46:
                    self.pri_report.ui.math_grade_label.setText("E")
                    self.pri_report.ui.math_remark_label.setText("Pass")
                elif row[14] >= 46 and row[14] < 50:
                    self.pri_report.ui.math_grade_label.setText("D")
                    self.pri_report.ui.math_remark_label.setText("Pass")
                elif row[14] >= 50 and row[14] < 60:
                    self.pri_report.ui.math_grade_label.setText("C")
                    self.pri_report.ui.math_remark_label.setText("Good")
                elif row[14] >= 60 and row[14] < 70:
                    self.pri_report.ui.math_grade_label.setText("B")
                    self.pri_report.ui.math_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.math_grade_label.setText("A")
                    self.pri_report.ui.math_remark_label.setText("Excellent")
                self.pri_report.ui.irs_c1_label.setText(str(row[15]))
                self.pri_report.ui.irs_c2_label.setText(str(row[16]))
                self.pri_report.ui.irs_ass_label.setText(str(row[17]))
                self.pri_report.ui.irs_att_label.setText(str(row[18]))
                self.pri_report.ui.irs_exam_label.setText(str(row[19]))
                self.pri_report.ui.irs_total_label.setText(str(row[20]))
                if row[20] < 40:
                    self.pri_report.ui.irs_grade_label.setText("F")
                    self.pri_report.ui.irs_remark_label.setText("Fail")
                elif row[20] >= 40 and row[20] < 46:
                    self.pri_report.ui.irs_grade_label.setText("E")
                    self.pri_report.ui.irs_remark_label.setText("Pass")
                elif row[20] >= 46 and row[20] < 50:
                    self.pri_report.ui.irs_grade_label.setText("D")
                    self.pri_report.ui.irs_remark_label.setText("Pass")
                elif row[20] >= 50 and row[20] < 60:
                    self.pri_report.ui.irs_grade_label.setText("C")
                    self.pri_report.ui.irs_remark_label.setText("Good")
                elif row[20] >= 60 and row[20] < 70:
                    self.pri_report.ui.irs_grade_label.setText("B")
                    self.pri_report.ui.irs_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.irs_grade_label.setText("A")
                    self.pri_report.ui.irs_remark_label.setText("Excellent")
                self.pri_report.ui.civic_c1_label.setText(str(row[21]))
                self.pri_report.ui.civic_c2_label.setText(str(row[22]))
                self.pri_report.ui.civic_ass_label.setText(str(row[23]))
                self.pri_report.ui.civic_att_label.setText(str(row[24]))
                self.pri_report.ui.civic_exam_label.setText(str(row[25]))
                self.pri_report.ui.civic_total_label.setText(str(row[26]))
                if row[26] < 40:
                    self.pri_report.ui.civic_grade_label.setText("F")
                    self.pri_report.ui.civic_remark_label.setText("Fail")
                elif row[26] >= 40 and row[26] < 46:
                    self.pri_report.ui.civic_grade_label.setText("E")
                    self.pri_report.ui.civic_remark_label.setText("Pass")
                elif row[26] >= 46 and row[26] < 50:
                    self.pri_report.ui.civic_grade_label.setText("D")
                    self.pri_report.ui.civic_remark_label.setText("Pass")
                elif row[26] >= 50 and row[26] < 60:
                    self.pri_report.ui.civic_grade_label.setText("C")
                    self.pri_report.ui.civic_remark_label.setText("Good")
                elif row[26] >= 60 and row[26] < 70:
                    self.pri_report.ui.civic_grade_label.setText("B")
                    self.pri_report.ui.civic_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.civic_grade_label.setText("A")
                    self.pri_report.ui.civic_remark_label.setText("Excellent")
                self.pri_report.ui.computer_c1_label.setText(str(row[27]))
                self.pri_report.ui.computer_c2_label.setText(str(row[28]))
                self.pri_report.ui.computer_ass_label.setText(str(row[29]))
                self.pri_report.ui.computer_att_label.setText(str(row[30]))
                self.pri_report.ui.computer_exam_label.setText(str(row[31]))
                self.pri_report.ui.computer_total_label.setText(str(row[32]))
                if row[32] < 40:
                    self.pri_report.ui.computer_grade_label.setText("F")
                    self.pri_report.ui.computer_remark_label.setText("Fail")
                elif row[32] >= 40 and row[32] < 46:
                    self.pri_report.ui.computer_grade_label.setText("E")
                    self.pri_report.ui.computer_remark_label.setText("Pass")
                elif row[32] >= 46 and row[32] < 50:
                    self.pri_report.ui.computer_grade_label.setText("D")
                    self.pri_report.ui.computer_remark_label.setText("Pass")
                elif row[32] >= 50 and row[32] < 60:
                    self.pri_report.ui.computer_grade_label.setText("C")
                    self.pri_report.ui.computer_remark_label.setText("Good")
                elif row[32] >= 60 and row[32] < 70:
                    self.pri_report.ui.computer_grade_label.setText("B")
                    self.pri_report.ui.computer_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.computer_grade_label.setText("A")
                    self.pri_report.ui.computer_remark_label.setText("Excellent")
                self.pri_report.ui.basic_c1_label.setText(str(row[33]))
                self.pri_report.ui.basic_c2_label.setText(str(row[34]))
                self.pri_report.ui.basic_ass_label.setText(str(row[35]))
                self.pri_report.ui.basic_att_label.setText(str(row[36]))
                self.pri_report.ui.basic_exam_label.setText(str(row[37]))
                self.pri_report.ui.basic_total_label.setText(str(row[38]))
                if row[38] < 40:
                    self.pri_report.ui.basic_grade_label.setText("F")
                    self.pri_report.ui.basic_remark_label.setText("Fail")
                elif row[38] >= 40 and row[38] < 46:
                    self.pri_report.ui.basic_grade_label.setText("E")
                    self.pri_report.ui.basic_remark_label.setText("Pass")
                elif row[38] >= 46 and row[38] < 50:
                    self.pri_report.ui.basic_grade_label.setText("D")
                    self.pri_report.ui.basic_remark_label.setText("Pass")
                elif row[38] >= 50 and row[38] < 60:
                    self.pri_report.ui.basic_grade_label.setText("C")
                    self.pri_report.ui.basic_remark_label.setText("Good")
                elif row[38] >= 60 and row[38] < 70:
                    self.pri_report.ui.basic_grade_label.setText("B")
                    self.pri_report.ui.basic_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.basic_grade_label.setText("A")
                    self.pri_report.ui.basic_remark_label.setText("Excellent")
                self.pri_report.ui.quant_c1_label.setText(str(row[39]))
                self.pri_report.ui.quant_c2_label.setText(str(row[40]))
                self.pri_report.ui.quant_ass_label.setText(str(row[41]))
                self.pri_report.ui.quant_att_label.setText(str(row[42]))
                self.pri_report.ui.quant_exam_label.setText(str(row[43]))
                self.pri_report.ui.quant_total_label.setText(str(row[44]))
                if row[44] < 40:
                    self.pri_report.ui.quant_grade_label.setText("F")
                    self.pri_report.ui.quant_remark_label.setText("Fail")
                elif row[44] >= 40 and row[44] < 46:
                    self.pri_report.ui.quant_grade_label.setText("E")
                    self.pri_report.ui.quant_remark_label.setText("Pass")
                elif row[44] >= 46 and row[44] < 50:
                    self.pri_report.ui.quant_grade_label.setText("D")
                    self.pri_report.ui.quant_remark_label.setText("Pass")
                elif row[44] >= 50 and row[44] < 60:
                    self.pri_report.ui.quant_grade_label.setText("C")
                    self.pri_report.ui.quant_remark_label.setText("Good")
                elif row[44] >= 60 and row[44] < 70:
                    self.pri_report.ui.quant_grade_label.setText("B")
                    self.pri_report.ui.quant_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.quant_grade_label.setText("A")
                    self.pri_report.ui.quant_remark_label.setText("Excellent")
                self.pri_report.ui.verbal_c1_label.setText(str(row[45]))
                self.pri_report.ui.verbal_c2_label.setText(str(row[46]))
                self.pri_report.ui.verbal_ass_label.setText(str(row[47]))
                self.pri_report.ui.verbal_att_label.setText(str(row[48]))
                self.pri_report.ui.verbal_exam_label.setText(str(row[49]))
                self.pri_report.ui.verbal_total_label.setText(str(row[50]))
                if row[50] < 40:
                    self.pri_report.ui.verbal_grade_label.setText("F")
                    self.pri_report.ui.verbal_remark_label.setText("Fail")
                elif row[50] >= 40 and row[50] < 46:
                    self.pri_report.ui.verbal_grade_label.setText("E")
                    self.pri_report.ui.verbal_remark_label.setText("Pass")
                elif row[50] >= 46 and row[50] < 50:
                    self.pri_report.ui.verbal_grade_label.setText("D")
                    self.pri_report.ui.verbal_remark_label.setText("Pass")
                elif row[50] >= 50 and row[50] < 60:
                    self.pri_report.ui.verbal_grade_label.setText("C")
                    self.pri_report.ui.verbal_remark_label.setText("Good")
                elif row[50] >= 60 and row[50] < 70:
                    self.pri_report.ui.verbal_grade_label.setText("B")
                    self.pri_report.ui.verbal_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.verbal_grade_label.setText("A")
                    self.pri_report.ui.verbal_remark_label.setText("Excellent")
                self.pri_report.ui.arabic_c1_label.setText(str(row[51]))
                self.pri_report.ui.arabic_c2_label.setText(str(row[52]))
                self.pri_report.ui.arabic_ass_label.setText(str(row[53]))
                self.pri_report.ui.arabic_att_label.setText(str(row[54]))
                self.pri_report.ui.arabic_exam_label.setText(str(row[55]))
                self.pri_report.ui.arabic_total_label.setText(str(row[56]))
                if row[56] < 40:
                    self.pri_report.ui.arabic_grade_label.setText("F")
                    self.pri_report.ui.arabic_remark_label.setText("Fail")
                elif row[56] >= 40 and row[56] < 46:
                    self.pri_report.ui.arabic_grade_label.setText("E")
                    self.pri_report.ui.arabic_remark_label.setText("Pass")
                elif row[56] >= 46 and row[56] < 50:
                    self.pri_report.ui.arabic_grade_label.setText("D")
                    self.pri_report.ui.arabic_remark_label.setText("Pass")
                elif row[56] >= 50 and row[56] < 60:
                    self.pri_report.ui.arabic_grade_label.setText("C")
                    self.pri_report.ui.arabic_remark_label.setText("Good")
                elif row[56] >= 60 and row[50] < 70:
                    self.pri_report.ui.arabic_grade_label.setText("B")
                    self.pri_report.ui.arabic_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.arabic_grade_label.setText("A")
                    self.pri_report.ui.arabic_remark_label.setText("Excellent")
                self.pri_report.ui.qur_c1_label.setText(str(row[57]))
                self.pri_report.ui.qur_c2_label.setText(str(row[58]))
                self.pri_report.ui.qur_ass_label.setText(str(row[59]))
                self.pri_report.ui.qur_att_label.setText(str(row[60]))
                self.pri_report.ui.qur_exam_label.setText(str(row[61]))
                self.pri_report.ui.qur_total_label.setText(str(row[62]))
                if row[62] < 40:
                    self.pri_report.ui.qur_grade_label.setText("F")
                    self.pri_report.ui.qur_remark_label.setText("Fail")
                elif row[62] >= 40 and row[62] < 46:
                    self.pri_report.ui.qur_grade_label.setText("E")
                    self.pri_report.ui.qur_remark_label.setText("Pass")
                elif row[62] >= 46 and row[62] < 50:
                    self.pri_report.ui.qur_grade_label.setText("D")
                    self.pri_report.ui.qur_remark_label.setText("Pass")
                elif row[62] >= 50 and row[62] < 60:
                    self.pri_report.ui.qur_grade_label.setText("C")
                    self.pri_report.ui.qur_remark_label.setText("Good")
                elif row[62] >= 60 and row[62] < 70:
                    self.pri_report.ui.qur_grade_label.setText("B")
                    self.pri_report.ui.qur_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.qur_grade_label.setText("A")
                    self.pri_report.ui.qur_remark_label.setText("Excellent")
                self.pri_report.ui.agric_c1_label.setText(str(row[63]))
                self.pri_report.ui.agric_c2_label.setText(str(row[64]))
                self.pri_report.ui.agric_ass_label.setText(str(row[65]))
                self.pri_report.ui.agric_att_label.setText(str(row[66]))
                self.pri_report.ui.agric_exam_label.setText(str(row[67]))
                self.pri_report.ui.agric_total_label.setText(str(row[68]))
                if row[68] < 40:
                    self.pri_report.ui.agric_grade_label.setText("F")
                    self.pri_report.ui.agric_remark_label.setText("Fail")
                elif row[68] >= 40 and row[68] < 46:
                    self.pri_report.ui.agric_grade_label.setText("E")
                    self.pri_report.ui.agric_remark_label.setText("Pass")
                elif row[68] >= 46 and row[68] < 50:
                    self.pri_report.ui.agric_grade_label.setText("D")
                    self.pri_report.ui.agric_remark_label.setText("Pass")
                elif row[68] >= 50 and row[68] < 60:
                    self.pri_report.ui.agric_grade_label.setText("C")
                    self.pri_report.ui.agric_remark_label.setText("Good")
                elif row[68] >= 60 and row[68] < 70:
                    self.pri_report.ui.agric_grade_label.setText("B")
                    self.pri_report.ui.agric_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.agric_grade_label.setText("A")
                    self.pri_report.ui.agric_remark_label.setText("Excellent")

                self.pri_report.ui.phe_c1_label.setText(str(row[69]))
                self.pri_report.ui.phe_c2_label.setText(str(row[70]))
                self.pri_report.ui.phe_ass_label.setText(str(row[71]))
                self.pri_report.ui.phe_att_label.setText(str(row[72]))
                self.pri_report.ui.phe_exam_label.setText(str(row[73]))
                self.pri_report.ui.phe_total_label.setText(str(row[74]))
                if row[74] < 40:
                    self.pri_report.ui.phe_grade_label.setText("F")
                    self.pri_report.ui.phe_remark_label.setText("Fail")
                elif row[74] >= 40 and row[74] < 46:
                    self.pri_report.ui.phe_grade_label.setText("E")
                    self.pri_report.ui.phe_remark_label.setText("Pass")
                elif row[74] >= 46 and row[74] < 50:
                    self.pri_report.ui.phe_grade_label.setText("D")
                    self.pri_report.ui.phe_remark_label.setText("Pass")
                elif row[74] >= 50 and row[74] < 60:
                    self.pri_report.ui.phe_grade_label.setText("C")
                    self.pri_report.ui.phe_remark_label.setText("Good")
                elif row[74] >= 60 and row[74] < 70:
                    self.pri_report.ui.phe_grade_label.setText("B")
                    self.pri_report.ui.phe_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.phe_grade_label.setText("A")
                    self.pri_report.ui.phe_remark_label.setText("Excellent")

                self.pri_report.ui.creative_c1_label.setText(str(row[75]))
                self.pri_report.ui.creative_c2_label.setText(str(row[76]))
                self.pri_report.ui.creative_ass_label.setText(str(row[77]))
                self.pri_report.ui.creative_att_label.setText(str(row[78]))
                self.pri_report.ui.creative_exam_label.setText(str(row[79]))
                self.pri_report.ui.creative_total_label.setText(str(row[80]))
                if row[80] < 40:
                    self.pri_report.ui.creative_grade_label.setText("F")
                    self.pri_report.ui.creative_remark_label.setText("Fail")
                elif row[80] >= 40 and row[80] < 46:
                    self.pri_report.ui.creative_grade_label.setText("E")
                    self.pri_report.ui.creative_remark_label.setText("Pass")
                elif row[80] >= 46 and row[80] < 50:
                    self.pri_report.ui.creative_grade_label.setText("D")
                    self.pri_report.ui.creative_remark_label.setText("Pass")
                elif row[80] >= 50 and row[80] < 60:
                    self.pri_report.ui.creative_grade_label.setText("C")
                    self.pri_report.ui.creative_remark_label.setText("Good")
                elif row[80] >= 60 and row[80] < 70:
                    self.pri_report.ui.creative_grade_label.setText("B")
                    self.pri_report.ui.creative_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.creative_grade_label.setText("A")
                    self.pri_report.ui.creative_remark_label.setText("Excellent")

                self.pri_report.ui.handwriting_c1_label.setText(str(row[81]))
                self.pri_report.ui.handwriting_c2_label.setText(str(row[82]))
                self.pri_report.ui.handwriting_ass_label.setText(str(row[83]))
                self.pri_report.ui.handwriting_att_label.setText(str(row[84]))
                self.pri_report.ui.handwriting_exam_label.setText(str(row[85]))
                self.pri_report.ui.handwriting_total_label.setText(str(row[86]))
                if row[86] < 40:
                    self.pri_report.ui.handwriting_grade_label.setText("F")
                    self.pri_report.ui.handwriting_remark_label.setText("Fail")
                elif row[86] >= 40 and row[86] < 46:
                    self.pri_report.ui.handwriting_grade_label.setText("E")
                    self.pri_report.ui.handwriting_remark_label.setText("Pass")
                elif row[86] >= 46 and row[86] < 50:
                    self.pri_report.ui.handwriting_grade_label.setText("D")
                    self.pri_report.ui.handwriting_remark_label.setText("Pass")
                elif row[86] >= 50 and row[86] < 60:
                    self.pri_report.ui.handwriting_grade_label.setText("C")
                    self.pri_report.ui.handwriting_remark_label.setText("Good")
                elif row[86] >= 60 and row[86] < 70:
                    self.pri_report.ui.handwriting_grade_label.setText("B")
                    self.pri_report.ui.handwriting_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.handwriting_grade_label.setText("A")
                    self.pri_report.ui.handwriting_remark_label.setText("Excellent")

                self.pri_report.ui.total_scores_label.setText(str(row[87]))
                self.pri_report.ui.avg_label.setText(str(row[88]))
                if row[88] < 40:
                    self.pri_report.ui.master_com_label.setText("Good attempt but try harder next time.")
                    self.pri_report.ui.head_com_label.setText("Good result, try harder next time.")
                elif row[88] >= 40 and row[88] < 50:
                    self.pri_report.ui.master_com_label.setText("Good performance, try harder next time.")
                    self.pri_report.ui.head_com_label.setText("Nice try, keep trying.")
                elif row[88] >= 50 and row[88] < 60:
                    self.pri_report.ui.master_com_label.setText("Good result, keep trying.")
                    self.pri_report.ui.head_com_label.setText("Good performance, keep trying.")
                elif row[88] >= 60 and row[88] < 70:
                    self.pri_report.ui.master_com_label.setText("This is a good result, keep it up.")
                    self.pri_report.ui.head_com_label.setText("Good performance, keep it up.")
                else:
                    self.pri_report.ui.master_com_label.setText("This is an excellent result. Keep it on.")
                    self.pri_report.ui.head_com_label.setText("An Excellent result, keep it on.")

                positions = []
                cmd10 = "SELECT * FROM t_pri_scores_first WHERE score_class = ? ORDER BY avg DESC"
                cur.execute(cmd10, (classes_combo,))
                rows = cur.fetchall()
                for row in rows:
                    positions.append(row[1])
                self.pri_report.ui.out_of_label.setText(str(len(positions)))
                for i in range(len(positions)):
                    if admission_no == positions[i]:
                        if i in range (10, len(positions), 100):
                            self.pri_report.ui.position_label.setText(str(i+1)+"th")
                        elif i in range (11, len(positions), 100):
                            self.pri_report.ui.position_label.setText(str(i+1)+"th")
                        elif i in range (12, len(positions), 100):
                            self.pri_report.ui.position_label.setText(str(i+1)+"th")
                        elif i in range (0, len(positions), 10):
                            self.pri_report.ui.position_label.setText(str(i+1)+"st")
                        elif i in range (1, len(positions), 10):
                            self.pri_report.ui.position_label.setText(str(i+1)+"nd")
                        elif i in range (2, len(positions), 10):
                            self.pri_report.ui.position_label.setText(str(i+1)+"rd")
                        else:
                            self.pri_report.ui.position_label.setText(str(i+1)+"th")


                cmd4 = "SELECT * FROM t_classes WHERE class_name = ?"
                cur.execute(cmd4, (classes_combo,))
                row = cur.fetchone()
                if row[2] == None:
                    self.pri_report.ui.master_name_label.setText(str(row[1]))
                else:
                    self.pri_report.ui.master_name_label.setText(str(row[1]))
                    pixmap = QPixmap()
                    pixmap.loadFromData(QByteArray.fromBase64(row[2]))
                    self.pri_report.ui.master_sig_label.setPixmap(QPixmap(pixmap))

                cmd5 = "SELECT * FROM t_senior_users WHERE role = 'headmaster'"
                cur.execute(cmd5)
                row = cur.fetchone()
                self.pri_report.ui.head_name_label.setText(row[1])
                pixmap = QPixmap()
                pixmap.loadFromData(QByteArray.fromBase64(row[5]))
                self.pri_report.ui.head_sig_label.setPixmap(QPixmap(pixmap))
                cmd6 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd6)
                row = cur.fetchone()
                self.pri_report.ui.next_term_label.setText(row[3])
                cmd7 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd7)
                row = cur.fetchone()
                self.pri_report.ui.fees_label.setText(row[6])
                cmd8 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd8)
                row = cur.fetchone()
                self.pri_report.ui.session_label.setText(row[2])
                if self.ui.punctuality_a_radio.isChecked() == False and self.ui.punctuality_b_radio.isChecked() == False and self.ui.punctuality_c_radio.isChecked() == False and self.ui.punctuality_d_radio.isChecked() == False and self.ui.punctuality_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grade in punctuality", QMessageBox.Ok)
                elif self.ui.neatness_a_radio.isChecked() == False and self.ui.neatness_b_radio.isChecked() == False and self.ui.neatness_c_radio.isChecked() == False and self.ui.neatness_d_radio.isChecked() == False and self.ui.neatness_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in neatness", QMessageBox.Ok)
                elif self.ui.games_a_radio.isChecked() == False and self.ui.games_b_radio.isChecked() == False and self.ui.games_c_radio.isChecked() == False and self.ui.games_d_radio.isChecked() == False and self.ui.games_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in games", QMessageBox.Ok)
                elif self.ui.attentiveness_a_radio.isChecked() == False and self.ui.attentiveness_b_radio.isChecked() == False and self.ui.attentiveness_c_radio.isChecked() == False and self.ui.attentiveness_d_radio.isChecked() == False and self.ui.attentiveness_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in attentiveness in class", QMessageBox.Ok)
                elif self.ui.relationship_a_radio.isChecked() == False and self.ui.relationship_b_radio.isChecked() == False and self.ui.relationship_c_radio.isChecked() == False and self.ui.relationship_d_radio.isChecked() == False and self.ui.relationship_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in relationship with others", QMessageBox.Ok)
                elif self.ui.honesty_a_radio.isChecked() == False and self.ui.honesty_b_radio.isChecked() == False and self.ui.honesty_c_radio.isChecked() == False and self.ui.honesty_d_radio.isChecked() == False and self.ui.honesty_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in honesty", QMessageBox.Ok)
                else:
                    self.printReport()
            except Error:
                QMessageBox.critical(self, "Generating Report", "ERROR: Please ensure all pupil's scores have been recorded in all subjects", QMessageBox.Ok)
            except TypeError:
                QMessageBox.critical(self, "Generating Report", "ERROR: Please ensure all pupil's scores have been recorded in all subjects", QMessageBox.Ok)

    def generatePriReportPDF(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox.currentText()
        admission_no = self.ui.stud_adm_no_comboBox.currentText()
        cmd1 = "SELECT * FROM t_studs WHERE admission_no = ?"
        cur.execute(cmd1, (admission_no,))
        row = cur.fetchone()
        if row == None:
            QMessageBox.critical(self, "Printing Report", "ERROR: Please select a class and pupil's admission number before generating report", QMessageBox.Ok)
        else:
            self.pri_report.ui.name_label.setText(row[1])
            self.pri_report.ui.class_label.setText(row[3])
            self.pri_report.ui.sex_label.setText(row[5])
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray.fromBase64(row[6]))
            self.pri_report.ui.photo_label.setPixmap(QPixmap(pixmap))
            try:
                cmd3 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
                cur.execute(cmd3, (admission_no,))
                row = cur.fetchone()
                self.pri_report.ui.english_c1_label.setText(str(row[3]))
                self.pri_report.ui.english_c2_label.setText(str(row[4]))
                self.pri_report.ui.english_ass_label.setText(str(row[5]))
                self.pri_report.ui.english_att_label.setText(str(row[6]))
                self.pri_report.ui.english_exam_label.setText(str(row[7]))
                self.pri_report.ui.english_total_label.setText(str(row[8]))
                if row[8] < 40:
                    self.pri_report.ui.english_grade_label.setText("F")
                    self.pri_report.ui.english_remark_label.setText("Fail")
                elif row[8] >= 40 and row[8] < 46:
                    self.pri_report.ui.english_grade_label.setText("E")
                    self.pri_report.ui.english_remark_label.setText("Pass")
                elif row[8] >= 46 and row[8] < 50:
                    self.pri_report.ui.english_grade_label.setText("D")
                    self.pri_report.ui.english_remark_label.setText("Pass")
                elif row[8] >= 50 and row[8] < 60:
                    self.pri_report.ui.english_grade_label.setText("C")
                    self.pri_report.ui.english_remark_label.setText("Good")
                elif row[8] >= 60 and row[8] < 70:
                    self.pri_report.ui.english_grade_label.setText("B")
                    self.pri_report.ui.english_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.english_grade_label.setText("A")
                    self.pri_report.ui.english_remark_label.setText("Excellent")
                self.pri_report.ui.math_c1_label.setText(str(row[9]))
                self.pri_report.ui.math_c2_label.setText(str(row[10]))
                self.pri_report.ui.math_ass_label.setText(str(row[11]))
                self.pri_report.ui.math_att_label.setText(str(row[12]))
                self.pri_report.ui.math_exam_label.setText(str(row[13]))
                self.pri_report.ui.math_total_label.setText(str(row[14]))
                if row[14] < 40:
                    self.pri_report.ui.math_grade_label.setText("F")
                    self.pri_report.ui.math_remark_label.setText("Fail")
                elif row[14] >= 40 and row[14] < 46:
                    self.pri_report.ui.math_grade_label.setText("E")
                    self.pri_report.ui.math_remark_label.setText("Pass")
                elif row[14] >= 46 and row[14] < 50:
                    self.pri_report.ui.math_grade_label.setText("D")
                    self.pri_report.ui.math_remark_label.setText("Pass")
                elif row[14] >= 50 and row[14] < 60:
                    self.pri_report.ui.math_grade_label.setText("C")
                    self.pri_report.ui.math_remark_label.setText("Good")
                elif row[14] >= 60 and row[14] < 70:
                    self.pri_report.ui.math_grade_label.setText("B")
                    self.pri_report.ui.math_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.math_grade_label.setText("A")
                    self.pri_report.ui.math_remark_label.setText("Excellent")
                self.pri_report.ui.irs_c1_label.setText(str(row[15]))
                self.pri_report.ui.irs_c2_label.setText(str(row[16]))
                self.pri_report.ui.irs_ass_label.setText(str(row[17]))
                self.pri_report.ui.irs_att_label.setText(str(row[18]))
                self.pri_report.ui.irs_exam_label.setText(str(row[19]))
                self.pri_report.ui.irs_total_label.setText(str(row[20]))
                if row[20] < 40:
                    self.pri_report.ui.irs_grade_label.setText("F")
                    self.pri_report.ui.irs_remark_label.setText("Fail")
                elif row[20] >= 40 and row[20] < 46:
                    self.pri_report.ui.irs_grade_label.setText("E")
                    self.pri_report.ui.irs_remark_label.setText("Pass")
                elif row[20] >= 46 and row[20] < 50:
                    self.pri_report.ui.irs_grade_label.setText("D")
                    self.pri_report.ui.irs_remark_label.setText("Pass")
                elif row[20] >= 50 and row[20] < 60:
                    self.pri_report.ui.irs_grade_label.setText("C")
                    self.pri_report.ui.irs_remark_label.setText("Good")
                elif row[20] >= 60 and row[20] < 70:
                    self.pri_report.ui.irs_grade_label.setText("B")
                    self.pri_report.ui.irs_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.irs_grade_label.setText("A")
                    self.pri_report.ui.irs_remark_label.setText("Excellent")
                self.pri_report.ui.civic_c1_label.setText(str(row[21]))
                self.pri_report.ui.civic_c2_label.setText(str(row[22]))
                self.pri_report.ui.civic_ass_label.setText(str(row[23]))
                self.pri_report.ui.civic_att_label.setText(str(row[24]))
                self.pri_report.ui.civic_exam_label.setText(str(row[25]))
                self.pri_report.ui.civic_total_label.setText(str(row[26]))
                if row[26] < 40:
                    self.pri_report.ui.civic_grade_label.setText("F")
                    self.pri_report.ui.civic_remark_label.setText("Fail")
                elif row[26] >= 40 and row[26] < 46:
                    self.pri_report.ui.civic_grade_label.setText("E")
                    self.pri_report.ui.civic_remark_label.setText("Pass")
                elif row[26] >= 46 and row[26] < 50:
                    self.pri_report.ui.civic_grade_label.setText("D")
                    self.pri_report.ui.civic_remark_label.setText("Pass")
                elif row[26] >= 50 and row[26] < 60:
                    self.pri_report.ui.civic_grade_label.setText("C")
                    self.pri_report.ui.civic_remark_label.setText("Good")
                elif row[26] >= 60 and row[26] < 70:
                    self.pri_report.ui.civic_grade_label.setText("B")
                    self.pri_report.ui.civic_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.civic_grade_label.setText("A")
                    self.pri_report.ui.civic_remark_label.setText("Excellent")
                self.pri_report.ui.computer_c1_label.setText(str(row[27]))
                self.pri_report.ui.computer_c2_label.setText(str(row[28]))
                self.pri_report.ui.computer_ass_label.setText(str(row[29]))
                self.pri_report.ui.computer_att_label.setText(str(row[30]))
                self.pri_report.ui.computer_exam_label.setText(str(row[31]))
                self.pri_report.ui.computer_total_label.setText(str(row[32]))
                if row[32] < 40:
                    self.pri_report.ui.computer_grade_label.setText("F")
                    self.pri_report.ui.computer_remark_label.setText("Fail")
                elif row[32] >= 40 and row[32] < 46:
                    self.pri_report.ui.computer_grade_label.setText("E")
                    self.pri_report.ui.computer_remark_label.setText("Pass")
                elif row[32] >= 46 and row[32] < 50:
                    self.pri_report.ui.computer_grade_label.setText("D")
                    self.pri_report.ui.computer_remark_label.setText("Pass")
                elif row[32] >= 50 and row[32] < 60:
                    self.pri_report.ui.computer_grade_label.setText("C")
                    self.pri_report.ui.computer_remark_label.setText("Good")
                elif row[32] >= 60 and row[32] < 70:
                    self.pri_report.ui.computer_grade_label.setText("B")
                    self.pri_report.ui.computer_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.computer_grade_label.setText("A")
                    self.pri_report.ui.computer_remark_label.setText("Excellent")
                self.pri_report.ui.basic_c1_label.setText(str(row[33]))
                self.pri_report.ui.basic_c2_label.setText(str(row[34]))
                self.pri_report.ui.basic_ass_label.setText(str(row[35]))
                self.pri_report.ui.basic_att_label.setText(str(row[36]))
                self.pri_report.ui.basic_exam_label.setText(str(row[37]))
                self.pri_report.ui.basic_total_label.setText(str(row[38]))
                if row[38] < 40:
                    self.pri_report.ui.basic_grade_label.setText("F")
                    self.pri_report.ui.basic_remark_label.setText("Fail")
                elif row[38] >= 40 and row[38] < 46:
                    self.pri_report.ui.basic_grade_label.setText("E")
                    self.pri_report.ui.basic_remark_label.setText("Pass")
                elif row[38] >= 46 and row[38] < 50:
                    self.pri_report.ui.basic_grade_label.setText("D")
                    self.pri_report.ui.basic_remark_label.setText("Pass")
                elif row[38] >= 50 and row[38] < 60:
                    self.pri_report.ui.basic_grade_label.setText("C")
                    self.pri_report.ui.basic_remark_label.setText("Good")
                elif row[38] >= 60 and row[38] < 70:
                    self.pri_report.ui.basic_grade_label.setText("B")
                    self.pri_report.ui.basic_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.basic_grade_label.setText("A")
                    self.pri_report.ui.basic_remark_label.setText("Excellent")
                self.pri_report.ui.quant_c1_label.setText(str(row[39]))
                self.pri_report.ui.quant_c2_label.setText(str(row[40]))
                self.pri_report.ui.quant_ass_label.setText(str(row[41]))
                self.pri_report.ui.quant_att_label.setText(str(row[42]))
                self.pri_report.ui.quant_exam_label.setText(str(row[43]))
                self.pri_report.ui.quant_total_label.setText(str(row[44]))
                if row[44] < 40:
                    self.pri_report.ui.quant_grade_label.setText("F")
                    self.pri_report.ui.quant_remark_label.setText("Fail")
                elif row[44] >= 40 and row[44] < 46:
                    self.pri_report.ui.quant_grade_label.setText("E")
                    self.pri_report.ui.quant_remark_label.setText("Pass")
                elif row[44] >= 46 and row[44] < 50:
                    self.pri_report.ui.quant_grade_label.setText("D")
                    self.pri_report.ui.quant_remark_label.setText("Pass")
                elif row[44] >= 50 and row[44] < 60:
                    self.pri_report.ui.quant_grade_label.setText("C")
                    self.pri_report.ui.quant_remark_label.setText("Good")
                elif row[44] >= 60 and row[44] < 70:
                    self.pri_report.ui.quant_grade_label.setText("B")
                    self.pri_report.ui.quant_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.quant_grade_label.setText("A")
                    self.pri_report.ui.quant_remark_label.setText("Excellent")
                self.pri_report.ui.verbal_c1_label.setText(str(row[45]))
                self.pri_report.ui.verbal_c2_label.setText(str(row[46]))
                self.pri_report.ui.verbal_ass_label.setText(str(row[47]))
                self.pri_report.ui.verbal_att_label.setText(str(row[48]))
                self.pri_report.ui.verbal_exam_label.setText(str(row[49]))
                self.pri_report.ui.verbal_total_label.setText(str(row[50]))
                if row[50] < 40:
                    self.pri_report.ui.verbal_grade_label.setText("F")
                    self.pri_report.ui.verbal_remark_label.setText("Fail")
                elif row[50] >= 40 and row[50] < 46:
                    self.pri_report.ui.verbal_grade_label.setText("E")
                    self.pri_report.ui.verbal_remark_label.setText("Pass")
                elif row[50] >= 46 and row[50] < 50:
                    self.pri_report.ui.verbal_grade_label.setText("D")
                    self.pri_report.ui.verbal_remark_label.setText("Pass")
                elif row[50] >= 50 and row[50] < 60:
                    self.pri_report.ui.verbal_grade_label.setText("C")
                    self.pri_report.ui.verbal_remark_label.setText("Good")
                elif row[50] >= 60 and row[50] < 70:
                    self.pri_report.ui.verbal_grade_label.setText("B")
                    self.pri_report.ui.verbal_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.verbal_grade_label.setText("A")
                    self.pri_report.ui.verbal_remark_label.setText("Excellent")
                self.pri_report.ui.arabic_c1_label.setText(str(row[51]))
                self.pri_report.ui.arabic_c2_label.setText(str(row[52]))
                self.pri_report.ui.arabic_ass_label.setText(str(row[53]))
                self.pri_report.ui.arabic_att_label.setText(str(row[54]))
                self.pri_report.ui.arabic_exam_label.setText(str(row[55]))
                self.pri_report.ui.arabic_total_label.setText(str(row[56]))
                if row[56] < 40:
                    self.pri_report.ui.arabic_grade_label.setText("F")
                    self.pri_report.ui.arabic_remark_label.setText("Fail")
                elif row[56] >= 40 and row[56] < 46:
                    self.pri_report.ui.arabic_grade_label.setText("E")
                    self.pri_report.ui.arabic_remark_label.setText("Pass")
                elif row[56] >= 46 and row[56] < 50:
                    self.pri_report.ui.arabic_grade_label.setText("D")
                    self.pri_report.ui.arabic_remark_label.setText("Pass")
                elif row[56] >= 50 and row[56] < 60:
                    self.pri_report.ui.arabic_grade_label.setText("C")
                    self.pri_report.ui.arabic_remark_label.setText("Good")
                elif row[56] >= 60 and row[50] < 70:
                    self.pri_report.ui.arabic_grade_label.setText("B")
                    self.pri_report.ui.arabic_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.arabic_grade_label.setText("A")
                    self.pri_report.ui.arabic_remark_label.setText("Excellent")
                self.pri_report.ui.qur_c1_label.setText(str(row[57]))
                self.pri_report.ui.qur_c2_label.setText(str(row[58]))
                self.pri_report.ui.qur_ass_label.setText(str(row[59]))
                self.pri_report.ui.qur_att_label.setText(str(row[60]))
                self.pri_report.ui.qur_exam_label.setText(str(row[61]))
                self.pri_report.ui.qur_total_label.setText(str(row[62]))
                if row[62] < 40:
                    self.pri_report.ui.qur_grade_label.setText("F")
                    self.pri_report.ui.qur_remark_label.setText("Fail")
                elif row[62] >= 40 and row[62] < 46:
                    self.pri_report.ui.qur_grade_label.setText("E")
                    self.pri_report.ui.qur_remark_label.setText("Pass")
                elif row[62] >= 46 and row[62] < 50:
                    self.pri_report.ui.qur_grade_label.setText("D")
                    self.pri_report.ui.qur_remark_label.setText("Pass")
                elif row[62] >= 50 and row[62] < 60:
                    self.pri_report.ui.qur_grade_label.setText("C")
                    self.pri_report.ui.qur_remark_label.setText("Good")
                elif row[62] >= 60 and row[62] < 70:
                    self.pri_report.ui.qur_grade_label.setText("B")
                    self.pri_report.ui.qur_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.qur_grade_label.setText("A")
                    self.pri_report.ui.qur_remark_label.setText("Excellent")
                self.pri_report.ui.agric_c1_label.setText(str(row[63]))
                self.pri_report.ui.agric_c2_label.setText(str(row[64]))
                self.pri_report.ui.agric_ass_label.setText(str(row[65]))
                self.pri_report.ui.agric_att_label.setText(str(row[66]))
                self.pri_report.ui.agric_exam_label.setText(str(row[67]))
                self.pri_report.ui.agric_total_label.setText(str(row[68]))
                if row[68] < 40:
                    self.pri_report.ui.agric_grade_label.setText("F")
                    self.pri_report.ui.agric_remark_label.setText("Fail")
                elif row[68] >= 40 and row[68] < 46:
                    self.pri_report.ui.agric_grade_label.setText("E")
                    self.pri_report.ui.agric_remark_label.setText("Pass")
                elif row[68] >= 46 and row[68] < 50:
                    self.pri_report.ui.agric_grade_label.setText("D")
                    self.pri_report.ui.agric_remark_label.setText("Pass")
                elif row[68] >= 50 and row[68] < 60:
                    self.pri_report.ui.agric_grade_label.setText("C")
                    self.pri_report.ui.agric_remark_label.setText("Good")
                elif row[68] >= 60 and row[68] < 70:
                    self.pri_report.ui.agric_grade_label.setText("B")
                    self.pri_report.ui.agric_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.agric_grade_label.setText("A")
                    self.pri_report.ui.agric_remark_label.setText("Excellent")

                self.pri_report.ui.phe_c1_label.setText(str(row[69]))
                self.pri_report.ui.phe_c2_label.setText(str(row[70]))
                self.pri_report.ui.phe_ass_label.setText(str(row[71]))
                self.pri_report.ui.phe_att_label.setText(str(row[72]))
                self.pri_report.ui.phe_exam_label.setText(str(row[73]))
                self.pri_report.ui.phe_total_label.setText(str(row[74]))
                if row[74] < 40:
                    self.pri_report.ui.phe_grade_label.setText("F")
                    self.pri_report.ui.phe_remark_label.setText("Fail")
                elif row[74] >= 40 and row[74] < 46:
                    self.pri_report.ui.phe_grade_label.setText("E")
                    self.pri_report.ui.phe_remark_label.setText("Pass")
                elif row[74] >= 46 and row[74] < 50:
                    self.pri_report.ui.phe_grade_label.setText("D")
                    self.pri_report.ui.phe_remark_label.setText("Pass")
                elif row[74] >= 50 and row[74] < 60:
                    self.pri_report.ui.phe_grade_label.setText("C")
                    self.pri_report.ui.phe_remark_label.setText("Good")
                elif row[74] >= 60 and row[74] < 70:
                    self.pri_report.ui.phe_grade_label.setText("B")
                    self.pri_report.ui.phe_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.phe_grade_label.setText("A")
                    self.pri_report.ui.phe_remark_label.setText("Excellent")

                self.pri_report.ui.creative_c1_label.setText(str(row[75]))
                self.pri_report.ui.creative_c2_label.setText(str(row[76]))
                self.pri_report.ui.creative_ass_label.setText(str(row[77]))
                self.pri_report.ui.creative_att_label.setText(str(row[78]))
                self.pri_report.ui.creative_exam_label.setText(str(row[79]))
                self.pri_report.ui.creative_total_label.setText(str(row[80]))
                if row[80] < 40:
                    self.pri_report.ui.creative_grade_label.setText("F")
                    self.pri_report.ui.creative_remark_label.setText("Fail")
                elif row[80] >= 40 and row[80] < 46:
                    self.pri_report.ui.creative_grade_label.setText("E")
                    self.pri_report.ui.creative_remark_label.setText("Pass")
                elif row[80] >= 46 and row[80] < 50:
                    self.pri_report.ui.creative_grade_label.setText("D")
                    self.pri_report.ui.creative_remark_label.setText("Pass")
                elif row[80] >= 50 and row[80] < 60:
                    self.pri_report.ui.creative_grade_label.setText("C")
                    self.pri_report.ui.creative_remark_label.setText("Good")
                elif row[80] >= 60 and row[80] < 70:
                    self.pri_report.ui.creative_grade_label.setText("B")
                    self.pri_report.ui.creative_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.creative_grade_label.setText("A")
                    self.pri_report.ui.creative_remark_label.setText("Excellent")

                self.pri_report.ui.handwriting_c1_label.setText(str(row[81]))
                self.pri_report.ui.handwriting_c2_label.setText(str(row[82]))
                self.pri_report.ui.handwriting_ass_label.setText(str(row[83]))
                self.pri_report.ui.handwriting_att_label.setText(str(row[84]))
                self.pri_report.ui.handwriting_exam_label.setText(str(row[85]))
                self.pri_report.ui.handwriting_total_label.setText(str(row[86]))
                if row[86] < 40:
                    self.pri_report.ui.handwriting_grade_label.setText("F")
                    self.pri_report.ui.handwriting_remark_label.setText("Fail")
                elif row[86] >= 40 and row[86] < 46:
                    self.pri_report.ui.handwriting_grade_label.setText("E")
                    self.pri_report.ui.handwriting_remark_label.setText("Pass")
                elif row[86] >= 46 and row[86] < 50:
                    self.pri_report.ui.handwriting_grade_label.setText("D")
                    self.pri_report.ui.handwriting_remark_label.setText("Pass")
                elif row[86] >= 50 and row[86] < 60:
                    self.pri_report.ui.handwriting_grade_label.setText("C")
                    self.pri_report.ui.handwriting_remark_label.setText("Good")
                elif row[86] >= 60 and row[86] < 70:
                    self.pri_report.ui.handwriting_grade_label.setText("B")
                    self.pri_report.ui.handwriting_remark_label.setText("Very Good")
                else:
                    self.pri_report.ui.handwriting_grade_label.setText("A")
                    self.pri_report.ui.handwriting_remark_label.setText("Excellent")

                self.pri_report.ui.total_scores_label.setText(str(row[87]))
                self.pri_report.ui.avg_label.setText(str(row[88]))
                if row[88] < 40:
                    self.pri_report.ui.master_com_label.setText("Good attempt but try harder next time.")
                    self.pri_report.ui.head_com_label.setText("Good result, try harder next time.")
                elif row[88] >= 40 and row[88] < 50:
                    self.pri_report.ui.master_com_label.setText("Good performance, try harder next time.")
                    self.pri_report.ui.head_com_label.setText("Nice try, keep trying.")
                elif row[88] >= 50 and row[88] < 60:
                    self.pri_report.ui.master_com_label.setText("Good result, keep trying.")
                    self.pri_report.ui.head_com_label.setText("Good performance, keep trying.")
                elif row[88] >= 60 and row[88] < 70:
                    self.pri_report.ui.master_com_label.setText("This is a good result, keep it up.")
                    self.pri_report.ui.head_com_label.setText("Good performance, keep it up.")
                else:
                    self.pri_report.ui.master_com_label.setText("This is an excellent result. Keep it on.")
                    self.pri_report.ui.head_com_label.setText("An Excellent result, keep it on.")

                positions = []
                cmd10 = "SELECT * FROM t_pri_scores_first WHERE score_class = ? ORDER BY avg DESC"
                cur.execute(cmd10, (classes_combo,))
                rows = cur.fetchall()
                for row in rows:
                    positions.append(row[1])
                self.pri_report.ui.out_of_label.setText(str(len(positions)))
                for i in range(len(positions)):
                    if admission_no == positions[i]:
                        if i in range (10, len(positions), 100):
                            self.pri_report.ui.position_label.setText(str(i+1)+"th")
                        elif i in range (11, len(positions), 100):
                            self.pri_report.ui.position_label.setText(str(i+1)+"th")
                        elif i in range (12, len(positions), 100):
                            self.pri_report.ui.position_label.setText(str(i+1)+"th")
                        elif i in range (0, len(positions), 10):
                            self.pri_report.ui.position_label.setText(str(i+1)+"st")
                        elif i in range (1, len(positions), 10):
                            self.pri_report.ui.position_label.setText(str(i+1)+"nd")
                        elif i in range (2, len(positions), 10):
                            self.pri_report.ui.position_label.setText(str(i+1)+"rd")
                        else:
                            self.pri_report.ui.position_label.setText(str(i+1)+"th")

                cmd4 = "SELECT * FROM t_classes WHERE class_name = ?"
                cur.execute(cmd4, (classes_combo,))
                row = cur.fetchone()
                if row[2] == None:
                    self.pri_report.ui.master_name_label.setText(str(row[1]))
                else:
                    self.pri_report.ui.master_name_label.setText(str(row[1]))
                    pixmap = QPixmap()
                    pixmap.loadFromData(QByteArray.fromBase64(row[2]))
                    self.pri_report.ui.master_sig_label.setPixmap(QPixmap(pixmap))

                cmd5 = "SELECT * FROM t_senior_users WHERE role = 'headmaster'"
                cur.execute(cmd5)
                row = cur.fetchone()
                self.pri_report.ui.head_name_label.setText(row[1])
                pixmap = QPixmap()
                pixmap.loadFromData(QByteArray.fromBase64(row[5]))
                self.pri_report.ui.head_sig_label.setPixmap(QPixmap(pixmap))
                cmd6 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd6)
                row = cur.fetchone()
                self.pri_report.ui.next_term_label.setText(row[3])
                cmd7 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd7)
                row = cur.fetchone()
                self.pri_report.ui.fees_label.setText(row[6])
                cmd8 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd8)
                row = cur.fetchone()
                self.pri_report.ui.session_label.setText(row[2])
                if self.ui.punctuality_a_radio.isChecked() == False and self.ui.punctuality_b_radio.isChecked() == False and self.ui.punctuality_c_radio.isChecked() == False and self.ui.punctuality_d_radio.isChecked() == False and self.ui.punctuality_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grade in punctuality", QMessageBox.Ok)
                elif self.ui.neatness_a_radio.isChecked() == False and self.ui.neatness_b_radio.isChecked() == False and self.ui.neatness_c_radio.isChecked() == False and self.ui.neatness_d_radio.isChecked() == False and self.ui.neatness_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in neatness", QMessageBox.Ok)
                elif self.ui.games_a_radio.isChecked() == False and self.ui.games_b_radio.isChecked() == False and self.ui.games_c_radio.isChecked() == False and self.ui.games_d_radio.isChecked() == False and self.ui.games_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in games", QMessageBox.Ok)
                elif self.ui.attentiveness_a_radio.isChecked() == False and self.ui.attentiveness_b_radio.isChecked() == False and self.ui.attentiveness_c_radio.isChecked() == False and self.ui.attentiveness_d_radio.isChecked() == False and self.ui.attentiveness_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in attentiveness in class", QMessageBox.Ok)
                elif self.ui.relationship_a_radio.isChecked() == False and self.ui.relationship_b_radio.isChecked() == False and self.ui.relationship_c_radio.isChecked() == False and self.ui.relationship_d_radio.isChecked() == False and self.ui.relationship_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in relationship with others", QMessageBox.Ok)
                elif self.ui.honesty_a_radio.isChecked() == False and self.ui.honesty_b_radio.isChecked() == False and self.ui.honesty_c_radio.isChecked() == False and self.ui.honesty_d_radio.isChecked() == False and self.ui.honesty_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in honesty", QMessageBox.Ok)
                else:
                    self.printPDF()
            except Error as e:
                print(e)
                #QMessageBox.critical(self, "Generating Report", "ERROR: Please ensure all pupil's scores have been recorded in all subjects", QMessageBox.Ok)
            except TypeError as e:
                print(e)
                #QMessageBox.critical(self, "Generating Report", "ERROR: Please ensure all pupil's scores have been recorded in all subjects", QMessageBox.Ok)

    def displayRadios(self):
        if self.ui.punctuality_a_radio.isChecked():
            self.pri_report.ui.punctuality_a_label.setText("v")
            self.pri_report.ui.punctuality_b_label.setText("")
            self.pri_report.ui.punctuality_c_label.setText("")
            self.pri_report.ui.punctuality_d_label.setText("")
            self.pri_report.ui.punctuality_e_label.setText("")
        elif self.ui.punctuality_b_radio.isChecked():
            self.pri_report.ui.punctuality_a_label.setText("")
            self.pri_report.ui.punctuality_b_label.setText("v")
            self.pri_report.ui.punctuality_c_label.setText("")
            self.pri_report.ui.punctuality_d_label.setText("")
            self.pri_report.ui.punctuality_e_label.setText("")
        elif self.ui.punctuality_c_radio.isChecked():
            self.pri_report.ui.punctuality_a_label.setText("")
            self.pri_report.ui.punctuality_b_label.setText("")
            self.pri_report.ui.punctuality_c_label.setText("v")
            self.pri_report.ui.punctuality_d_label.setText("")
            self.pri_report.ui.punctuality_e_label.setText("")
        elif self.ui.punctuality_d_radio.isChecked():
            self.pri_report.ui.punctuality_a_label.setText("")
            self.pri_report.ui.punctuality_b_label.setText("")
            self.pri_report.ui.punctuality_c_label.setText("")
            self.pri_report.ui.punctuality_d_label.setText("v")
            self.pri_report.ui.punctuality_e_label.setText("")
        elif self.ui.punctuality_e_radio.isChecked():
            self.pri_report.ui.punctuality_a_label.setText("")
            self.pri_report.ui.punctuality_b_label.setText("")
            self.pri_report.ui.punctuality_c_label.setText("")
            self.pri_report.ui.punctuality_d_label.setText("")
            self.pri_report.ui.punctuality_e_label.setText("v")
        if self.ui.neatness_a_radio.isChecked():
            self.pri_report.ui.neatness_a_label.setText("v")
            self.pri_report.ui.neatness_b_label.setText("")
            self.pri_report.ui.neatness_c_label.setText("")
            self.pri_report.ui.neatness_d_label.setText("")
            self.pri_report.ui.neatness_e_label.setText("")
        elif self.ui.neatness_b_radio.isChecked():
            self.pri_report.ui.neatness_a_label.setText("")
            self.pri_report.ui.neatness_b_label.setText("v")
            self.pri_report.ui.neatness_c_label.setText("")
            self.pri_report.ui.neatness_d_label.setText("")
            self.pri_report.ui.neatness_e_label.setText("")
        elif self.ui.neatness_c_radio.isChecked():
            self.pri_report.ui.neatness_a_label.setText("")
            self.pri_report.ui.neatness_b_label.setText("")
            self.pri_report.ui.neatness_c_label.setText("v")
            self.pri_report.ui.neatness_d_label.setText("")
            self.pri_report.ui.neatness_e_label.setText("")
        elif self.ui.neatness_d_radio.isChecked():
            self.pri_report.ui.neatness_a_label.setText("")
            self.pri_report.ui.neatness_b_label.setText("")
            self.pri_report.ui.neatness_c_label.setText("")
            self.pri_report.ui.neatness_d_label.setText("v")
            self.pri_report.ui.neatness_e_label.setText("")
        elif self.ui.neatness_e_radio.isChecked():
            self.pri_report.ui.neatness_a_label.setText("")
            self.pri_report.ui.neatness_b_label.setText("")
            self.pri_report.ui.neatness_c_label.setText("")
            self.pri_report.ui.neatness_d_label.setText("")
            self.pri_report.ui.neatness_e_label.setText("v")
        if self.ui.games_a_radio.isChecked():
            self.pri_report.ui.games_a_label.setText("v")
            self.pri_report.ui.games_b_label.setText("")
            self.pri_report.ui.games_c_label.setText("")
            self.pri_report.ui.games_d_label.setText("")
            self.pri_report.ui.games_e_label.setText("")
        elif self.ui.games_b_radio.isChecked():
            self.pri_report.ui.games_a_label.setText("")
            self.pri_report.ui.games_b_label.setText("v")
            self.pri_report.ui.games_c_label.setText("")
            self.pri_report.ui.games_d_label.setText("")
            self.pri_report.ui.games_e_label.setText("")
        elif self.ui.games_b_radio.isChecked():
            self.pri_report.ui.games_a_label.setText("")
            self.pri_report.ui.games_b_label.setText("v")
            self.pri_report.ui.games_c_label.setText("")
            self.pri_report.ui.games_d_label.setText("")
            self.pri_report.ui.games_e_label.setText("")
        elif self.ui.games_c_radio.isChecked():
            self.pri_report.ui.games_a_label.setText("")
            self.pri_report.ui.games_b_label.setText("")
            self.pri_report.ui.games_c_label.setText("v")
            self.pri_report.ui.games_d_label.setText("")
            self.pri_report.ui.games_e_label.setText("")
        elif self.ui.games_d_radio.isChecked():
            self.pri_report.ui.games_a_label.setText("")
            self.pri_report.ui.games_b_label.setText("")
            self.pri_report.ui.games_c_label.setText("")
            self.pri_report.ui.games_d_label.setText("v")
            self.pri_report.ui.games_e_label.setText("")
        elif self.ui.games_e_radio.isChecked():
            self.pri_report.ui.games_a_label.setText("")
            self.pri_report.ui.games_b_label.setText("")
            self.pri_report.ui.games_c_label.setText("")
            self.pri_report.ui.games_d_label.setText("")
            self.pri_report.ui.games_e_label.setText("v")
        if self.ui.attentiveness_a_radio.isChecked():
            self.pri_report.ui.attentiveness_a_label.setText("v")
            self.pri_report.ui.attentiveness_b_label.setText("")
            self.pri_report.ui.attentiveness_c_label.setText("")
            self.pri_report.ui.attentiveness_d_label.setText("")
            self.pri_report.ui.attentiveness_e_label.setText("")
        elif self.ui.attentiveness_b_radio.isChecked():
            self.pri_report.ui.attentiveness_a_label.setText("")
            self.pri_report.ui.attentiveness_b_label.setText("v")
            self.pri_report.ui.attentiveness_c_label.setText("")
            self.pri_report.ui.attentiveness_d_label.setText("")
            self.pri_report.ui.attentiveness_e_label.setText("")
        elif self.ui.attentiveness_b_radio.isChecked():
            self.pri_report.ui.attentiveness_a_label.setText("")
            self.pri_report.ui.attentiveness_b_label.setText("v")
            self.pri_report.ui.attentiveness_c_label.setText("")
            self.pri_report.ui.attentiveness_d_label.setText("")
            self.pri_report.ui.attentiveness_e_label.setText("")
        elif self.ui.attentiveness_c_radio.isChecked():
            self.pri_report.ui.attentiveness_a_label.setText("")
            self.pri_report.ui.attentiveness_b_label.setText("")
            self.pri_report.ui.attentiveness_c_label.setText("v")
            self.pri_report.ui.attentiveness_d_label.setText("")
            self.pri_report.ui.attentiveness_e_label.setText("")
        elif self.ui.attentiveness_d_radio.isChecked():
            self.pri_report.ui.attentiveness_a_label.setText("")
            self.pri_report.ui.attentiveness_b_label.setText("")
            self.pri_report.ui.attentiveness_c_label.setText("")
            self.pri_report.ui.attentiveness_d_label.setText("v")
            self.pri_report.ui.attentiveness_e_label.setText("")
        elif self.ui.attentiveness_e_radio.isChecked():
            self.pri_report.ui.attentiveness_a_label.setText("")
            self.pri_report.ui.attentiveness_b_label.setText("")
            self.pri_report.ui.attentiveness_c_label.setText("")
            self.pri_report.ui.attentiveness_d_label.setText("")
            self.pri_report.ui.attentiveness_e_label.setText("v")
        if self.ui.relationship_a_radio.isChecked():
            self.pri_report.ui.relationship_a_label.setText("v")
            self.pri_report.ui.relationship_b_label.setText("")
            self.pri_report.ui.relationship_c_label.setText("")
            self.pri_report.ui.relationship_d_label.setText("")
            self.pri_report.ui.relationship_e_label.setText("")
        elif self.ui.relationship_b_radio.isChecked():
            self.pri_report.ui.relationship_a_label.setText("")
            self.pri_report.ui.relationship_b_label.setText("v")
            self.pri_report.ui.relationship_c_label.setText("")
            self.pri_report.ui.relationship_d_label.setText("")
            self.pri_report.ui.relationship_e_label.setText("")
        elif self.ui.relationship_b_radio.isChecked():
            self.pri_report.ui.relationship_a_label.setText("")
            self.pri_report.ui.relationship_b_label.setText("v")
            self.pri_report.ui.relationship_c_label.setText("")
            self.pri_report.ui.relationship_d_label.setText("")
            self.pri_report.ui.relationship_e_label.setText("")
        elif self.ui.relationship_c_radio.isChecked():
            self.pri_report.ui.relationship_a_label.setText("")
            self.pri_report.ui.relationship_b_label.setText("")
            self.pri_report.ui.relationship_c_label.setText("v")
            self.pri_report.ui.relationship_d_label.setText("")
            self.pri_report.ui.relationship_e_label.setText("")
        elif self.ui.relationship_d_radio.isChecked():
            self.pri_report.ui.relationship_a_label.setText("")
            self.pri_report.ui.relationship_b_label.setText("")
            self.pri_report.ui.relationship_c_label.setText("")
            self.pri_report.ui.relationship_d_label.setText("v")
            self.pri_report.ui.relationship_e_label.setText("")
        elif self.ui.honesty_e_radio.isChecked():
            self.pri_report.ui.honesty_a_label.setText("")
            self.pri_report.ui.honesty_b_label.setText("")
            self.pri_report.ui.honesty_c_label.setText("")
            self.pri_report.ui.honesty_d_label.setText("")
            self.pri_report.ui.honesty_e_label.setText("v")
        if self.ui.honesty_a_radio.isChecked():
            self.pri_report.ui.honesty_a_label.setText("v")
            self.pri_report.ui.honesty_b_label.setText("")
            self.pri_report.ui.honesty_c_label.setText("")
            self.pri_report.ui.honesty_d_label.setText("")
            self.pri_report.ui.honesty_e_label.setText("")
        elif self.ui.honesty_b_radio.isChecked():
            self.pri_report.ui.honesty_a_label.setText("")
            self.pri_report.ui.honesty_b_label.setText("v")
            self.pri_report.ui.honesty_c_label.setText("")
            self.pri_report.ui.honesty_d_label.setText("")
            self.pri_report.ui.honesty_e_label.setText("")
        elif self.ui.honesty_b_radio.isChecked():
            self.pri_report.ui.honesty_a_label.setText("")
            self.pri_report.ui.honesty_b_label.setText("v")
            self.pri_report.ui.honesty_c_label.setText("")
            self.pri_report.ui.honesty_d_label.setText("")
            self.pri_report.ui.honesty_e_label.setText("")
        elif self.ui.honesty_c_radio.isChecked():
            self.pri_report.ui.honesty_a_label.setText("")
            self.pri_report.ui.honesty_b_label.setText("")
            self.pri_report.ui.honesty_c_label.setText("v")
            self.pri_report.ui.honesty_d_label.setText("")
            self.pri_report.ui.honesty_e_label.setText("")
        elif self.ui.honesty_d_radio.isChecked():
            self.pri_report.ui.honesty_a_label.setText("")
            self.pri_report.ui.honesty_b_label.setText("")
            self.pri_report.ui.honesty_c_label.setText("")
            self.pri_report.ui.honesty_d_label.setText("v")
            self.pri_report.ui.honesty_e_label.setText("")
        elif self.ui.honesty_e_radio.isChecked():
            self.pri_report.ui.honesty_a_label.setText("")
            self.pri_report.ui.honesty_b_label.setText("")
            self.pri_report.ui.honesty_c_label.setText("")
            self.pri_report.ui.honesty_d_label.setText("")
            self.pri_report.ui.honesty_e_label.setText("v")


    def printReport(self):
        printer = QPrinter(QtPrintSupport.QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            painter = QPainter()
            painter.begin(printer)
            xscale = printer.pageRect().width() * 1.0 / self.pri_report.width()
            yscale = printer.pageRect().height() * 1.0 / self.pri_report.height()
            scale = min(xscale, yscale)
            painter.translate(printer.paperRect().center())
            painter.scale(scale, scale)
            painter.translate(-self.pri_report.width() / 2, -self.pri_report.height() / 2)
            self.pri_report.render(painter)
            painter.end()

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
            self.print_widget(self.pri_report, fn)

class PriReport(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PriReportForm()
        self.ui.setupUi(self)
        #Generates Current Date
        self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.ui.dateTimeEdit.hide()
        self.ui.print_date_label.setText(self.ui.dateTimeEdit.text())

class PriScoresRecord2(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_PriScoreRec2ndForm()
        self.ui.setupUi(self)
        self.displayClasses()

        self.ui.class_comboBox.currentTextChanged.connect(self.displayStuds)
        self.ui.stud_adm_no_comboBox.currentTextChanged.connect(self.displayName)
        self.ui.stud_adm_no_comboBox.currentTextChanged.connect(self.displaySpinVals)
        self.ui.qur_score_btn.clicked.connect(self.saveQurScores)
        self.ui.qur_score_btn.clicked.connect(self.saveIbadatScores)
        self.ui.qur_score_btn.clicked.connect(self.saveArabic1Scores)
        self.ui.qur_score_btn.clicked.connect(self.saveArabic2Scores)
        self.ui.qur_score_btn.clicked.connect(self.saveMathScores)
        self.ui.qur_score_btn.clicked.connect(self.saveEnglishScores)
        self.ui.qur_score_btn.clicked.connect(self.saveCompScores)
        self.ui.qur_score_btn.clicked.connect(self.saveBasScScores)
        self.ui.qur_score_btn.clicked.connect(self.saveReligionScores)
        self.ui.qur_score_btn.clicked.connect(self.saveCivicScores)
        self.ui.qur_score_btn.clicked.connect(self.saveVerbalScores)
        self.ui.qur_score_btn.clicked.connect(self.saveQuantScores)
        self.ui.qur_score_btn.clicked.connect(self.saveHandwiritingScores)
        self.ui.qur_score_btn.clicked.connect(self.saveFrenchScores)
        self.ui.qur_score_btn.clicked.connect(self.saveJollyScores)
        self.ui.qur_score_btn.clicked.connect(self.computeTotAvg)

    def displayClasses(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        query = cur.execute('SELECT * FROM t_classes ORDER BY class_name')
        rows = cur.fetchall()
        classes = ["Select a class"]
        self.ui.class_comboBox.clear()
        for row in rows:
            classes.append(row[0])
        self.ui.class_comboBox.addItems(classes)
        con.commit()
        con.close()

    def displayStuds(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox.currentText()
        cmd = "SELECT * FROM t_studs WHERE stud_class = ? ORDER BY admission_no"
        cur.execute(cmd, (classes_combo,))
        rows = cur.fetchall()
        adm_nos = ["Select a pupil"]
        self.ui.stud_adm_no_comboBox.clear()
        for row in rows:
            adm_nos.append(row[0])
        self.ui.stud_adm_no_comboBox.addItems(adm_nos)
        con.close()

    def displayName(self):
        self.ui.name_label.setText("")
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no_combo = self.ui.stud_adm_no_comboBox.currentText()
        cmd = "SELECT * FROM t_studs WHERE admission_no = ?"
        cur.execute(cmd, (stud_no_combo,))
        row = cur.fetchone()
        if row == None:
            self.ui.name_label.setText("")
        else:
            self.ui.name_label.setText("Name: " + row[1])

    def displaySpinVals(self):
        self.ui.qur_c1_spin.setValue(0)
        self.ui.qur_c2_spin.setValue(0)
        self.ui.qur_ass_spin.setValue(0)
        self.ui.qur_exam_spin.setValue(0)
        self.ui.ibadat_c1_spin.setValue(0)
        self.ui.ibadat_c2_spin.setValue(0)
        self.ui.ibadat_ass_spin.setValue(0)
        self.ui.ibadat_exam_spin.setValue(0)
        self.ui.arabic1_c1_spin.setValue(0)
        self.ui.arabic1_c2_spin.setValue(0)
        self.ui.arabic1_ass_spin.setValue(0)
        self.ui.arabic1_exam_spin.setValue(0)
        self.ui.arabic2_c1_spin.setValue(0)
        self.ui.arabic2_c2_spin.setValue(0)
        self.ui.arabic2_ass_spin.setValue(0)
        self.ui.arabic2_exam_spin.setValue(0)
        self.ui.math_c1_spin.setValue(0)
        self.ui.math_c2_spin.setValue(0)
        self.ui.math_ass_spin.setValue(0)
        self.ui.math_exam_spin.setValue(0)
        self.ui.eng_c1_spin.setValue(0)
        self.ui.eng_c2_spin.setValue(0)
        self.ui.eng_ass_spin.setValue(0)
        self.ui.eng_exam_spin.setValue(0)
        self.ui.comp_c1_spin.setValue(0)
        self.ui.comp_c2_spin.setValue(0)
        self.ui.comp_ass_spin.setValue(0)
        self.ui.comp_exam_spin.setValue(0)
        self.ui.bas_sc_c1_spin.setValue(0)
        self.ui.bas_sc_c2_spin.setValue(0)
        self.ui.bas_sc_ass_spin.setValue(0)
        self.ui.bas_sc_exam_spin.setValue(0)
        self.ui.religion_c1_spin.setValue(0)
        self.ui.religion_c2_spin.setValue(0)
        self.ui.religion_ass_spin.setValue(0)
        self.ui.religion_exam_spin.setValue(0)
        self.ui.civic_c1_spin.setValue(0)
        self.ui.civic_c2_spin.setValue(0)
        self.ui.civic_ass_spin.setValue(0)
        self.ui.civic_exam_spin.setValue(0)
        self.ui.verbal_c1_spin.setValue(0)
        self.ui.verbal_c2_spin.setValue(0)
        self.ui.verbal_ass_spin.setValue(0)
        self.ui.verbal_exam_spin.setValue(0)
        self.ui.quant_c1_spin.setValue(0)
        self.ui.quant_c2_spin.setValue(0)
        self.ui.quant_ass_spin.setValue(0)
        self.ui.quant_exam_spin.setValue(0)
        self.ui.basic_c1_spin.setValue(0)
        self.ui.basic_c2_spin.setValue(0)
        self.ui.basic_ass_spin.setValue(0)
        self.ui.basic_exam_spin.setValue(0)
        self.ui.french_c1_spin.setValue(0)
        self.ui.french_c2_spin.setValue(0)
        self.ui.french_ass_spin.setValue(0)
        self.ui.french_exam_spin.setValue(0)
        self.ui.jolly_c1_spin.setValue(0)
        self.ui.jolly_c2_spin.setValue(0)
        self.ui.jolly_ass_spin.setValue(0)
        self.ui.jolly_exam_spin.setValue(0)

        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        try:
            cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row != None and row[3] != None and row[4] != None and row[5] != None and row[6] != None:
                self.ui.qur_c1_spin.setValue(row[3])
                self.ui.qur_c2_spin.setValue(row[4])
                self.ui.qur_ass_spin.setValue(row[5])
                self.ui.qur_exam_spin.setValue(row[6])
            if row != None and row[8] != None and row[9] != None and row[10] != None and row[11] != None:
                self.ui.ibadat_c1_spin.setValue(row[8])
                self.ui.ibadat_c2_spin.setValue(row[9])
                self.ui.ibadat_ass_spin.setValue(row[10])
                self.ui.ibadat_exam_spin.setValue(row[11])
            if row != None and row[13] != None and row[14] != None and row[15] != None and row[16] != None:
                self.ui.arabic1_c1_spin.setValue(row[13])
                self.ui.arabic1_c2_spin.setValue(row[14])
                self.ui.arabic1_ass_spin.setValue(row[15])
                self.ui.arabic1_exam_spin.setValue(row[16])
            if row != None and row[18] != None and row[19] != None and row[20] != None and row[21] != None:
                self.ui.arabic2_c1_spin.setValue(row[18])
                self.ui.arabic2_c2_spin.setValue(row[19])
                self.ui.arabic2_ass_spin.setValue(row[20])
                self.ui.arabic2_exam_spin.setValue(row[21])
            if row != None and row[23] != None and row[24] != None and row[25] != None and row[26] != None:
                self.ui.math_c1_spin.setValue(row[23])
                self.ui.math_c2_spin.setValue(row[24])
                self.ui.math_ass_spin.setValue(row[25])
                self.ui.math_exam_spin.setValue(row[26])
            if row != None and row[28] != None and row[29] != None and row[30] != None and row[31] != None:
                self.ui.eng_c1_spin.setValue(row[28])
                self.ui.eng_c2_spin.setValue(row[29])
                self.ui.eng_ass_spin.setValue(row[30])
                self.ui.eng_exam_spin.setValue(row[31])
            if row != None and row[33] != None and row[34] != None and row[35] != None and row[36] != None:
                self.ui.comp_c1_spin.setValue(row[33])
                self.ui.comp_c2_spin.setValue(row[34])
                self.ui.comp_ass_spin.setValue(row[35])
                self.ui.comp_exam_spin.setValue(row[36])
            if row != None and row[38] != None and row[39] != None and row[40] != None and row[41] != None:
                self.ui.bas_sc_c1_spin.setValue(row[38])
                self.ui.bas_sc_c2_spin.setValue(row[39])
                self.ui.bas_sc_ass_spin.setValue(row[40])
                self.ui.bas_sc_exam_spin.setValue(row[41])
            if row != None and row[43] != None and row[44] != None and row[45] != None and row[46] != None:
                self.ui.religion_c1_spin.setValue(row[43])
                self.ui.religion_c2_spin.setValue(row[44])
                self.ui.religion_ass_spin.setValue(row[45])
                self.ui.religion_exam_spin.setValue(row[46])
            if row != None and row[48] != None and row[49] != None and row[50] != None and row[51] != None:
                self.ui.civic_c1_spin.setValue(row[48])
                self.ui.civic_c2_spin.setValue(row[49])
                self.ui.civic_ass_spin.setValue(row[50])
                self.ui.civic_exam_spin.setValue(row[51])
            if row != None and row[53] != None and row[54] != None and row[55] != None and row[56] != None:
                self.ui.verbal_c1_spin.setValue(row[53])
                self.ui.verbal_c2_spin.setValue(row[54])
                self.ui.verbal_ass_spin.setValue(row[55])
                self.ui.verbal_exam_spin.setValue(row[56])
            if row != None and row[58] != None and row[59] != None and row[60] != None and row[61] != None:
                self.ui.quant_c1_spin.setValue(row[58])
                self.ui.quant_c2_spin.setValue(row[59])
                self.ui.quant_ass_spin.setValue(row[60])
                self.ui.quant_exam_spin.setValue(row[61])
            if row != None and row[63] != None and row[64] != None and row[65] != None and row[66] != None:
                self.ui.basic_c1_spin.setValue(row[63])
                self.ui.basic_c2_spin.setValue(row[64])
                self.ui.basic_ass_spin.setValue(row[65])
                self.ui.basic_exam_spin.setValue(row[66])
            if row != None and row[68] != None and row[69] != None and row[70] != None and row[71] != None:
                self.ui.french_c1_spin.setValue(row[68])
                self.ui.french_c2_spin.setValue(row[69])
                self.ui.french_ass_spin.setValue(row[70])
                self.ui.french_exam_spin.setValue(row[71])
            if row != None and row[73] != None and row[74] != None and row[75] != None and row[76] != None:
                self.ui.jolly_c1_spin.setValue(row[73])
                self.ui.jolly_c2_spin.setValue(row[74])
                self.ui.jolly_ass_spin.setValue(row[75])
                self.ui.jolly_exam_spin.setValue(row[76])
        except Error as e:
            QMessageBox.critical(self, "Saving Score", str(e), QMessageBox.Ok)

    def saveQurScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        qur_c1 = self.ui.qur_c1_spin.value()
        qur_c2 = self.ui.qur_c2_spin.value()
        qur_ass = self.ui.qur_ass_spin.value()
        qur_exam = self.ui.qur_exam_spin.value()
        qur_total = qur_c1 + qur_c2 + qur_ass + qur_exam
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_second(stud_no, score_class, qur_c1, qur_c2, qur_ass, qur_exam, qur_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, qur_c1, qur_c2, qur_ass, qur_exam, qur_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, score_class = ?, qur_c1 = ?, qur_c2 = ?, qur_ass = ?, qur_exam = ?, qur_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, qur_c1, qur_c2, qur_ass, qur_exam, qur_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveIbadatScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        ibadat_c1 = self.ui.ibadat_c1_spin.value()
        ibadat_c2 = self.ui.ibadat_c2_spin.value()
        ibadat_ass = self.ui.ibadat_ass_spin.value()
        ibadat_exam = self.ui.ibadat_exam_spin.value()
        ibadat_total = ibadat_c1 + ibadat_c2 + ibadat_ass + ibadat_exam
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_second(stud_no, score_class, ibadat_c1, ibadat_c2, ibadat_ass, ibadat_exam, ibadat_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, ibadat_c1, ibadat_c2, ibadat_ass, ibadat_exam, ibadat_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, score_class = ?, ibadat_c1 = ?, ibadat_c2 = ?, ibadat_ass = ?, ibadat_exam = ?, ibadat_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, ibadat_c1, ibadat_c2, ibadat_ass, ibadat_exam, ibadat_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveArabic1Scores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        arabic1_c1 = self.ui.arabic1_c1_spin.value()
        arabic1_c2 = self.ui.arabic1_c2_spin.value()
        arabic1_ass = self.ui.arabic1_ass_spin.value()
        arabic1_exam = self.ui.arabic1_exam_spin.value()
        arabic1_total = arabic1_c1 + arabic1_c2 + arabic1_ass + arabic1_exam
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_second(stud_no, score_class, arabic1_c1, arabic1_c2, arabic1_ass, arabic1_exam, arabic1_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, arabic1_c1, arabic1_c2, arabic1_ass, arabic1_exam, arabic1_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, score_class = ?, arabic1_c1 = ?, arabic1_c2 = ?, arabic1_ass = ?, arabic1_exam = ?, arabic1_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, arabic1_c1, arabic1_c2, arabic1_ass, arabic1_exam, arabic1_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveArabic2Scores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        arabic2_c1 = self.ui.arabic2_c1_spin.value()
        arabic2_c2 = self.ui.arabic2_c2_spin.value()
        arabic2_ass = self.ui.arabic2_ass_spin.value()
        arabic2_exam = self.ui.arabic2_exam_spin.value()
        arabic2_total = arabic2_c1 + arabic2_c2 + arabic2_ass + arabic2_exam
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_second(stud_no, score_class, arabic2_c1, arabic2_c2, arabic2_ass, arabic2_exam, arabic2_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, arabic2_c1, arabic2_c2, arabic2_ass, arabic2_exam, arabic2_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, score_class = ?, arabic2_c1 = ?, arabic2_c2 = ?, arabic2_ass = ?, arabic2_exam = ?, arabic2_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, arabic2_c1, arabic2_c2, arabic2_ass, arabic2_exam, arabic2_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveMathScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        math_c1 = self.ui.math_c1_spin.value()
        math_c2 = self.ui.math_c2_spin.value()
        math_ass = self.ui.math_ass_spin.value()
        math_exam = self.ui.math_exam_spin.value()
        math_total = math_c1 + math_c2 + math_ass + math_exam
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_second(stud_no, score_class, math_c1, math_c2, math_ass, math_exam, math_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, math_c1, math_c2, math_ass, math_exam, math_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, score_class = ?, math_c1 = ?, math_c2 = ?, math_ass = ?, math_exam = ?, math_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, math_c1, math_c2, math_ass, math_exam, math_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveEnglishScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        eng_c1 = self.ui.eng_c1_spin.value()
        eng_c2 = self.ui.eng_c2_spin.value()
        eng_ass = self.ui.eng_ass_spin.value()
        eng_exam = self.ui.eng_exam_spin.value()
        eng_total = eng_c1 + eng_c2 + eng_ass + eng_exam
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_second(stud_no, score_class, eng_c1, eng_c2, eng_ass, eng_exam, eng_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, eng_c1, eng_c2, eng_ass, eng_exam, eng_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, score_class = ?, eng_c1 = ?, eng_c2 = ?, eng_ass = ?, eng_exam = ?, eng_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, eng_c1, eng_c2, eng_ass, eng_exam, eng_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveCompScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        comp_c1 = self.ui.comp_c1_spin.value()
        comp_c2 = self.ui.comp_c2_spin.value()
        comp_ass = self.ui.comp_ass_spin.value()
        comp_exam = self.ui.comp_exam_spin.value()
        comp_total = comp_c1 + comp_c2 + comp_ass + comp_exam
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_second(stud_no, score_class, comp_c1, comp_c2, comp_ass, comp_exam, comp_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, comp_c1, comp_c2, comp_ass, comp_exam, comp_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, score_class = ?, comp_c1 = ?, comp_c2 = ?, comp_ass = ?, comp_exam = ?, comp_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, comp_c1, comp_c2, comp_ass, comp_exam, comp_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveBasScScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        bas_sc_c1 = self.ui.bas_sc_c1_spin.value()
        bas_sc_c2 = self.ui.bas_sc_c2_spin.value()
        bas_sc_ass = self.ui.bas_sc_ass_spin.value()
        bas_sc_exam = self.ui.bas_sc_exam_spin.value()
        bas_sc_total = bas_sc_c1 + bas_sc_c2 + bas_sc_ass + bas_sc_exam
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_second(stud_no, score_class, bas_sc_c1, bas_sc_c2, bas_sc_ass, bas_sc_exam, bas_sc_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, bas_sc_c1, bas_sc_c2, bas_sc_ass, bas_sc_exam, bas_sc_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, score_class = ?, bas_sc_c1 = ?, bas_sc_c2 = ?, bas_sc_ass = ?, bas_sc_exam = ?, bas_sc_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, bas_sc_c1, bas_sc_c2, bas_sc_ass, bas_sc_exam, bas_sc_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveReligionScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        religion_c1 = self.ui.religion_c1_spin.value()
        religion_c2 = self.ui.religion_c2_spin.value()
        religion_ass = self.ui.religion_ass_spin.value()
        religion_exam = self.ui.religion_exam_spin.value()
        religion_total = religion_c1 + religion_c2 + religion_ass + religion_exam
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_second(stud_no, score_class, religion_c1, religion_c2, religion_ass, religion_exam, religion_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, religion_c1, religion_c2, religion_ass, religion_exam, religion_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, score_class = ?, religion_c1 = ?, religion_c2 = ?, religion_ass = ?, religion_exam = ?, religion_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, religion_c1, religion_c2, religion_ass, religion_exam, religion_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveCivicScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        civic_c1 = self.ui.civic_c1_spin.value()
        civic_c2 = self.ui.civic_c2_spin.value()
        civic_ass = self.ui.civic_ass_spin.value()
        civic_exam = self.ui.civic_exam_spin.value()
        civic_total = civic_c1 + civic_c2 + civic_ass + civic_exam
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_second(stud_no, score_class, civic_c1, civic_c2, civic_ass, civic_exam, civic_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, civic_c1, civic_c2, civic_ass, civic_exam, civic_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, score_class = ?, civic_c1 = ?, civic_c2 = ?, civic_ass = ?, civic_exam = ?, civic_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, civic_c1, civic_c2, civic_ass, civic_exam, civic_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveVerbalScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        verbal_c1 = self.ui.verbal_c1_spin.value()
        verbal_c2 = self.ui.verbal_c2_spin.value()
        verbal_ass = self.ui.verbal_ass_spin.value()
        verbal_exam = self.ui.verbal_exam_spin.value()
        verbal_total = verbal_c1 + verbal_c2 + verbal_ass + verbal_exam
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_second(stud_no, score_class, verbal_c1, verbal_c2, verbal_ass, verbal_exam, verbal_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, verbal_c1, verbal_c2, verbal_ass, verbal_exam, verbal_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, score_class = ?, verbal_c1 = ?, verbal_c2 = ?, verbal_ass = ?, verbal_exam = ?, verbal_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, verbal_c1, verbal_c2, verbal_ass, verbal_exam, verbal_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveQuantScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        quant_c1 = self.ui.quant_c1_spin.value()
        quant_c2 = self.ui.quant_c2_spin.value()
        quant_ass = self.ui.quant_ass_spin.value()
        quant_exam = self.ui.quant_exam_spin.value()
        quant_total = quant_c1 + quant_c2 + quant_ass + quant_exam
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_second(stud_no, score_class, quant_c1, quant_c2, quant_ass, quant_exam, quant_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, quant_c1, quant_c2, quant_ass, quant_exam, quant_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, score_class = ?, quant_c1 = ?, quant_c2 = ?, quant_ass = ?, quant_exam = ?, quant_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, quant_c1, quant_c2, quant_ass, quant_exam, quant_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveHandwiritingScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        basic_c1 = self.ui.basic_c1_spin.value()
        basic_c2 = self.ui.basic_c2_spin.value()
        basic_ass = self.ui.basic_ass_spin.value()
        basic_exam = self.ui.basic_exam_spin.value()
        basic_total = basic_c1 + basic_c2 + basic_ass + basic_exam
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_second(stud_no, score_class, basic_c1, basic_c2, basic_ass, basic_exam, basic_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, basic_c1, basic_c2, basic_ass, basic_exam, basic_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, score_class = ?, basic_c1 = ?, basic_c2 = ?, basic_ass = ?, basic_exam = ?, basic_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, basic_c1, basic_c2, basic_ass, basic_exam, basic_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveFrenchScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        french_c1 = self.ui.french_c1_spin.value()
        french_c2 = self.ui.french_c2_spin.value()
        french_ass = self.ui.french_ass_spin.value()
        french_exam = self.ui.french_exam_spin.value()
        french_total = french_c1 + french_c2 + french_ass + french_exam
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_second(stud_no, score_class, french_c1, french_c2, french_ass, french_exam, french_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, french_c1, french_c2, french_ass, french_exam, french_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, score_class = ?, french_c1 = ?, french_c2 = ?, french_ass = ?, french_exam = ?, french_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, french_c1, french_c2, french_ass, french_exam, french_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveJollyScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        jolly_c1 = self.ui.jolly_c1_spin.value()
        jolly_c2 = self.ui.jolly_c2_spin.value()
        jolly_ass = self.ui.jolly_ass_spin.value()
        jolly_exam = self.ui.jolly_exam_spin.value()
        jolly_total = jolly_c1 + jolly_c2 + jolly_ass + jolly_exam
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_second(stud_no, score_class, jolly_c1, jolly_c2, jolly_ass, jolly_exam, jolly_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, jolly_c1, jolly_c2, jolly_ass, jolly_exam, jolly_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, score_class = ?, jolly_c1 = ?, jolly_c2 = ?, jolly_ass = ?, jolly_exam = ?, jolly_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, jolly_c1, jolly_c2, jolly_ass, jolly_exam, jolly_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def computeTotAvg(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        cmd1 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
        cur.execute(cmd1, (stud_no,))
        row = cur.fetchone()
        if row == None:
            pass
        elif row[7] != None and row[12] != None and row[17] != None and row[22] != None and row[27] != None and row[32] != None and row[37] != None and row[42] != None and row[47] != None and row[52] != None and row[57] != None and row[62] != None and row[67] != None and row[72] != None and row[77] != None:
            try:
                all_total = row[7] + row[12] + row[17] + row[22] + row[27] + row[32] + row[37] + row[42]+ row[47] + row[52] + row[57] + row[62] + row[67] + row[72] + row[77]
                avg = round((all_total/1500)*100, 4)

                cmd2 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
                cur.execute(cmd2, (stud_no,))
                row = cur.fetchone()
                if row == None:
                    total_cum = all_total
                    avg_cum = round((total_cum/1500)*100, 4)
                elif row[78] == None:
                    total_cum = all_total
                    avg_cum = round((total_cum/1500)*100, 4)
                else:
                    total_cum = row[78] + all_total
                    avg_cum = round((total_cum/3000)*100, 4)
                cmd3 = "UPDATE t_pri_scores_second SET stud_no = ?, all_total = ?, avg = ?, total_cum = ?, avg_cum = ?  WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, all_total, avg, total_cum, avg_cum, stud_no,))
                con.commit()
                QMessageBox.information(self, "Saving Score",  "Pupil's scores saved successfully", QMessageBox.Ok)
            except Error as e:
                QMessageBox.critical(self, "Saving Score", str(e), QMessageBox.Ok)
            except TypeError as e:
                QMessageBox.critical(self, "Saving Score", str(e), QMessageBox.Ok)
            finally:
                con.close()

class PriScoresView2(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PriScore2ndForm()
        self.ui.setupUi(self)
        self.pri_report2 = PriReport2()
        self.displayClasses()
        self.listStudsScores()
        self.ui.class_comboBox.currentTextChanged.connect(self.listClass)
        self.ui.class_comboBox.currentTextChanged.connect(self.displayStuds)
        self.ui.switch_back_btn.clicked.connect(self.listStudsScores)
        self.ui.report_gen_btn.clicked.connect(self.displayRadios)
        self.ui.report_gen_btn.clicked.connect(self.generatePriReport)
        self.ui.pdf_btn.clicked.connect(self.displayRadios)
        self.ui.pdf_btn.clicked.connect(self.generatePriReportPDF)
        self.ui.del_btn.clicked.connect(self.deleteStud)
        self.ui.stud_adm_no_comboBox.currentTextChanged.connect(self.displayName)

    def displayClasses(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        query = cur.execute('SELECT * FROM t_pri_scores_second ORDER BY score_class')
        self.ui.class_comboBox.clear()
        classes = ["Select a class"]
        rows = cur.fetchall()
        for row in rows:
            if row[2] not in classes:
                classes.append(row[2])
        self.ui.class_comboBox.addItems(classes)
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

    def listStudsScores(self):
        self.displayClasses()
        self.ui.tableWidget_2.hide()
        self.ui.tableWidget.setRowCount(0)
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        cmd = "SELECT * FROM t_pri_scores_second ORDER BY stud_no"
        cur.execute(cmd)
        rows = cur.fetchall()
        for row_number, row_data in enumerate(rows):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                it = QTableWidgetItem()
                it.setText(str(column_data))
                self.ui.tableWidget.setItem(row_number, column_number, it)
        self.ui.tableWidget.show()
        self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.ui.tableWidget.setColumnWidth(0,0)
        con.close()

    def listClass(self):
        self.ui.tableWidget.hide()
        self.ui.tableWidget_2.setRowCount(0)
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox.currentText()
        cmd = "SELECT * FROM t_pri_scores_second WHERE score_class = ? ORDER BY stud_no"
        cur.execute(cmd, (classes_combo,))
        rows = cur.fetchall()
        for row_number, row_data in enumerate(rows):
            self.ui.tableWidget_2.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                it = QTableWidgetItem()
                it.setText(str(column_data))
                self.ui.tableWidget_2.setItem(row_number, column_number, it)
        self.ui.tableWidget_2.show()
        self.ui.tableWidget_2.horizontalHeader().setDefaultSectionSize(180)
        self.ui.tableWidget_2.setColumnWidth(0,0)
        self.ui.class_comboBox.show()
        con.close()

    def displayStuds(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox.currentText()
        cmd = "SELECT * FROM t_pri_scores_second WHERE score_class = ? ORDER BY stud_no"
        cur.execute(cmd, (classes_combo,))
        rows = cur.fetchall()
        adm_nos = ["Select an admission number"]
        self.ui.stud_adm_no_comboBox.clear()
        for row in rows:
            adm_nos.append(row[1])
        self.ui.stud_adm_no_comboBox.addItems(adm_nos)
        con.close()

    def displayName(self):
        self.ui.name_label.setText("")
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no_combo = self.ui.stud_adm_no_comboBox.currentText()
        cmd = "SELECT * FROM t_studs WHERE admission_no = ?"
        cur.execute(cmd, (stud_no_combo,))
        row = cur.fetchone()
        if row == None:
            self.ui.name_label.setText("")
        else:
            self.ui.name_label.setText("Name: \n" + row[1])

    def deleteStud(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        if stud_no == "Select an admission number":
            QMessageBox.critical(self, "Deleting Pupil", "ERROR: Please select pupil's admission number before pressing delete", QMessageBox.Ok)
        elif stud_no == "":
            QMessageBox.critical(self, "Deleting Pupil", "ERROR: Please select a class and pupil's admission number before pressing delete", QMessageBox.Ok)
        else:
            cmd = "DELETE FROM t_pri_scores_second WHERE stud_no = ?"
            buttonReply = QMessageBox.warning(self, 'Deleting Pupil', "WARNING: Deleting will remove all the pupil's score records in the class. Do you still wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                cur.execute(cmd, (stud_no,))
                con.commit()
                self.displayStuds()
                con.close()

    def generatePriReport(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox.currentText()
        admission_no = self.ui.stud_adm_no_comboBox.currentText()
        cmd1 = "SELECT * FROM t_studs WHERE admission_no = ?"
        cur.execute(cmd1, (admission_no,))
        row = cur.fetchone()
        if row == None:
            QMessageBox.critical(self, "Printing Report", "ERROR: Please select a class and pupil's admission number before generating report", QMessageBox.Ok)
        else:
            self.pri_report2.ui.name_label.setText(row[1])
            self.pri_report2.ui.class_label.setText(row[3])
            self.pri_report2.ui.sex_label.setText(row[5])
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray.fromBase64(row[6]))
            self.pri_report2.ui.photo_label.setPixmap(QPixmap(pixmap))
            try:
                cmd3 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
                cur.execute(cmd3, (admission_no,))
                row = cur.fetchone()
                self.pri_report2.ui.qur_c1_label.setText(str(row[3]))
                self.pri_report2.ui.qur_c2_label.setText(str(row[4]))
                self.pri_report2.ui.qur_ass_label.setText(str(row[5]))
                self.pri_report2.ui.qur_exam_label.setText(str(row[6]))
                self.pri_report2.ui.qur_total_label.setText(str(row[7]))
                if row[7] < 40:
                    self.pri_report2.ui.qur_grade_label.setText("F")
                    self.pri_report2.ui.qur_remark_label.setText("Fail")
                elif row[7] >= 40 and row[7] < 50:
                    self.pri_report2.ui.qur_grade_label.setText("D")
                    self.pri_report2.ui.qur_remark_label.setText("Pass")
                elif row[7] >= 50 and row[7] < 60:
                    self.pri_report2.ui.qur_grade_label.setText("C")
                    self.pri_report2.ui.qur_remark_label.setText("Good")
                elif row[7] >= 60 and row[7] < 70:
                    self.pri_report2.ui.qur_grade_label.setText("B")
                    self.pri_report2.ui.qur_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.qur_grade_label.setText("A")
                    self.pri_report2.ui.qur_remark_label.setText("Excellent")
                self.pri_report2.ui.ibadat_c1_label.setText(str(row[8]))
                self.pri_report2.ui.ibadat_c2_label.setText(str(row[9]))
                self.pri_report2.ui.ibadat_ass_label.setText(str(row[10]))
                self.pri_report2.ui.ibadat_exam_label.setText(str(row[11]))
                self.pri_report2.ui.ibadat_total_label.setText(str(row[12]))
                if row[12] < 40:
                    self.pri_report2.ui.ibadat_grade_label.setText("F")
                    self.pri_report2.ui.ibadat_remark_label.setText("Fail")
                elif row[12] >= 40 and row[12] < 50:
                    self.pri_report2.ui.ibadat_grade_label.setText("D")
                    self.pri_report2.ui.ibadat_remark_label.setText("Pass")
                elif row[12] >= 50 and row[12] < 60:
                    self.pri_report2.ui.ibadat_grade_label.setText("C")
                    self.pri_report2.ui.ibadat_remark_label.setText("Good")
                elif row[12] >= 60 and row[12] < 70:
                    self.pri_report2.ui.ibadat_grade_label.setText("B")
                    self.pri_report2.ui.ibadat_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.ibadat_grade_label.setText("A")
                    self.pri_report2.ui.ibadat_remark_label.setText("Excellent")
                self.pri_report2.ui.arabic1_c1_label.setText(str(row[13]))
                self.pri_report2.ui.arabic1_c2_label.setText(str(row[14]))
                self.pri_report2.ui.arabic1_ass_label.setText(str(row[15]))
                self.pri_report2.ui.arabic1_exam_label.setText(str(row[16]))
                self.pri_report2.ui.arabic1_total_label.setText(str(row[17]))
                if row[17] < 40:
                    self.pri_report2.ui.arabic1_grade_label.setText("F")
                    self.pri_report2.ui.arabic1_remark_label.setText("Fail")
                elif row[17] >= 40 and row[17] < 50:
                    self.pri_report2.ui.arabic1_grade_label.setText("D")
                    self.pri_report2.ui.arabic1_remark_label.setText("Pass")
                elif row[17] >= 50 and row[17] < 60:
                    self.pri_report2.ui.arabic1_grade_label.setText("C")
                    self.pri_report2.ui.arabic1_remark_label.setText("Good")
                elif row[17] >= 60 and row[17] < 70:
                    self.pri_report2.ui.arabic1_grade_label.setText("B")
                    self.pri_report2.ui.arabic1_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.arabic1_grade_label.setText("A")
                    self.pri_report2.ui.arabic1_remark_label.setText("Excellent")
                self.pri_report2.ui.arabic2_c1_label.setText(str(row[18]))
                self.pri_report2.ui.arabic2_c2_label.setText(str(row[19]))
                self.pri_report2.ui.arabic2_ass_label.setText(str(row[20]))
                self.pri_report2.ui.arabic2_exam_label.setText(str(row[21]))
                self.pri_report2.ui.arabic2_total_label.setText(str(row[22]))
                if row[22] < 40:
                    self.pri_report2.ui.arabic2_grade_label.setText("F")
                    self.pri_report2.ui.arabic2_remark_label.setText("Fail")
                elif row[22] >= 40 and row[22] < 50:
                    self.pri_report2.ui.arabic2_grade_label.setText("D")
                    self.pri_report2.ui.arabic2_remark_label.setText("Pass")
                elif row[22] >= 50 and row[22] < 60:
                    self.pri_report2.ui.arabic2_grade_label.setText("C")
                    self.pri_report2.ui.arabic2_remark_label.setText("Good")
                elif row[22] >= 60 and row[22] < 70:
                    self.pri_report2.ui.arabic2_grade_label.setText("B")
                    self.pri_report2.ui.arabic2_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.arabic2_grade_label.setText("A")
                    self.pri_report2.ui.arabic2_remark_label.setText("Excellent")
                self.pri_report2.ui.math_c1_label.setText(str(row[23]))
                self.pri_report2.ui.math_c2_label.setText(str(row[24]))
                self.pri_report2.ui.math_ass_label.setText(str(row[25]))
                self.pri_report2.ui.math_exam_label.setText(str(row[26]))
                self.pri_report2.ui.math_total_label.setText(str(row[27]))
                if row[27] < 40:
                    self.pri_report2.ui.math_grade_label.setText("F")
                    self.pri_report2.ui.math_remark_label.setText("Fail")
                elif row[27] >= 40 and row[27] < 50:
                    self.pri_report2.ui.math_grade_label.setText("D")
                    self.pri_report2.ui.math_remark_label.setText("Pass")
                elif row[27] >= 50 and row[27] < 60:
                    self.pri_report2.ui.math_grade_label.setText("C")
                    self.pri_report2.ui.math_remark_label.setText("Good")
                elif row[27] >= 60 and row[27] < 70:
                    self.pri_report2.ui.math_grade_label.setText("B")
                    self.pri_report2.ui.math_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.math_grade_label.setText("A")
                    self.pri_report2.ui.math_remark_label.setText("Excellent")
                self.pri_report2.ui.eng_c1_label.setText(str(row[28]))
                self.pri_report2.ui.eng_c2_label.setText(str(row[29]))
                self.pri_report2.ui.eng_ass_label.setText(str(row[30]))
                self.pri_report2.ui.eng_exam_label.setText(str(row[31]))
                self.pri_report2.ui.eng_total_label.setText(str(row[32]))
                if row[32] < 40:
                    self.pri_report2.ui.eng_grade_label.setText("F")
                    self.pri_report2.ui.eng_remark_label.setText("Fail")
                elif row[32] >= 40 and row[32] < 50:
                    self.pri_report2.ui.eng_grade_label.setText("D")
                    self.pri_report2.ui.eng_remark_label.setText("Pass")
                elif row[32] >= 50 and row[32] < 60:
                    self.pri_report2.ui.eng_grade_label.setText("C")
                    self.pri_report2.ui.eng_remark_label.setText("Good")
                elif row[32] >= 60 and row[32] < 70:
                    self.pri_report2.ui.eng_grade_label.setText("B")
                    self.pri_report2.ui.eng_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.eng_grade_label.setText("A")
                    self.pri_report2.ui.eng_remark_label.setText("Excellent")
                self.pri_report2.ui.comp_c1_label.setText(str(row[33]))
                self.pri_report2.ui.comp_c2_label.setText(str(row[34]))
                self.pri_report2.ui.comp_ass_label.setText(str(row[35]))
                self.pri_report2.ui.comp_exam_label.setText(str(row[36]))
                self.pri_report2.ui.comp_total_label.setText(str(row[37]))
                if row[37] < 40:
                    self.pri_report2.ui.comp_grade_label.setText("F")
                    self.pri_report2.ui.comp_remark_label.setText("Fail")
                elif row[37] >= 40 and row[37] < 50:
                    self.pri_report2.ui.comp_grade_label.setText("D")
                    self.pri_report2.ui.comp_remark_label.setText("Pass")
                elif row[37] >= 50 and row[37] < 60:
                    self.pri_report2.ui.comp_grade_label.setText("C")
                    self.pri_report2.ui.comp_remark_label.setText("Good")
                elif row[37] >= 60 and row[37] < 70:
                    self.pri_report2.ui.comp_grade_label.setText("B")
                    self.pri_report2.ui.comp_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.comp_grade_label.setText("A")
                    self.pri_report2.ui.comp_remark_label.setText("Excellent")
                self.pri_report2.ui.bas_sc_c1_label.setText(str(row[38]))
                self.pri_report2.ui.bas_sc_c2_label.setText(str(row[39]))
                self.pri_report2.ui.bas_sc_ass_label.setText(str(row[40]))
                self.pri_report2.ui.bas_sc_exam_label.setText(str(row[41]))
                self.pri_report2.ui.bas_sc_total_label.setText(str(row[42]))
                if row[42] < 40:
                    self.pri_report2.ui.bas_sc_grade_label.setText("F")
                    self.pri_report2.ui.bas_sc_remark_label.setText("Fail")
                elif row[42] >= 40 and row[42] < 50:
                    self.pri_report2.ui.bas_sc_grade_label.setText("D")
                    self.pri_report2.ui.bas_sc_remark_label.setText("Pass")
                elif row[42] >= 50 and row[42] < 60:
                    self.pri_report2.ui.bas_sc_grade_label.setText("C")
                    self.pri_report2.ui.bas_sc_remark_label.setText("Good")
                elif row[42] >= 60 and row[42] < 70:
                    self.pri_report2.ui.bas_sc_grade_label.setText("B")
                    self.pri_report2.ui.bas_sc_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.bas_sc_grade_label.setText("A")
                    self.pri_report2.ui.bas_sc_remark_label.setText("Excellent")
                self.pri_report2.ui.religion_c1_label.setText(str(row[43]))
                self.pri_report2.ui.religion_c2_label.setText(str(row[44]))
                self.pri_report2.ui.religion_ass_label.setText(str(row[45]))
                self.pri_report2.ui.religion_exam_label.setText(str(row[46]))
                self.pri_report2.ui.religion_total_label.setText(str(row[47]))
                if row[47] < 40:
                    self.pri_report2.ui.religion_grade_label.setText("F")
                    self.pri_report2.ui.religion_remark_label.setText("Fail")
                elif row[47] >= 40 and row[47] < 50:
                    self.pri_report2.ui.religion_grade_label.setText("D")
                    self.pri_report2.ui.religion_remark_label.setText("Pass")
                elif row[47] >= 50 and row[47] < 60:
                    self.pri_report2.ui.religion_grade_label.setText("C")
                    self.pri_report2.ui.religion_remark_label.setText("Good")
                elif row[47] >= 60 and row[47] < 70:
                    self.pri_report2.ui.religion_grade_label.setText("B")
                    self.pri_report2.ui.religion_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.religion_grade_label.setText("A")
                    self.pri_report2.ui.religion_remark_label.setText("Excellent")
                self.pri_report2.ui.civic_c1_label.setText(str(row[48]))
                self.pri_report2.ui.civic_c2_label.setText(str(row[49]))
                self.pri_report2.ui.civic_ass_label.setText(str(row[50]))
                self.pri_report2.ui.civic_exam_label.setText(str(row[51]))
                self.pri_report2.ui.civic_total_label.setText(str(row[52]))
                if row[52] < 40:
                    self.pri_report2.ui.civic_grade_label.setText("F")
                    self.pri_report2.ui.civic_remark_label.setText("Fail")
                elif row[52] >= 40 and row[52] < 50:
                    self.pri_report2.ui.civic_grade_label.setText("D")
                    self.pri_report2.ui.civic_remark_label.setText("Pass")
                elif row[52] >= 50 and row[52] < 60:
                    self.pri_report2.ui.civic_grade_label.setText("C")
                    self.pri_report2.ui.civic_remark_label.setText("Good")
                elif row[52] >= 60 and row[52] < 70:
                    self.pri_report2.ui.civic_grade_label.setText("B")
                    self.pri_report2.ui.civic_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.civic_grade_label.setText("A")
                    self.pri_report2.ui.civic_remark_label.setText("Excellent")
                self.pri_report2.ui.verbal_c1_label.setText(str(row[53]))
                self.pri_report2.ui.verbal_c2_label.setText(str(row[54]))
                self.pri_report2.ui.verbal_ass_label.setText(str(row[55]))
                self.pri_report2.ui.verbal_exam_label.setText(str(row[56]))
                self.pri_report2.ui.verbal_total_label.setText(str(row[57]))
                if row[57] < 40:
                    self.pri_report2.ui.verbal_grade_label.setText("F")
                    self.pri_report2.ui.verbal_remark_label.setText("Fail")
                elif row[57] >= 40 and row[57] < 50:
                    self.pri_report2.ui.verbal_grade_label.setText("D")
                    self.pri_report2.ui.verbal_remark_label.setText("Pass")
                elif row[57] >= 50 and row[57] < 60:
                    self.pri_report2.ui.verbal_grade_label.setText("C")
                    self.pri_report2.ui.verbal_remark_label.setText("Good")
                elif row[57] >= 60 and row[57] < 70:
                    self.pri_report2.ui.verbal_grade_label.setText("B")
                    self.pri_report2.ui.verbal_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.verbal_grade_label.setText("A")
                    self.pri_report2.ui.verbal_remark_label.setText("Excellent")
                self.pri_report2.ui.quant_c1_label.setText(str(row[58]))
                self.pri_report2.ui.quant_c2_label.setText(str(row[59]))
                self.pri_report2.ui.quant_ass_label.setText(str(row[60]))
                self.pri_report2.ui.quant_exam_label.setText(str(row[61]))
                self.pri_report2.ui.quant_total_label.setText(str(row[62]))
                if row[62] < 40:
                    self.pri_report2.ui.quant_grade_label.setText("F")
                    self.pri_report2.ui.quant_remark_label.setText("Fail")
                elif row[62] >= 40 and row[62] < 50:
                    self.pri_report2.ui.quant_grade_label.setText("D")
                    self.pri_report2.ui.quant_remark_label.setText("Pass")
                elif row[62] >= 50 and row[62] < 60:
                    self.pri_report2.ui.quant_grade_label.setText("C")
                    self.pri_report2.ui.quant_remark_label.setText("Good")
                elif row[62] >= 60 and row[62] < 70:
                    self.pri_report2.ui.quant_grade_label.setText("B")
                    self.pri_report2.ui.quant_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.quant_grade_label.setText("A")
                    self.pri_report2.ui.quant_remark_label.setText("Excellent")
                self.pri_report2.ui.basic_c1_label.setText(str(row[63]))
                self.pri_report2.ui.basic_c2_label.setText(str(row[64]))
                self.pri_report2.ui.basic_ass_label.setText(str(row[65]))
                self.pri_report2.ui.basic_exam_label.setText(str(row[66]))
                self.pri_report2.ui.basic_total_label.setText(str(row[67]))
                if row[67] < 40:
                    self.pri_report2.ui.basic_grade_label.setText("F")
                    self.pri_report2.ui.basic_remark_label.setText("Fail")
                elif row[67] >= 40 and row[67] < 50:
                    self.pri_report2.ui.basic_grade_label.setText("D")
                    self.pri_report2.ui.basic_remark_label.setText("Pass")
                elif row[67] >= 50 and row[67] < 60:
                    self.pri_report2.ui.basic_grade_label.setText("C")
                    self.pri_report2.ui.basic_remark_label.setText("Good")
                elif row[67] >= 60 and row[67] < 70:
                    self.pri_report2.ui.basic_grade_label.setText("B")
                    self.pri_report2.ui.basic_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.basic_grade_label.setText("A")
                    self.pri_report2.ui.basic_remark_label.setText("Excellent")
                self.pri_report2.ui.french_c1_label.setText(str(row[68]))
                self.pri_report2.ui.french_c2_label.setText(str(row[69]))
                self.pri_report2.ui.french_ass_label.setText(str(row[70]))
                self.pri_report2.ui.french_exam_label.setText(str(row[71]))
                self.pri_report2.ui.french_total_label.setText(str(row[72]))
                if row[72] < 40:
                    self.pri_report2.ui.french_grade_label.setText("F")
                    self.pri_report2.ui.french_remark_label.setText("Fail")
                elif row[72] >= 40 and row[72] < 50:
                    self.pri_report2.ui.french_grade_label.setText("D")
                    self.pri_report2.ui.french_remark_label.setText("Pass")
                elif row[72] >= 50 and row[72] < 60:
                    self.pri_report2.ui.french_grade_label.setText("C")
                    self.pri_report2.ui.french_remark_label.setText("Good")
                elif row[72] >= 60 and row[72] < 70:
                    self.pri_report2.ui.french_grade_label.setText("B")
                    self.pri_report2.ui.french_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.french_grade_label.setText("A")
                    self.pri_report2.ui.french_remark_label.setText("Excellent")
                self.pri_report2.ui.jolly_c1_label.setText(str(row[73]))
                self.pri_report2.ui.jolly_c2_label.setText(str(row[74]))
                self.pri_report2.ui.jolly_ass_label.setText(str(row[75]))
                self.pri_report2.ui.jolly_exam_label.setText(str(row[76]))
                self.pri_report2.ui.jolly_total_label.setText(str(row[77]))
                if row[77] < 40:
                    self.pri_report2.ui.jolly_grade_label.setText("F")
                    self.pri_report2.ui.jolly_remark_label.setText("Fail")
                elif row[77] >= 40 and row[77] < 50:
                    self.pri_report2.ui.jolly_grade_label.setText("D")
                    self.pri_report2.ui.jolly_remark_label.setText("Pass")
                elif row[77] >= 50 and row[77] < 60:
                    self.pri_report2.ui.jolly_grade_label.setText("C")
                    self.pri_report2.ui.jolly_remark_label.setText("Good")
                elif row[77] >= 60 and row[77] < 70:
                    self.pri_report2.ui.jolly_grade_label.setText("B")
                    self.pri_report2.ui.jolly_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.jolly_grade_label.setText("A")
                    self.pri_report2.ui.jolly_remark_label.setText("Excellent")
                self.pri_report2.ui.total_scores2_label.setText(str(row[78]))
                self.pri_report2.ui.avg2_label.setText(str(row[79]))
                self.pri_report2.ui.total_cum_label.setText(str(row[80]))
                self.pri_report2.ui.avg_cum_label.setText(str(row[81]))
                if row[79] < 40:
                    self.pri_report2.ui.master_com_label.setText("Bad result. Be careful.")
                    self.pri_report2.ui.head_com_label.setText("Bad result.")
                elif row[79] >= 40 and row[79] < 50:
                    self.pri_report2.ui.master_com_label.setText("Weak result. Work hard.")
                    self.pri_report2.ui.head_com_label.setText("Weak result.")
                elif row[79] >= 50 and row[79] < 60:
                    self.pri_report2.ui.master_com_label.setText("Fair result. Work hard.")
                    self.pri_report2.ui.head_com_label.setText("Fair result.")
                elif row[79] >= 60 and row[79] < 70:
                    self.pri_report2.ui.master_com_label.setText("Good result. Put more effort.")
                    self.pri_report2.ui.head_com_label.setText("Good result.")
                else:
                    self.pri_report2.ui.master_com_label.setText("Excellent result. Keep on.")
                    self.pri_report2.ui.head_com_label.setText("Excellent result.")
                cmd9 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
                cur.execute(cmd9, (admission_no,))
                row = cur.fetchone()
                if row == None:
                    self.pri_report2.ui.total_scores_label.setText("None")
                    self.pri_report2.ui.avg_label.setText("None")
                elif row[78] == None and row[79] == None:
                    self.pri_report2.ui.total_scores_label.setText("None")
                    self.pri_report2.ui.avg_label.setText("None")
                else:
                    self.pri_report2.ui.total_scores_label.setText(str(row[78]))
                    self.pri_report2.ui.avg_label.setText(str(row[79]))
                cmd4 = "SELECT * FROM t_classes WHERE class_name = ?"
                cur.execute(cmd4, (classes_combo,))
                row = cur.fetchone()
                if row[2] == None:
                    self.pri_report2.ui.master_name_label.setText(str(row[1]))
                else:
                    self.pri_report2.ui.master_name_label.setText(str(row[1]))
                    pixmap = QPixmap()
                    pixmap.loadFromData(QByteArray.fromBase64(row[2]))
                    self.pri_report2.ui.master_sig_label.setPixmap(QPixmap(pixmap))
                cmd5 = "SELECT * FROM t_senior_users WHERE role = 'headmaster'"
                cur.execute(cmd5)
                row = cur.fetchone()
                self.pri_report2.ui.head_name_label.setText(row[1])
                pixmap = QPixmap()
                pixmap.loadFromData(QByteArray.fromBase64(row[5]))
                self.pri_report2.ui.head_sig_label.setPixmap(QPixmap(pixmap))
                cmd6 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd6)
                row = cur.fetchone()
                self.pri_report2.ui.next_term_label.setText(row[3])
                cmd7 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd7)
                row = cur.fetchone()
                self.pri_report2.ui.fees_label.setText(row[6])
                cmd8 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd8)
                row = cur.fetchone()
                self.pri_report2.ui.session_label.setText(row[2])
                if self.ui.att_a_radio.isChecked() == False and self.ui.att_b_radio.isChecked() == False and self.ui.att_c_radio.isChecked() == False and self.ui.att_d_radio.isChecked() == False and self.ui.att_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grade in attendance", QMessageBox.Ok)
                elif self.ui.con_a_radio.isChecked() == False and self.ui.con_b_radio.isChecked() == False and self.ui.con_c_radio.isChecked() == False and self.ui.con_d_radio.isChecked() == False and self.ui.con_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in conduct", QMessageBox.Ok)
                elif self.ui.neat_a_radio.isChecked() == False and self.ui.neat_b_radio.isChecked() == False and self.ui.neat_c_radio.isChecked() == False and self.ui.neat_d_radio.isChecked() == False and self.ui.neat_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in neatness", QMessageBox.Ok)
                else:
                    self.printReport2()
            except Error:
                QMessageBox.critical(self, "Generating Report", "ERROR: Please ensure all pupil's scores have been recorded in all subjects", QMessageBox.Ok)
            except TypeError:
                QMessageBox.critical(self, "Generating Report", "ERROR: Please ensure all pupil's scores have been recorded in all subjects", QMessageBox.Ok)

    def generatePriReportPDF(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox.currentText()
        admission_no = self.ui.stud_adm_no_comboBox.currentText()
        cmd1 = "SELECT * FROM t_studs WHERE admission_no = ?"
        cur.execute(cmd1, (admission_no,))
        row = cur.fetchone()
        if row == None:
            QMessageBox.critical(self, "Printing Report", "ERROR: Please select a class and pupil's admission number before generating report", QMessageBox.Ok)
        else:
            self.pri_report2.ui.name_label.setText(row[1])
            self.pri_report2.ui.class_label.setText(row[3])
            self.pri_report2.ui.sex_label.setText(row[5])
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray.fromBase64(row[6]))
            self.pri_report2.ui.photo_label.setPixmap(QPixmap(pixmap))
            try:
                cmd3 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
                cur.execute(cmd3, (admission_no,))
                row = cur.fetchone()
                self.pri_report2.ui.qur_c1_label.setText(str(row[3]))
                self.pri_report2.ui.qur_c2_label.setText(str(row[4]))
                self.pri_report2.ui.qur_ass_label.setText(str(row[5]))
                self.pri_report2.ui.qur_exam_label.setText(str(row[6]))
                self.pri_report2.ui.qur_total_label.setText(str(row[7]))
                if row[7] < 40:
                    self.pri_report2.ui.qur_grade_label.setText("F")
                    self.pri_report2.ui.qur_remark_label.setText("Fail")
                elif row[7] >= 40 and row[7] < 50:
                    self.pri_report2.ui.qur_grade_label.setText("D")
                    self.pri_report2.ui.qur_remark_label.setText("Pass")
                elif row[7] >= 50 and row[7] < 60:
                    self.pri_report2.ui.qur_grade_label.setText("C")
                    self.pri_report2.ui.qur_remark_label.setText("Good")
                elif row[7] >= 60 and row[7] < 70:
                    self.pri_report2.ui.qur_grade_label.setText("B")
                    self.pri_report2.ui.qur_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.qur_grade_label.setText("A")
                    self.pri_report2.ui.qur_remark_label.setText("Excellent")
                self.pri_report2.ui.ibadat_c1_label.setText(str(row[8]))
                self.pri_report2.ui.ibadat_c2_label.setText(str(row[9]))
                self.pri_report2.ui.ibadat_ass_label.setText(str(row[10]))
                self.pri_report2.ui.ibadat_exam_label.setText(str(row[11]))
                self.pri_report2.ui.ibadat_total_label.setText(str(row[12]))
                if row[12] < 40:
                    self.pri_report2.ui.ibadat_grade_label.setText("F")
                    self.pri_report2.ui.ibadat_remark_label.setText("Fail")
                elif row[12] >= 40 and row[12] < 50:
                    self.pri_report2.ui.ibadat_grade_label.setText("D")
                    self.pri_report2.ui.ibadat_remark_label.setText("Pass")
                elif row[12] >= 50 and row[12] < 60:
                    self.pri_report2.ui.ibadat_grade_label.setText("C")
                    self.pri_report2.ui.ibadat_remark_label.setText("Good")
                elif row[12] >= 60 and row[12] < 70:
                    self.pri_report2.ui.ibadat_grade_label.setText("B")
                    self.pri_report2.ui.ibadat_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.ibadat_grade_label.setText("A")
                    self.pri_report2.ui.ibadat_remark_label.setText("Excellent")
                self.pri_report2.ui.arabic1_c1_label.setText(str(row[13]))
                self.pri_report2.ui.arabic1_c2_label.setText(str(row[14]))
                self.pri_report2.ui.arabic1_ass_label.setText(str(row[15]))
                self.pri_report2.ui.arabic1_exam_label.setText(str(row[16]))
                self.pri_report2.ui.arabic1_total_label.setText(str(row[17]))
                if row[17] < 40:
                    self.pri_report2.ui.arabic1_grade_label.setText("F")
                    self.pri_report2.ui.arabic1_remark_label.setText("Fail")
                elif row[17] >= 40 and row[17] < 50:
                    self.pri_report2.ui.arabic1_grade_label.setText("D")
                    self.pri_report2.ui.arabic1_remark_label.setText("Pass")
                elif row[17] >= 50 and row[17] < 60:
                    self.pri_report2.ui.arabic1_grade_label.setText("C")
                    self.pri_report2.ui.arabic1_remark_label.setText("Good")
                elif row[17] >= 60 and row[17] < 70:
                    self.pri_report2.ui.arabic1_grade_label.setText("B")
                    self.pri_report2.ui.arabic1_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.arabic1_grade_label.setText("A")
                    self.pri_report2.ui.arabic1_remark_label.setText("Excellent")
                self.pri_report2.ui.arabic2_c1_label.setText(str(row[18]))
                self.pri_report2.ui.arabic2_c2_label.setText(str(row[19]))
                self.pri_report2.ui.arabic2_ass_label.setText(str(row[20]))
                self.pri_report2.ui.arabic2_exam_label.setText(str(row[21]))
                self.pri_report2.ui.arabic2_total_label.setText(str(row[22]))
                if row[22] < 40:
                    self.pri_report2.ui.arabic2_grade_label.setText("F")
                    self.pri_report2.ui.arabic2_remark_label.setText("Fail")
                elif row[22] >= 40 and row[22] < 50:
                    self.pri_report2.ui.arabic2_grade_label.setText("D")
                    self.pri_report2.ui.arabic2_remark_label.setText("Pass")
                elif row[22] >= 50 and row[22] < 60:
                    self.pri_report2.ui.arabic2_grade_label.setText("C")
                    self.pri_report2.ui.arabic2_remark_label.setText("Good")
                elif row[22] >= 60 and row[22] < 70:
                    self.pri_report2.ui.arabic2_grade_label.setText("B")
                    self.pri_report2.ui.arabic2_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.arabic2_grade_label.setText("A")
                    self.pri_report2.ui.arabic2_remark_label.setText("Excellent")
                self.pri_report2.ui.math_c1_label.setText(str(row[23]))
                self.pri_report2.ui.math_c2_label.setText(str(row[24]))
                self.pri_report2.ui.math_ass_label.setText(str(row[25]))
                self.pri_report2.ui.math_exam_label.setText(str(row[26]))
                self.pri_report2.ui.math_total_label.setText(str(row[27]))
                if row[27] < 40:
                    self.pri_report2.ui.math_grade_label.setText("F")
                    self.pri_report2.ui.math_remark_label.setText("Fail")
                elif row[27] >= 40 and row[27] < 50:
                    self.pri_report2.ui.math_grade_label.setText("D")
                    self.pri_report2.ui.math_remark_label.setText("Pass")
                elif row[27] >= 50 and row[27] < 60:
                    self.pri_report2.ui.math_grade_label.setText("C")
                    self.pri_report2.ui.math_remark_label.setText("Good")
                elif row[27] >= 60 and row[27] < 70:
                    self.pri_report2.ui.math_grade_label.setText("B")
                    self.pri_report2.ui.math_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.math_grade_label.setText("A")
                    self.pri_report2.ui.math_remark_label.setText("Excellent")
                self.pri_report2.ui.eng_c1_label.setText(str(row[28]))
                self.pri_report2.ui.eng_c2_label.setText(str(row[29]))
                self.pri_report2.ui.eng_ass_label.setText(str(row[30]))
                self.pri_report2.ui.eng_exam_label.setText(str(row[31]))
                self.pri_report2.ui.eng_total_label.setText(str(row[32]))
                if row[32] < 40:
                    self.pri_report2.ui.eng_grade_label.setText("F")
                    self.pri_report2.ui.eng_remark_label.setText("Fail")
                elif row[32] >= 40 and row[32] < 50:
                    self.pri_report2.ui.eng_grade_label.setText("D")
                    self.pri_report2.ui.eng_remark_label.setText("Pass")
                elif row[32] >= 50 and row[32] < 60:
                    self.pri_report2.ui.eng_grade_label.setText("C")
                    self.pri_report2.ui.eng_remark_label.setText("Good")
                elif row[32] >= 60 and row[32] < 70:
                    self.pri_report2.ui.eng_grade_label.setText("B")
                    self.pri_report2.ui.eng_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.eng_grade_label.setText("A")
                    self.pri_report2.ui.eng_remark_label.setText("Excellent")
                self.pri_report2.ui.comp_c1_label.setText(str(row[33]))
                self.pri_report2.ui.comp_c2_label.setText(str(row[34]))
                self.pri_report2.ui.comp_ass_label.setText(str(row[35]))
                self.pri_report2.ui.comp_exam_label.setText(str(row[36]))
                self.pri_report2.ui.comp_total_label.setText(str(row[37]))
                if row[37] < 40:
                    self.pri_report2.ui.comp_grade_label.setText("F")
                    self.pri_report2.ui.comp_remark_label.setText("Fail")
                elif row[37] >= 40 and row[37] < 50:
                    self.pri_report2.ui.comp_grade_label.setText("D")
                    self.pri_report2.ui.comp_remark_label.setText("Pass")
                elif row[37] >= 50 and row[37] < 60:
                    self.pri_report2.ui.comp_grade_label.setText("C")
                    self.pri_report2.ui.comp_remark_label.setText("Good")
                elif row[37] >= 60 and row[37] < 70:
                    self.pri_report2.ui.comp_grade_label.setText("B")
                    self.pri_report2.ui.comp_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.comp_grade_label.setText("A")
                    self.pri_report2.ui.comp_remark_label.setText("Excellent")
                self.pri_report2.ui.bas_sc_c1_label.setText(str(row[38]))
                self.pri_report2.ui.bas_sc_c2_label.setText(str(row[39]))
                self.pri_report2.ui.bas_sc_ass_label.setText(str(row[40]))
                self.pri_report2.ui.bas_sc_exam_label.setText(str(row[41]))
                self.pri_report2.ui.bas_sc_total_label.setText(str(row[42]))
                if row[42] < 40:
                    self.pri_report2.ui.bas_sc_grade_label.setText("F")
                    self.pri_report2.ui.bas_sc_remark_label.setText("Fail")
                elif row[42] >= 40 and row[42] < 50:
                    self.pri_report2.ui.bas_sc_grade_label.setText("D")
                    self.pri_report2.ui.bas_sc_remark_label.setText("Pass")
                elif row[42] >= 50 and row[42] < 60:
                    self.pri_report2.ui.bas_sc_grade_label.setText("C")
                    self.pri_report2.ui.bas_sc_remark_label.setText("Good")
                elif row[42] >= 60 and row[42] < 70:
                    self.pri_report2.ui.bas_sc_grade_label.setText("B")
                    self.pri_report2.ui.bas_sc_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.bas_sc_grade_label.setText("A")
                    self.pri_report2.ui.bas_sc_remark_label.setText("Excellent")
                self.pri_report2.ui.religion_c1_label.setText(str(row[43]))
                self.pri_report2.ui.religion_c2_label.setText(str(row[44]))
                self.pri_report2.ui.religion_ass_label.setText(str(row[45]))
                self.pri_report2.ui.religion_exam_label.setText(str(row[46]))
                self.pri_report2.ui.religion_total_label.setText(str(row[47]))
                if row[47] < 40:
                    self.pri_report2.ui.religion_grade_label.setText("F")
                    self.pri_report2.ui.religion_remark_label.setText("Fail")
                elif row[47] >= 40 and row[47] < 50:
                    self.pri_report2.ui.religion_grade_label.setText("D")
                    self.pri_report2.ui.religion_remark_label.setText("Pass")
                elif row[47] >= 50 and row[47] < 60:
                    self.pri_report2.ui.religion_grade_label.setText("C")
                    self.pri_report2.ui.religion_remark_label.setText("Good")
                elif row[47] >= 60 and row[47] < 70:
                    self.pri_report2.ui.religion_grade_label.setText("B")
                    self.pri_report2.ui.religion_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.religion_grade_label.setText("A")
                    self.pri_report2.ui.religion_remark_label.setText("Excellent")
                self.pri_report2.ui.civic_c1_label.setText(str(row[48]))
                self.pri_report2.ui.civic_c2_label.setText(str(row[49]))
                self.pri_report2.ui.civic_ass_label.setText(str(row[50]))
                self.pri_report2.ui.civic_exam_label.setText(str(row[51]))
                self.pri_report2.ui.civic_total_label.setText(str(row[52]))
                if row[52] < 40:
                    self.pri_report2.ui.civic_grade_label.setText("F")
                    self.pri_report2.ui.civic_remark_label.setText("Fail")
                elif row[52] >= 40 and row[52] < 50:
                    self.pri_report2.ui.civic_grade_label.setText("D")
                    self.pri_report2.ui.civic_remark_label.setText("Pass")
                elif row[52] >= 50 and row[52] < 60:
                    self.pri_report2.ui.civic_grade_label.setText("C")
                    self.pri_report2.ui.civic_remark_label.setText("Good")
                elif row[52] >= 60 and row[52] < 70:
                    self.pri_report2.ui.civic_grade_label.setText("B")
                    self.pri_report2.ui.civic_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.civic_grade_label.setText("A")
                    self.pri_report2.ui.civic_remark_label.setText("Excellent")
                self.pri_report2.ui.verbal_c1_label.setText(str(row[53]))
                self.pri_report2.ui.verbal_c2_label.setText(str(row[54]))
                self.pri_report2.ui.verbal_ass_label.setText(str(row[55]))
                self.pri_report2.ui.verbal_exam_label.setText(str(row[56]))
                self.pri_report2.ui.verbal_total_label.setText(str(row[57]))
                if row[57] < 40:
                    self.pri_report2.ui.verbal_grade_label.setText("F")
                    self.pri_report2.ui.verbal_remark_label.setText("Fail")
                elif row[57] >= 40 and row[57] < 50:
                    self.pri_report2.ui.verbal_grade_label.setText("D")
                    self.pri_report2.ui.verbal_remark_label.setText("Pass")
                elif row[57] >= 50 and row[57] < 60:
                    self.pri_report2.ui.verbal_grade_label.setText("C")
                    self.pri_report2.ui.verbal_remark_label.setText("Good")
                elif row[57] >= 60 and row[57] < 70:
                    self.pri_report2.ui.verbal_grade_label.setText("B")
                    self.pri_report2.ui.verbal_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.verbal_grade_label.setText("A")
                    self.pri_report2.ui.verbal_remark_label.setText("Excellent")
                self.pri_report2.ui.quant_c1_label.setText(str(row[58]))
                self.pri_report2.ui.quant_c2_label.setText(str(row[59]))
                self.pri_report2.ui.quant_ass_label.setText(str(row[60]))
                self.pri_report2.ui.quant_exam_label.setText(str(row[61]))
                self.pri_report2.ui.quant_total_label.setText(str(row[62]))
                if row[62] < 40:
                    self.pri_report2.ui.quant_grade_label.setText("F")
                    self.pri_report2.ui.quant_remark_label.setText("Fail")
                elif row[62] >= 40 and row[62] < 50:
                    self.pri_report2.ui.quant_grade_label.setText("D")
                    self.pri_report2.ui.quant_remark_label.setText("Pass")
                elif row[62] >= 50 and row[62] < 60:
                    self.pri_report2.ui.quant_grade_label.setText("C")
                    self.pri_report2.ui.quant_remark_label.setText("Good")
                elif row[62] >= 60 and row[62] < 70:
                    self.pri_report2.ui.quant_grade_label.setText("B")
                    self.pri_report2.ui.quant_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.quant_grade_label.setText("A")
                    self.pri_report2.ui.quant_remark_label.setText("Excellent")
                self.pri_report2.ui.basic_c1_label.setText(str(row[63]))
                self.pri_report2.ui.basic_c2_label.setText(str(row[64]))
                self.pri_report2.ui.basic_ass_label.setText(str(row[65]))
                self.pri_report2.ui.basic_exam_label.setText(str(row[66]))
                self.pri_report2.ui.basic_total_label.setText(str(row[67]))
                if row[67] < 40:
                    self.pri_report2.ui.basic_grade_label.setText("F")
                    self.pri_report2.ui.basic_remark_label.setText("Fail")
                elif row[67] >= 40 and row[67] < 50:
                    self.pri_report2.ui.basic_grade_label.setText("D")
                    self.pri_report2.ui.basic_remark_label.setText("Pass")
                elif row[67] >= 50 and row[67] < 60:
                    self.pri_report2.ui.basic_grade_label.setText("C")
                    self.pri_report2.ui.basic_remark_label.setText("Good")
                elif row[67] >= 60 and row[67] < 70:
                    self.pri_report2.ui.basic_grade_label.setText("B")
                    self.pri_report2.ui.basic_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.basic_grade_label.setText("A")
                    self.pri_report2.ui.basic_remark_label.setText("Excellent")
                self.pri_report2.ui.french_c1_label.setText(str(row[68]))
                self.pri_report2.ui.french_c2_label.setText(str(row[69]))
                self.pri_report2.ui.french_ass_label.setText(str(row[70]))
                self.pri_report2.ui.french_exam_label.setText(str(row[71]))
                self.pri_report2.ui.french_total_label.setText(str(row[72]))
                if row[72] < 40:
                    self.pri_report2.ui.french_grade_label.setText("F")
                    self.pri_report2.ui.french_remark_label.setText("Fail")
                elif row[72] >= 40 and row[72] < 50:
                    self.pri_report2.ui.french_grade_label.setText("D")
                    self.pri_report2.ui.french_remark_label.setText("Pass")
                elif row[72] >= 50 and row[72] < 60:
                    self.pri_report2.ui.french_grade_label.setText("C")
                    self.pri_report2.ui.french_remark_label.setText("Good")
                elif row[72] >= 60 and row[72] < 70:
                    self.pri_report2.ui.french_grade_label.setText("B")
                    self.pri_report2.ui.french_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.french_grade_label.setText("A")
                    self.pri_report2.ui.french_remark_label.setText("Excellent")
                self.pri_report2.ui.jolly_c1_label.setText(str(row[73]))
                self.pri_report2.ui.jolly_c2_label.setText(str(row[74]))
                self.pri_report2.ui.jolly_ass_label.setText(str(row[75]))
                self.pri_report2.ui.jolly_exam_label.setText(str(row[76]))
                self.pri_report2.ui.jolly_total_label.setText(str(row[77]))
                if row[77] < 40:
                    self.pri_report2.ui.jolly_grade_label.setText("F")
                    self.pri_report2.ui.jolly_remark_label.setText("Fail")
                elif row[77] >= 40 and row[77] < 50:
                    self.pri_report2.ui.jolly_grade_label.setText("D")
                    self.pri_report2.ui.jolly_remark_label.setText("Pass")
                elif row[77] >= 50 and row[77] < 60:
                    self.pri_report2.ui.jolly_grade_label.setText("C")
                    self.pri_report2.ui.jolly_remark_label.setText("Good")
                elif row[77] >= 60 and row[77] < 70:
                    self.pri_report2.ui.jolly_grade_label.setText("B")
                    self.pri_report2.ui.jolly_remark_label.setText("Very Good")
                else:
                    self.pri_report2.ui.jolly_grade_label.setText("A")
                    self.pri_report2.ui.jolly_remark_label.setText("Excellent")
                self.pri_report2.ui.total_scores2_label.setText(str(row[78]))
                self.pri_report2.ui.avg2_label.setText(str(row[79]))
                self.pri_report2.ui.total_cum_label.setText(str(row[80]))
                self.pri_report2.ui.avg_cum_label.setText(str(row[81]))
                if row[79] < 40:
                    self.pri_report2.ui.master_com_label.setText("Bad result. Be careful.")
                    self.pri_report2.ui.head_com_label.setText("Bad result.")
                elif row[79] >= 40 and row[79] < 50:
                    self.pri_report2.ui.master_com_label.setText("Weak result. Work hard.")
                    self.pri_report2.ui.head_com_label.setText("Weak result.")
                elif row[79] >= 50 and row[79] < 60:
                    self.pri_report2.ui.master_com_label.setText("Fair result. Work hard.")
                    self.pri_report2.ui.head_com_label.setText("Fair result.")
                elif row[79] >= 60 and row[79] < 70:
                    self.pri_report2.ui.master_com_label.setText("Good result. Put more effort.")
                    self.pri_report2.ui.head_com_label.setText("Good result.")
                else:
                    self.pri_report2.ui.master_com_label.setText("Excellent result. Keep on.")
                    self.pri_report2.ui.head_com_label.setText("Excellent result.")
                cmd9 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
                cur.execute(cmd9, (admission_no,))
                row = cur.fetchone()
                if row == None:
                    self.pri_report2.ui.total_scores_label.setText("None")
                    self.pri_report2.ui.avg_label.setText("None")
                elif row[78] == None and row[79] == None:
                    self.pri_report2.ui.total_scores_label.setText("None")
                    self.pri_report2.ui.avg_label.setText("None")
                else:
                    self.pri_report2.ui.total_scores_label.setText(str(row[78]))
                    self.pri_report2.ui.avg_label.setText(str(row[79]))

                cmd4 = "SELECT * FROM t_classes WHERE class_name = ?"
                cur.execute(cmd4, (classes_combo,))
                row = cur.fetchone()
                if row[2] == None:
                    self.pri_report2.ui.master_name_label.setText(str(row[1]))
                else:
                    self.pri_report2.ui.master_name_label.setText(str(row[1]))
                    pixmap = QPixmap()
                    pixmap.loadFromData(QByteArray.fromBase64(row[2]))
                    self.pri_report2.ui.master_sig_label.setPixmap(QPixmap(pixmap))
                cmd5 = "SELECT * FROM t_senior_users WHERE role = 'headmaster'"
                cur.execute(cmd5)
                row = cur.fetchone()
                self.pri_report2.ui.head_name_label.setText(row[1])
                pixmap = QPixmap()
                pixmap.loadFromData(QByteArray.fromBase64(row[5]))
                self.pri_report2.ui.head_sig_label.setPixmap(QPixmap(pixmap))

                cmd6 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd6)
                row = cur.fetchone()
                self.pri_report2.ui.next_term_label.setText(row[3])
                cmd7 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd7)
                row = cur.fetchone()
                self.pri_report2.ui.fees_label.setText(row[6])
                cmd8 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd8)
                row = cur.fetchone()
                self.pri_report2.ui.session_label.setText(row[2])
                if self.ui.att_a_radio.isChecked() == False and self.ui.att_b_radio.isChecked() == False and self.ui.att_c_radio.isChecked() == False and self.ui.att_d_radio.isChecked() == False and self.ui.att_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grade in attendance", QMessageBox.Ok)
                elif self.ui.con_a_radio.isChecked() == False and self.ui.con_b_radio.isChecked() == False and self.ui.con_c_radio.isChecked() == False and self.ui.con_d_radio.isChecked() == False and self.ui.con_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in conduct", QMessageBox.Ok)
                elif self.ui.neat_a_radio.isChecked() == False and self.ui.neat_b_radio.isChecked() == False and self.ui.neat_c_radio.isChecked() == False and self.ui.neat_d_radio.isChecked() == False and self.ui.neat_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in neatness", QMessageBox.Ok)
                else:
                    self.printPDF2()
            except Error:
                QMessageBox.critical(self, "Generating Report", "ERROR: Please ensure all pupil's scores have been recorded in all subjects", QMessageBox.Ok)
            except TypeError:
                QMessageBox.critical(self, "Generating Report", "ERROR: Please ensure all pupil's scores have been recorded in all subjects", QMessageBox.Ok)

    def displayRadios(self):
        if self.ui.att_a_radio.isChecked():
            self.pri_report2.ui.att_a_label.setText("v")
            self.pri_report2.ui.att_b_label.setText("")
            self.pri_report2.ui.att_c_label.setText("")
            self.pri_report2.ui.att_d_label.setText("")
            self.pri_report2.ui.att_e_label.setText("")
        elif self.ui.att_b_radio.isChecked():
            self.pri_report2.ui.att_a_label.setText("")
            self.pri_report2.ui.att_b_label.setText("v")
            self.pri_report2.ui.att_c_label.setText("")
            self.pri_report2.ui.att_d_label.setText("")
            self.pri_report2.ui.att_e_label.setText("")
        elif self.ui.att_c_radio.isChecked():
            self.pri_report2.ui.att_a_label.setText("")
            self.pri_report2.ui.att_b_label.setText("")
            self.pri_report2.ui.att_c_label.setText("v")
            self.pri_report2.ui.att_d_label.setText("")
            self.pri_report2.ui.att_e_label.setText("")
        elif self.ui.att_d_radio.isChecked():
            self.pri_report2.ui.att_a_label.setText("")
            self.pri_report2.ui.att_b_label.setText("")
            self.pri_report2.ui.att_c_label.setText("")
            self.pri_report2.ui.att_d_label.setText("v")
            self.pri_report2.ui.att_e_label.setText("")
        elif self.ui.att_e_radio.isChecked():
            self.pri_report2.ui.att_a_label.setText("")
            self.pri_report2.ui.att_b_label.setText("")
            self.pri_report2.ui.att_c_label.setText("")
            self.pri_report2.ui.att_d_label.setText("")
            self.pri_report2.ui.att_e_label.setText("v")
        if self.ui.con_a_radio.isChecked():
            self.pri_report2.ui.con_a_label.setText("v")
            self.pri_report2.ui.con_b_label.setText("")
            self.pri_report2.ui.con_c_label.setText("")
            self.pri_report2.ui.con_d_label.setText("")
            self.pri_report2.ui.con_e_label.setText("")
        elif self.ui.con_b_radio.isChecked():
            self.pri_report2.ui.con_a_label.setText("")
            self.pri_report2.ui.con_b_label.setText("v")
            self.pri_report2.ui.con_c_label.setText("")
            self.pri_report2.ui.con_d_label.setText("")
            self.pri_report2.ui.con_e_label.setText("")
        elif self.ui.con_c_radio.isChecked():
            self.pri_report2.ui.con_a_label.setText("")
            self.pri_report2.ui.con_b_label.setText("")
            self.pri_report2.ui.con_c_label.setText("v")
            self.pri_report2.ui.con_d_label.setText("")
            self.pri_report2.ui.con_e_label.setText("")
        elif self.ui.con_d_radio.isChecked():
            self.pri_report2.ui.con_a_label.setText("")
            self.pri_report2.ui.con_b_label.setText("")
            self.pri_report2.ui.con_c_label.setText("")
            self.pri_report2.ui.con_d_label.setText("v")
            self.pri_report2.ui.con_e_label.setText("")
        elif self.ui.con_e_radio.isChecked():
            self.pri_report2.ui.con_a_label.setText("")
            self.pri_report2.ui.con_b_label.setText("")
            self.pri_report2.ui.con_c_label.setText("")
            self.pri_report2.ui.con_d_label.setText("")
            self.pri_report2.ui.con_e_label.setText("v")
        if self.ui.neat_a_radio.isChecked():
            self.pri_report2.ui.neat_a_label.setText("v")
            self.pri_report2.ui.neat_b_label.setText("")
            self.pri_report2.ui.neat_c_label.setText("")
            self.pri_report2.ui.neat_d_label.setText("")
            self.pri_report2.ui.neat_e_label.setText("")
        elif self.ui.neat_b_radio.isChecked():
            self.pri_report2.ui.neat_a_label.setText("")
            self.pri_report2.ui.neat_b_label.setText("v")
            self.pri_report2.ui.neat_c_label.setText("")
            self.pri_report2.ui.neat_d_label.setText("")
            self.pri_report2.ui.neat_e_label.setText("")
        elif self.ui.neat_b_radio.isChecked():
            self.pri_report2.ui.neat_a_label.setText("")
            self.pri_report2.ui.neat_b_label.setText("v")
            self.pri_report2.ui.neat_c_label.setText("")
            self.pri_report2.ui.neat_d_label.setText("")
            self.pri_report2.ui.neat_e_label.setText("")
        elif self.ui.neat_c_radio.isChecked():
            self.pri_report2.ui.neat_a_label.setText("")
            self.pri_report2.ui.neat_b_label.setText("")
            self.pri_report2.ui.neat_c_label.setText("v")
            self.pri_report2.ui.neat_d_label.setText("")
            self.pri_report2.ui.neat_e_label.setText("")
        elif self.ui.neat_d_radio.isChecked():
            self.pri_report2.ui.neat_a_label.setText("")
            self.pri_report2.ui.neat_b_label.setText("")
            self.pri_report2.ui.neat_c_label.setText("")
            self.pri_report2.ui.neat_d_label.setText("v")
            self.pri_report2.ui.neat_e_label.setText("")
        elif self.ui.neat_e_radio.isChecked():
            self.pri_report2.ui.neat_a_label.setText("")
            self.pri_report2.ui.neat_b_label.setText("")
            self.pri_report2.ui.neat_c_label.setText("")
            self.pri_report2.ui.neat_d_label.setText("")
            self.pri_report2.ui.neat_e_label.setText("v")

    def printReport2(self):
        printer = QPrinter(QtPrintSupport.QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            painter = QPainter()
            painter.begin(printer)
            xscale = printer.pageRect().width() * 1.0 / self.pri_report2.width()
            yscale = printer.pageRect().height() * 1.0 / self.pri_report2.height()
            scale = min(xscale, yscale)
            painter.translate(printer.paperRect().center())
            painter.scale(scale, scale)
            painter.translate(-self.pri_report2.width() / 2, -self.pri_report2.height() / 2)
            self.pri_report2.render(painter)
            painter.end()

    def print_widget(self, widget, filename):
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        printer.setOutputFileName(filename)
        painter = QtGui.QPainter(printer)
        xscale = printer.pageRect().width() * 1.0 / widget.width()
        yscale = printer.pageRect().height() * 1.0 / widget.height()
        scale = min(xscale, yscale)
        painter.translate(printer.paperRect().center())
        painter.scale(scale, scale)
        painter.translate(-widget.width() / 2, -widget.height() / 2)
        widget.render(painter)
        painter.end()

    def printPDF2(self):
        fn, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Export PDF", None, "PDF files (.pdf);;All Files()"
        )
        if fn:
            if QtCore.QFileInfo(fn).suffix() == "":
                fn += ".pdf"
            self.print_widget(self.pri_report2, fn)


class PriReport2(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PriReport2ndForm()
        self.ui.setupUi(self)
        #Generates Current Date
        self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.ui.dateTimeEdit.hide()
        self.ui.print_date_label.setText(self.ui.dateTimeEdit.text())


class PriScoresRecord3(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_PriScoreRec3rdForm()
        self.ui.setupUi(self)
        self.displayClasses()

        self.ui.class_comboBox.currentTextChanged.connect(self.displayStuds)
        self.ui.stud_adm_no_comboBox.currentTextChanged.connect(self.displayName)
        self.ui.stud_adm_no_comboBox.currentTextChanged.connect(self.displaySpinVals)
        self.ui.qur_score_btn.clicked.connect(self.saveQurScores)
        self.ui.qur_score_btn.clicked.connect(self.saveIbadatScores)
        self.ui.qur_score_btn.clicked.connect(self.saveArabic1Scores)
        self.ui.qur_score_btn.clicked.connect(self.saveArabic2Scores)
        self.ui.qur_score_btn.clicked.connect(self.saveMathScores)
        self.ui.qur_score_btn.clicked.connect(self.saveEnglishScores)
        self.ui.qur_score_btn.clicked.connect(self.saveCompScores)
        self.ui.qur_score_btn.clicked.connect(self.saveBasScScores)
        self.ui.qur_score_btn.clicked.connect(self.saveReligionScores)
        self.ui.qur_score_btn.clicked.connect(self.saveCivicScores)
        self.ui.qur_score_btn.clicked.connect(self.saveVerbalScores)
        self.ui.qur_score_btn.clicked.connect(self.saveQuantScores)
        self.ui.qur_score_btn.clicked.connect(self.saveHandwiritingScores)
        self.ui.qur_score_btn.clicked.connect(self.saveFrenchScores)
        self.ui.qur_score_btn.clicked.connect(self.saveJollyScores)
        self.ui.qur_score_btn.clicked.connect(self.computeTotAvg)

    def displayClasses(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        query = cur.execute('SELECT * FROM t_classes ORDER BY class_name')
        rows = cur.fetchall()
        classes = ["Select a class"]
        self.ui.class_comboBox.clear()
        for row in rows:
            classes.append(row[0])
        self.ui.class_comboBox.addItems(classes)
        con.commit()
        con.close()

    def displayStuds(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox.currentText()
        cmd = "SELECT * FROM t_studs WHERE stud_class = ? ORDER BY admission_no"
        cur.execute(cmd, (classes_combo,))
        rows = cur.fetchall()
        adm_nos = ["Select a pupil"]
        self.ui.stud_adm_no_comboBox.clear()
        for row in rows:
            adm_nos.append(row[0])
        self.ui.stud_adm_no_comboBox.addItems(adm_nos)
        con.close()

    def displayName(self):
        self.ui.name_label.setText("")
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no_combo = self.ui.stud_adm_no_comboBox.currentText()
        cmd = "SELECT * FROM t_studs WHERE admission_no = ?"
        cur.execute(cmd, (stud_no_combo,))
        row = cur.fetchone()
        if row == None:
            self.ui.name_label.setText("")
        else:
            self.ui.name_label.setText("Name: " + row[1])

    def displaySpinVals(self):
        self.ui.qur_c1_spin.setValue(0)
        self.ui.qur_c2_spin.setValue(0)
        self.ui.qur_ass_spin.setValue(0)
        self.ui.qur_exam_spin.setValue(0)
        self.ui.ibadat_c1_spin.setValue(0)
        self.ui.ibadat_c2_spin.setValue(0)
        self.ui.ibadat_ass_spin.setValue(0)
        self.ui.ibadat_exam_spin.setValue(0)
        self.ui.arabic1_c1_spin.setValue(0)
        self.ui.arabic1_c2_spin.setValue(0)
        self.ui.arabic1_ass_spin.setValue(0)
        self.ui.arabic1_exam_spin.setValue(0)
        self.ui.arabic2_c1_spin.setValue(0)
        self.ui.arabic2_c2_spin.setValue(0)
        self.ui.arabic2_ass_spin.setValue(0)
        self.ui.arabic2_exam_spin.setValue(0)
        self.ui.math_c1_spin.setValue(0)
        self.ui.math_c2_spin.setValue(0)
        self.ui.math_ass_spin.setValue(0)
        self.ui.math_exam_spin.setValue(0)
        self.ui.eng_c1_spin.setValue(0)
        self.ui.eng_c2_spin.setValue(0)
        self.ui.eng_ass_spin.setValue(0)
        self.ui.eng_exam_spin.setValue(0)
        self.ui.comp_c1_spin.setValue(0)
        self.ui.comp_c2_spin.setValue(0)
        self.ui.comp_ass_spin.setValue(0)
        self.ui.comp_exam_spin.setValue(0)
        self.ui.bas_sc_c1_spin.setValue(0)
        self.ui.bas_sc_c2_spin.setValue(0)
        self.ui.bas_sc_ass_spin.setValue(0)
        self.ui.bas_sc_exam_spin.setValue(0)
        self.ui.religion_c1_spin.setValue(0)
        self.ui.religion_c2_spin.setValue(0)
        self.ui.religion_ass_spin.setValue(0)
        self.ui.religion_exam_spin.setValue(0)
        self.ui.civic_c1_spin.setValue(0)
        self.ui.civic_c2_spin.setValue(0)
        self.ui.civic_ass_spin.setValue(0)
        self.ui.civic_exam_spin.setValue(0)
        self.ui.verbal_c1_spin.setValue(0)
        self.ui.verbal_c2_spin.setValue(0)
        self.ui.verbal_ass_spin.setValue(0)
        self.ui.verbal_exam_spin.setValue(0)
        self.ui.quant_c1_spin.setValue(0)
        self.ui.quant_c2_spin.setValue(0)
        self.ui.quant_ass_spin.setValue(0)
        self.ui.quant_exam_spin.setValue(0)
        self.ui.basic_c1_spin.setValue(0)
        self.ui.basic_c2_spin.setValue(0)
        self.ui.basic_ass_spin.setValue(0)
        self.ui.basic_exam_spin.setValue(0)
        self.ui.french_c1_spin.setValue(0)
        self.ui.french_c2_spin.setValue(0)
        self.ui.french_ass_spin.setValue(0)
        self.ui.french_exam_spin.setValue(0)
        self.ui.jolly_c1_spin.setValue(0)
        self.ui.jolly_c2_spin.setValue(0)
        self.ui.jolly_ass_spin.setValue(0)
        self.ui.jolly_exam_spin.setValue(0)

        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        try:
            cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row != None and row[3] != None and row[4] != None and row[5] != None and row[6] != None:
                self.ui.qur_c1_spin.setValue(row[3])
                self.ui.qur_c2_spin.setValue(row[4])
                self.ui.qur_ass_spin.setValue(row[5])
                self.ui.qur_exam_spin.setValue(row[6])
            if row != None and row[8] != None and row[9] != None and row[10] != None and row[11] != None:
                self.ui.ibadat_c1_spin.setValue(row[8])
                self.ui.ibadat_c2_spin.setValue(row[9])
                self.ui.ibadat_ass_spin.setValue(row[10])
                self.ui.ibadat_exam_spin.setValue(row[11])
            if row != None and row[13] != None and row[14] != None and row[15] != None and row[16] != None:
                self.ui.arabic1_c1_spin.setValue(row[13])
                self.ui.arabic1_c2_spin.setValue(row[14])
                self.ui.arabic1_ass_spin.setValue(row[15])
                self.ui.arabic1_exam_spin.setValue(row[16])
            if row != None and row[18] != None and row[19] != None and row[20] != None and row[21] != None:
                self.ui.arabic2_c1_spin.setValue(row[18])
                self.ui.arabic2_c2_spin.setValue(row[19])
                self.ui.arabic2_ass_spin.setValue(row[20])
                self.ui.arabic2_exam_spin.setValue(row[21])
            if row != None and row[23] != None and row[24] != None and row[25] != None and row[26] != None:
                self.ui.math_c1_spin.setValue(row[23])
                self.ui.math_c2_spin.setValue(row[24])
                self.ui.math_ass_spin.setValue(row[25])
                self.ui.math_exam_spin.setValue(row[26])
            if row != None and row[28] != None and row[29] != None and row[30] != None and row[31] != None:
                self.ui.eng_c1_spin.setValue(row[28])
                self.ui.eng_c2_spin.setValue(row[29])
                self.ui.eng_ass_spin.setValue(row[30])
                self.ui.eng_exam_spin.setValue(row[31])
            if row != None and row[33] != None and row[34] != None and row[35] != None and row[36] != None:
                self.ui.comp_c1_spin.setValue(row[33])
                self.ui.comp_c2_spin.setValue(row[34])
                self.ui.comp_ass_spin.setValue(row[35])
                self.ui.comp_exam_spin.setValue(row[36])
            if row != None and row[38] != None and row[39] != None and row[40] != None and row[41] != None:
                self.ui.bas_sc_c1_spin.setValue(row[38])
                self.ui.bas_sc_c2_spin.setValue(row[39])
                self.ui.bas_sc_ass_spin.setValue(row[40])
                self.ui.bas_sc_exam_spin.setValue(row[41])
            if row != None and row[43] != None and row[44] != None and row[45] != None and row[46] != None:
                self.ui.religion_c1_spin.setValue(row[43])
                self.ui.religion_c2_spin.setValue(row[44])
                self.ui.religion_ass_spin.setValue(row[45])
                self.ui.religion_exam_spin.setValue(row[46])
            if row != None and row[48] != None and row[49] != None and row[50] != None and row[51] != None:
                self.ui.civic_c1_spin.setValue(row[48])
                self.ui.civic_c2_spin.setValue(row[49])
                self.ui.civic_ass_spin.setValue(row[50])
                self.ui.civic_exam_spin.setValue(row[51])
            if row != None and row[53] != None and row[54] != None and row[55] != None and row[56] != None:
                self.ui.verbal_c1_spin.setValue(row[53])
                self.ui.verbal_c2_spin.setValue(row[54])
                self.ui.verbal_ass_spin.setValue(row[55])
                self.ui.verbal_exam_spin.setValue(row[56])
            if row != None and row[58] != None and row[59] != None and row[60] != None and row[61] != None:
                self.ui.quant_c1_spin.setValue(row[58])
                self.ui.quant_c2_spin.setValue(row[59])
                self.ui.quant_ass_spin.setValue(row[60])
                self.ui.quant_exam_spin.setValue(row[61])
            if row != None and row[63] != None and row[64] != None and row[65] != None and row[66] != None:
                self.ui.basic_c1_spin.setValue(row[63])
                self.ui.basic_c2_spin.setValue(row[64])
                self.ui.basic_ass_spin.setValue(row[65])
                self.ui.basic_exam_spin.setValue(row[66])
            if row != None and row[68] != None and row[69] != None and row[70] != None and row[71] != None:
                self.ui.french_c1_spin.setValue(row[68])
                self.ui.french_c2_spin.setValue(row[69])
                self.ui.french_ass_spin.setValue(row[70])
                self.ui.french_exam_spin.setValue(row[71])
            if row != None and row[73] != None and row[74] != None and row[75] != None and row[76] != None:
                self.ui.jolly_c1_spin.setValue(row[73])
                self.ui.jolly_c2_spin.setValue(row[74])
                self.ui.jolly_ass_spin.setValue(row[75])
                self.ui.jolly_exam_spin.setValue(row[76])
        except Error as e:
            QMessageBox.critical(self, "Saving Score", str(e), QMessageBox.Ok)

    def saveQurScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        qur_c1 = self.ui.qur_c1_spin.value()
        qur_c2 = self.ui.qur_c2_spin.value()
        qur_ass = self.ui.qur_ass_spin.value()
        qur_exam = self.ui.qur_exam_spin.value()
        qur_total = qur_c1 + qur_c2 + qur_ass + qur_exam
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_third(stud_no, score_class, qur_c1, qur_c2, qur_ass, qur_exam, qur_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, qur_c1, qur_c2, qur_ass, qur_exam, qur_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, score_class = ?, qur_c1 = ?, qur_c2 = ?, qur_ass = ?, qur_exam = ?, qur_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, qur_c1, qur_c2, qur_ass, qur_exam, qur_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveIbadatScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        ibadat_c1 = self.ui.ibadat_c1_spin.value()
        ibadat_c2 = self.ui.ibadat_c2_spin.value()
        ibadat_ass = self.ui.ibadat_ass_spin.value()
        ibadat_exam = self.ui.ibadat_exam_spin.value()
        ibadat_total = ibadat_c1 + ibadat_c2 + ibadat_ass + ibadat_exam
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_third(stud_no, score_class, ibadat_c1, ibadat_c2, ibadat_ass, ibadat_exam, ibadat_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, ibadat_c1, ibadat_c2, ibadat_ass, ibadat_exam, ibadat_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, score_class = ?, ibadat_c1 = ?, ibadat_c2 = ?, ibadat_ass = ?, ibadat_exam = ?, ibadat_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, ibadat_c1, ibadat_c2, ibadat_ass, ibadat_exam, ibadat_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveArabic1Scores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        arabic1_c1 = self.ui.arabic1_c1_spin.value()
        arabic1_c2 = self.ui.arabic1_c2_spin.value()
        arabic1_ass = self.ui.arabic1_ass_spin.value()
        arabic1_exam = self.ui.arabic1_exam_spin.value()
        arabic1_total = arabic1_c1 + arabic1_c2 + arabic1_ass + arabic1_exam
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_third(stud_no, score_class, arabic1_c1, arabic1_c2, arabic1_ass, arabic1_exam, arabic1_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, arabic1_c1, arabic1_c2, arabic1_ass, arabic1_exam, arabic1_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, score_class = ?, arabic1_c1 = ?, arabic1_c2 = ?, arabic1_ass = ?, arabic1_exam = ?, arabic1_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, arabic1_c1, arabic1_c2, arabic1_ass, arabic1_exam, arabic1_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveArabic2Scores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        arabic2_c1 = self.ui.arabic2_c1_spin.value()
        arabic2_c2 = self.ui.arabic2_c2_spin.value()
        arabic2_ass = self.ui.arabic2_ass_spin.value()
        arabic2_exam = self.ui.arabic2_exam_spin.value()
        arabic2_total = arabic2_c1 + arabic2_c2 + arabic2_ass + arabic2_exam
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_third(stud_no, score_class, arabic2_c1, arabic2_c2, arabic2_ass, arabic2_exam, arabic2_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, arabic2_c1, arabic2_c2, arabic2_ass, arabic2_exam, arabic2_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, score_class = ?, arabic2_c1 = ?, arabic2_c2 = ?, arabic2_ass = ?, arabic2_exam = ?, arabic2_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, arabic2_c1, arabic2_c2, arabic2_ass, arabic2_exam, arabic2_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveMathScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        math_c1 = self.ui.math_c1_spin.value()
        math_c2 = self.ui.math_c2_spin.value()
        math_ass = self.ui.math_ass_spin.value()
        math_exam = self.ui.math_exam_spin.value()
        math_total = math_c1 + math_c2 + math_ass + math_exam
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_third(stud_no, score_class, math_c1, math_c2, math_ass, math_exam, math_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, math_c1, math_c2, math_ass, math_exam, math_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, score_class = ?, math_c1 = ?, math_c2 = ?, math_ass = ?, math_exam = ?, math_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, math_c1, math_c2, math_ass, math_exam, math_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveEnglishScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        eng_c1 = self.ui.eng_c1_spin.value()
        eng_c2 = self.ui.eng_c2_spin.value()
        eng_ass = self.ui.eng_ass_spin.value()
        eng_exam = self.ui.eng_exam_spin.value()
        eng_total = eng_c1 + eng_c2 + eng_ass + eng_exam
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_third(stud_no, score_class, eng_c1, eng_c2, eng_ass, eng_exam, eng_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, eng_c1, eng_c2, eng_ass, eng_exam, eng_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, score_class = ?, eng_c1 = ?, eng_c2 = ?, eng_ass = ?, eng_exam = ?, eng_total  = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, eng_c1, eng_c2, eng_ass, eng_exam, eng_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveCompScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        comp_c1 = self.ui.comp_c1_spin.value()
        comp_c2 = self.ui.comp_c2_spin.value()
        comp_ass = self.ui.comp_ass_spin.value()
        comp_exam = self.ui.comp_exam_spin.value()
        comp_total = comp_c1 + comp_c2 + comp_ass + comp_exam
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_third(stud_no, score_class, comp_c1, comp_c2, comp_ass, comp_exam, comp_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, comp_c1, comp_c2, comp_ass, comp_exam, comp_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, score_class = ?, comp_c1 = ?, comp_c2 = ?, comp_ass = ?, comp_exam = ?, comp_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, comp_c1, comp_c2, comp_ass, comp_exam, comp_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveBasScScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        bas_sc_c1 = self.ui.bas_sc_c1_spin.value()
        bas_sc_c2 = self.ui.bas_sc_c2_spin.value()
        bas_sc_ass = self.ui.bas_sc_ass_spin.value()
        bas_sc_exam = self.ui.bas_sc_exam_spin.value()
        bas_sc_total = bas_sc_c1 + bas_sc_c2 + bas_sc_ass + bas_sc_exam
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_third(stud_no, score_class, bas_sc_c1, bas_sc_c2, bas_sc_ass, bas_sc_exam, bas_sc_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, bas_sc_c1, bas_sc_c2, bas_sc_ass, bas_sc_exam, bas_sc_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, score_class = ?, bas_sc_c1 = ?, bas_sc_c2 = ?, bas_sc_ass = ?, bas_sc_exam = ?, bas_sc_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, bas_sc_c1, bas_sc_c2, bas_sc_ass, bas_sc_exam, bas_sc_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveReligionScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        religion_c1 = self.ui.religion_c1_spin.value()
        religion_c2 = self.ui.religion_c2_spin.value()
        religion_ass = self.ui.religion_ass_spin.value()
        religion_exam = self.ui.religion_exam_spin.value()
        religion_total = religion_c1 + religion_c2 + religion_ass + religion_exam
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_third(stud_no, score_class, religion_c1, religion_c2, religion_ass, religion_exam, religion_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, religion_c1, religion_c2, religion_ass, religion_exam, religion_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, score_class = ?, religion_c1 = ?, religion_c2 = ?, religion_ass = ?, religion_exam = ?, religion_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, religion_c1, religion_c2, religion_ass, religion_exam, religion_total, stud_no,))
                con.commit()

        except Error:
            pass
        finally:
            con.close()

    def saveCivicScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        civic_c1 = self.ui.civic_c1_spin.value()
        civic_c2 = self.ui.civic_c2_spin.value()
        civic_ass = self.ui.civic_ass_spin.value()
        civic_exam = self.ui.civic_exam_spin.value()
        civic_total = civic_c1 + civic_c2 + civic_ass + civic_exam
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_third(stud_no, score_class, civic_c1, civic_c2, civic_ass, civic_exam, civic_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, civic_c1, civic_c2, civic_ass, civic_exam, civic_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, score_class = ?, civic_c1 = ?, civic_c2 = ?, civic_ass = ?, civic_exam = ?, civic_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, civic_c1, civic_c2, civic_ass, civic_exam, civic_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveVerbalScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        verbal_c1 = self.ui.verbal_c1_spin.value()
        verbal_c2 = self.ui.verbal_c2_spin.value()
        verbal_ass = self.ui.verbal_ass_spin.value()
        verbal_exam = self.ui.verbal_exam_spin.value()
        verbal_total = verbal_c1 + verbal_c2 + verbal_ass + verbal_exam
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_third(stud_no, score_class, verbal_c1, verbal_c2, verbal_ass, verbal_exam, verbal_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, verbal_c1, verbal_c2, verbal_ass, verbal_exam, verbal_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, score_class = ?, verbal_c1 = ?, verbal_c2 = ?, verbal_ass = ?, verbal_exam = ?, verbal_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, verbal_c1, verbal_c2, verbal_ass, verbal_exam, verbal_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveQuantScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        quant_c1 = self.ui.quant_c1_spin.value()
        quant_c2 = self.ui.quant_c2_spin.value()
        quant_ass = self.ui.quant_ass_spin.value()
        quant_exam = self.ui.quant_exam_spin.value()
        quant_total = quant_c1 + quant_c2 + quant_ass + quant_exam
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_third(stud_no, score_class, quant_c1, quant_c2, quant_ass, quant_exam, quant_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, quant_c1, quant_c2, quant_ass, quant_exam, quant_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, score_class = ?, quant_c1 = ?, quant_c2 = ?, quant_ass = ?, quant_exam = ?, quant_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, quant_c1, quant_c2, quant_ass, quant_exam, quant_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveHandwiritingScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        basic_c1 = self.ui.basic_c1_spin.value()
        basic_c2 = self.ui.basic_c2_spin.value()
        basic_ass = self.ui.basic_ass_spin.value()
        basic_exam = self.ui.basic_exam_spin.value()
        basic_total = basic_c1 + basic_c2 + basic_ass + basic_exam
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_third(stud_no, score_class, basic_c1, basic_c2, basic_ass, basic_exam, basic_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, basic_c1, basic_c2, basic_ass, basic_exam, basic_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, score_class = ?, basic_c1 = ?, basic_c2 = ?, basic_ass = ?, basic_exam = ?, basic_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, basic_c1, basic_c2, basic_ass, basic_exam, basic_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveFrenchScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        french_c1 = self.ui.french_c1_spin.value()
        french_c2 = self.ui.french_c2_spin.value()
        french_ass = self.ui.french_ass_spin.value()
        french_exam = self.ui.french_exam_spin.value()
        french_total = french_c1 + french_c2 + french_ass + french_exam
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_third(stud_no, score_class, french_c1, french_c2, french_ass, french_exam, french_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, french_c1, french_c2, french_ass, french_exam, french_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, score_class = ?, french_c1 = ?, french_c2 = ?, french_ass = ?, french_exam = ?, french_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, french_c1, french_c2, french_ass, french_exam, french_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def saveJollyScores(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        score_class = self.ui.class_comboBox.currentText()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        jolly_c1 = self.ui.jolly_c1_spin.value()
        jolly_c2 = self.ui.jolly_c2_spin.value()
        jolly_ass = self.ui.jolly_ass_spin.value()
        jolly_exam = self.ui.jolly_exam_spin.value()
        jolly_total = jolly_c1 + jolly_c2 + jolly_ass + jolly_exam
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        try:
            cur.execute(cmd1, (stud_no,))
            row = cur.fetchone()
            if row == None:
                cmd2 = "INSERT INTO t_pri_scores_third(stud_no, score_class, jolly_c1, jolly_c2, jolly_ass, jolly_exam, jolly_total) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(cmd2, (stud_no, score_class, jolly_c1, jolly_c2, jolly_ass, jolly_exam, jolly_total,))
                con.commit()
            else:
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, score_class = ?, jolly_c1 = ?, jolly_c2 = ?, jolly_ass = ?, jolly_exam = ?, jolly_total = ? WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, score_class, jolly_c1, jolly_c2, jolly_ass, jolly_exam, jolly_total, stud_no,))
                con.commit()
        except Error:
            pass
        finally:
            con.close()

    def computeTotAvg(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        cmd1 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
        cur.execute(cmd1, (stud_no,))
        row = cur.fetchone()
        if row == None:
            pass
        elif row[7] != None and row[12] != None and row[17] != None and row[22] != None and row[27] != None and row[32] != None and row[37] != None and row[42] != None and row[47] != None and row[52] != None and row[57] != None and row[62] != None and row[67] != None and row[72] != None and row[77] != None:
            try:
                all_total = row[7] + row[12] + row[17] + row[22] + row[27] + row[32] + row[37] + row[42]+ row[47] + row[52] + row[57] + row[62] + row[67] + row[72] + row[77]
                avg = round(all_total/15, 4)
                cmd0 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
                cur.execute(cmd0, (stud_no,))
                row = cur.fetchone()
                if row == None:
                    total_cum0 = all_total
                    avg0 = avg
                elif row[78] == None:
                    total_cum0 = all_total
                    avg0 = avg
                else:
                    total_cum0 = row[78] + all_total
                    avg0 = round((row[78] + all_total)/30,4)
                cmd2 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
                cur.execute(cmd2, (stud_no,))
                row = cur.fetchone()
                if row == None:
                    total_cum = total_cum0
                    avg_cum = avg0
                elif row[78] == row[80]:
                    total_cum = row[78] + total_cum0
                    avg_cum = round(total_cum/30, 4)
                else:
                    total_cum = row[78] + total_cum0
                    avg_cum = round(total_cum/45, 4)
                cmd3 = "UPDATE t_pri_scores_third SET stud_no = ?, all_total = ?, avg = ?, total_cum = ?, avg_cum = ?  WHERE stud_no = ?"
                cur.execute(cmd3, (stud_no, all_total, avg, total_cum, avg_cum, stud_no,))
                con.commit()
                QMessageBox.information(self, "Saving Score",  "Pupil's scores saved successfully", QMessageBox.Ok)
            except Error as e:
                QMessageBox.critical(self, "Saving Score", str(e), QMessageBox.Ok)
            except TypeError as e:
                QMessageBox.critical(self, "Saving Score", str(e), QMessageBox.Ok)
            finally:
                con.close()


class PriScoresView3(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PriScore3rdForm()
        self.ui.setupUi(self)
        self.pri_report3 = PriReport3()
        self.displayClasses()
        self.listStudsScores()
        self.ui.class_comboBox.currentTextChanged.connect(self.listClass)
        self.ui.class_comboBox.currentTextChanged.connect(self.displayStuds)
        self.ui.switch_back_btn.clicked.connect(self.listStudsScores)
        self.ui.report_gen_btn.clicked.connect(self.displayRadios)
        self.ui.report_gen_btn.clicked.connect(self.generatePriReport)
        self.ui.pdf_btn.clicked.connect(self.displayRadios)
        self.ui.pdf_btn.clicked.connect(self.generatePriReportPDF)
        self.ui.del_btn.clicked.connect(self.deleteStud)
        self.ui.stud_adm_no_comboBox.currentTextChanged.connect(self.displayName)

    def displayClasses(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        query = cur.execute('SELECT * FROM t_pri_scores_third ORDER BY score_class')
        self.ui.class_comboBox.clear()
        classes = ["Select a class"]
        rows = cur.fetchall()
        for row in rows:
            if row[2] not in classes:
                classes.append(row[2])
        self.ui.class_comboBox.addItems(classes)
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

    def listStudsScores(self):
        self.displayClasses()
        self.ui.tableWidget_2.hide()
        self.ui.tableWidget.setRowCount(0)
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        cmd = "SELECT * FROM t_pri_scores_third ORDER BY stud_no"
        cur.execute(cmd)
        rows = cur.fetchall()
        for row_number, row_data in enumerate(rows):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                it = QTableWidgetItem()
                it.setText(str(column_data))
                self.ui.tableWidget.setItem(row_number, column_number, it)
        self.ui.tableWidget.show()
        self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.ui.tableWidget.setColumnWidth(0,0)
        con.close()

    def listClass(self):
        self.ui.tableWidget.hide()
        self.ui.tableWidget_2.setRowCount(0)
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox.currentText()
        cmd = "SELECT * FROM t_pri_scores_third WHERE score_class = ? ORDER BY stud_no"
        cur.execute(cmd, (classes_combo,))
        rows = cur.fetchall()
        for row_number, row_data in enumerate(rows):
            self.ui.tableWidget_2.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                it = QTableWidgetItem()
                it.setText(str(column_data))
                self.ui.tableWidget_2.setItem(row_number, column_number, it)
        self.ui.tableWidget_2.show()
        self.ui.tableWidget_2.horizontalHeader().setDefaultSectionSize(180)
        self.ui.tableWidget_2.setColumnWidth(0,0)
        self.ui.class_comboBox.show()
        con.close()

    def displayStuds(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox.currentText()
        cmd = "SELECT * FROM t_pri_scores_third WHERE score_class = ? ORDER BY stud_no"
        cur.execute(cmd, (classes_combo,))
        rows = cur.fetchall()
        adm_nos = ["Select an admission number"]
        self.ui.stud_adm_no_comboBox.clear()
        for row in rows:
            adm_nos.append(row[1])
        self.ui.stud_adm_no_comboBox.addItems(adm_nos)
        con.close()

    def displayName(self):
        self.ui.name_label.setText("")
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no_combo = self.ui.stud_adm_no_comboBox.currentText()
        cmd = "SELECT * FROM t_studs WHERE admission_no = ?"
        cur.execute(cmd, (stud_no_combo,))
        row = cur.fetchone()
        if row == None:
            self.ui.name_label.setText("")
        else:
            self.ui.name_label.setText("Name: \n" + row[1])

    def deleteStud(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        stud_no = self.ui.stud_adm_no_comboBox.currentText()
        if stud_no == "Select an admission number":
            QMessageBox.critical(self, "Deleting Pupil", "ERROR: Please select pupil's admission number before pressing delete", QMessageBox.Ok)
        elif stud_no == "":
            QMessageBox.critical(self, "Deleting Pupil", "ERROR: Please select a class and pupil's admission number before pressing delete", QMessageBox.Ok)
        else:
            cmd = "DELETE FROM t_pri_scores_third WHERE stud_no = ?"
            buttonReply = QMessageBox.warning(self, 'Deleting Pupil', "WARNING: Deleting will remove all the pupil's score records in the class. Do you still wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                cur.execute(cmd, (stud_no,))
                con.commit()
                self.displayStuds()
                con.close()

    def generatePriReport(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox.currentText()
        admission_no = self.ui.stud_adm_no_comboBox.currentText()
        cmd1 = "SELECT * FROM t_studs WHERE admission_no = ?"
        cur.execute(cmd1, (admission_no,))
        row = cur.fetchone()
        if row == None:
            QMessageBox.critical(self, "Printing Report", "ERROR: Please select a class and pupil's admission number before generating report", QMessageBox.Ok)
        else:
            self.pri_report3.ui.name_label.setText(row[1])
            self.pri_report3.ui.class_label.setText(row[3])
            self.pri_report3.ui.sex_label.setText(row[5])
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray.fromBase64(row[6]))
            self.pri_report3.ui.photo_label.setPixmap(QPixmap(pixmap))
            try:
                cmd3 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
                cur.execute(cmd3, (admission_no,))
                row = cur.fetchone()
                self.pri_report3.ui.qur_c1_label.setText(str(row[3]))
                self.pri_report3.ui.qur_c2_label.setText(str(row[4]))
                self.pri_report3.ui.qur_ass_label.setText(str(row[5]))
                self.pri_report3.ui.qur_exam_label.setText(str(row[6]))
                self.pri_report3.ui.qur_total_label.setText(str(row[7]))
                if row[7] < 40:
                    self.pri_report3.ui.qur_grade_label.setText("F")
                    self.pri_report3.ui.qur_remark_label.setText("Fail")
                elif row[7] >= 40 and row[7] < 50:
                    self.pri_report3.ui.qur_grade_label.setText("D")
                    self.pri_report3.ui.qur_remark_label.setText("Pass")
                elif row[7] >= 50 and row[7] < 60:
                    self.pri_report3.ui.qur_grade_label.setText("C")
                    self.pri_report3.ui.qur_remark_label.setText("Good")
                elif row[7] >= 60 and row[7] < 70:
                    self.pri_report3.ui.qur_grade_label.setText("B")
                    self.pri_report3.ui.qur_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.qur_grade_label.setText("A")
                    self.pri_report3.ui.qur_remark_label.setText("Excellent")
                self.pri_report3.ui.ibadat_c1_label.setText(str(row[8]))
                self.pri_report3.ui.ibadat_c2_label.setText(str(row[9]))
                self.pri_report3.ui.ibadat_ass_label.setText(str(row[10]))
                self.pri_report3.ui.ibadat_exam_label.setText(str(row[11]))
                self.pri_report3.ui.ibadat_total_label.setText(str(row[12]))
                if row[12] < 40:
                    self.pri_report3.ui.ibadat_grade_label.setText("F")
                    self.pri_report3.ui.ibadat_remark_label.setText("Fail")
                elif row[12] >= 40 and row[12] < 50:
                    self.pri_report3.ui.ibadat_grade_label.setText("D")
                    self.pri_report3.ui.ibadat_remark_label.setText("Pass")
                elif row[12] >= 50 and row[12] < 60:
                    self.pri_report3.ui.ibadat_grade_label.setText("C")
                    self.pri_report3.ui.ibadat_remark_label.setText("Good")
                elif row[12] >= 60 and row[12] < 70:
                    self.pri_report3.ui.ibadat_grade_label.setText("B")
                    self.pri_report3.ui.ibadat_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.ibadat_grade_label.setText("A")
                    self.pri_report3.ui.ibadat_remark_label.setText("Excellent")
                self.pri_report3.ui.arabic1_c1_label.setText(str(row[13]))
                self.pri_report3.ui.arabic1_c2_label.setText(str(row[14]))
                self.pri_report3.ui.arabic1_ass_label.setText(str(row[15]))
                self.pri_report3.ui.arabic1_exam_label.setText(str(row[16]))
                self.pri_report3.ui.arabic1_total_label.setText(str(row[17]))
                if row[17] < 40:
                    self.pri_report3.ui.arabic1_grade_label.setText("F")
                    self.pri_report3.ui.arabic1_remark_label.setText("Fail")
                elif row[17] >= 40 and row[17] < 50:
                    self.pri_report3.ui.arabic1_grade_label.setText("D")
                    self.pri_report3.ui.arabic1_remark_label.setText("Pass")
                elif row[17] >= 50 and row[17] < 60:
                    self.pri_report3.ui.arabic1_grade_label.setText("C")
                    self.pri_report3.ui.arabic1_remark_label.setText("Good")
                elif row[17] >= 60 and row[17] < 70:
                    self.pri_report3.ui.arabic1_grade_label.setText("B")
                    self.pri_report3.ui.arabic1_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.arabic1_grade_label.setText("A")
                    self.pri_report3.ui.arabic1_remark_label.setText("Excellent")
                self.pri_report3.ui.arabic2_c1_label.setText(str(row[18]))
                self.pri_report3.ui.arabic2_c2_label.setText(str(row[19]))
                self.pri_report3.ui.arabic2_ass_label.setText(str(row[20]))
                self.pri_report3.ui.arabic2_exam_label.setText(str(row[21]))
                self.pri_report3.ui.arabic2_total_label.setText(str(row[22]))
                if row[22] < 40:
                    self.pri_report3.ui.arabic2_grade_label.setText("F")
                    self.pri_report3.ui.arabic2_remark_label.setText("Fail")
                elif row[22] >= 40 and row[22] < 50:
                    self.pri_report3.ui.arabic2_grade_label.setText("D")
                    self.pri_report3.ui.arabic2_remark_label.setText("Pass")
                elif row[22] >= 50 and row[22] < 60:
                    self.pri_report3.ui.arabic2_grade_label.setText("C")
                    self.pri_report3.ui.arabic2_remark_label.setText("Good")
                elif row[22] >= 60 and row[22] < 70:
                    self.pri_report3.ui.arabic2_grade_label.setText("B")
                    self.pri_report3.ui.arabic2_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.arabic2_grade_label.setText("A")
                    self.pri_report3.ui.arabic2_remark_label.setText("Excellent")
                self.pri_report3.ui.math_c1_label.setText(str(row[23]))
                self.pri_report3.ui.math_c2_label.setText(str(row[24]))
                self.pri_report3.ui.math_ass_label.setText(str(row[25]))
                self.pri_report3.ui.math_exam_label.setText(str(row[26]))
                self.pri_report3.ui.math_total_label.setText(str(row[27]))
                if row[27] < 40:
                    self.pri_report3.ui.math_grade_label.setText("F")
                    self.pri_report3.ui.math_remark_label.setText("Fail")
                elif row[27] >= 40 and row[27] < 50:
                    self.pri_report3.ui.math_grade_label.setText("D")
                    self.pri_report3.ui.math_remark_label.setText("Pass")
                elif row[27] >= 50 and row[27] < 60:
                    self.pri_report3.ui.math_grade_label.setText("C")
                    self.pri_report3.ui.math_remark_label.setText("Good")
                elif row[27] >= 60 and row[27] < 70:
                    self.pri_report3.ui.math_grade_label.setText("B")
                    self.pri_report3.ui.math_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.math_grade_label.setText("A")
                    self.pri_report3.ui.math_remark_label.setText("Excellent")
                self.pri_report3.ui.eng_c1_label.setText(str(row[28]))
                self.pri_report3.ui.eng_c2_label.setText(str(row[29]))
                self.pri_report3.ui.eng_ass_label.setText(str(row[30]))
                self.pri_report3.ui.eng_exam_label.setText(str(row[31]))
                self.pri_report3.ui.eng_total_label.setText(str(row[32]))
                if row[32] < 40:
                    self.pri_report3.ui.eng_grade_label.setText("F")
                    self.pri_report3.ui.eng_remark_label.setText("Fail")
                elif row[32] >= 40 and row[32] < 50:
                    self.pri_report3.ui.eng_grade_label.setText("D")
                    self.pri_report3.ui.eng_remark_label.setText("Pass")
                elif row[32] >= 50 and row[32] < 60:
                    self.pri_report3.ui.eng_grade_label.setText("C")
                    self.pri_report3.ui.eng_remark_label.setText("Good")
                elif row[32] >= 60 and row[32] < 70:
                    self.pri_report3.ui.eng_grade_label.setText("B")
                    self.pri_report3.ui.eng_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.eng_grade_label.setText("A")
                    self.pri_report3.ui.eng_remark_label.setText("Excellent")
                self.pri_report3.ui.comp_c1_label.setText(str(row[33]))
                self.pri_report3.ui.comp_c2_label.setText(str(row[34]))
                self.pri_report3.ui.comp_ass_label.setText(str(row[35]))
                self.pri_report3.ui.comp_exam_label.setText(str(row[36]))
                self.pri_report3.ui.comp_total_label.setText(str(row[37]))
                if row[37] < 40:
                    self.pri_report3.ui.comp_grade_label.setText("F")
                    self.pri_report3.ui.comp_remark_label.setText("Fail")
                elif row[37] >= 40 and row[37] < 50:
                    self.pri_report3.ui.comp_grade_label.setText("D")
                    self.pri_report3.ui.comp_remark_label.setText("Pass")
                elif row[37] >= 50 and row[37] < 60:
                    self.pri_report3.ui.comp_grade_label.setText("C")
                    self.pri_report3.ui.comp_remark_label.setText("Good")
                elif row[37] >= 60 and row[37] < 70:
                    self.pri_report3.ui.comp_grade_label.setText("B")
                    self.pri_report3.ui.comp_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.comp_grade_label.setText("A")
                    self.pri_report3.ui.comp_remark_label.setText("Excellent")
                self.pri_report3.ui.bas_sc_c1_label.setText(str(row[38]))
                self.pri_report3.ui.bas_sc_c2_label.setText(str(row[39]))
                self.pri_report3.ui.bas_sc_ass_label.setText(str(row[40]))
                self.pri_report3.ui.bas_sc_exam_label.setText(str(row[41]))
                self.pri_report3.ui.bas_sc_total_label.setText(str(row[42]))
                if row[42] < 40:
                    self.pri_report3.ui.bas_sc_grade_label.setText("F")
                    self.pri_report3.ui.bas_sc_remark_label.setText("Fail")
                elif row[42] >= 40 and row[42] < 50:
                    self.pri_report3.ui.bas_sc_grade_label.setText("D")
                    self.pri_report3.ui.bas_sc_remark_label.setText("Pass")
                elif row[42] >= 50 and row[42] < 60:
                    self.pri_report3.ui.bas_sc_grade_label.setText("C")
                    self.pri_report3.ui.bas_sc_remark_label.setText("Good")
                elif row[42] >= 60 and row[42] < 70:
                    self.pri_report3.ui.bas_sc_grade_label.setText("B")
                    self.pri_report3.ui.bas_sc_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.bas_sc_grade_label.setText("A")
                    self.pri_report3.ui.bas_sc_remark_label.setText("Excellent")
                self.pri_report3.ui.religion_c1_label.setText(str(row[43]))
                self.pri_report3.ui.religion_c2_label.setText(str(row[44]))
                self.pri_report3.ui.religion_ass_label.setText(str(row[45]))
                self.pri_report3.ui.religion_exam_label.setText(str(row[46]))
                self.pri_report3.ui.religion_total_label.setText(str(row[47]))
                if row[47] < 40:
                    self.pri_report3.ui.religion_grade_label.setText("F")
                    self.pri_report3.ui.religion_remark_label.setText("Fail")
                elif row[47] >= 40 and row[47] < 50:
                    self.pri_report3.ui.religion_grade_label.setText("D")
                    self.pri_report3.ui.religion_remark_label.setText("Pass")
                elif row[47] >= 50 and row[47] < 60:
                    self.pri_report3.ui.religion_grade_label.setText("C")
                    self.pri_report3.ui.religion_remark_label.setText("Good")
                elif row[47] >= 60 and row[47] < 70:
                    self.pri_report3.ui.religion_grade_label.setText("B")
                    self.pri_report3.ui.religion_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.religion_grade_label.setText("A")
                    self.pri_report3.ui.religion_remark_label.setText("Excellent")
                self.pri_report3.ui.civic_c1_label.setText(str(row[48]))
                self.pri_report3.ui.civic_c2_label.setText(str(row[49]))
                self.pri_report3.ui.civic_ass_label.setText(str(row[50]))
                self.pri_report3.ui.civic_exam_label.setText(str(row[51]))
                self.pri_report3.ui.civic_total_label.setText(str(row[52]))
                if row[52] < 40:
                    self.pri_report3.ui.civic_grade_label.setText("F")
                    self.pri_report3.ui.civic_remark_label.setText("Fail")
                elif row[52] >= 40 and row[52] < 50:
                    self.pri_report3.ui.civic_grade_label.setText("D")
                    self.pri_report3.ui.civic_remark_label.setText("Pass")
                elif row[52] >= 50 and row[52] < 60:
                    self.pri_report3.ui.civic_grade_label.setText("C")
                    self.pri_report3.ui.civic_remark_label.setText("Good")
                elif row[52] >= 60 and row[52] < 70:
                    self.pri_report3.ui.civic_grade_label.setText("B")
                    self.pri_report3.ui.civic_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.civic_grade_label.setText("A")
                    self.pri_report3.ui.civic_remark_label.setText("Excellent")
                self.pri_report3.ui.verbal_c1_label.setText(str(row[53]))
                self.pri_report3.ui.verbal_c2_label.setText(str(row[54]))
                self.pri_report3.ui.verbal_ass_label.setText(str(row[55]))
                self.pri_report3.ui.verbal_exam_label.setText(str(row[56]))
                self.pri_report3.ui.verbal_total_label.setText(str(row[57]))
                if row[57] < 40:
                    self.pri_report3.ui.verbal_grade_label.setText("F")
                    self.pri_report3.ui.verbal_remark_label.setText("Fail")
                elif row[57] >= 40 and row[57] < 50:
                    self.pri_report3.ui.verbal_grade_label.setText("D")
                    self.pri_report3.ui.verbal_remark_label.setText("Pass")
                elif row[57] >= 50 and row[57] < 60:
                    self.pri_report3.ui.verbal_grade_label.setText("C")
                    self.pri_report3.ui.verbal_remark_label.setText("Good")
                elif row[57] >= 60 and row[57] < 70:
                    self.pri_report3.ui.verbal_grade_label.setText("B")
                    self.pri_report3.ui.verbal_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.verbal_grade_label.setText("A")
                    self.pri_report3.ui.verbal_remark_label.setText("Excellent")
                self.pri_report3.ui.quant_c1_label.setText(str(row[58]))
                self.pri_report3.ui.quant_c2_label.setText(str(row[59]))
                self.pri_report3.ui.quant_ass_label.setText(str(row[60]))
                self.pri_report3.ui.quant_exam_label.setText(str(row[61]))
                self.pri_report3.ui.quant_total_label.setText(str(row[62]))
                if row[62] < 40:
                    self.pri_report3.ui.quant_grade_label.setText("F")
                    self.pri_report3.ui.quant_remark_label.setText("Fail")
                elif row[62] >= 40 and row[62] < 50:
                    self.pri_report3.ui.quant_grade_label.setText("D")
                    self.pri_report3.ui.quant_remark_label.setText("Pass")
                elif row[62] >= 50 and row[62] < 60:
                    self.pri_report3.ui.quant_grade_label.setText("C")
                    self.pri_report3.ui.quant_remark_label.setText("Good")
                elif row[62] >= 60 and row[62] < 70:
                    self.pri_report3.ui.quant_grade_label.setText("B")
                    self.pri_report3.ui.quant_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.quant_grade_label.setText("A")
                    self.pri_report3.ui.quant_remark_label.setText("Excellent")
                self.pri_report3.ui.basic_c1_label.setText(str(row[63]))
                self.pri_report3.ui.basic_c2_label.setText(str(row[64]))
                self.pri_report3.ui.basic_ass_label.setText(str(row[65]))
                self.pri_report3.ui.basic_exam_label.setText(str(row[66]))
                self.pri_report3.ui.basic_total_label.setText(str(row[67]))
                if row[67] < 40:
                    self.pri_report3.ui.basic_grade_label.setText("F")
                    self.pri_report3.ui.basic_remark_label.setText("Fail")
                elif row[67] >= 40 and row[67] < 50:
                    self.pri_report3.ui.basic_grade_label.setText("D")
                    self.pri_report3.ui.basic_remark_label.setText("Pass")
                elif row[67] >= 50 and row[67] < 60:
                    self.pri_report3.ui.basic_grade_label.setText("C")
                    self.pri_report3.ui.basic_remark_label.setText("Good")
                elif row[67] >= 60 and row[67] < 70:
                    self.pri_report3.ui.basic_grade_label.setText("B")
                    self.pri_report3.ui.basic_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.basic_grade_label.setText("A")
                    self.pri_report3.ui.basic_remark_label.setText("Excellent")
                self.pri_report3.ui.french_c1_label.setText(str(row[68]))
                self.pri_report3.ui.french_c2_label.setText(str(row[69]))
                self.pri_report3.ui.french_ass_label.setText(str(row[70]))
                self.pri_report3.ui.french_exam_label.setText(str(row[71]))
                self.pri_report3.ui.french_total_label.setText(str(row[72]))
                if row[72] < 40:
                    self.pri_report3.ui.french_grade_label.setText("F")
                    self.pri_report3.ui.french_remark_label.setText("Fail")
                elif row[72] >= 40 and row[72] < 50:
                    self.pri_report3.ui.french_grade_label.setText("D")
                    self.pri_report3.ui.french_remark_label.setText("Pass")
                elif row[72] >= 50 and row[72] < 60:
                    self.pri_report3.ui.french_grade_label.setText("C")
                    self.pri_report3.ui.french_remark_label.setText("Good")
                elif row[72] >= 60 and row[72] < 70:
                    self.pri_report3.ui.french_grade_label.setText("B")
                    self.pri_report3.ui.french_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.french_grade_label.setText("A")
                    self.pri_report3.ui.french_remark_label.setText("Excellent")
                self.pri_report3.ui.jolly_c1_label.setText(str(row[73]))
                self.pri_report3.ui.jolly_c2_label.setText(str(row[74]))
                self.pri_report3.ui.jolly_ass_label.setText(str(row[75]))
                self.pri_report3.ui.jolly_exam_label.setText(str(row[76]))
                self.pri_report3.ui.jolly_total_label.setText(str(row[77]))
                if row[77] < 40:
                    self.pri_report3.ui.jolly_grade_label.setText("F")
                    self.pri_report3.ui.jolly_remark_label.setText("Fail")
                elif row[77] >= 40 and row[77] < 50:
                    self.pri_report3.ui.jolly_grade_label.setText("D")
                    self.pri_report3.ui.jolly_remark_label.setText("Pass")
                elif row[77] >= 50 and row[77] < 60:
                    self.pri_report3.ui.jolly_grade_label.setText("C")
                    self.pri_report3.ui.jolly_remark_label.setText("Good")
                elif row[77] >= 60 and row[77] < 70:
                    self.pri_report3.ui.jolly_grade_label.setText("B")
                    self.pri_report3.ui.jolly_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.jolly_grade_label.setText("A")
                    self.pri_report3.ui.jolly_remark_label.setText("Excellent")
                self.pri_report3.ui.total_scores3_label.setText(str(row[78]))
                self.pri_report3.ui.avg3_label.setText(str(row[79]))
                self.pri_report3.ui.total_cum_label.setText(str(row[80]))
                self.pri_report3.ui.avg_cum_label.setText(str(row[81]))
                if row[79] < 40:
                    self.pri_report3.ui.master_com_label.setText("Bad result. Be careful.")
                    self.pri_report3.ui.head_com_label.setText("Bad result.")
                elif row[79] >= 40 and row[79] < 50:
                    self.pri_report3.ui.master_com_label.setText("Weak result. Work hard.")
                    self.pri_report3.ui.head_com_label.setText("Weak result.")
                elif row[79] >= 50 and row[79] < 60:
                    self.pri_report3.ui.master_com_label.setText("Fair result. Work hard.")
                    self.pri_report3.ui.head_com_label.setText("Fair result.")
                elif row[79] >= 60 and row[79] < 70:
                    self.pri_report3.ui.master_com_label.setText("Good result. Put more effort.")
                    self.pri_report3.ui.head_com_label.setText("Good result.")
                else:
                    self.pri_report3.ui.master_com_label.setText("Excellent result. Keep on.")
                    self.pri_report3.ui.head_com_label.setText("Excellent result.")
                cmd9 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
                cur.execute(cmd9, (admission_no,))
                row = cur.fetchone()
                if row == None:
                    self.pri_report3.ui.total_scores_label.setText("None")
                    self.pri_report3.ui.avg_label.setText("None")
                elif row[78] == None and row[79] == None:
                    self.pri_report3.ui.total_scores_label.setText("None")
                    self.pri_report3.ui.avg_label.setText("None")
                else:
                    self.pri_report3.ui.total_scores_label.setText(str(row[78]))
                    self.pri_report3.ui.avg_label.setText(str(row[79]))
                cmd10 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
                cur.execute(cmd10, (admission_no,))
                row = cur.fetchone()
                if row == None:
                    self.pri_report3.ui.total_scores2_label.setText("None")
                    self.pri_report3.ui.avg2_label.setText("None")
                elif row[78] == None and row[79] == None:
                    self.pri_report3.ui.total_scores2_label.setText("None")
                    self.pri_report3.ui.avg2_label.setText("None")
                else:
                    self.pri_report3.ui.total_scores2_label.setText(str(row[78]))
                    self.pri_report3.ui.avg2_label.setText(str(row[79]))
                positions = []
                cmd11 = "SELECT * FROM t_pri_scores_third WHERE score_class = ? ORDER BY avg_cum DESC"
                cur.execute(cmd11, (classes_combo,))
                rows = cur.fetchall()
                for row in rows:
                    positions.append(row[1])
                self.pri_report3.ui.out_of_label.setText(str(len(positions)))
                for i in range(len(positions)):
                    if admission_no == positions[i]:
                        if i in range (10, len(positions), 100):
                            self.pri_report3.ui.position_label.setText(str(i+1)+"th")
                        elif i in range (11, len(positions), 100):
                            self.pri_report3.ui.position_label.setText(str(i+1)+"th")
                        elif i in range (12, len(positions), 100):
                            self.pri_report3.ui.position_label.setText(str(i+1)+"th")
                        elif i in range (0, len(positions), 10):
                            self.pri_report3.ui.position_label.setText(str(i+1)+"st")
                        elif i in range (1, len(positions), 10):
                            self.pri_report3.ui.position_label.setText(str(i+1)+"nd")
                        elif i in range (2, len(positions), 10):
                            self.pri_report3.ui.position_label.setText(str(i+1)+"rd")
                        else:
                            self.pri_report3.ui.position_label.setText(str(i+1)+"th")
                cmd4 = "SELECT * FROM t_classes WHERE class_name = ?"
                cur.execute(cmd4, (classes_combo,))
                row = cur.fetchone()
                if row[2] == None:
                    self.pri_report3.ui.master_name_label.setText(str(row[1]))
                else:
                    self.pri_report3.ui.master_name_label.setText(str(row[1]))
                    pixmap = QPixmap()
                    pixmap.loadFromData(QByteArray.fromBase64(row[2]))
                    self.pri_report3.ui.master_sig_label.setPixmap(QPixmap(pixmap))
                cmd5 = "SELECT * FROM t_senior_users WHERE role = 'headmaster'"
                cur.execute(cmd5)
                row = cur.fetchone()
                self.pri_report3.ui.head_name_label.setText(row[1])
                pixmap = QPixmap()
                pixmap.loadFromData(QByteArray.fromBase64(row[5]))
                self.pri_report3.ui.head_sig_label.setPixmap(QPixmap(pixmap))
                cmd6 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd6)
                row = cur.fetchone()
                self.pri_report3.ui.next_term_label.setText(row[3])
                cmd7 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd7)
                row = cur.fetchone()
                self.pri_report3.ui.fees_label.setText(row[6])
                cmd8 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd8)
                row = cur.fetchone()
                self.pri_report3.ui.session_label.setText(row[2])
                if self.ui.att_a_radio.isChecked() == False and self.ui.att_b_radio.isChecked() == False and self.ui.att_c_radio.isChecked() == False and self.ui.att_d_radio.isChecked() == False and self.ui.att_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grade in attendance", QMessageBox.Ok)
                elif self.ui.con_a_radio.isChecked() == False and self.ui.con_b_radio.isChecked() == False and self.ui.con_c_radio.isChecked() == False and self.ui.con_d_radio.isChecked() == False and self.ui.con_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in conduct", QMessageBox.Ok)
                elif self.ui.neat_a_radio.isChecked() == False and self.ui.neat_b_radio.isChecked() == False and self.ui.neat_c_radio.isChecked() == False and self.ui.neat_d_radio.isChecked() == False and self.ui.neat_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in neatness", QMessageBox.Ok)
                else:
                    self.printReport3()
            except Error:
                QMessageBox.critical(self, "Generating Report", "ERROR: Please ensure all pupil's scores have been recorded in all subjects", QMessageBox.Ok)
            except TypeError:
                QMessageBox.critical(self, "Generating Report", "ERROR: Please ensure all pupil's scores have been recorded in all subjects", QMessageBox.Ok)

    def generatePriReportPDF(self):
        con = sqlite3.connect("futuredb.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        classes_combo = self.ui.class_comboBox.currentText()
        admission_no = self.ui.stud_adm_no_comboBox.currentText()
        cmd1 = "SELECT * FROM t_studs WHERE admission_no = ?"
        cur.execute(cmd1, (admission_no,))
        row = cur.fetchone()
        if row == None:
            QMessageBox.critical(self, "Printing Report", "ERROR: Please select a class and pupil's admission number before generating report", QMessageBox.Ok)
        else:
            self.pri_report3.ui.name_label.setText(row[1])
            self.pri_report3.ui.class_label.setText(row[3])
            self.pri_report3.ui.sex_label.setText(row[5])
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray.fromBase64(row[6]))
            self.pri_report3.ui.photo_label.setPixmap(QPixmap(pixmap))
            try:
                cmd3 = "SELECT * FROM t_pri_scores_third WHERE stud_no = ?"
                cur.execute(cmd3, (admission_no,))
                row = cur.fetchone()
                self.pri_report3.ui.qur_c1_label.setText(str(row[3]))
                self.pri_report3.ui.qur_c2_label.setText(str(row[4]))
                self.pri_report3.ui.qur_ass_label.setText(str(row[5]))
                self.pri_report3.ui.qur_exam_label.setText(str(row[6]))
                self.pri_report3.ui.qur_total_label.setText(str(row[7]))
                if row[7] < 40:
                    self.pri_report3.ui.qur_grade_label.setText("F")
                    self.pri_report3.ui.qur_remark_label.setText("Fail")
                elif row[7] >= 40 and row[7] < 50:
                    self.pri_report3.ui.qur_grade_label.setText("D")
                    self.pri_report3.ui.qur_remark_label.setText("Pass")
                elif row[7] >= 50 and row[7] < 60:
                    self.pri_report3.ui.qur_grade_label.setText("C")
                    self.pri_report3.ui.qur_remark_label.setText("Good")
                elif row[7] >= 60 and row[7] < 70:
                    self.pri_report3.ui.qur_grade_label.setText("B")
                    self.pri_report3.ui.qur_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.qur_grade_label.setText("A")
                    self.pri_report3.ui.qur_remark_label.setText("Excellent")
                self.pri_report3.ui.ibadat_c1_label.setText(str(row[8]))
                self.pri_report3.ui.ibadat_c2_label.setText(str(row[9]))
                self.pri_report3.ui.ibadat_ass_label.setText(str(row[10]))
                self.pri_report3.ui.ibadat_exam_label.setText(str(row[11]))
                self.pri_report3.ui.ibadat_total_label.setText(str(row[12]))
                if row[12] < 40:
                    self.pri_report3.ui.ibadat_grade_label.setText("F")
                    self.pri_report3.ui.ibadat_remark_label.setText("Fail")
                elif row[12] >= 40 and row[12] < 50:
                    self.pri_report3.ui.ibadat_grade_label.setText("D")
                    self.pri_report3.ui.ibadat_remark_label.setText("Pass")
                elif row[12] >= 50 and row[12] < 60:
                    self.pri_report3.ui.ibadat_grade_label.setText("C")
                    self.pri_report3.ui.ibadat_remark_label.setText("Good")
                elif row[12] >= 60 and row[12] < 70:
                    self.pri_report3.ui.ibadat_grade_label.setText("B")
                    self.pri_report3.ui.ibadat_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.ibadat_grade_label.setText("A")
                    self.pri_report3.ui.ibadat_remark_label.setText("Excellent")
                self.pri_report3.ui.arabic1_c1_label.setText(str(row[13]))
                self.pri_report3.ui.arabic1_c2_label.setText(str(row[14]))
                self.pri_report3.ui.arabic1_ass_label.setText(str(row[15]))
                self.pri_report3.ui.arabic1_exam_label.setText(str(row[16]))
                self.pri_report3.ui.arabic1_total_label.setText(str(row[17]))
                if row[17] < 40:
                    self.pri_report3.ui.arabic1_grade_label.setText("F")
                    self.pri_report3.ui.arabic1_remark_label.setText("Fail")
                elif row[17] >= 40 and row[17] < 50:
                    self.pri_report3.ui.arabic1_grade_label.setText("D")
                    self.pri_report3.ui.arabic1_remark_label.setText("Pass")
                elif row[17] >= 50 and row[17] < 60:
                    self.pri_report3.ui.arabic1_grade_label.setText("C")
                    self.pri_report3.ui.arabic1_remark_label.setText("Good")
                elif row[17] >= 60 and row[17] < 70:
                    self.pri_report3.ui.arabic1_grade_label.setText("B")
                    self.pri_report3.ui.arabic1_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.arabic1_grade_label.setText("A")
                    self.pri_report3.ui.arabic1_remark_label.setText("Excellent")
                self.pri_report3.ui.arabic2_c1_label.setText(str(row[18]))
                self.pri_report3.ui.arabic2_c2_label.setText(str(row[19]))
                self.pri_report3.ui.arabic2_ass_label.setText(str(row[20]))
                self.pri_report3.ui.arabic2_exam_label.setText(str(row[21]))
                self.pri_report3.ui.arabic2_total_label.setText(str(row[22]))
                if row[22] < 40:
                    self.pri_report3.ui.arabic2_grade_label.setText("F")
                    self.pri_report3.ui.arabic2_remark_label.setText("Fail")
                elif row[22] >= 40 and row[22] < 50:
                    self.pri_report3.ui.arabic2_grade_label.setText("D")
                    self.pri_report3.ui.arabic2_remark_label.setText("Pass")
                elif row[22] >= 50 and row[22] < 60:
                    self.pri_report3.ui.arabic2_grade_label.setText("C")
                    self.pri_report3.ui.arabic2_remark_label.setText("Good")
                elif row[22] >= 60 and row[22] < 70:
                    self.pri_report3.ui.arabic2_grade_label.setText("B")
                    self.pri_report3.ui.arabic2_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.arabic2_grade_label.setText("A")
                    self.pri_report3.ui.arabic2_remark_label.setText("Excellent")
                self.pri_report3.ui.math_c1_label.setText(str(row[23]))
                self.pri_report3.ui.math_c2_label.setText(str(row[24]))
                self.pri_report3.ui.math_ass_label.setText(str(row[25]))
                self.pri_report3.ui.math_exam_label.setText(str(row[26]))
                self.pri_report3.ui.math_total_label.setText(str(row[27]))
                if row[27] < 40:
                    self.pri_report3.ui.math_grade_label.setText("F")
                    self.pri_report3.ui.math_remark_label.setText("Fail")
                elif row[27] >= 40 and row[27] < 50:
                    self.pri_report3.ui.math_grade_label.setText("D")
                    self.pri_report3.ui.math_remark_label.setText("Pass")
                elif row[27] >= 50 and row[27] < 60:
                    self.pri_report3.ui.math_grade_label.setText("C")
                    self.pri_report3.ui.math_remark_label.setText("Good")
                elif row[27] >= 60 and row[27] < 70:
                    self.pri_report3.ui.math_grade_label.setText("B")
                    self.pri_report3.ui.math_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.math_grade_label.setText("A")
                    self.pri_report3.ui.math_remark_label.setText("Excellent")
                self.pri_report3.ui.eng_c1_label.setText(str(row[28]))
                self.pri_report3.ui.eng_c2_label.setText(str(row[29]))
                self.pri_report3.ui.eng_ass_label.setText(str(row[30]))
                self.pri_report3.ui.eng_exam_label.setText(str(row[31]))
                self.pri_report3.ui.eng_total_label.setText(str(row[32]))
                if row[32] < 40:
                    self.pri_report3.ui.eng_grade_label.setText("F")
                    self.pri_report3.ui.eng_remark_label.setText("Fail")
                elif row[32] >= 40 and row[32] < 50:
                    self.pri_report3.ui.eng_grade_label.setText("D")
                    self.pri_report3.ui.eng_remark_label.setText("Pass")
                elif row[32] >= 50 and row[32] < 60:
                    self.pri_report3.ui.eng_grade_label.setText("C")
                    self.pri_report3.ui.eng_remark_label.setText("Good")
                elif row[32] >= 60 and row[32] < 70:
                    self.pri_report3.ui.eng_grade_label.setText("B")
                    self.pri_report3.ui.eng_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.eng_grade_label.setText("A")
                    self.pri_report3.ui.eng_remark_label.setText("Excellent")
                self.pri_report3.ui.comp_c1_label.setText(str(row[33]))
                self.pri_report3.ui.comp_c2_label.setText(str(row[34]))
                self.pri_report3.ui.comp_ass_label.setText(str(row[35]))
                self.pri_report3.ui.comp_exam_label.setText(str(row[36]))
                self.pri_report3.ui.comp_total_label.setText(str(row[37]))
                if row[37] < 40:
                    self.pri_report3.ui.comp_grade_label.setText("F")
                    self.pri_report3.ui.comp_remark_label.setText("Fail")
                elif row[37] >= 40 and row[37] < 50:
                    self.pri_report3.ui.comp_grade_label.setText("D")
                    self.pri_report3.ui.comp_remark_label.setText("Pass")
                elif row[37] >= 50 and row[37] < 60:
                    self.pri_report3.ui.comp_grade_label.setText("C")
                    self.pri_report3.ui.comp_remark_label.setText("Good")
                elif row[37] >= 60 and row[37] < 70:
                    self.pri_report3.ui.comp_grade_label.setText("B")
                    self.pri_report3.ui.comp_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.comp_grade_label.setText("A")
                    self.pri_report3.ui.comp_remark_label.setText("Excellent")
                self.pri_report3.ui.bas_sc_c1_label.setText(str(row[38]))
                self.pri_report3.ui.bas_sc_c2_label.setText(str(row[39]))
                self.pri_report3.ui.bas_sc_ass_label.setText(str(row[40]))
                self.pri_report3.ui.bas_sc_exam_label.setText(str(row[41]))
                self.pri_report3.ui.bas_sc_total_label.setText(str(row[42]))
                if row[42] < 40:
                    self.pri_report3.ui.bas_sc_grade_label.setText("F")
                    self.pri_report3.ui.bas_sc_remark_label.setText("Fail")
                elif row[42] >= 40 and row[42] < 50:
                    self.pri_report3.ui.bas_sc_grade_label.setText("D")
                    self.pri_report3.ui.bas_sc_remark_label.setText("Pass")
                elif row[42] >= 50 and row[42] < 60:
                    self.pri_report3.ui.bas_sc_grade_label.setText("C")
                    self.pri_report3.ui.bas_sc_remark_label.setText("Good")
                elif row[42] >= 60 and row[42] < 70:
                    self.pri_report3.ui.bas_sc_grade_label.setText("B")
                    self.pri_report3.ui.bas_sc_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.bas_sc_grade_label.setText("A")
                    self.pri_report3.ui.bas_sc_remark_label.setText("Excellent")
                self.pri_report3.ui.religion_c1_label.setText(str(row[43]))
                self.pri_report3.ui.religion_c2_label.setText(str(row[44]))
                self.pri_report3.ui.religion_ass_label.setText(str(row[45]))
                self.pri_report3.ui.religion_exam_label.setText(str(row[46]))
                self.pri_report3.ui.religion_total_label.setText(str(row[47]))
                if row[47] < 40:
                    self.pri_report3.ui.religion_grade_label.setText("F")
                    self.pri_report3.ui.religion_remark_label.setText("Fail")
                elif row[47] >= 40 and row[47] < 50:
                    self.pri_report3.ui.religion_grade_label.setText("D")
                    self.pri_report3.ui.religion_remark_label.setText("Pass")
                elif row[47] >= 50 and row[47] < 60:
                    self.pri_report3.ui.religion_grade_label.setText("C")
                    self.pri_report3.ui.religion_remark_label.setText("Good")
                elif row[47] >= 60 and row[47] < 70:
                    self.pri_report3.ui.religion_grade_label.setText("B")
                    self.pri_report3.ui.religion_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.religion_grade_label.setText("A")
                    self.pri_report3.ui.religion_remark_label.setText("Excellent")
                self.pri_report3.ui.civic_c1_label.setText(str(row[48]))
                self.pri_report3.ui.civic_c2_label.setText(str(row[49]))
                self.pri_report3.ui.civic_ass_label.setText(str(row[50]))
                self.pri_report3.ui.civic_exam_label.setText(str(row[51]))
                self.pri_report3.ui.civic_total_label.setText(str(row[52]))
                if row[52] < 40:
                    self.pri_report3.ui.civic_grade_label.setText("F")
                    self.pri_report3.ui.civic_remark_label.setText("Fail")
                elif row[52] >= 40 and row[52] < 50:
                    self.pri_report3.ui.civic_grade_label.setText("D")
                    self.pri_report3.ui.civic_remark_label.setText("Pass")
                elif row[52] >= 50 and row[52] < 60:
                    self.pri_report3.ui.civic_grade_label.setText("C")
                    self.pri_report3.ui.civic_remark_label.setText("Good")
                elif row[52] >= 60 and row[52] < 70:
                    self.pri_report3.ui.civic_grade_label.setText("B")
                    self.pri_report3.ui.civic_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.civic_grade_label.setText("A")
                    self.pri_report3.ui.civic_remark_label.setText("Excellent")
                self.pri_report3.ui.verbal_c1_label.setText(str(row[53]))
                self.pri_report3.ui.verbal_c2_label.setText(str(row[54]))
                self.pri_report3.ui.verbal_ass_label.setText(str(row[55]))
                self.pri_report3.ui.verbal_exam_label.setText(str(row[56]))
                self.pri_report3.ui.verbal_total_label.setText(str(row[57]))
                if row[57] < 40:
                    self.pri_report3.ui.verbal_grade_label.setText("F")
                    self.pri_report3.ui.verbal_remark_label.setText("Fail")
                elif row[57] >= 40 and row[57] < 50:
                    self.pri_report3.ui.verbal_grade_label.setText("D")
                    self.pri_report3.ui.verbal_remark_label.setText("Pass")
                elif row[57] >= 50 and row[57] < 60:
                    self.pri_report3.ui.verbal_grade_label.setText("C")
                    self.pri_report3.ui.verbal_remark_label.setText("Good")
                elif row[57] >= 60 and row[57] < 70:
                    self.pri_report3.ui.verbal_grade_label.setText("B")
                    self.pri_report3.ui.verbal_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.verbal_grade_label.setText("A")
                    self.pri_report3.ui.verbal_remark_label.setText("Excellent")
                self.pri_report3.ui.quant_c1_label.setText(str(row[58]))
                self.pri_report3.ui.quant_c2_label.setText(str(row[59]))
                self.pri_report3.ui.quant_ass_label.setText(str(row[60]))
                self.pri_report3.ui.quant_exam_label.setText(str(row[61]))
                self.pri_report3.ui.quant_total_label.setText(str(row[62]))
                if row[62] < 40:
                    self.pri_report3.ui.quant_grade_label.setText("F")
                    self.pri_report3.ui.quant_remark_label.setText("Fail")
                elif row[62] >= 40 and row[62] < 50:
                    self.pri_report3.ui.quant_grade_label.setText("D")
                    self.pri_report3.ui.quant_remark_label.setText("Pass")
                elif row[62] >= 50 and row[62] < 60:
                    self.pri_report3.ui.quant_grade_label.setText("C")
                    self.pri_report3.ui.quant_remark_label.setText("Good")
                elif row[62] >= 60 and row[62] < 70:
                    self.pri_report3.ui.quant_grade_label.setText("B")
                    self.pri_report3.ui.quant_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.quant_grade_label.setText("A")
                    self.pri_report3.ui.quant_remark_label.setText("Excellent")
                self.pri_report3.ui.basic_c1_label.setText(str(row[63]))
                self.pri_report3.ui.basic_c2_label.setText(str(row[64]))
                self.pri_report3.ui.basic_ass_label.setText(str(row[65]))
                self.pri_report3.ui.basic_exam_label.setText(str(row[66]))
                self.pri_report3.ui.basic_total_label.setText(str(row[67]))
                if row[67] < 40:
                    self.pri_report3.ui.basic_grade_label.setText("F")
                    self.pri_report3.ui.basic_remark_label.setText("Fail")
                elif row[67] >= 40 and row[67] < 50:
                    self.pri_report3.ui.basic_grade_label.setText("D")
                    self.pri_report3.ui.basic_remark_label.setText("Pass")
                elif row[67] >= 50 and row[67] < 60:
                    self.pri_report3.ui.basic_grade_label.setText("C")
                    self.pri_report3.ui.basic_remark_label.setText("Good")
                elif row[67] >= 60 and row[67] < 70:
                    self.pri_report3.ui.basic_grade_label.setText("B")
                    self.pri_report3.ui.basic_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.basic_grade_label.setText("A")
                    self.pri_report3.ui.basic_remark_label.setText("Excellent")
                self.pri_report3.ui.french_c1_label.setText(str(row[68]))
                self.pri_report3.ui.french_c2_label.setText(str(row[69]))
                self.pri_report3.ui.french_ass_label.setText(str(row[70]))
                self.pri_report3.ui.french_exam_label.setText(str(row[71]))
                self.pri_report3.ui.french_total_label.setText(str(row[72]))
                if row[72] < 40:
                    self.pri_report3.ui.french_grade_label.setText("F")
                    self.pri_report3.ui.french_remark_label.setText("Fail")
                elif row[72] >= 40 and row[72] < 50:
                    self.pri_report3.ui.french_grade_label.setText("D")
                    self.pri_report3.ui.french_remark_label.setText("Pass")
                elif row[72] >= 50 and row[72] < 60:
                    self.pri_report3.ui.french_grade_label.setText("C")
                    self.pri_report3.ui.french_remark_label.setText("Good")
                elif row[72] >= 60 and row[72] < 70:
                    self.pri_report3.ui.french_grade_label.setText("B")
                    self.pri_report3.ui.french_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.french_grade_label.setText("A")
                    self.pri_report3.ui.french_remark_label.setText("Excellent")
                self.pri_report3.ui.jolly_c1_label.setText(str(row[73]))
                self.pri_report3.ui.jolly_c2_label.setText(str(row[74]))
                self.pri_report3.ui.jolly_ass_label.setText(str(row[75]))
                self.pri_report3.ui.jolly_exam_label.setText(str(row[76]))
                self.pri_report3.ui.jolly_total_label.setText(str(row[77]))
                if row[77] < 40:
                    self.pri_report3.ui.jolly_grade_label.setText("F")
                    self.pri_report3.ui.jolly_remark_label.setText("Fail")
                elif row[77] >= 40 and row[77] < 50:
                    self.pri_report3.ui.jolly_grade_label.setText("D")
                    self.pri_report3.ui.jolly_remark_label.setText("Pass")
                elif row[77] >= 50 and row[77] < 60:
                    self.pri_report3.ui.jolly_grade_label.setText("C")
                    self.pri_report3.ui.jolly_remark_label.setText("Good")
                elif row[77] >= 60 and row[77] < 70:
                    self.pri_report3.ui.jolly_grade_label.setText("B")
                    self.pri_report3.ui.jolly_remark_label.setText("Very Good")
                else:
                    self.pri_report3.ui.jolly_grade_label.setText("A")
                    self.pri_report3.ui.jolly_remark_label.setText("Excellent")
                self.pri_report3.ui.total_scores3_label.setText(str(row[78]))
                self.pri_report3.ui.avg3_label.setText(str(row[79]))
                self.pri_report3.ui.total_cum_label.setText(str(row[80]))
                self.pri_report3.ui.avg_cum_label.setText(str(row[81]))
                if row[79] < 40:
                    self.pri_report3.ui.master_com_label.setText("Bad result. Be careful.")
                    self.pri_report3.ui.head_com_label.setText("Bad result.")
                elif row[79] >= 40 and row[79] < 50:
                    self.pri_report3.ui.master_com_label.setText("Weak result. Work hard.")
                    self.pri_report3.ui.head_com_label.setText("Weak result.")
                elif row[79] >= 50 and row[79] < 60:
                    self.pri_report3.ui.master_com_label.setText("Fair result. Work hard.")
                    self.pri_report3.ui.head_com_label.setText("Fair result.")
                elif row[79] >= 60 and row[79] < 70:
                    self.pri_report3.ui.master_com_label.setText("Good result. Put more effort.")
                    self.pri_report3.ui.head_com_label.setText("Good result.")
                else:
                    self.pri_report3.ui.master_com_label.setText("Excellent result. Keep on.")
                    self.pri_report3.ui.head_com_label.setText("Excellent result.")
                cmd9 = "SELECT * FROM t_pri_scores_first WHERE stud_no = ?"
                cur.execute(cmd9, (admission_no,))
                row = cur.fetchone()
                if row == None:
                    self.pri_report3.ui.total_scores_label.setText("None")
                    self.pri_report3.ui.avg_label.setText("None")
                elif row[78] == None and row[79] == None:
                    self.pri_report3.ui.total_scores_label.setText("None")
                    self.pri_report3.ui.avg_label.setText("None")
                else:
                    self.pri_report3.ui.total_scores_label.setText(str(row[78]))
                    self.pri_report3.ui.avg_label.setText(str(row[79]))
                cmd10 = "SELECT * FROM t_pri_scores_second WHERE stud_no = ?"
                cur.execute(cmd10, (admission_no,))
                row = cur.fetchone()
                if row == None:
                    self.pri_report3.ui.total_scores2_label.setText("None")
                    self.pri_report3.ui.avg2_label.setText("None")
                elif row[78] == None and row[79] == None:
                    self.pri_report3.ui.total_scores2_label.setText("None")
                    self.pri_report3.ui.avg2_label.setText("None")
                else:
                    self.pri_report3.ui.total_scores2_label.setText(str(row[78]))
                    self.pri_report3.ui.avg2_label.setText(str(row[79]))
                positions = []
                cmd11 = "SELECT * FROM t_pri_scores_third WHERE score_class = ? ORDER BY avg_cum DESC"
                cur.execute(cmd11, (classes_combo,))
                rows = cur.fetchall()
                for row in rows:
                    positions.append(row[1])
                self.pri_report3.ui.out_of_label.setText(str(len(positions)))
                for i in range(len(positions)):
                    if admission_no == positions[i]:
                        if i in range (10, len(positions), 100):
                            self.pri_report3.ui.position_label.setText(str(i+1)+"th")
                        elif i in range (11, len(positions), 100):
                            self.pri_report3.ui.position_label.setText(str(i+1)+"th")
                        elif i in range (12, len(positions), 100):
                            self.pri_report3.ui.position_label.setText(str(i+1)+"th")
                        elif i in range (0, len(positions), 10):
                            self.pri_report3.ui.position_label.setText(str(i+1)+"st")
                        elif i in range (1, len(positions), 10):
                            self.pri_report3.ui.position_label.setText(str(i+1)+"nd")
                        elif i in range (2, len(positions), 10):
                            self.pri_report3.ui.position_label.setText(str(i+1)+"rd")
                        else:
                            self.pri_report3.ui.position_label.setText(str(i+1)+"th")
                cmd4 = "SELECT * FROM t_classes WHERE class_name = ?"
                cur.execute(cmd4, (classes_combo,))
                row = cur.fetchone()
                if row[2] == None:
                    self.pri_report3.ui.master_name_label.setText(str(row[1]))
                else:
                    self.pri_report3.ui.master_name_label.setText(str(row[1]))
                    pixmap = QPixmap()
                    pixmap.loadFromData(QByteArray.fromBase64(row[2]))
                    self.pri_report3.ui.master_sig_label.setPixmap(QPixmap(pixmap))
                cmd5 = "SELECT * FROM t_senior_users WHERE role = 'headmaster'"
                cur.execute(cmd5)
                row = cur.fetchone()
                self.pri_report3.ui.head_name_label.setText(row[1])
                pixmap = QPixmap()
                pixmap.loadFromData(QByteArray.fromBase64(row[5]))
                self.pri_report3.ui.head_sig_label.setPixmap(QPixmap(pixmap))
                cmd6 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd6)
                row = cur.fetchone()
                self.pri_report3.ui.next_term_label.setText(row[3])
                cmd7 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd7)
                row = cur.fetchone()
                self.pri_report3.ui.fees_label.setText(row[6])
                cmd8 = "SELECT * FROM t_senior_users WHERE role = 'mgmt'"
                cur.execute(cmd8)
                row = cur.fetchone()
                self.pri_report3.ui.session_label.setText(row[2])
                if self.ui.att_a_radio.isChecked() == False and self.ui.att_b_radio.isChecked() == False and self.ui.att_c_radio.isChecked() == False and self.ui.att_d_radio.isChecked() == False and self.ui.att_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grade in attendance", QMessageBox.Ok)
                elif self.ui.con_a_radio.isChecked() == False and self.ui.con_b_radio.isChecked() == False and self.ui.con_c_radio.isChecked() == False and self.ui.con_d_radio.isChecked() == False and self.ui.con_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in conduct", QMessageBox.Ok)
                elif self.ui.neat_a_radio.isChecked() == False and self.ui.neat_b_radio.isChecked() == False and self.ui.neat_c_radio.isChecked() == False and self.ui.neat_d_radio.isChecked() == False and self.ui.neat_e_radio.isChecked() == False:
                    QMessageBox.critical(self, "Printing Report", "ERROR: Please select pupil's grades in neatness", QMessageBox.Ok)
                else:
                    self.printPDF3()
            except Error:
                QMessageBox.critical(self, "Generating Report", "ERROR: Please ensure all pupil's scores have been recorded in all subjects", QMessageBox.Ok)
            except TypeError:
                QMessageBox.critical(self, "Generating Report", "ERROR: Please ensure all pupil's scores have been recorded in all subjects", QMessageBox.Ok)

    def displayRadios(self):
        if self.ui.att_a_radio.isChecked():
            self.pri_report3.ui.att_a_label.setText("v")
            self.pri_report3.ui.att_b_label.setText("")
            self.pri_report3.ui.att_c_label.setText("")
            self.pri_report3.ui.att_d_label.setText("")
            self.pri_report3.ui.att_e_label.setText("")
        elif self.ui.att_b_radio.isChecked():
            self.pri_report3.ui.att_a_label.setText("")
            self.pri_report3.ui.att_b_label.setText("v")
            self.pri_report3.ui.att_c_label.setText("")
            self.pri_report3.ui.att_d_label.setText("")
            self.pri_report3.ui.att_e_label.setText("")
        elif self.ui.att_c_radio.isChecked():
            self.pri_report3.ui.att_a_label.setText("")
            self.pri_report3.ui.att_b_label.setText("")
            self.pri_report3.ui.att_c_label.setText("v")
            self.pri_report3.ui.att_d_label.setText("")
            self.pri_report3.ui.att_e_label.setText("")
        elif self.ui.att_d_radio.isChecked():
            self.pri_report3.ui.att_a_label.setText("")
            self.pri_report3.ui.att_b_label.setText("")
            self.pri_report3.ui.att_c_label.setText("")
            self.pri_report3.ui.att_d_label.setText("v")
            self.pri_report3.ui.att_e_label.setText("")
        elif self.ui.att_e_radio.isChecked():
            self.pri_report3.ui.att_a_label.setText("")
            self.pri_report3.ui.att_b_label.setText("")
            self.pri_report3.ui.att_c_label.setText("")
            self.pri_report3.ui.att_d_label.setText("")
            self.pri_report3.ui.att_e_label.setText("v")
        if self.ui.con_a_radio.isChecked():
            self.pri_report3.ui.con_a_label.setText("v")
            self.pri_report3.ui.con_b_label.setText("")
            self.pri_report3.ui.con_c_label.setText("")
            self.pri_report3.ui.con_d_label.setText("")
            self.pri_report3.ui.con_e_label.setText("")
        elif self.ui.con_b_radio.isChecked():
            self.pri_report3.ui.con_a_label.setText("")
            self.pri_report3.ui.con_b_label.setText("v")
            self.pri_report3.ui.con_c_label.setText("")
            self.pri_report3.ui.con_d_label.setText("")
            self.pri_report3.ui.con_e_label.setText("")
        elif self.ui.con_c_radio.isChecked():
            self.pri_report3.ui.con_a_label.setText("")
            self.pri_report3.ui.con_b_label.setText("")
            self.pri_report3.ui.con_c_label.setText("v")
            self.pri_report3.ui.con_d_label.setText("")
            self.pri_report3.ui.con_e_label.setText("")
        elif self.ui.con_d_radio.isChecked():
            self.pri_report3.ui.con_a_label.setText("")
            self.pri_report3.ui.con_b_label.setText("")
            self.pri_report3.ui.con_c_label.setText("")
            self.pri_report3.ui.con_d_label.setText("v")
            self.pri_report3.ui.con_e_label.setText("")
        elif self.ui.con_e_radio.isChecked():
            self.pri_report3.ui.con_a_label.setText("")
            self.pri_report3.ui.con_b_label.setText("")
            self.pri_report3.ui.con_c_label.setText("")
            self.pri_report3.ui.con_d_label.setText("")
            self.pri_report3.ui.con_e_label.setText("v")
        if self.ui.neat_a_radio.isChecked():
            self.pri_report3.ui.neat_a_label.setText("v")
            self.pri_report3.ui.neat_b_label.setText("")
            self.pri_report3.ui.neat_c_label.setText("")
            self.pri_report3.ui.neat_d_label.setText("")
            self.pri_report3.ui.neat_e_label.setText("")
        elif self.ui.neat_b_radio.isChecked():
            self.pri_report3.ui.neat_a_label.setText("")
            self.pri_report3.ui.neat_b_label.setText("v")
            self.pri_report3.ui.neat_c_label.setText("")
            self.pri_report3.ui.neat_d_label.setText("")
            self.pri_report3.ui.neat_e_label.setText("")
        elif self.ui.neat_b_radio.isChecked():
            self.pri_report3.ui.neat_a_label.setText("")
            self.pri_report3.ui.neat_b_label.setText("v")
            self.pri_report3.ui.neat_c_label.setText("")
            self.pri_report3.ui.neat_d_label.setText("")
            self.pri_report3.ui.neat_e_label.setText("")
        elif self.ui.neat_c_radio.isChecked():
            self.pri_report3.ui.neat_a_label.setText("")
            self.pri_report3.ui.neat_b_label.setText("")
            self.pri_report3.ui.neat_c_label.setText("v")
            self.pri_report3.ui.neat_d_label.setText("")
            self.pri_report3.ui.neat_e_label.setText("")
        elif self.ui.neat_d_radio.isChecked():
            self.pri_report3.ui.neat_a_label.setText("")
            self.pri_report3.ui.neat_b_label.setText("")
            self.pri_report3.ui.neat_c_label.setText("")
            self.pri_report3.ui.neat_d_label.setText("v")
            self.pri_report3.ui.neat_e_label.setText("")
        elif self.ui.neat_e_radio.isChecked():
            self.pri_report3.ui.neat_a_label.setText("")
            self.pri_report3.ui.neat_b_label.setText("")
            self.pri_report3.ui.neat_c_label.setText("")
            self.pri_report3.ui.neat_d_label.setText("")
            self.pri_report3.ui.neat_e_label.setText("v")

    def printReport3(self):
        printer = QPrinter(QtPrintSupport.QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            painter = QPainter()
            painter.begin(printer)
            xscale = printer.pageRect().width() * 1.0 / self.pri_report3.width()
            yscale = printer.pageRect().height() * 1.0 / self.pri_report3.height()
            scale = min(xscale, yscale)
            painter.translate(printer.paperRect().center())
            painter.scale(scale, scale)
            painter.translate(-self.pri_report3.width() / 2, -self.pri_report3.height() / 2)
            self.pri_report3.render(painter)
            painter.end()

    def print_widget(self, widget, filename):
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        printer.setOutputFileName(filename)
        painter = QtGui.QPainter(printer)
        xscale = printer.pageRect().width() * 1.0 / widget.width()
        yscale = printer.pageRect().height() * 1.0 / widget.height()
        scale = min(xscale, yscale)
        painter.translate(printer.paperRect().center())
        painter.scale(scale, scale)
        painter.translate(-widget.width() / 2, -widget.height() / 2)
        widget.render(painter)
        painter.end()

    def printPDF3(self):
        fn, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Export PDF", None, "PDF files (.pdf);;All Files()"
        )
        if fn:
            if QtCore.QFileInfo(fn).suffix() == "":
                fn += ".pdf"
            self.print_widget(self.pri_report3, fn)

class PriReport3(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PriReport3rdForm()
        self.ui.setupUi(self)
        #Generates Current Date
        self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.ui.dateTimeEdit.hide()
        self.ui.print_date_label.setText(self.ui.dateTimeEdit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pri_scores_record = PriScoresRecord()
    pri_scores_record.show()
    sys.exit(app.exec_())
