import tkinter as tk
import tkinter as ttk
from tkinter import ttk
import sqlite3
from tkinter import *
from variables import *
from tkinter import messagebox
import tkinter as msgb



"""def drop():
    connection=sqlite3.connect('studentdata.db')
    cur=connection.cursor()
    cur.execute("DROP TABLE centres")
    
drop()
"""
def create():
    connection=sqlite3.connect('studentdata.db')
    cur=connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students(student_id VARCHAR PRIMARY KEY,\
                                                      student_name VARCHAR(150) NOT NULL,\
                                                        gender VARCHAR(10),\
                                                            center_name VARCHAR(20),\
                                                                 class_type VARCHAR(30),\
                                                                      contact_number VARCHAR(20),\
                                                                         level VARCHAR(30),\
                                                                             date_of_admission DATE,\
                                                                                 feePayable,\
                                                                                 FOREIGN KEY (center_name) REFERENCES centres (center_name) )")
    
    cur.execute("CREATE TABLE IF NOT EXISTS subjects(subject_no INT,\
            subject_name VARCHAR PRIMARY KEY,\
            level VARCHAR(30))")
    cur.execute("CREATE TABLE IF NOT EXISTS centres(center_name VARCHAR PRIMARY KEY,\
            population INT,\
                expectedFee INT,\
                    feePaid INT,\
                        arreas INT,\
                            expenses INT )")
    cur.execute('CREATE TABLE IF NOT EXISTS fee(invoice_no VARCHAR PRIMARY KEY,\
        date DATE, \
            student_id,\
                center_name, \
                    paid integer, \
                    fee_payable integer,\
                            arreas integer,\
                                FOREIGN KEY (student_id) REFERENCES students(student_id),\
                                    FOREIGN KEY (center_name) REFERENCES centres(center_name))')
    cur.execute("CREATE TABLE IF NOT EXISTS expence(receiptNo VARCHAR PRIMARY KEY,\
        center_name,\
            purpose VARCHAR,\
                amount VARCHAR,\
                    date DATE,\
                    FOREIGN KEY (center_name) REFERENCES centres(center_name))")
    cur.execute('CREATE TABLE IF NOT EXISTS attendance (attendance_no INT PRIMARY KEY, \
        center_name VARCHAR,\
            subject_name VARCHAR,\
                student_id VARCHAR, \
                    attendance_grade,\
                        class_type VARCHAR,\
                            lecturer_name VARCHAR(100),\
                                date_taught DATE,\
                                    lecture_grade VARCHAR(10),\
                                        examined DATE, \
                                            FOREIGN KEY (student_id) REFERENCES students(student_id),\
                                                FOREIGN KEY (center_name) REFERENCES centres(center_name),\
                                                    FOREIGN KEY (subject_name) REFERENCES subjects (subject_name))')
                
    connection.commit()
def insert_expence():
    connection=sqlite3.connect('studentdata.db')
    cur=connection.cursor()
    cur.execute("SELECT EXISTS (SELECT 1 FROM expence  WHERE receiptNo='"+str(rct_no.get())+"')")
    exists = cur.fetchone()[0]
    if exists:
        messagebox.showerror('Record already exists', 'That  Receipt Number already exist, Please check and try again')
    else:
        if (rct_no.get()=="" or rct_no.get()==" ") or (cntr.get()=="" or cntr.get()==" ") or (ppse.get()=="" or ppse.get()==" ") or\
            (amnt.get()=="" or amnt.get()==" ") or (dat.get()=="" or dat.get()==" "):
            messagebox.showerror('Missing field', 'Please check and fill in all fields')
        else:
            cur.execute("INSERT INTO expence values(?,?,?,?,?)", (rct_no.get(),
                                                cntr.get(),
                                                ppse.get(),
                                                amnt.get(),
                                                dat.get()))
        
            messagebox.showinfo("Success","👍\nRecord has been inserted")
        connection.commit()
    
    expClear()
def updateExpense():
    connection=sqlite3.connect('studentdata.db')
    cur=connection.cursor()
    if (rct_no.get()=="" or rct_no.get()==" ") or (cntr.get()=="" or cntr.get()==" ") or (ppse.get()=="" or ppse.get()==" ") or\
            (amnt.get()=="" or amnt.get()==" ") or (dat.get()=="" or dat.get()==" "):
            messagebox.showerror('Missing field', 'Please check and fill in all fields')
    else:
        cur.execute("UPDATE expences SET receiptNo=?, center_name=?, purpose=?, amount=?, date=? WHERE receiptNo='"+str(rct_no.get())+"'",
                                           (rct_no.get(),
                                            cntr.get(),
                                            ppse.get(),
                                            amnt.get(),
                                            dat.get()))
    
        messagebox.showinfo("Success","👍\nRecord has been inserted")
    connection.commit()
def SearchExpence():
  
        connection=sqlite3.connect('studentdata.db')
        cur=connection.cursor()

 
       

def insert_fee():
    connection=sqlite3.connect('studentdata.db')
    cur=connection.cursor()
    
    cur.execute("SELECT EXISTS (SELECT 1 FROM fee  WHERE invoice_no='"+str(invce_no.get())+"')")
    exists = cur.fetchone()[0]
    if exists:
        messagebox.showerror('Record already exists', 'That  Invoice Number already exist, Please check and try again')
    else:
        if (invce_no.get()==""or invce_no.get()==" ")or\
            (inv_date.get()=="" or inv_date.get()=="") or\
            (student_idNo.get()=="" or student_idNo.get()==" ")or\
            (center_idNo.get()=="" or center_idNo.get()==" " )or\
            (studpaid.get()=="" or studpaid.get()==" " )or\
            (studfee_payable.get()=="" or studfee_payable.get()==" ") or\
            (stud_fee_arreas.get()=="" or stud_fee_arreas.get()==""):
            messagebox.showerror('Missing field', 'Please check and fill in all fields')
        else:
            cur.execute("INSERT INTO fee values(?,?,?,?,?,?,?)",( invce_no.get(),
                                                            inv_date.get(),
                                                            student_idNo.get(),
                                                             center_idNo.get(),
                                                              studpaid.get(),                                                               
                                                                studfee_payable.get(),
                                                                    stud_fee_arreas.get()))
           
            messagebox.showinfo("Success","👍\nRecord has been inserted")
        connection.commit()
        clearFee()
def updateFee():
    connection=sqlite3.connect('studentdata.db')
    cur=connection.cursor() 
    if (invce_no.get()==""or invce_no.get()==" ")or\
            (inv_date.get()=="" or inv_date.get()=="") or\
            (student_idNo.get()=="" or student_idNo.get()==" ")or\
            (center_idNo.get()=="" or center_idNo.get()==" " )or\
            (studpaid.get()=="" or studpaid.get()==" " )or\
            (studfee_payable.get()=="" or studfee_payable.get()==" ") or\
            (stud_fee_arreas.get()=="" or stud_fee_arreas.get()==""):
            messagebox.showerror('Missing field', 'Please check and fill in all fields')
    else:
        cur.execute("UPDATE fee SET invoice_no=?,\
        date =?, \
            student_id=?,\
                center_name=?, \
                    paid integer=?, \
                    fee_payable integer=?,\
                            arreas integer=? WHERE invoice_no='"+str(att_no.get())+"'",
                                                       ( invce_no.get(),
                                                        inv_date.get(),
                                                        student_idNo.get(),
                                                            center_idNo.get(),
                                                            studpaid.get(),                                                               
                                                            studfee_payable.get(),
                                                                stud_fee_arreas.get()))
        
        messagebox.showinfo("Success","👍\nRecord has been inserted")
    connection.commit()
    clearFee()

"""def cents():
        connection=sqlite3.connect('studentdata.db')
        cur=connection.cursor()
        cur.execute("SELECT center_name FROM centres")
        rows=cur.fetchall()
        return [row[0] for row in rows]
def subs():
    connection=sqlite3.connect('studentdata.db')
    cur=connection.cursor()
    cur.execute("SELECT subject_name FROM subjects")
    rows=cur.fetchall()
    return [row[0] for row in rows]
def studs():
    connection=sqlite3.connect('studentdata.db')
    cur=connection.cursor()
    cur.execute("SELECT student_name FROM students")
    rows=cur.fetchall()
    return [row[0] for row in rows]
stm=studs()
sm=subs()    
cm=cents() 
def studs_id():
    connection=sqlite3.connect('studentdata.db')
    cur=connection.cursor()
    cur.execute("SELECT student_id FROM students")
    centas = []
    for row in cur.fetchall():
        centas.append(row) 
    return centas
stm_id=studs_id()"""
def insert_student():
        connection=sqlite3.connect('studentdata.db')
        cur=connection.cursor() 
        
        cur.execute("SELECT EXISTS (SELECT 1 FROM students WHERE student_id='"+str(Sid.get())+"')")
        exists = cur.fetchone()[0]
        if exists:
           messagebox.showerror('Record already exists', 'Looks like the record already exists')
        else:
            if (Sid.get()=="" or Sid.get()==" ") or\
                (Sname.get()==""or Sname.get()==" " )or \
                (Sgender.get()==""or Sgender.get()=="")or\
                (Scenter_name.get()==""or Scenter_name.get()=="")or\
                (Sclass_type.get()==""or Sclass_type.get()=="")or\
                (Scontact_number.get()==""or Scontact_number.get()=="")or\
                (Slevel.get()==""or Slevel.get()=="")or\
                (Sdate_of_admission.get()==""or Sdate_of_admission.get()=="")or\
                (courseFee.get()=="" or courseFee.get()==""):
                    messagebox.showerror('Missing field', 'Please check and fill in all fields')
                    
            else:
                cur.execute("INSERT INTO students values(?,?,?,?,?,?,?,?,?)",(Sid.get(),
                                                                    Sname.get(),
                                                                    Sgender.get(),
                                                                    Scenter_name.get(),
                                                                    Sclass_type.get(),
                                                                    Scontact_number.get(),
                                                                    Slevel.get(),
                                                                    Sdate_of_admission.get(),
                                                                    courseFee.get()))  
                messagebox.showinfo("Success","👍\nRecord has been inserted")
            connection.commit()
        clearStudent()
def updateStudents():
    connection=sqlite3.connect('studentdata.db')
    cur=connection.cursor()
    if (Sid.get()=="" or Sid.get()==" ") or\
                (Sname.get()==""or Sname.get()==" " )or \
                (Sgender.get()==""or Sgender.get()=="")or\
                (Scenter_name.get()==""or Scenter_name.get()=="")or\
                (Sclass_type.get()==""or Sclass_type.get()=="")or\
                (Scontact_number.get()==""or Scontact_number.get()=="")or\
                (Slevel.get()==""or Slevel.get()=="")or\
                (Sdate_of_admission.get()==""or Sdate_of_admission.get()==""):
                    messagebox.showerror('Missing field', 'Please check and fill in all fields')             
    else:
        cur.execute("UPDATE students SET student_id=?,\
                                                student_name=?,\
                                                gender=?,\
                                                center_name=?,\
                                                class_type=?,\
                                                contact_number=?,\
                                                level=?,\
                                                date_of_admission=? WHERE student_id='"+str(Sid.get())+"'",(Sid.get(),
                                                            Sname.get(),
                                                            Sgender.get(),
                                                            Scenter_name.get(),
                                                            Sclass_type.get(),
                                                            Scontact_number.get(),
                                                            Slevel.get(),
                                                            Sdate_of_admission.get()))  
        messagebox.showinfo("Success","👍\nRecord has been inserted")
    connection.commit()
    clearStudent()
def insert_attendance():
    connection=sqlite3.connect('studentdata.db')
    cur=connection.cursor()
    cur.execute("SELECT EXISTS (SELECT 1 FROM attendance WHERE attendance_no='"+str(att_no.get())+"')")
    exists = cur.fetchone()[0]
    if exists:
        messagebox.showerror('Record already exists', 'That attendance Number already exist, Please use a different digit!')
    else:
        if (att_no.get()=="" or att_no.get()==" ")or\
            (cen_name.get()=="" or cen_name.get()==" ")or\
            (subj_nm.get()=="" or subj_nm.get()==" ")or\
            (studentID.get()==""or studentID.get()==" ")or\
            (att_grade.get()=="" or att_grade.get()==" ")or\
            (lec_Name.get()=="" or lec_Name.get()==" ")or\
            (date_T.get()=="" or date_T.get()==" ")or\
            (lect_grade.get()=="" or lect_grade.get()==" ")or\
            (examined_date.get()=="" or examined_date.get()==" "):
                messagebox.showerror('Missing field', 'Please check and fill in all fields')
        else:
            cur.execute("INSERT INTO attendance values(?,?,?,?,?,?,?,?,?,?)",(att_no.get(),
                                                            cen_name.get(),                                                            
                                                            subj_nm.get(),
                                                            studentID.get(),
                                                            att_grade.get(),
                                                            class_Typ.get(),
                                                            lec_Name.get(),
                                                            date_T.get(),
                                                            lect_grade.get(),
                                                            examined_date.get()))
            messagebox.showinfo("Success","👍\nRecord has been inserted")
        connection.commit()
    
        clearAttendance()
def updateAttendance():
    connection=sqlite3.connect('studentdata.db')   
    cur=connection.cursor() 
    if (att_no.get()=="" or att_no.get()==" ")or\
            (cen_name.get()=="" or cen_name.get()==" ")or\
            (subj_nm.get()=="" or subj_nm.get()==" ")or\
            (studentID.get()==""or studentID.get()==" ")or\
            (att_grade.get()=="" or att_grade.get()==" ")or\
            (lec_Name.get()=="" or lec_Name.get()==" ")or\
            (date_T.get()=="" or date_T.get()==" ")or\
            (lect_grade.get()=="" or lect_grade.get()==" ")or\
            (examined_date.get()=="" or examined_date.get()==" "):
                messagebox.showerror('Missing field', 'Please check and fill in all fields')
    else:
        cur.execute("UPDATE attendance SET attendance_no=?, center_name=?, subject_name=?, student_id=?, attendance_grade=?, class_type=?, lecturer_name=?, date_taught=?, lecture_grade=?, examined=? WHERE attendance_no='"+str(att_no.get())+"'",(
                                                            att_no.get(),
                                                            cen_name.get(),                                                            
                                                            subj_nm.get(),
                                                            studentID.get(),
                                                            att_grade.get(),
                                                            class_Typ.get(),
                                                            lec_Name.get(),
                                                            date_T.get(),
                                                            lect_grade.get(),
                                                            examined_date.get()))
        messagebox.showinfo("Success","👍\nRecord has been updated")
    connection.commit()
    
                                              
def insert_subject():
    
    connection=sqlite3.connect('studentdata.db')   
    cur=connection.cursor()
    
    cur.execute("SELECT EXISTS (SELECT 1 FROM subjects WHERE subject_no='"+str(subNo.get())+"')")
    exists = cur.fetchone()[0]
    if exists:
        messagebox.showerror('Record already exists', 'That Number already exist, Please use a different digit!')
    else:
        if (subNo.get()==""or subNo.get()==" ")or\
            (subName.get()==""or subName.get()==" ")or\
            (subLevel.get()==""or subLevel.get()==" "):
                messagebox.showerror('Missing field', 'Please check and fill in all fields')
        else:
            cur.execute("INSERT INTO subjects values(?,?,?)",(subNo.get(),
                                                  subName.get(),
                                                  subLevel.get()))
                     
            messagebox.showinfo("Success","👍\nRecord has been inserted")
        connection.commit()
    clearSubject()
def updateSubject():
    connection=sqlite3.connect('studentdata.db')
    cur=connection.cursor() 
    if (subNo.get()==""or subNo.get()==" ")or\
            (subName.get()==""or subName.get()==" ")or\
            (subLevel.get()==""or subLevel.get()==" "):
                messagebox.showerror('Missing field', 'Please check and fill in all fields')
    else:
        cur.execute("UPDATE subjects SET subject_no=?, subject_name=?, level=? WHERE subject_name='"+str(subName.get())+"'",(
                                                                    subNo.get(),
                                                                    subName.get(),
                                                                    subLevel.get()))
        messagebox.showinfo("Success","👍\nRecord has been updated") 
    connection.commit()
    
    def clearSubject():
        subNo.set(''),
        subName.set(''),
        subLevel.set('')
    clearSubject()

def insert_centers():
    connection=sqlite3.connect('studentdata.db')
    cur=connection.cursor() 
    
    cur.execute("SELECT EXISTS (SELECT 1 FROM centres WHERE center_name='"+str(centa_name.get())+"')")
    exists = cur.fetchone()[0]
    if exists:
        messagebox.showerror('Record already exists', 'Looks like the record already exists. Please check the Center name and try again')
    else:
        if (centa_name.get()==""or centa_name.get()==" ")or\
            (no_students.get()==""or no_students.get()==" ")or\
            (expectedFee.get()==""or expectedFee.get()==" ")or\
            (center_expences.get()==""or center_expences.get()==" ")or\
            (fee_Paid.get()==""or fee_Paid.get()==" ")or\
            (fee_arreas.get()==""or fee_arreas.get()==" "):
                messagebox.showerror('Missing field', 'Please check and fill in all fields')
        else:
            cur.execute("INSERT INTO centres values(?,?,?,?,?,?)",(centa_name.get(),
                                                                no_students.get(),
                                                                expectedFee.get(),
                                                                center_expences.get(),
                                                                fee_Paid.get(),
                                                                fee_arreas.get()))
            messagebox.showinfo("Success","👍\nRecord has been inserted")
        connection.commit() 
        
    clearCenters()
def updateCenter():
    
    connection=sqlite3.connect('studentdata.db')
    cur=connection.cursor() 
    if (centa_name.get()==""or centa_name.get()==" ")or\
            (no_students.get()==""or no_students.get()==" ")or\
            (expectedFee.get()==""or expectedFee.get()==" ")or\
            (center_expences.get()==""or center_expences.get()==" ")or\
            (fee_Paid.get()==""or fee_Paid.get()==" ")or\
            (fee_arreas.get()==""or fee_arreas.get()==" "):
                messagebox.showerror('Missing field', 'Please check and fill in all fields')
    else:
    
        cur.execute("UPDATE centres SET population=?,expectedFee=?,expences=?, feePaid=?, arreas=? WHERE center_name='"+str(centa_name.get())+"'",(
                                                                    no_students.get(),
                                                                    expectedFee.get(),
                                                                    center_expences.get(),
                                                                    fee_Paid.get(),
                                                                    fee_arreas.get())) 
        messagebox.showinfo("Success","👍\nRecord has been updated")
    connection.commit()
    
    clearCenters()


             
