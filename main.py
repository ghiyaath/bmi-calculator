# Calculating BMI

from tkinter import *
from tkinter import messagebox

# title and the heading
window = Tk()
window.title("BMI Calculator")
window.geometry("800x500")
window.config(bg="light blue")
heading = Label(window, font=("Arial 25 bold"), text='Ideal Body Mass Index')
heading2 = Label(window, font=("Arial 25 bold"), text='Calculator')
heading.place(x=250, y=0)
heading2.place(x=300, y=35)

frame = Frame(window,bg="silver", width=500, height=200, borderwidth=1, relief='ridge')
frame.place(relx=0.15, rely=0.15)

# functioning to the weight entry
weight = Label(frame,text="Weight(kg):")
weight.place(relx=0, rely=0)
weight_entry = Entry(frame)
weight_entry.place(relx=0.3, rely=0)

# functioning to the height entry
height = Label(frame, text="Height(cm):")
height.place(relx=0, rely=0.2)
height_entry = Entry(frame)
height_entry.place(relx=0.3, rely=0.2)

# functions to the gender drop down
gender = Label(frame, text="Gender:")
gender.place(rely=0.43, relx=0)

# Age label entry
age = Label(frame, text="Age:")
age.place(rely=0.7, relx=0)
age_entry = Entry(frame, state='readonly')
age_entry.place(rely=0.7, relx=0.3)

options = ['Select...', 'Male', "Female"]
variable = StringVar(frame)
variable.set(options[0])


def activate(value):
    variable.set(value)
    if value != "Select...":
        age_entry.config(state='normal')
    else:
        age_entry.config(state='readonly')


gender_menu = OptionMenu(frame, variable, *options, command=activate)
gender_menu.place(relx=0.3, rely=0.4)

def bmi_calc():
    try:
        float(weight_entry.get())
        float(height_entry.get())
        float(age_entry.get())
        if variable.get() == "Select...":
            raise ValueError
        elif variable.get() == "Male":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + 11.5
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        elif variable.get() == "Female":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + (
                        0.03 * float(age_entry.get())) + 11
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
    except ValueError:
        messagebox.showerror(title=None, message='Gender was not specified or invalid entry was given')
        delete()

# placing the buttons and letting it function correctly

calculate = Button(window,bg="blue", fg="white", borderwidth=5, font=("Arial 15 bold"), text="Calculate your Ideal Body Mass Index", width=50, command=bmi_calc)
calculate.place(rely=0.57, relx=0.15)

# putting labels in and letting them function correctly

bmi = Label(window, text="BMI:")
bmi.place(rely=0.75, relx=0.1)
bmi_field = Entry(window, state='readonly')
bmi_field.place(rely=0.75, relx=0.2)
ideal_bmi = Label(window, text='Ideal BMI:')
ideal_bmi.place(rely=0.75, relx=0.5)
ideal_field = Entry(window, state='readonly')
ideal_field.place(rely=0.75, relx=0.65)

# defining delete

def delete():
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    age_entry.config(state='normal')
    bmi_field.config(state='normal')
    ideal_field.config(state='normal')
    age_entry.delete(0, END)
    bmi_field.delete(0, END)
    ideal_field.delete(0, END)
    age_entry.config(state='readonly')
    bmi_field.config(state='readonly')
    ideal_field.config(state='readonly')
    weight_entry.focus()
    variable.set(options[0])

# working clear button

clear = Button(window,bg="red", fg="white", borderwidth=5, font=("Arial 15 bold"), text='Clear', command=delete)
clear.place(rely=0.85, relx=0.1)

# working exit button

exit = Button(window, bg="red", fg="white", borderwidth=5, font=("Arial 15 bold"), text='Exit', command='exit')
exit.place(rely=0.85, relx=0.83)

window.mainloop()
