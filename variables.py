from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter import ttk
import sqlite3


root = tk.Tk()
window=tk.Frame(root)
Sid=StringVar()
Sname=StringVar()
Sgender=StringVar()
Scenter_name=StringVar()
Sclass_type=StringVar()
Scontact_number=StringVar()
Slevel=StringVar()
Sdate_of_admission=StringVar()  

subNo=StringVar()
subName=StringVar()
subLevel=StringVar()
subDate=StringVar()

att_no=StringVar()
subj_nm=StringVar()
cen_name=StringVar()
lec_Name=StringVar()
studentID=StringVar()
date_T=StringVar()
lect_grade=StringVar()
att_grade=StringVar()
class_Typ=StringVar()
examined_date=StringVar()

ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

#placeholder set value function



datelbl=StringVar()
def clearSubject():
        subNo.set(''),
        subName.set(''),
        subLevel.set('')
    

def clearFee():
            invce_no.set(''),
            inv_date.set(''),
            student_idNo.set(''),
            center_idNo.set(''),
            studfee_payable.set(''),
            studpaid.set(''),
            stud_fee_arreas.set('')
def expClear():
            rct_no.set(''),
            ppse.set(''),
            cntr.set(''),
            amnt.set(''),
            dat.set('')


def clearStudent():
            Sid.set(''),
            Sname.set(''),
            Sgender.set(''),
            Scenter_name.set(''),
            Sclass_type.set(''),
            Scontact_number.set(''),
            Slevel.set(''),
            Sdate_of_admission.set(''),
            courseFee.set('')

def clearCenters():
            centa_name.set(''),
            no_students.set(''),
            expectedFee.set(''),
            fee_Paid.set(''),
            fee_arreas.set('')

def clearAttendance():
        att_no.set(''),
        subj_nm.set(''),
        cen_name.set(''),
        lec_Name.set(''),
        studentID.set(''),
        date_T.set(''),
        lect_grade.set(''),
        att_grade.set(''),
        class_Typ.set(''),
        examined_date.set('')

centa_name=StringVar()
no_students=StringVar()
expectedFee=StringVar()
center_expences=StringVar()
fee_Paid=StringVar()
fee_arreas=StringVar()

attendanceId=StringVar()
clasId=StringVar()
studeId=StringVar()
subj_Id=StringVar()
D_taught=StringVar()

searched_student_id=StringVar()

classes_tree=ttk.Treeview()
attendanceTable=ttk.Treeview() 
windowFrame=tk.Frame()

style= ttk.Style(window)

invce_no=StringVar()
inv_date=StringVar()
student_idNo=StringVar()
center_idNo=StringVar()
studfee_payable=StringVar()
studpaid=StringVar()
stud_fee_arreas=StringVar()

rct_no=StringVar()
ppse=StringVar()
cntr=StringVar()
amnt=StringVar()
dat=StringVar()

searched_center_name=StringVar()

s=searched_student_id.get()
n=searched_student_id.set('')



rev_id=StringVar()
c_id=StringVar()
no_of_students=StringVar()
coll_fee=StringVar()
exps=StringVar()
pd_fee=StringVar()
are_fee=StringVar()

search_by=StringVar()
search_txt=StringVar()

courseFee=StringVar()
def refresh():
    root.update()
    root.update_idletasks()

   
Cname=StringVar()
#studs=int()
setfee=60000
Fee=IntVar()
paidfee=IntVar()
arrea=IntVar()

#Feepayable_fld= studs * setfee
#expectedfee= totalFee - expences
#arrea = expectedfee - paidfee
expectedfee=IntVar()
totalFee=IntVar()
    
    

