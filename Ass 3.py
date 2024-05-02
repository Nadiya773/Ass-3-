import tkinter as tk
from tkinter import messagebox
import pickle
from datetime import datetime

#define employee class
class Employee:
    def __init__(self,name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details

#define event class
class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address):
        self.event_id = event_id
        self.theme = theme
        self.event_type = event_type
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address

 #define client class
class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

#define supplier class
class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

#define guest class
class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

#define venue class
class Venue:
    def __init__(self, venue_id, name, address, contact, min_capacity, max_capacity):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity

#define caterer class
class Caterer:
    def __init__(self, caterer_id, name, address, contact_details, menu, min_capacity, max_capacity):
        self.caterer_id = caterer_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.menu = menu
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity


#Define GUI class
class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Management System of the Event")
        self.geometry("600x400")

        #Employee frame
        self.employee_frame = tk.Frame(self)
        self.employee_frame.pack(pady=10)

        self.employee_label = tk.Label(self.employee_frame, text="Employee Details:")
        self.employee_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.name_label = tk.Label(self.employee_frame, text="Name:")
        self.name_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = tk.Entry(self.employee_frame)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.employee_id_label = tk.Label(self.employee_frame, text="Employee ID:")
        self.employee_id_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.employee_id_entry = tk.Entry(self.employee_frame)
        self.employee_id_entry.grid(row=2, column=1, padx=5, pady=5)

        self.department_label = tk.Label(self.employee_frame, text="Department:")
        self.department_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.department_entry = tk.Entry(self.employee_frame)
        self.department_entry.grid(row=3, column=1, padx=5, pady=5)

        self.job_title_label = tk.Label(self.employee_frame, text="job title:")
        self.job_title_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.job_title_entry = tk.Entry(self.employee_frame)
        self.job_title_entry.grid(row=4, column=1, padx=5, pady=5)

        self.basic_salary_label = tk.Label(self.employee_frame, text="Basic salary:")
        self.basic_salary_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.basic_salary_entry = tk.Entry(self.employee_frame)
        self.basic_salary_entry.grid(row=5, column=1, padx=5, pady=5)

        self.age_label = tk.Label(self.employee_frame, text="Age")
        self.age_label.grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.age_entry = tk.Entry(self.employee_frame)
        self.age_entry.grid(row=6, column=1, padx=5, pady=5)

        self.date_of_birth_label = tk.Label(self.employee_frame, text="Date of birth:")
        self.date_of_birth_label.grid(row=7, column=0, sticky="w", padx=5, pady=5)
        self.date_of_birth_entry = tk.Entry(self.employee_frame)
        self.date_of_birth_entry.grid(row=7, column=1, padx=5, pady=5)

        self.passport_details_label = tk.Label(self.employee_frame, text="passport details:")
        self.passport_details_label.grid(row=8, column=0, sticky="w", padx=5, pady=5)
        self.passport_details_entry = tk.Entry(self.employee_frame)
        self.passport_details_entry.grid(row=8, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.employee_frame, text="Add Employee", command=self.add_employee)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        #Display frame
        self.display_frame = tk.Frame(self)
        self.display_frame.pack(pady=10)

        self.display_label = tk.Label(self.display_frame, text="Display Details:")
        self.display_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.id_label = tk.Label(self.display_frame, text="ID:")
        self.id_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.id_entry = tk.Entry(self.display_frame)
        self.id_entry.grid(row=1, column=1, padx=5, pady=5)

        self.display_button = tk.Button(self.display_frame, text="Display Details", command=self.display_details)
        self.display_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_employee(self):
        name = self.name_entry.get()
        employee_id = self.employee_id_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = self.basic_salary_entry.get()
        age = self.age_entry.get()
        date_of_birth = self.date_of_birth_entry.get()
        passport_details = self.passport_details_entry.get()

        #validation
        if not all([name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details]):
            messagebox.showerror("Error", "Please enter all required information.")
            return

        #create employee object
        employee = Employee(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)

        #Save employee to file
        self.save_data("employee.pickle", employee)

        #clear entry fields
        self.name_entry.delete(0, tk.END)
        self.employee_id_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.job_title_entry.delete(0, tk.END)
        self.basic_salary_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.date_of_birth_entry.delete(0, tk.END)
        self.passport_details_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Employee added succesfully")

    def save_data(self, filename, data):
        try:
            with open(filename, "ab") as file:
                pickle.dump(data, file)
        except Exception as e:
            messagebox.showerror("Error", f"failed to save data : {e}")

    def display_details(self):
        entity_id = self.id_entry.get()

        #validation
        if not entity_id:
            messagebox.showerror("Error", "enter ID")
            return

        #display details
        try:
            with open("employee.pickle", "rb") as file:
                while True:
                    try:
                        employee = pickle.load(file)
                        if employee.employee_id == entity_id:
                            messagebox.showinfo("Employee Details", f"Name:{employee.name}\nEmployee ID : {employee.employee_id}\nDepartment: {employee.department}\nJob Title: {employee.job_title}\nBasic Salary: {employee.basic_salary}\nAge: {employee.age}\nDate of Birth: {employee.date_of_birth}\nPassport Details: {employee.passport_details}")
                            return
                    except EOFError:
                        break
            messagebox.showerror("Error", "Employee not found.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Employee file not found")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")


if __name__ == "__main__":
    app = GUI()
    app.mainloop()




