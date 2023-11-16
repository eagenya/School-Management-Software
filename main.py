import tkinter as tk
from tkcalendar import DateEntry
import tkinter as ttk
from tkinter import ttk
import sqlite3
from tkinter import *
from variables import *
from database_end import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from datetime import date
from time import strftime
import traceback
import sys
import os
#https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

    
#photo = PhotoImage(file=resource_path('dist\logo.png'))
root.geometry("1366x768")
root.title('JCC School of Ministry')
#root.iconbitmap(resource_path('dist\\icon.ico'))
root.resizable(0, 0)

#def dashboard():

options_frame =tk.Frame(root, bg='#c3c3c3')
options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width = 150, height=700)


window.pack(side=LEFT)
window.pack_propagate(False)
window.configure(width=1250, height=1000)
#window.place()

    
main_frame=tk.LabelFrame(window,)
main_frame.pack(expand=True, fill=BOTH)
main_frame.pack_propagate(False)
main_frame.configure(width=700, height=600)

"""lb= tk.Label(main_frame, image=photo)
lb.pack()"""
"""dash_frame.pack(fill=BOTH)
dash_frame.pack_propagate(False)"""
#dash_frame.config(width = 1200, height=700, bg='sienna')
"""home=Label(root, image=photo)
home.pack(fill=BOTH, expand=True)"""
#def hom():
    #window.pack_forget()
def dashboard():
        """lb= tk.Label(main_frame, image=photo)
        lb.pack()"""
        
        student_btn = tk.Button(main_frame, text='Manage Students', cursor="hand2", font=('Bold',20),
               bg='orange', borderwidth="0", bd=10,  activebackground="#CF1E14",
            fg='white',command= student_entries)
        student_btn.grid(row=2, column=1,padx=130, pady=300,)

        cntr_btn = tk.Button(main_frame, text='Manage Centres', cursor="hand2", font=('Bold',20),
                            fg='#158aff', bd=10, bg='green', command= centres)
        cntr_btn.grid(row= 2, column=2, padx=50, pady=20)

        sbjct_btn = tk.Button(main_frame, text='Manage Subjects/Units', cursor="hand2", font=('Bold',16),
                            fg='#158aff', bd=10, bg='#ffc0cb', command= subject)
        sbjct_btn.grid(row=2, column=3, padx=50,pady=20)

def delete_portal():
    
 for frame in windowFrame.winfo_children():
     options_frame.destroy() 

def delete_pages():
 for frame in main_frame.winfo_children():
     frame.destroy()  
def subject():
    delete_pages() 
    delete_portal() 
    
    att=tk.LabelFrame(main_frame,)
    att.pack()
    att.grid(row=1,column=1, pady=50)
            
    subject_frame=tk.LabelFrame(att, font=('elephant',15), text='Subject', bg = 'lightblue',bd = 15,relief = 'ridge')
    #subject_frame.pack()
    subject_frame.grid(row=1, column=1, padx=0, pady=0, sticky=W)
    
    
    
    subject_no=tk.Label(subject_frame,font=('Helvetica', 15), bg = 'lightblue', text='No.:').grid(row=1, column=1,padx=5, pady=20)
    subject_name=tk.Label(subject_frame,font=('Helvetica', 15), bg = 'lightblue', text='Subject Name').grid(row=1, column=3,padx=20, pady=20)
    subj_level=tk.Label(subject_frame,font=('Helvetica', 15),  bg = 'lightblue',text='Level').grid(row=1, column=5, padx=5,pady=20)
        
    subject_no=tk.Entry(subject_frame, textvariable=subNo, width=20).grid(row=1, column=2)
    subject_name=tk.Entry(subject_frame, textvariable=subName, width=70).grid(row=1, column=4)
    subj_level=ttk.Combobox(subject_frame, values=('Certificate','Diploma'), state='readonly', textvariable=subLevel, width=20).grid(row=1, column=6)
    
    
    submitbtn=tk.Button(subject_frame, font=('Elephant', 15), bg='green', cursor="hand2",text='Add',command=insert_subject).grid(row=3, column=7, padx=60, pady=20)   
    submitbtn=tk.Button(subject_frame, font=('Elephant', 15), bg='orange', cursor="hand2",text='Edit',command=updateSubject).grid(row=3, column=6, padx=20, pady=20)   
    
    
    attend_frame=tk.LabelFrame(main_frame,  font=('elephant',15), text='Class Attendance', bg='teal', bd=15,relief='ridge')
    attend_frame.grid(row=3, column=1, pady=30,sticky=W) 
    attendance_no=tk.Label(attend_frame,font=('Helvetica', 13), text='No.:', bg='teal').grid(row=1, column=1, padx=5, pady=5)
    subject_namel=tk.Label(attend_frame,font=('Helvetica', 13), text='Subject name:', bg='teal').grid(row=2, column=1, padx=5, pady=10)
    center_namelbl=tk.Label(attend_frame,font=('Helvetica', 13), text='Centre Name:', bg='teal').grid(row=1, column=3, padx=5, pady=20)
    student_idl=tk.Label(attend_frame,font=('Helvetica', 13), text='Student Id:', bg='teal').grid(row=1, column=5, padx=5, pady=20)
    lecturer_namelbl=tk.Label(attend_frame,font=('Helvetica', 13), text='Lecturer Name:', bg='teal').grid(row=2, column=3, padx=5, pady=20)
    dateT=tk.Label(attend_frame, font=('Helvetica', 13),text='Date Taught:', bg='teal').grid(row=2, column=5, padx=5, pady=5)
    Lect_Grade=tk.Label(attend_frame,font=('Helvetica', 13),text='Lecturer %:', bg='teal').grid(row=1, column=7, padx=5, pady=20)
    attendance_grade=tk.Label(attend_frame,font=('Helvetica', 13), text='Attendance %:', bg='teal').grid(row=3, column=1, padx=5, pady=20)
    class_type=tk.Label(attend_frame,font=('Helvetica', 13), text='Class Type:', bg='teal').grid(row=3, column=3, padx=5, pady=20)
    examined=tk.Label(attend_frame, font=('Helvetica', 13),text='Date Examine:', bg='teal').grid(row=3, column=5, padx=5, pady=20)
    
    
    
    attenda_no=tk.Entry(attend_frame,textvariable=att_no, width=20).grid(row=1, column=2, padx=2, pady=5)
    subject_nm=Entry(attend_frame, textvariable=subj_nm, width=20).grid(row=2, column=2, padx=5, pady=5)
    center_name=Entry(attend_frame,textvariable=cen_name, width=20).grid(row=1, column=4, padx=5, pady=5)
    studID=tk.Entry(attend_frame, textvariable=studentID, width=20).grid(row=1, column=6, padx=5, pady=5)
    lectureName=tk.Entry(attend_frame,textvariable=lec_Name, width=20).grid(row=2, column=4, padx=5, pady=5)
    dateTe=DateEntry(attend_frame,textvariable=date_T, width=20).grid(row=2, column=6, padx=5, pady=5)
    lecturer_grade=Entry(attend_frame,textvariable= lect_grade, width=10).grid(row=1, column=8, padx=20, pady=5)
    attend_grade=Entry(attend_frame,textvariable= att_grade, width=10).grid(row=3, column=2, padx=52, pady=5)
    classType=ttk.Combobox(attend_frame, values=("Regular","Evening","Pastors","Diploma"),state='readonly', textvariable=class_Typ,width=15).grid(row=3, column=4, padx=5, pady=5)
    examineddate=DateEntry(attend_frame, textvariable=examined_date,width=20).grid(row=3, column=6, padx=5, pady=5)
    


    submitbtn=tk.Button(attend_frame, bg='green', font=('elephant',15), cursor="hand2", text='Add',command=insert_attendance).grid(row=4, column=8,padx=60, pady=20)
    Button(attend_frame, bg='orange', font=('elephant',15), cursor="hand2", text='Edit',command=updateAttendance).grid(row=4, column=6,padx=7, pady=20)
    
       
        #submitbtn=tk.Button(m2_frame, bg='skyblue', text='Submit',command=entries).grid(row=1, column=1,padx=5, pady=5)
    
def student_entries():
    delete_pages()
    
    fee_frame=tk.LabelFrame(main_frame, font=('elephant',15), text='Students School Fee payment', bd=15, bg='lightcoral')
    #
    fee_frame.grid(row=2, column=1, padx=5, pady=40, sticky=W)
    invoice_no=tk.Entry(fee_frame, textvariable= invce_no ).grid(row=1,  column=2, pady=20, padx=5, sticky=E )
    f_inv_date=DateEntry(fee_frame, textvariable= inv_date ).grid(row=1,  column=4, pady=5, padx=5, sticky=E )
    f_student_id=Entry(fee_frame,  textvariable=student_idNo  ).grid(row=2,  column=2, pady=5, padx=5, sticky=E )
    f_center_id=Entry(fee_frame, textvariable= center_idNo ).grid(row=3,  column=2, pady=20, padx=5, sticky=E )
    fee_payable=tk.Entry(fee_frame, textvariable= studfee_payable  ).grid(row=2,  column=4, pady=5, padx=5, sticky=E )
    f_paid=tk.Entry(fee_frame, width=15, textvariable=studpaid).grid(row=1,  column=6, padx=5, pady=5, sticky=W )
    f_arreas=tk.Entry(fee_frame, textvariable=stud_fee_arreas ).grid(row=2,  column=6, pady=5, padx=5, sticky=E )
    
    invoice_no=tk.Label(fee_frame,font=('Helvetica', 15), bg='lightcoral', text= 'Invoice No' ).grid(row=1,  column=1, padx=5, pady=5, sticky=W )
    f_inv_date=tk.Label(fee_frame,font=('Helvetica', 15), bg='lightcoral', text= 'Invoice Date' ).grid(row=1,  column=3, padx=50, pady=5, sticky=W )
    f_student_id=tk.Label(fee_frame,font=('Helvetica', 15), bg='lightcoral', text='Student ID'  ).grid(row=2,  column=1, padx=5, pady=5, sticky=W )
    f_center_id=tk.Label(fee_frame,font=('Helvetica', 15), bg='lightcoral', text= 'Centre Name' ).grid(row=3,  column=1, padx=5, pady=5, sticky=W )
    fee_payable=tk.Label(fee_frame,font=('Helvetica', 15), bg='lightcoral', text= 'Total Fee Required'  ).grid(row=2,  column=3, pady=30, padx=50, sticky=W )
    f_paid=tk.Label(fee_frame,font=('Helvetica', 15), bg='lightcoral', text='Total Fee Paid').grid(row=1,  column=5, padx=2, pady=5, sticky=W )
    f_arreas=tk.Label(fee_frame,font=('Helvetica', 15), bg='lightcoral', text='Arreas' ).grid(row=2,  column=5, padx=5, pady=5, sticky=W )
    
    submitbtn=tk.Button(fee_frame, bg='skyblue',font=('Elephant', 15), cursor="hand2", text='Add',command=insert_fee).grid(row=4, column=7,padx=60, pady=5)
    Button(fee_frame, bg='orange',font=('Elephant', 15), cursor="hand2", text='Edit',command=updateFee).grid(row=4, column=6,padx=10, pady=5)   
             
    student_frame=tk.LabelFrame(main_frame, font=('elephant',15), text='Student', bg = 'lightblue',bd = 15, relief = 'ridge')
    student_frame.pack()
    student_frame.pack_propagate(0)
    student_frame.grid(row=1,column=1, padx=5, pady=30, sticky=W)
    student_id=tk.Entry(student_frame, textvariable=Sid, width=20).grid(row=1, column=2, padx=0, pady=20)
    student_name=tk.Entry(student_frame,textvariable=Sname, width=30).grid(row=1, column=4, padx=0, pady=20)
    gender=ttk.Combobox(student_frame,values=("Male","Female"),state='readonly', textvariable=Sgender, width=20).grid(row=1, column=6, padx=0, pady=20) 
    center_name=Entry(student_frame,textvariable=Scenter_name, width=20).grid(row=3, column=4,padx=0, pady=20)
    class_type=ttk.Combobox(student_frame,values=("Regular","Evening","Pastors","Diploma"),state='readonly', textvariable=Sclass_type, width=20).grid(row=2, column=2,  padx=0, pady=20)
    contact_number=tk.Entry(student_frame,textvariable=Scontact_number, width=30).grid(row=2, column=4, padx=0, pady=20)
    level=ttk.Combobox(student_frame,values=("Certificate","Diploma"),state='readonly', textvariable=Slevel, width=20).grid(row=2, column=6,padx=0, pady=20)
    date_of_admission=DateEntry(student_frame, textvariable=Sdate_of_admission,width=20).grid(row=3, column=2,padx=0, pady=20)
    feeRequired=tk.Entry(student_frame, textvariable=courseFee,width=20).grid(row=3, column=6,padx=0, pady=20)

    student_idl=tk.Label(student_frame,font=('Helvetica', 13),text='Student Id:', bg = 'lightblue', width=20).grid(row=1, column=1, padx=0)
    student_namel=tk.Label(student_frame,font=('Helvetica', 13),text='Student Name:', bg = 'lightblue', width=20).grid(row=1, column=3, padx=0)
    genderl=tk.Label(student_frame, font=('Helvetica', 13),text='Gender:', bg = 'lightblue', width=20).grid(row=1, column=5, padx=0) 
    center_idl=tk.Label(student_frame,font=('Helvetica', 13), text='Centre:', bg = 'lightblue', width=20).grid(row=3, column=3, padx=0)
    class_typel=tk.Label(student_frame,font=('Helvetica', 13), text='Class Type:', bg = 'lightblue', width=20).grid(row=2, column=1,pady=20, padx=0)
    contact_numberl=tk.Label(student_frame,font=('Helvetica', 13), text='Contact:', bg = 'lightblue', width=20).grid(row=2, column=3, pady=20, padx=0)
    levell=tk.Label(student_frame,font=('Helvetica', 13), text='Level:', bg = 'lightblue', width=20).grid(row=2, column=5, pady=40)
    date_of_admissionl=tk.Label(student_frame, font=('Helvetica', 13),text='Date of Admission:', bg = 'lightblue', width=20).grid(row=3, column=1, pady=20, padx=0)
    fee=tk.Label(student_frame, font=('Helvetica', 13),text='Course Fee:', bg = 'lightblue', width=20).grid(row=3, column=5, pady=20, padx=0)
    
    submitbtn=tk.Button(student_frame, bg='green', font=('Elephant',10), cursor="hand2", text='Add', command=insert_student ).grid(row=4, column=7, padx=20,pady=5)
    Button(student_frame, bg='orange', font=('Elephant',10), cursor="hand2", text='Edit', command=updateStudents ).grid(row=4, column=6, padx=20,pady=5)
    

    
def centres():
    delete_pages()
    
    expeEnrol=tk.LabelFrame(main_frame,)
    expeEnrol.pack()
    expeEnrol.grid(row=2,column=1, pady=50)
    ###################Centers####################
    centers_frame=tk.LabelFrame(main_frame, font=('elephant',15), text='Centers', bg='grey', bd=15, relief='ridge')
    centers_frame.pack()
    centers_frame.grid(row=1, column=1, sticky=W, pady=50)
    centaName=tk.Label(centers_frame, font=('Helvetica', 15), text='Center Name', bg='grey').grid(row=1, column=1, padx=5, pady=5)
    NumberStudents=tk.Label(centers_frame,font=('Helvetica', 15), text='Population', bg='grey').grid(row=1, column=5, padx=5, pady=5)
    ExpctedFee=tk.Label(centers_frame,font=('Helvetica', 15), text='Expected Fee', bg='grey').grid(row=1, column=7, padx=50, pady=5)
    expncs=tk.Label(centers_frame,font=('Helvetica', 15), text='Center Expenses', bg='grey').grid(row=2, column=7, padx=5, pady=5)
    paid=tk.Label(centers_frame,font=('Helvetica', 15), text='Fee Paid', bg='grey').grid(row=2, column=1, padx=5, pady=5)
    arrea=tk.Label(centers_frame,font=('Helvetica', 15), text='Center Arrear', bg='grey').grid(row=2, column=5, padx=50, pady=5)
    
    cen_name=tk.Entry(centers_frame,font=('Helvetica', 10),textvariable=centa_name, width=20).grid(row=1, column=2, padx=5,pady=5)
    noOf_students=tk.Entry(centers_frame,font=('Helvetica', 10),textvariable=no_students, width=20).grid(row=1, column=6, padx=5,pady=50)
    expected_Fee=tk.Entry(centers_frame,font=('Helvetica', 10),textvariable=expectedFee, width=20).grid(row=1, column=8, padx=50,pady=5)
    expences=tk.Entry(centers_frame,font=('Helvetica', 10),textvariable=center_expences, width=20).grid(row=2, column=8, padx=5,pady=5)
    feePaid=tk.Entry(centers_frame,font=('Helvetica', 10),textvariable=fee_Paid, width=20).grid(row=2, column=2, padx=5,pady=5)
    arreas=tk.Entry(centers_frame, font=('Helvetica', 10),textvariable=fee_arreas, width=20).grid(row=2, column=6, padx=5,pady=5)
    
    updatebtn=tk.Button(centers_frame, bg='olivedrab', font=('Elephant',15), text='Update',command=updateCenter).grid(row=3, column=7,padx=5, pady=10)
         
    submitbtn=tk.Button(centers_frame, bg='green', font=('Elephant',15), text='Add',command=insert_centers).grid(row=3, column=8,padx=5, pady=5)
     
    
    #management_2_btn=tk.Button(heading_frame, text='Fees, Attendance & Subjects', bd=0,font=15, bg='green', command=entries_2).grid(row=1, column=2,padx=20, pady=0,sticky=W) 
    #tk.Button(heading_frame, text='View Students', cursor="hand2", font=15, bg='green',bd=0, command=portal).grid(row=1, column=3,padx=20, pady=0)
    
    expence_frame=tk.LabelFrame(expeEnrol, font=('elephant',15), text='Expences', bg = 'rosybrown',bd = 15,relief = 'ridge')
    #expence_frame.pack()
    expence_frame.grid(row=1, column=2, padx=0, pady=0, sticky=N)
    
    receipt_Id=tk.Label(expence_frame, font=('Helvetica', 15),bg = 'rosybrown', text='Receipt No.').grid(row=1, column=1,padx=5, pady=50)
    centre_name=tk.Label(expence_frame, font=('Helvetica', 15),bg = 'rosybrown', text='Centre:').grid(row=1, column=3,padx=60, pady=20)
    purpose=tk.Label(expence_frame, font=('Helvetica', 15), bg = 'rosybrown',text='Purpose').grid(row=2, column=3, padx=5,pady=20)
    amount=tk.Label(expence_frame, font=('Helvetica', 15), bg = 'rosybrown',text='Amount').grid(row=2, column=1, padx=5,pady=5)
    date=tk.Label(expence_frame, font=('Helvetica', 15), bg = 'rosybrown',text='Date').grid(row=1, column=5, padx=5,pady=5)
    
    receipt_Id=tk.Entry(expence_frame,font=('Helvetica', 15), textvariable=rct_no, width=20).grid(row=1, column=2)
    cent_name=Entry(expence_frame, font=('Helvetica', 15), textvariable=cntr, width=20).grid(row=1, column=4)
    purpose=tk.Entry(expence_frame,font=('Helvetica', 15), textvariable=ppse, width=20).grid(row=2, column=4)
    amt=tk.Entry(expence_frame,font=('Helvetica', 15), textvariable=amnt, width=20).grid(row=2, column=2)
    dte=DateEntry(expence_frame,font=('Helvetica', 15),  textvariable=dat, width=20).grid(row=1, column=6, padx=5,pady=5)
    submitbtn=tk.Button(expence_frame,font=('Elephant', 15), bg='green',cursor="hand2",text='Add',command=insert_expence).grid(row=4, column=6, padx=110, pady=10)
    Button(expence_frame, font=('Elephant', 15), bg='orange',cursor="hand2",text='Edit',command=updateExpense).grid(row=4, column=5, padx=30, pady=10)   
    #Button(expence_frame, font=('Elephant', 15), bg='grey',cursor="hand2",text='Search',command=SearchExpence).grid(row=4, column=3, padx=30, pady=10)   
    
windowFrame=tk.Frame()

#R=StringVar()

heading_frame=tk.LabelFrame(window, bg='green' )
heading_frame.pack(side=LEFT, padx=40)
heading_frame.pack_propagate(False)
heading_frame.configure(width=100, height=40)
heading_frame.place(x=3, y=0, width=1325)


datelbl.set(str(date.today()))

datestamp = Label(heading_frame)
datestamp.place(relx=0.794, rely=0.05, width=102, height=36)
datestamp.configure(font="-family {Poppins Light} -size 12")
datestamp.configure(foreground="orange")
datestamp.configure(background="green")

"""datstamp.insert(END, datelbl.get())
datstamp.configure(state="disabled")"""
tk.Button(root, text='Refresh',font=('Helvetica',13), command=refresh, cursor="hand2", fg='white', background='black').place(x=1, y=1)

clock = Label(heading_frame)
clock.place( relx=0.694, rely=0.05, width=102, height=36)
clock.configure(font="-family {Poppins Light} -size 12")
clock.configure(foreground="orange")
clock.configure(background="green")
#portalbtn= tk.Button(heading_frame, text='Students, Classes and Centres', font=1, bg='green',bd=0, command=entries).grid(row=1, column=1,padx=20, pady=0)

def subjects():
    def fetch_data():
         con=sqlite3.connect("studentdata.db")
         cur = con.cursor()
         cur.execute("select * from subjects ")
         rows = cur.fetchall()
         if len(rows)!=0:

             subjects_tree.delete(*subjects_tree.get_children())
             for row in rows:
                 subjects_tree.insert('',END,values=row)
             con.commit()
         con.close()
         #subjects_tree.place(x=10, y=150)
                  
    def search_data():
         con=sqlite3.connect("studentdata.db")
         cur = con.cursor()
         cur.execute("select * from subjects where " + str(search_by.get())+" ='"+str(search_txt.get())+"'")
         rows = cur.fetchall()
         if len(rows)!=0:

             subjects_tree.delete(*subjects_tree.get_children())
             for row in rows:
                 subjects_tree.insert('',END,values=row)
             con.commit()
         con.close()     
    
    sbjct_frame= tk.LabelFrame(main_frame, bg='teal')
    lbl= tk.Label(main_frame, text='                                                                                                                                                         ',
                  bg='teal', font=('Bold', 20), )
    lbl.pack(side=TOP)
    lbl.grid(row=1, column=1, sticky=N)
    sbjct_frame.pack(side=LEFT)
    sbjct_frame.pack_propagate(False)
    sbjct_frame.config(width=1200, height=700)
    
       
    schFrame=tk.Frame(main_frame, bg='teal')
    schFrame.pack()
    schFrame.grid(row=2,column=1, sticky=W, pady=20)
    
    combo_search = ttk.Combobox(schFrame,textvariable=search_by,width=10, font=("times new roman", 18, "bold"), state='readonly')
    combo_search[f'values'] = ("Subject_Name", "Level")
    combo_search.grid(row=1, column=3)
    
    txt_search= Entry(schFrame,textvariable=search_txt,width=20, font=("times new roman", 18, "bold"))
    txt_search.grid(row=1, column=4, padx=20)
    
    lbl_search = Label(schFrame, text="Search By", bg='teal', fg="white",font=("times new roman", 20, "bold"))
    lbl_search.grid(row=1, column=1, padx=20)

    searchbtn = Button(schFrame, text="Search", cursor="hand2", width=10,pady=5,command=search_data)
    searchbtn.grid(row=1,column=5,padx=50)
    
    showallbtn = Button(schFrame, text="Show All", cursor="hand2", width=10, pady=5,command=fetch_data)
    showallbtn.grid(row=1, column=6,padx=20)

    
    Table_Frame = Frame(main_frame, bd=4, relief=RIDGE, bg="crimson", width=600)
    Table_Frame.grid(row=3, column=1, padx=20, pady=70, sticky=W)
    scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
    scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
    subjects_tree = ttk.Treeview(Table_Frame,column=("subject_no","subject_name","level",),
                                        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=subjects_tree.xview)
    scroll_y.config(command=subjects_tree.yview)
    subjects_tree.heading("subject_no",text="No.")
    subjects_tree.heading("subject_name", text="Subject Name")
    subjects_tree.heading("level", text="Level")
    
    style.theme_use('clam')
    style.configure(".",rowheight=40, font=('Helvetica', 15))
    style.configure("Treeview.Heading", font=('Helvetica', 18), foreground='blue')
            
    subjects_tree['show'] = 'headings'
    subjects_tree.column("subject_no",width=100)
    subjects_tree.column("subject_name", width=500)
    subjects_tree.column("level", width=200)
    

    subjects_tree.pack(fill=BOTH , expand=100)
    
    #subjects_tree.bind("<ButtonRelease-1>",get_cursor)


    fetch_data()
        
def portal():
    options_frame.grid_forget() 
    
    def hide_indicator():
        profile_indicator.config(bg='grey')
        att_indicator.config(bg='grey')
        fee_indicator.config(bg='grey')
    def indicator(lb, page):
        hide_indicator()
        lb.config(bg='#158aff')
        delete_page()
        page()
    def delete_page():
          for frame in frame2.winfo_children():
            frame.destroy()       
    #delete_pages()
    windowFrame=tk.Frame(main_frame, bg='green')
    windowFrame.pack(side=LEFT, padx=0,pady=20)
    windowFrame.place(x=1, y=1, )
    windowFrame.pack_propagate(False)
    windowFrame.configure(width=1400, height=1000)
    
    frame2=tk.Frame(windowFrame, bg='sienna')
    frame2.pack(side=LEFT, padx=0,pady=20)
    frame2.place(x=210, y=100, )
    frame2.pack_propagate(False)
    frame2.configure(width=1400, height=1000)
    
    
    
    def studentName():
      
        if searched_student_id.get()=="":
            messagebox.showerror("Error", "Please Insert student ID to search!")
        else:    
            connection=sqlite3.connect('studentdata.db')
            cur=connection.cursor()
            cur.execute("SELECT student_name from students WHERE student_id='"+str(searched_student_id.get())+"'")
            L=cur.fetchone()
            cur.execute("SELECT student_id  from students WHERE student_id='"+str(searched_student_id.get())+"'")
            i=cur.fetchone()
            cur.execute("SELECT centres.center_name  from students JOIN centres ON centres.center_name=students.center_name WHERE student_id='"+str(searched_student_id.get())+"'")
            c=cur.fetchone()
            def printhead():
                namel=tk.Label(sidePanel, bg='grey', font=('Bold',15),width=20,bd=0, fg='yellow', text=L).grid(row=1,column=1, pady=0, sticky=N)
                namel=tk.Label(sidePanel, bg='grey', font=('Bold',15),width=20,bd=0, fg='yellow', text=i).grid(row=2,column=1, pady=0, sticky=N)
                namel=tk.Label(sidePanel, bg='grey', font=('Bold',15),width=20,bd=0, fg='yellow', text=c).grid(row=3,column=1, pady=0, sticky=N)
            
            if L:
                return printhead()
            else:
                messagebox.showerror("Error", "Student with that Id Does not exist.\
                    Please be sure to add the student into the system or check the student ID and try again")
            
    
    searchbox_frame=tk.Frame(windowFrame, bg='grey', width=1325, height=80)
    searchbox_frame.place(x=210,y=30)
    #tk.Button(searchbox_frame, text='Refresh', command=refresh, cursor="hand2", background='green').grid(row=2, column=4, padx=5)
    searchbtn=tk.Button(searchbox_frame, bg='Black', foreground='white', cursor="hand2", command=studentName, text='Search').grid(row=2, column=3, padx=5, pady=5)
    searchEntry=Entry(searchbox_frame,textvariable=searched_student_id, width=15, font=('calibri', 15)).grid(row=2, column=1, padx=5)
    searchlbl=tk.Label(searchbox_frame, bg='grey', text='Enter student ID', foreground='black', font=('calibri', 15)).grid(row=1, column=1, padx=5, pady=5)
    def read_profile():
        #delete_page()
        if searched_student_id.get()=="":
            messagebox.showerror("Error", "You have not specified a student Please Enter student ID in the searchbox Above")
        else:
            connection=sqlite3.connect('studentdata.db')
            cur=connection.cursor()
            cur.execute("SELECT * FROM students WHERE student_id='"+str(searched_student_id.get())+"'  ")
            profile=cur.fetchall()
            
            student_id=tk.Label(frame2, bg='sienna', text='Admn No.:', font=('Elephant', 18),)
            student_id.place(x=400,y=20)
            student_name=tk.Label(frame2, bg='sienna',text=' Name:', font=('Elephant', 18),)
            student_name.place(x=20,y=20)
            gender=tk.Label(frame2, bg='sienna', text='Gender:', font=('Elephant', 18),)
            gender.place(x=750,y=20)
            center_id=tk.Label(frame2,bg='sienna', text='Centre: ', font=('Elephant', 18),)
            center_id.place(x=20,y=200)
            class_type=tk.Label(frame2, bg='sienna', text='Class Category', font=('Elephant', 18),)
            class_type.place(x=400,y=200)
            contact_number=tk.Label(frame2, bg='sienna', text='Contact:', font=('Elephant', 18),)
            contact_number.place(x=750,y=200)
            level=tk.Label(frame2, bg='sienna', text='Level of Study', font=('Elephant', 18),)
            level.place(x=20,y=400)
            date_of_admission=tk.Label(frame2, bg='sienna',text='Date Of Admission', font=('Elephant', 18),)
            date_of_admission.place(x=400,y=400)
            
            
            profile_student_id=tk.Label(frame2, bg='sienna', text=profile[0][0], fg='floralwhite',  font=('SimSun', 30),)
            profile_student_id.place(x=400,y=70)
            profile_student_name=tk.Label(frame2, text=profile[0][1], bg='sienna',fg='floralwhite', font=('SimSun', 30),)
            profile_student_name.place(x=20,y=70)
            profile_gender=tk.Label(frame2, text=profile[0][2], bg='sienna', fg='floralwhite',font=('SimSun', 30),)
            profile_gender.place(x=750,y=70)
            profile_center_id=tk.Label(frame2, text=profile[0][3], bg='sienna',fg='floralwhite', font=('SimSun', 30),)
            profile_center_id.place(x=20,y=250)
            profile_class_type=tk.Label(frame2, text=profile[0][4], bg='sienna',fg='floralwhite', font=('SimSun', 30),)
            profile_class_type.place(x=400,y=250)
            profile_contact_number=tk.Label(frame2, text=profile[0][5], bg='sienna',fg='floralwhite', font=('SimSun', 30),)
            profile_contact_number.place(x=750,y=250)
            profile_level=tk.Label(frame2, text=profile[0][6], bg='sienna',fg='floralwhite', font=('SimSun', 30),)
            profile_level.place(x=20,y=450)
            profile_date_of_admission=tk.Label(frame2, text=profile[0][7],fg='floralwhite', bg='sienna', font=('SimSun', 30),)
            profile_date_of_admission.place(x=400,y=450)
            
        
    def read_attendance():
        #delete_page()
        if searched_student_id.get()=="":
            messagebox.showerror("Error", "You have not specified a student Please Enter student ID in the searchbox Above")
        else:
            connection=sqlite3.connect('studentdata.db')
            cur=connection.cursor()
            cur.execute("SELECT subject_name, attendance_grade, date_taught, examined FROM attendance WHERE student_id='"+str(searched_student_id.get())+"'")
            rows=cur.fetchall()
            
            
    
            Table_Frame = Frame(frame2, bd=4, relief=RIDGE, bg="crimson", width=1000)
            Table_Frame.pack_propagate(False)
            Table_Frame.configure(width=980, height=600)
            Table_Frame.grid(row=2,column=1, sticky=E, pady=10, padx=15)

            scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
            subjects_tree = ttk.Treeview(Table_Frame,column=("subject_name", "attendance_grade","date_taught","examined" ),
                                                xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            for row in rows:
                subjects_tree.insert('', tk.END, values=row)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=subjects_tree.xview)
            scroll_y.config(command=subjects_tree.yview)
            subjects_tree.heading("subject_name",text="Subject Name")
            subjects_tree.heading("attendance_grade", text="Attendance %")
            subjects_tree.heading("date_taught", text="Date Taught")
            subjects_tree.heading("examined", text="Date Examined")
            
            
            style.theme_use('clam')
            style.configure(".", font=('Helvetica', 15))
            style.configure("Treeview.Heading", font=('Helvetica', 18), foreground='blue')
            subjects_tree['show'] = 'headings'
            subjects_tree.column("subject_name",width=200)
            subjects_tree.column("attendance_grade",width=50)
            subjects_tree.column("date_taught", width=50)
            subjects_tree.column("examined", width=50)

            subjects_tree.pack(fill=BOTH , expand=100)
        
        
    def read_fee():
        #delete_page()
        if searched_student_id.get()=="":
            messagebox.showerror("Error", "You have not specified a student Please Enter student ID in the searchbox Above")
        else:
            con = sqlite3.connect('studentdata.db')
            cur = con.cursor()
            cur.execute("SELECT fee.invoice_no, fee.date,  fee.paid,fee.fee_payable, fee.arreas FROM fee WHERE student_id='"+str(searched_student_id.get())+"'")
            fee_table=cur.fetchall()
            
            Table_Frame = Frame(frame2, bd=4, relief=RIDGE, bg="crimson", width=100)
            Table_Frame.pack_propagate(False)
            Table_Frame.configure(width=980, height=600)
            Table_Frame.grid(row=2,column=1, sticky=E, pady=10, padx=15)
            
            scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
            fee_tree = ttk.Treeview(Table_Frame,column=("invoice_no", "date", "paid", "fee_payable", "arreas"),
                                                xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            for row in fee_table:
                fee_tree.insert('', tk.END, values=row)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=fee_tree.xview)
            scroll_y.config(command=fee_tree.yview)
            fee_tree.heading("invoice_no",text="Invoice No")
            fee_tree.heading("date",text="Invoice Date")            
            fee_tree.heading("paid", text="Amount")
            fee_tree.heading("fee_payable",  text=("Fee Required"))
            fee_tree.heading("arreas", text="Arreas")
            
            style.theme_use('clam')
            style.configure(".", font=('Helvetica', 15))
            style.configure("Treeview.Heading", font=('Helvetica', 18),  foreground='blue')
            fee_tree['show'] = 'headings'
            fee_tree.column("invoice_no",width=20)
            fee_tree.column("date",width=20)
            fee_tree.column("paid", width=150)
            fee_tree.column("fee_payable", width=50)
            fee_tree.column("arreas", width=50)

            fee_tree.pack(fill=BOTH , expand=20)
            
            con.commit()    
        
    searchlbl=tk.Label(searchbox_frame, bg='grey',
                       text='                                                                                                                                                                     ', foreground='black', font=('calibri', 15)).grid(row=1, column=20, padx=5, pady=5)
    sidePanel=tk.Frame(windowFrame, bg='grey',  width=600, height=650)
    sidePanel.place(x=1,y=30)
    profilebtn=tk.Button(sidePanel, bg='grey',width=20,bd=0, cursor="hand2", font=('calibri', 15), text='Student Profile', command=lambda: indicator(profile_indicator, read_profile)).grid(row=3,column=1, padx=0, pady=20, sticky=S)
    subjectbtn=tk.Button(sidePanel, bg='grey',width=20,bd=0, cursor="hand2", font=('calibri', 15), text='Subjects Done', command=lambda: indicator(att_indicator, read_attendance)).grid(row=4,column=1, padx=0, pady=20,sticky=W)
    FeeStatementbtn=tk.Button(sidePanel, bg='grey',width=20,bd=0, cursor="hand2", font=('calibri', 15), command=lambda: indicator(fee_indicator, read_fee), text='Fee Statement',).grid(row=5,column=1, padx=0, pady=20,sticky=W)
    namel=tk.Label(sidePanel, bg='grey',width=20,bd=0, fg='black', textvariable=searched_student_id.get()).grid(row=1,column=1, pady=20)
    tk.Label(sidePanel, bg='grey',width=20,bd=0, text='  ',).grid(row=6,column=1, pady=250)
    
    
    
    fee_indicator=tk.Label(sidePanel, text='', bg='grey')
    fee_indicator.place(x=10, y=260, width=5, height=40)
    
    att_indicator=tk.Label(sidePanel, text='', bg='grey')
    att_indicator.place(x=10, y=180, width=5, height=36)
    
    profile_indicator=tk.Label(sidePanel, text='', bg='grey')
    profile_indicator.place(x=10, y=105, width=5, height=36)
def hide_indicator():
    dash_indicator.config(bg='#c3c3c3')
    student_indicator.config(bg='#c3c3c3')
    sbjct_indicator.config(bg='#c3c3c3')
    cntr_indicator.config(bg='#c3c3c3')
def delete_pages():
 for frame in main_frame.winfo_children():
     frame.destroy()
     
def indicator(lb, page):
    hide_indicator()
    lb.config(bg='#158aff')
    delete_pages()
    page()

def centers():
    
    def hide_indicator():
        profile_indicator.config(bg='grey')
        att_indicator.config(bg='grey')
        fee_indicator.config(bg='grey')
        population_indicator.config(bg='grey')
        subjectsT_indicator.config(bg='grey')
    def indicator(lb, page):
        hide_indicator()
        lb.config(bg='#158aff')
        delete_page()
        page()
    def delete_page():
          for frame in frame2.winfo_children():
            frame.destroy()       
    #delete_pages()
    windowFrame=tk.Frame(main_frame, bg='green')
    windowFrame.pack(side=TOP, padx=0,pady=20)
    windowFrame.place(x=1, y=1, )
    windowFrame.pack_propagate(False)
    windowFrame.configure(width=1400, height=1000)
    
    frame2=tk.Frame(windowFrame, bg='sienna')
    frame2.pack(side=TOP, padx=0,pady=20)
    frame2.place(x=210, y=100, )
    frame2.pack_propagate(False)
    frame2.configure(width=1400, height=1000)
    
    
    
    def centerName():
        if searched_center_name.get()=="":
            messagebox.showerror("Error", "Please Insert Centre Name to search!")
        else:    
            connection=sqlite3.connect('studentdata.db')
            cur=connection.cursor()
            cur.execute("SELECT center_name from centres WHERE center_name='"+str(searched_center_name.get())+"'")
            L=cur.fetchone()
            
            def printhead():
                #namel=tk.Label(sidePanel, bg='grey', font=('Bold',15),width=20,bd=0, fg='yellow', text=L).grid(row=1,column=1, pady=0, sticky=N)
                namel=tk.Label(sidePanel, bg='grey', font=('Bold',15),width=20,bd=0, fg='yellow', text=L).grid(row=2,column=1, pady=0, sticky=N)
                
            
            if L:
                return printhead()
            else:
                messagebox.showerror("Error", "Center with that Name Does not exist.\
                    Please be sure to add the student into the system or check the Centre Name and try again")
    
    searchbox_frame=tk.Frame(windowFrame, bg='grey', width=1325, height=80)
    searchbox_frame.place(x=215,y=25)
    tk.Button(searchbox_frame, text='Refresh', cursor="hand2", background='green').grid(row=2, column=4, padx=5)
    searchbtn=tk.Button(searchbox_frame, bg='Black', foreground='white', cursor="hand2", command=centerName, text='Search').grid(row=2, column=3, padx=5, pady=5)
    searchEntry=Entry(searchbox_frame, textvariable=searched_center_name, width=15,  font=('calibri', 15)).grid(row=2, column=1, padx=5)
    searchlbl=tk.Label(searchbox_frame, bg='grey', text='Enter Center Name', foreground='black', font=('calibri', 15)).grid(row=1, column=1, padx=5, pady=5)
    def read_expences():
        if searched_center_name.get()=="":
            messagebox.showerror("Error", "You have not specified a center Please Enter Center ID in the searchbox Above")
        else:
            connection=sqlite3.connect('studentdata.db')
            cur=connection.cursor()
            cur.execute("SELECT receiptNo, purpose, amount, date FROM expence WHERE center_name='"+str(searched_center_name.get())+"'  ")
            expence=cur.fetchall()
        
            Table_Frame = Frame(frame2, bd=4, relief=RIDGE, bg="crimson", width=1000)
            Table_Frame.pack_propagate(False)
            Table_Frame.configure(width=990, height=600)
            Table_Frame.grid(row=2,column=1, sticky=E, pady=10, padx=10)

            scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
            expence_tree = ttk.Treeview(Table_Frame,column=("receipt_no","purpose","amount", "date"),
                                                xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            for row in expence:
                expence_tree.insert('', tk.END, values=row)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=expence_tree.xview)
            scroll_y.config(command=expence_tree.yview)
            expence_tree.heading("receipt_no",text="Receipt No")
            expence_tree.heading("purpose",text="Purpose")
            expence_tree.heading("amount",text=("Amount"))
            #expence_tree.heading("class_id", text="class ID")
            expence_tree.heading("date", text="Date")
            
            style.theme_use('clam')
            style.configure(".", font=('Helvetica', 15))
            style.configure("Treeview.Heading", font=('Helvetica', 18), foreground='blue')
            expence_tree['show'] = 'headings'
            expence_tree.column("receipt_no",width=50)
            expence_tree.column("purpose",width=200)
            expence_tree.column("amount", width=10)
            expence_tree.column("date", width=10)

            expence_tree.pack(fill=BOTH , expand=100)
            
    def read_cent_info():
        #delete_page()
        if searched_center_name.get()=="":
            messagebox.showerror("Error", "You have not specified a center Please Enter Center name in the searchbox Above")
        else:
            con = sqlite3.connect('studentdata.db')
            cur = con.cursor()
            cur.execute("SELECT population, expectedFee, feePaid, expenses, arreas  FROM centres WHERE center_name='"+str(searched_center_name.get())+"'")
            cent_info=cur.fetchall()
            
            population=tk.Label(frame2, bg='sienna', text='Center Population:', font=('Elephant', 18),)
            population.place(x=20,y=20)
            expctdfee=tk.Label(frame2, bg='sienna',text='Center Expected Fee:', font=('Elephant', 18),)
            expctdfee.place(x=400,y=20)
            expns=tk.Label(frame2, bg='sienna', text='Total Expences:', font=('Elephant', 18),)
            expns.place(x=800,y=20)
            feepaid=tk.Label(frame2,bg='sienna', text='Fee Paid', font=('Elephant', 18),)
            feepaid.place(x=20,y=200)
            areas=tk.Label(frame2, bg='sienna', text='arreas', font=('Elephant', 18),)
            areas.place(x=400,y=200)
                        
            
            population=tk.Label(frame2, bg='sienna', text=cent_info[0][0], fg='floralwhite',  font=('SimSun', 30),)
            population.place(x=20,y=70)
            expctdfee=tk.Label(frame2, text=cent_info[0][1], bg='sienna',fg='floralwhite', font=('SimSun', 30),)
            expctdfee.place(x=400,y=70)
            feepaid=tk.Label(frame2, text=cent_info[0][2], bg='sienna',fg='floralwhite', font=('SimSun', 30),)
            feepaid.place(x=20,y=250)
            areas=tk.Label(frame2, text=cent_info[0][3], bg='sienna',fg='floralwhite', font=('SimSun', 30),)
            areas.place(x=400,y=250)
            expns=tk.Label(frame2, text=cent_info[0][4], bg='sienna', fg='floralwhite',font=('SimSun', 30),)
            expns.place(x=800,y=70)
    def read_population():
        #delete_page()
        if searched_center_name.get()=="":
            messagebox.showerror("Error", "You have not specified a student Please Enter center name in the searchbox Above")
        else:
            con = sqlite3.connect('studentdata.db')
            cur = con.cursor()
            cur.execute("SELECT student_id, student_name, gender, class_type, contact_number,level, date_of_admission FROM students WHERE center_name='"+str(searched_center_name.get())+"'")
            population_table=cur.fetchall()
            
            Table_Frame = Frame(frame2, bd=4, relief=RIDGE, bg="crimson", width=100)
            Table_Frame.pack_propagate(False)
            Table_Frame.configure(width=980, height=600)
            Table_Frame.grid(row=2,column=1, sticky=E, pady=10, padx=15)
            
            scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
            popu_tree = ttk.Treeview(Table_Frame,column=("student_id", "student_name", "gender", "class_type", "contact_number","level","date_of_admission"),
                                                xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            for row in population_table:
                popu_tree.insert('', tk.END, values=row)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=popu_tree.xview)
            scroll_y.config(command=popu_tree.yview)
            popu_tree.heading("student_id",text="ID")
            popu_tree.heading("student_name",text="Name")            
            popu_tree.heading("gender", text="Gender")
            popu_tree.heading("class_type",  text=("Class Type"))
            popu_tree.heading("contact_number", text="Contact")
            popu_tree.heading("level",  text=("Level"))
            popu_tree.heading("date_of_admission", text="Admission Date")
            
            style.theme_use('clam')
            style.configure(".", font=('Helvetica', 15))
            style.configure("Treeview.Heading", font=('Helvetica', 18),  foreground='blue')
            popu_tree['show'] = 'headings'
            popu_tree.column("student_id",width=5)
            popu_tree.column("student_name",width=50)
            popu_tree.column("gender", width=10)
            popu_tree.column("class_type", width=20)
            popu_tree.column("contact_number", width=20)
            popu_tree.column("level", width=10)
            popu_tree.column("date_of_admission", width=50)

            popu_tree.pack(fill=BOTH , expand=5)
            
            con.commit()    
        
    def read_subjectsT():
        if searched_center_name.get()=="":
            messagebox.showerror("Error", "You have not specified a student Please Enter Center Name in the searchbox Above")
        else:
            connection=sqlite3.connect('studentdata.db')
            cur=connection.cursor()
            cur.execute("SELECT attendance_no, subject_name, class_type, lecturer_name, date_taught,lecture_grade, examined FROM attendance WHERE center_name='"+str(searched_center_name.get())+"'")
            rows=cur.fetchall()
            
            
    
            Table_Frame = Frame(frame2, bd=4, relief=RIDGE, bg="crimson", width=1000)
            Table_Frame.pack_propagate(False)
            Table_Frame.configure(width=980, height=600)
            Table_Frame.grid(row=2,column=1, sticky=E, pady=10, padx=15)

            scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
            subjects_tree = ttk.Treeview(Table_Frame,column=("attendance_no", "subject_name","class_type", "lecturer_name", "date_taught","lecture_grade", "examined" ),
                                                xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            for row in rows:
                subjects_tree.insert('', tk.END, values=row)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=subjects_tree.xview)
            scroll_y.config(command=subjects_tree.yview)
            subjects_tree.heading("attendance_no",text="No")
            subjects_tree.heading("subject_name", text="Subject")
            subjects_tree.heading("class_type", text="class Type")
            subjects_tree.heading("lecturer_name", text="Lecturer")
            subjects_tree.heading("date_taught", text="Date Taught")
            subjects_tree.heading("lecture_grade", text="Lecture %")
            subjects_tree.heading("examined", text="Date Examined")
            
            style.theme_use('clam')
            style.configure(".", font=('Helvetica', 10))
            style.configure("Treeview.Heading", font=('Helvetica', 15), foreground='blue')
            subjects_tree['show'] = 'headings'
            subjects_tree.column("attendance_no",width=2)
            #subjects_tree.column("subject_name",width=50)
            subjects_tree.column("class_type",width=50)
            subjects_tree.column("lecturer_name", width=50)
            subjects_tree.column("date_taught", width=50)
            subjects_tree.column("lecture_grade", width=20)
            subjects_tree.column("examined", width=50)

            subjects_tree.pack(fill=BOTH , expand=100)
           
    searchlbl=tk.Label(searchbox_frame, bg='grey',
                       text='                                                                                                                                                                     ', foreground='black', font=('calibri', 15)).grid(row=1, column=20, padx=5, pady=5)
    sidePanel=tk.Frame(windowFrame, bg='grey',  width=600, height=650)
    sidePanel.place(x=1,y=0)
       
    profilebtn=tk.Button(sidePanel, bg='grey',width=21,bd=0, cursor="hand2", font=('calibri', 15), text='', command=lambda: indicator(profile_indicator,)).grid(row=3,column=1, padx=0, pady=20, sticky=S)
    subjectbtn=tk.Button(sidePanel, bg='grey',width=21,bd=0, cursor="hand2", font=('calibri', 15), text='Center Info', command=lambda: indicator(att_indicator, read_cent_info)).grid(row=4,column=1, padx=0, pady=20,sticky=W)
    FeeStatementbtn=tk.Button(sidePanel, bg='grey',width=21,bd=0, cursor="hand2", font=('calibri', 15), command=lambda: indicator(fee_indicator,read_expences ), text='Center Expences',).grid(row=5,column=1, padx=0, pady=20,sticky=W)
    populationbtn=tk.Button(sidePanel, bg='grey',width=21,bd=0,cursor="hand2",  font=('calibri', 15), command=lambda: indicator(population_indicator,read_population ), text='Center Population',).grid(row=6,column=1, padx=0, pady=20,sticky=W)
    subjectsTbtn=tk.Button(sidePanel, bg='grey',width=21,bd=0, cursor="hand2",  font=('calibri', 15), command=lambda: indicator(subjectsT_indicator,read_subjectsT ), text='Subjects Taught',).grid(row=7,column=1, padx=0, pady=20,sticky=W)
    
    namel=tk.Label(sidePanel, bg='grey',width=20,bd=0, fg='black', textvariable=searched_student_id.get()).grid(row=1,column=1, pady=20)
    tk.Label(sidePanel, bg='grey',width=20,bd=0, text='  ',).grid(row=8,column=1, pady=150)
    fee_indicator=tk.Label(sidePanel, text='', bg='grey')
    fee_indicator.place(x=10, y=260, width=5, height=40)
    
    att_indicator=tk.Label(sidePanel, text='', bg='grey')
    att_indicator.place(x=10, y=180, width=5, height=36)
    
    profile_indicator=tk.Label(sidePanel, text='', bg='grey')
    profile_indicator.place(x=10, y=105, width=5, height=36)
    
    population_indicator=tk.Label(sidePanel, text='', bg='grey')
    population_indicator.place(x=10, y=335, width=5, height=40)
    
    subjectsT_indicator=tk.Label(sidePanel, text='', bg='grey')
    subjectsT_indicator.place(x=10, y=413, width=5, height=40)


#options_frame= tk.PhotoImage(file='cape.png')

dash_btn = tk.Button(options_frame, text='Home', cursor="hand2", font=('Bold',15),
                     fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicator(dash_indicator, dashboard ))

dash_btn.place(x=10, y=100)
dash_indicator=tk.Label(options_frame, text='', bg='#c3c3c3')
dash_indicator.place(x=10, y=100, width=5, height=36)

student_btn = tk.Button(options_frame, text='Students', cursor="hand2", font=('Bold',15),
                     fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicator(student_indicator,portal ))
student_btn.place(x=10, y=150)
student_indicator=tk.Label(options_frame, text='', cursor="hand2", bg='#c3c3c3')
student_indicator.place(x=10, y=150, width=5, height=36)

sbjct_btn = tk.Button(options_frame, cursor="hand2",text='Subjects', font=('Bold',15),
                     fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicator(sbjct_indicator, subjects))
sbjct_btn.place(x=10, y=200)
sbjct_indicator=tk.Label(options_frame,  text='', bg='#c3c3c3')
sbjct_indicator.place(x=10, y=200, width=5, height=36)

cntr_btn = tk.Button(options_frame, text='Center', cursor="hand2", font=('Bold',15),
                     fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicator(cntr_indicator, centers))
cntr_btn.place(x=10, y=250)
cntr_indicator=tk.Label(options_frame, text='', bg='#c3c3c3')
cntr_indicator.place(x=10, y=250, width=5, height=36)





def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
    if sure == True:
        root.destroy()
root.protocol("WM_DELETE_WINDOW", Exit)

def time():
        string = strftime("%H:%M:%S %p")
        clock.config(text=string)
        clock.after(1000, time)
        
        datestamp.config(text=datelbl.get())
        
time()



create()

root.mainloop()