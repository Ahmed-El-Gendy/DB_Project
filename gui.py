import tkinter as tk
from tkinter import messagebox
import update_tables
import update_room
import update_menu
import update_guest_order
import update_guest_num
import update_guest
import update_feedback
import update_employee
import tables
import bill
import room

class EmployeeManagementApp:
    def __init__(self, master):
        self.master = master
        master.title("Employee Management System")

        self.insert_button = tk.Button(master, text="Insert", command=self.insert_data)
        self.insert_button.pack()

        self.update_button = tk.Button(master, text="Update", command=self.update_data)
        self.update_button.pack()

    def insert_data(self):
        insert_window = tk.Toplevel(self.master)
        insert_window.title("Insert Data")

        # Table selection
        table_label = tk.Label(insert_window, text="Select Table:")
        table_label.grid(row=0, column=0)
        table_var = tk.StringVar()
        table_var.set("Employee")  # Default value
        table_dropdown = tk.OptionMenu(insert_window, table_var, "Employee", "Feedback", "Guest", "Guest Number", "Guest Order", "Menu", "Room", "Tables", "Bill")
        table_dropdown.grid(row=0, column=1)

        # Function to show specific fields based on selected table
        def show_fields():
            selected_table = table_var.get()
            # Clear previous fields
            for widget in insert_window.winfo_children():
                if isinstance(widget, tk.Entry) or isinstance(widget, tk.Label):
                    widget.grid_forget()
            # Show fields based on selected table
            if selected_table == "Employee":
                fields = ["ID:", "Age:", "Nationality:", "Job:", "Salary:", "Manager ID:", "Name:"]
            elif selected_table == "Feedback":
                fields = ["Opinion:", "Rate:", "Guest ID:"]
            elif selected_table == "Guest":
                fields = ["ID:", "Name:", "Age:", "Nationality:"]
            elif selected_table == "Guest Number":
                fields = ["Guest ID:", "Phone Number:"]
            elif selected_table == "Guest Order":
                fields = ["Guest ID:", "Meal ID:", "Number of Order:"]
            elif selected_table == "Menu":
                fields = ["ID:", "Price:", "Name:"]
            elif selected_table == "Room":
                fields = ["State:", "Class:", "Price per Night:"]
            elif selected_table == "Tables":
                fields = ["Table Number:", "State:", "Chairs Number:"]
            elif selected_table == "Bill":
                fields = ["Guest ID:", "Receptionist ID:"]
            else:
                fields = []
            # Create input fields
            self.input_entries = []
            for i, field in enumerate(fields):
                tk.Label(insert_window, text=field).grid(row=i+1, column=0)
                entry = tk.Entry(insert_window)
                entry.grid(row=i+1, column=1)
                self.input_entries.append(entry)

        # Button to show fields based on selected table
        show_fields_button = tk.Button(insert_window, text="Show Fields", command=show_fields)
        show_fields_button.grid(row=0, column=2)

        # Function to insert data
        def insert():
            selected_table = table_var.get()
            data = [entry.get() for entry in self.input_entries]
            # Call the corresponding insert function based on selected table
            if selected_table == "Employee":
                self.insert_employee(*data)
            elif selected_table == "Feedback":
                self.insert_feedback(*data)
            elif selected_table == "Guest":
                self.insert_guest(*data)
            elif selected_table == "Guest Number":
                self.insert_guest_num(*data)
            elif selected_table == "Guest Order":
                self.insert_guest_order(*data)
            elif selected_table == "Menu":
                self.insert_menu(*data)
            elif selected_table == "Room":
                self.insert_room(*data)
            elif selected_table == "Tables":
                self.insert_tables(*data)
            elif selected_table == "Bill":
                self.insert_bill(*data)
            messagebox.showinfo("Success", "Data inserted successfully!")
            insert_window.destroy()

        # Insert button
        insert_button = tk.Button(insert_window, text="Insert", command=insert)
        insert_button.grid(row=8, columnspan=3)

    def update_data(self):
        update_window = tk.Toplevel(self.master)
        update_window.title("Update Data")

        # Table selection
        table_label = tk.Label(update_window, text="Select Table:")
        table_label.grid(row=0, column=0)
        table_var = tk.StringVar()
        table_var.set("Employee")  # Default value
        table_dropdown = tk.OptionMenu(update_window, table_var, "Employee", "Feedback", "Guest", "Guest Number", "Guest Order", "Menu", "Room", "Tables", "Bill")
        table_dropdown.grid(row=0, column=1)

        # Function to show specific fields based on selected table
        def show_fields():
            selected_table = table_var.get()
            # Clear previous fields
            for widget in update_window.winfo_children():
                if isinstance(widget, tk.Entry) or isinstance(widget, tk.Label):
                    widget.grid_forget()
            # Show fields based on selected table
            if selected_table == "Employee":
                fields = ["ID:", "Age:", "Nationality:", "Job:", "Salary:", "Manager ID:", "Name:"]
            elif selected_table == "Feedback":
                fields = ["ID:", "Opinion:", "Rate:", "Guest ID:"]
            elif selected_table == "Guest":
                fields = ["ID:", "Name:", "Age:", "Nationality:"]
            elif selected_table == "Guest Number":
                fields = ["Guest ID:", "Old Phone Number:", "New Phone Number:"]
            elif selected_table == "Guest Order":
                fields = ["Guest ID:", "Meal ID:", "Number of Order:"]
            elif selected_table == "Menu":
                fields = ["ID:", "Price:", "Name:"]
            elif selected_table == "Room":
                fields = ["ID:", "State:", "Guest ID:", "Receptionist ID:", "Interval Duration:"]
            elif selected_table == "Tables":
                fields = ["Table Number:", "State:", "Guest ID:", "Start:", "Receptionist ID:"]
            elif selected_table == "Bill":
                fields = ["Guest ID:", "Receptionist ID:"]
            else:
                fields = []
            # Create input fields
            self.input_entries = []
            for i, field in enumerate(fields):
                tk.Label(update_window, text=field).grid(row=i+1, column=0)
                entry = tk.Entry(update_window)
                entry.grid(row=i+1, column=1)
                self.input_entries.append(entry)

        # Button to show fields based on selected table
        show_fields_button = tk.Button(update_window, text="Show Fields", command=show_fields)
        show_fields_button.grid(row=0, column=2)

        # Function to update data
        def update():
            selected_table = table_var.get()
            data = [entry.get() for entry in self.input_entries]
            # Call the corresponding update function based on selected table
            if selected_table == "Employee":
                self.update_employee(*data)
            elif selected_table == "Feedback":
                self.update_feedback(*data)
            elif selected_table == "Guest":
                self.update_guest(*data)
            elif selected_table == "Guest Number":
                self.update_guest_num(*data)
            elif selected_table == "Guest Order":
                self.update_guest_order(*data)
            elif selected_table == "Menu":
                self.update_menu(*data)
            elif selected_table == "Room":
                self.update_room(*data)
            elif selected_table == "Tables":
                self.update_tables(*data)
            elif selected_table == "Bill":
                self.insert_bill(*data)  # Note: In update, calling insert_bill instead of update_bill
            messagebox.showinfo("Success", "Data updated successfully!")
            update_window.destroy()

        # Update button
        update_button = tk.Button(update_window, text="Update", command=update)
        update_button.grid(row=8, columnspan=3)

    # Define your insert functions here
    def insert_employee(self, id, age, nationality, job, salary, manager_id, name):
        pass

    def insert_feedback(self, opinion, rate, guest_id):
        pass

    def insert_guest(self, id, name, age, nationality):
        pass

    def insert_guest_num(self, guest_id, phone_number):
        pass

    def insert_guest_order(self, guest_id, meal_id, number_of_order):
        pass

    def insert_menu(self, id, price, name):
        pass

    def insert_room(self, state, clas, price_per_night):
        room.insert_room(state, clas, price_per_night)

    def insert_tables(self, table_num, state, chairs_num):
        tables.insert_tables(table_num, state, chairs_num)

    def insert_bill(self, guest_id, receptionist_id):
        bill.insert_bill(guest_id, receptionist_id)

    # Define your update functions here
    def update_employee(self, id, age, nationality, job, salary, manager_id, name):
        update_employee.update_employee(id, age, nationality, job, salary, manager_id, name)

    def update_feedback(self, id, opinion, rate, guest_id):
        update_feedback.update_feedback(id, opinion, rate, guest_id)

    def update_guest(self, id, name, age, nationality):
        update_guest.update_guest(id, name, age, nationality)

    def update_guest_num(self, guest_id, old_phone_number, new_phone_number):
        update_guest_num.update_guest_num(guest_id, old_phone_number, new_phone_number)

    def update_guest_order(self, guest_id, meal_id, number_of_order):
        update_guest_order.update_guest_order(guest_id, meal_id, number_of_order)

    def update_menu(self, id ,price, name):
        update_menu.update_menu(id, price, name)

    def update_room(self, id, state, guest_id, receptionist_id, interval_duration):
        update_room.update_room(id, state, guest_id, receptionist_id, interval_duration)

    def update_tables(self, table_num, state, guest_id, start, receptionist_id):
        update_tables.update_tables(table_num, state, guest_id, start, receptionist_id)


root = tk.Tk()
app = EmployeeManagementApp(root)
root.mainloop()
