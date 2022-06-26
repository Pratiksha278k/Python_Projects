
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext as st
from PIL import Image, ImageTk
from resizeimage import resizeimage
import bs4
import requests
import socket
import cx_Oracle
import datetime 

#=================================================
#Splash screen
#=================================================

window = Tk() 
window.title("SPLASH") 
window.geometry("400x500+450+100")

res = requests.get("https://www.brainyquote.com/quote_of_the_day.html")
soup = bs4.BeautifulSoup(res.text,'lxml')
quote = soup.find('img',{"class":"p-qotd"})
img_url = "https://www.brainyquote.com" + quote['data-img-url'] 
 
img_name = datetime.datetime.now().date() 
r = requests.get(img_url) 
with open(str(img_name) + ".jpg", "wb") as f:
	f.write(r.content) 
 
with open(str(img_name) + ".jpg",'r+b') as f:  	
	with Image.open(f) as image: 
 		cover = resizeimage.resize_cover(image, [300, 150]) 
	photo_image = ImageTk.PhotoImage(cover) 
	label1 = Label(window, image = photo_image)

try: 
	socket.create_connection(("www.google.com",80))
	res = requests.get("https://ipinfo.io/")
	data = res.json()  	#print(data)
	city = data['city']
	print(city)
	socket.create_connection(("www.google.com",80)) 
	api_address = "http://api.openweathermap.org/data/2.5/weather?units=metric"+"&q=" + "Mumbai" + "&appid=3f936e40460ffe6b0f4ee786f630564c"
	res1 = requests.get(api_address)
 	#print(res1)
	wdata = requests.get(api_address).json()
 	#print(wdata)
	temp = wdata['main']['temp']
	msg = 'You are in ' + city + ' and weather = ' +str(temp) 
	print(msg)
except OSError: 
	print("check network") 
 
labelcity = Label(window,text = 'LOCATION : ' + city)
labeltemp = Label(window,text = 'TEMPARATURE : ' + str(temp)) 

label1.pack(pady= 20)
labelcity.pack(pady=20)
labeltemp.pack(pady=20)  

window.after(5000, window.destroy) 

window.mainloop() 
 
#================================================
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext as st
from PIL import Image, ImageTk
from resizeimage import resizeimage
import bs4
import requests
import socket
import cx_Oracle
import datetime 

#=================================================

root=Tk()
root.title("Student Management system")
root.geometry("400x500+450+100")
root.configure(background="Yellow")
root.deiconify()

#=================================================

#==================================================
def f1():
	root.withdraw()
	adst.deiconify()
	entAddRno.focus()
	entAddRno.delete(0,'end')
	entAddName.delete(0,'end')
	entAddMarks.delete(0,'end')
#-----------------------------------------------
def f2():
	adst.withdraw()
	root.deiconify()
#--------------------------------------------------
def f3():
	root.withdraw()
	vist.deiconify()

	import cx_Oracle

	con=None
	cursor=None

	try:
		con=cx_Oracle.connect("System/xyz123")
		print("Connected")
		cursor=con.cursor()
		sql= "select * from student"
		cursor.execute(sql)
		rows=cursor.fetchall()
		msg=""
		for r in rows:
			print("Rno", r[0], "Name", r[1], "Mks", r[2])
			msg=msg+"RNo. "+str(r[0])+" Name "+r[1]+" Mks "+str(r[2])+"\r\n"
		stViewData.insert(INSERT, msg)
	except cx_Oracle.DatabaseError as e:
		print("Issue ", e)
	finally:
		cursor.close()
		if con is not None:
			con.close()
			print("Connection Closed")
#-------------------------------------------------------
def f4():
	vist.withdraw()
	root.deiconify()
	stViewData.config(state = NORMAL)
	stViewData.delete(1.0, END)
#------------------------------------------------------
def f5():

	con=None
	cursor=None

	try:
		con=None
		con=cx_Oracle.connect("System/xyz123")
		print("Connected.")
	
		rno=int(entAddRno.get())
		name=entAddName.get()
		marks=int(entAddMarks.get())
		if not name.isalpha():
			messagebox.showerror("Failure", "Alphabets only-for name")
			entAddName.delete(0,'end')
			entAddName.focus()
		elif((rno=='') or(name=='') or (marks=='')):
			messagebox.showerror('Failure', 'empty box')
		elif(rno < 0 ):
			messagebox.showerror('Failure','Rno should be positive')
			entAddRno.focus()
			entAddRno.delete(0,'end')
		elif((marks>100) or (marks<0)):
			messagebox.showerror('Failure',"marks should be between 0-100")
			entAddMarks.focus()	
			entAddMarks.delete(0,'end')
		else:
			cursor = con.cursor()
			sql = "insert into student values('%d','%s','%d')"
			args = (rno,name,marks)
			cursor.execute(sql % args)
			con.commit()
			print(cursor.rowcount,'record inserted')
			messagebox.showinfo('Success', str(cursor.rowcount) +' records inserted')
			entAddRno.focus()
			entAddRno.delete(0,'end')
			entAddName.delete(0,'end')
			entAddMarks.delete(0,'end')
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("issue",e)
		messagebox.showerror('Failure', 'rno must be unique value')
		entAddRno.focus()
		entAddRno.delete(0,'end')
	except ValueError as ve:
		con.rollback()
		print('issue',ve)
		messagebox.showerror('failure','rno and marks must be integer value') 
		entAddRno.focus()
		entAddMarks.delete(0,'end')
		entAddRno.delete(0,'end')
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
			print('connection closed')
#--------------------------------------------------------------------
def f6():
	root.withdraw()
	upst.deiconify()
	entUpstRno.focus()
	entUpstRno.delete(0,'end')
	entUpstName.delete(0,'end')
	entUpstMarks.delete(0,'end')
#----------------------------------------------------------------------
def f7():
	con = None
	cursor = None
	try:
		con = None
		con = cx_Oracle.connect("system/xyz123")
		print('connected')
		rno= int(entUpstRno.get())
		name =entUpstName.get()
		marks =int(entUpstMarks.get())
	
		if not name.isalpha():
			messagebox.showerror("failure","alphabets only for name")
			entUpstName.delete(0,'end')
			entUpstName.focus()
		elif((rno=='') or(name=='') or (marks=='')):
			messagebox.showerror('Failure','empty box')
		elif(rno < 0 ):
			messagebox.showerror('Failure','Rno should be +ve')
			entUpstRno.focus()
			entUpstRno.delete(0,'end')
		elif((marks>100) or (marks<0)):
			messagebox.showerror('Failure',"marks should be between 0-100")
			entUpstMarks.focus()
			entUpstMarks.delete(0,'end')
		else:
		
			cursor = con.cursor()
			sql = "update student set name ='%s',marks='%d' where rno='%d'"
			args = (name,marks,rno)
			cursor.execute(sql % args)
			con.commit()
			print(cursor.rowcount,'record updated')
			messagebox.showinfo('Success',str(cursor.rowcount)+' records updated')
			entUpstRno.focus()
			entUpstRno.delete(0,'end')
			entUpstName.delete(0,'end')
			entUpstMarks.delete(0,'end')
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("issue",e)
		messagebox.showerror('Failure', 'Roll no. already exists')
		entUpstRno.focus()
		entUpstRno.delete(0,'end')
	except ValueError as ve:
		con.rollback()
		print('issue',ve)
		messagebox.showerror('failure','Roll no. and marks must be integer')
		entUpstRno.focus()
		entUpstRno.delete(0,'end')
		entUpstMarks.delete(0,'end')
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
			print('connection closed')
#-----------------------------------------------------------------------------
def f8():
	upst.withdraw()
	root.deiconify()
#-----------------------------------------------------------------------------
def f9():
	root.withdraw()
	delst.deiconify()
	entDelRno.focus()
	entDelRno.delete(0,'end')
#---------------------------------------------------------------------------	
def f10():
	import cx_Oracle
	con = None
	cursor = None
	try:
		con = None
		con = cx_Oracle.connect("system/xyz123")
		print('connected')
		rno = int(entDelRno.get())
		if (rno ==''):
			messagebox.showerror('Failure','empty box')
		elif(rno < 0 ):
			messagebox.showerror('Failure','Rno should be +ve')
			entDelRno.delete(0,'end')
			entDelRno.focus()	
		else:
			cursor = con.cursor()
			sql = "delete from student where rno ='%d'"
			args = (rno)
			cursor.execute(sql % args)
			con.commit()
			print(cursor.rowcount,'record deleted')
			messagebox.showinfo('Success',str(cursor.rowcount)+' records deleted')
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("issue",e)
		messagebox.showerror('Failure',e)
	except ValueError as ve:
		con.rollback()
		print('issue',ve)
		messagebox.showerror('failure','Roll no. must be an integer') 
		entDelRno.focus()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
			print('connection closed')
	entDelRno.delete(0,'end')
#----------------------------------------------------------------------------
def f11():
	delst.withdraw()
	root.deiconify()
#--------------------------------------------------------------------------
def f12():
	import pandas as pd
	import matplotlib.pyplot as plt
	import numpy as np

	con=None
	cursor=None
	name=[]
	mark=[]
	try:
		con=cx_Oracle.connect("system/xyz123")
		print("connected")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		rows=cursor.fetchall()
		msg=""
		for r in rows:
			name.append(r[1])
			mark.append(r[2])
		plt.bar(name,mark,width=0.25,color='g',alpha=0.75)
		
		plt.title("Students Marks")
		plt.xlabel("Names")
		plt.ylabel("Marks")
		plt.grid()
		plt.show()	
	except cx_Oracle.DatabaseError as e:
		print("issue",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
			print("connection closed")


#===================================================


btnAdd=Button(root, text='Add', width=20, font=("Times New Roman", 14, "bold"), command=f1)
btnView=Button(root, text='View', width=20, font=("Times New Roman", 14, "bold"), command=f3)
btnUpdate=Button(root, text='Update', width=20, font=("Times New Roman", 14, "bold"), command=f6)
btnDelete=Button(root, text='Delete', width=20, font=("Times New Roman", 14, "bold"), command=f9)
btnGraph=Button(root, text='Graph', width=20, font=("Times New Roman", 14, "bold"), command=f12)

btnAdd.pack(pady=20)
btnView.pack(pady=20)
btnUpdate.pack(pady=20)
btnDelete.pack(pady=20)
btnGraph.pack(pady=20)

#====================================================
#add student
#====================================================

adst=Toplevel(root)
adst.title("Add Student Info.")
adst.geometry("400x500+450+100")
adst.configure(background="DodgerBlue3")
adst.withdraw()


lblRno=Label(adst, text="Enter Roll Number", font=("Elephant", 14))
entAddRno=Entry(adst, bd=5, font=("Times New Roman", 14))
lblName=Label(adst, text="Enter Name", font=("Elephant", 14))
entAddName=Entry(adst, bd=5, font=("Times New Roman", 14))
lblMarks=Label(adst, text="Enter Marks", font=("Elephant", 14))
entAddMarks=Entry(adst, bd=5, font=("Times New Roman", 14))

btnSave=Button(adst, text="SAVE", font=("Forte", 14), command=f5)
btnBack=Button(adst, text="BACK", font=("Forte", 14), command=f2)

lblRno.pack(pady=10)
entAddRno.pack(pady=10)
lblName.pack(pady=10)
entAddName.pack(pady=10)
lblMarks.pack(pady=10)
entAddMarks.pack(pady=10)
btnSave.pack(pady=20)
btnBack.pack(pady=20)

#=======================================================
#view student
#=======================================================

vist=Toplevel(root)
vist.title("View Student Info.")
vist.geometry("400x500+450+100")
vist.configure(background="pale violet red")
vist.withdraw()

stViewData=st.ScrolledText(vist, bd=5, width=30, height=20)
btnViewBack=Button(vist, text="BACK", font=("Forte", 14), command=f4)
stViewData.pack(pady=10)
btnViewBack.pack(pady=10)

#=======================================================
#Update student
#=======================================================

upst=Toplevel(root)
upst.title("Update Student Info.")
upst.geometry("400x500+450+100")
upst.configure(background="chartreuse3")
upst.withdraw()

lblRno=Label(upst, text="Enter Roll Number", font=("Elephant", 14))
entUpstRno=Entry(upst, bd=5, font=("Times New Roman", 14))
lblName=Label(upst, text="Enter Name", font=("Elephant", 14))
entUpstName=Entry(upst, bd=5, font=("Times New Roman", 14))
lblMarks=Label(upst, text="Enter Marks", font=("Elephant", 14))
entUpstMarks=Entry(upst, bd=5, font=("Times New Roman", 14))

btnSave=Button(upst, text="SAVE", font=("Forte", 14), command=f7)
btnBack=Button(upst, text="BACK", font=("Forte", 14), command=f8)

lblRno.pack(pady=10)
entUpstRno.pack(pady=10)
lblName.pack(pady=10)
entUpstName.pack(pady=10)
lblMarks.pack(pady=10)
entUpstMarks.pack(pady=10)
entUpstRno.focus()
btnSave.pack(pady=20)
btnBack.pack(pady=20)

#======================================================
#Delete Student
#=======================================================

delst=Toplevel(root)
delst.title("Delete Student Info.")
delst.geometry("400x500+450+100")
delst.configure(background="cyan4")
delst.withdraw()

lblRno=Label(delst, text="Enter Roll Number", font=("Elephant", 14))
entDelRno=Entry(delst, bd=5, font=("Times New Roman", 14))

btnSave=Button(delst, text="SAVE", font=("Forte", 14), command=f10)
btnBack=Button(delst, text="BACK", font=("Forte", 14), command=f11)

lblRno.pack(pady=10)
entDelRno.pack(pady=10)

entDelRno.focus()
btnSave.pack(pady=20)
btnBack.pack(pady=20)

#=======================================================
#Graph
#=======================================================

#def f12()

root.mainloop()
