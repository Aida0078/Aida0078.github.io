#ماژول های استفاده شده 
import pickle
from tkinter import *
from tkinter import messagebox

#کد های قسمت گرافیکی برنامه
root=Tk()

#مشخص کردن تایتل و اندازه پس زمینه
root.title("Contacts")
root.geometry("1000x700")


#دیکشنری(دفترچه مخاطبین)
contact={}


name_input=StringVar()
last_name_input=StringVar()
age_input=StringVar()
email_input=StringVar()
phone_input = StringVar()


#مشخص کردن لیبل ها و اینتری ها
name_label=Label(root,text="Name").grid(row=0,column=0)
name_entry=Entry(root,textvariable=name_input).grid(row=0,column=1)

last_name_label=Label(root,text="Last Name").grid(row=1,column=0)
last_name_entry=Entry(root,textvariable=last_name_input).grid(row=1,column=1)

phone_lable = Label(root,text="Phone").grid(row=2,column=0)
phone_entry = Entry(root,textvariable=phone_input).grid(row=2,column=1)

info_label=Label(root,text="Fill this box to search or delete your contact").grid(row=2,column=2)

age_label=Label(root,text="Age").grid(row=3,column=0)
age_entry=Entry(root,textvariable=age_input).grid(row=3,column=1)

email_label=Label(root,text="Email Adress").grid(row=4,column=0)
email_entry=Entry(root,textvariable=email_input).grid(row=4,column=1)

# فاصله ها
space_label = Label(root,text="\n").grid(row=5,column=0)
space = Label(root,text="\n").grid(row=8,column=0)
space = Label(root,text="\n").grid(row=10,column=0)

#مشخص کردن دکمه ها
add_button=Button(root,text="Add contact", command=lambda : add_contact()).grid(row=7, column=0)

delete_button=Button(root,text="Delete contact", command=lambda : delete_contact()).grid(row=8, column=0)

edit_button=Button(root,text="Edit contact", command=lambda : edit_contact()).grid(row=9, column=0)

search_button=Button(root,text="Search contact",command=lambda :search()).grid(row=10, column=0)

load_button=Button(root,text="load", command=lambda :show_all()).grid(row=12, column=0)

clear_button=Button(root,text="Clear",command=lambda :clear()).grid(row=14, column=4)



#لیست باکس
list_box=Listbox(root,width=70,height=17)

#کد های قسمت عملیاتی برنامه(توابع)
def add_contact ():
	global contact 
	contact_name = name_input.get()
	contact_last_name = last_name_input.get()
	contact_age = age_input.get()
	phone_number = phone_input.get()
	contact_email= email_input.get()
	contact[phone_number]={'Name':contact_name,'last_name':contact_last_name ,'age':contact_age,'Email_adress':contact_email}
	save()
	list_box.delete(0,END)
	list_box.insert(END,show_all())
	
def delete_contact ():
	global contact
	contact_number=phone_input.get()
	try:
		contact.pop(contact_number)
		save()
		list_box.delete(0, END)
		list_box.insert(END, show_all())
	except:
		messagebox.showinfo("Error","This number is not in your contact list")

def edit_contact ():
	global contact
	contact_name = name_input.get()
	contact_last_name = last_name_input.get()
	phone_number = phone_input.get()
	contact_age = age_input.get()
	contact_email = email_input.get()
	contact[phone_number]={'Name':contact_name,'last_name':contact_last_name ,'age':contact_age,'Email_adress':contact_email}
	save()
	list_box.delete(0, END)
	list_box.insert(END, show_all())


def search():
	global contact
	load()
	try:
		contact_number = phone_input.get()
		contact[contact_number]
		cn = contact[contact_number]["Name"]+"     "+contact[contact_number]["last_name"]+"     "+contact [contact_number]["age"]+"     "+contact[contact_number]["Email_adress"]
		list_box.delete(0,END)
		list_box.insert(END, cn)
	except:
		messagebox.showinfo("Error","This number is not in your contact list")

def save():
	global contact
	my_file=open("contact.txt","wb")
	pickle.dump(contact,my_file)
	my_file.close()
	
	
def load():
	global contact
	my_file=open("contact.txt","rb")
	contact=pickle.load(my_file)
	my_file.close()
	
	
def show_all():
	global contact
	load()
	for key in contact:
		cn = key+"     "+contact[key]["Name"]+"     "+contact[key]["last_name"]+"     "+contact [key]["age"]+"     "+contact[key]["Email_adress"]
		list_box.insert(END,cn)


def clear():
	list_box.delete(0,END)

list_box.grid(row=13,column=3)
mainloop()