
from tkinter import*

root=Tk()
root.title("Driving License")
root.geometry("300x400")



root.configure(bg="white")
canvas = Canvas(root, width=300, height=400)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 300, 55, fill="#1463B0")
canvas.create_rectangle(0, 345, 300, 400, fill="#1463B0")

label_heading = canvas.create_text(150, 90, font=('Times', '24', 'bold italic'), text="Driving License")
label_name_tag = canvas.create_text(40, 165, font=('Times', '16', 'bold'), text="Id :")
label_grade_tag = canvas.create_text(40, 205, font=('Times', '16', 'bold'), text="Name :")
label_subjects_tag = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="Date of Birth :")
label_subjects_tag = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="Pin-Code :")
label_subjects_tag = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="Address :")
label_subjects_tag = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="Vehicle-type :")

label_id = Label(root)
label_name = Label(root)
label_dateOfBirth = Label(root)
label_pincode = Label(root)
label_address = Label(root)
label_vehicletype = Label(root)


def myCardDetails():
    id = "1234567890"
    print(type(id))
    name = "Tasya Parikh" 
    print(type(name)) 
    dateOfBirth = "20 Octomber 2009"
    print(type(date-of-birth)) 
    pinCode = "389151"
    print(type(pin-code))
    vehicleType = "two-wheeler,four-wheeler" 
    print(type(vehicle-type))
    
    
    label_id['text'] = Id
    label_name['text'] = Name 
    label_dateOfBirth['text'] = Date-of-birth
    label_pincode['text'] = Pin-Code
    label_address['text'] = Address
    label_vehicletype['text'] = Vehicle-type

button1 = Button(root, text = "Driving License", command=myCardDetails)

button1.configure(width=20, activebackground="#9EC6EE", relief=FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(120, 165, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(90, 205, anchor=CENTER, window=label_name)
label_dateOfBirth_window = canvas.create_window(155, 252, anchor=CENTER, window=label_dateOfBirth)
label_pincode_window = canvas.create_window(90, 205, anchor=CENTER, window=label_pincode)
label_vehicletype_window = canvas.create_window(90, 205, anchor=CENTER, window=label_vehicletype)

canvas.pack()

root.mainloop()

