import tkinter as tk

class DatabaseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Insertion")

        # Guest ID Entry
        self.guest_id_label = tk.Label(root, text="Guest ID:")
        self.guest_id_label.grid(row=0, column=0)
        self.guest_id_entry = tk.Entry(root)
        self.guest_id_entry.grid(row=0, column=1)

        # Phone Number Entry
        self.phone_number_label = tk.Label(root, text="Phone Number:")
        self.phone_number_label.grid(row=1, column=0)
        self.phone_number_entry = tk.Entry(root)
        self.phone_number_entry.grid(row=1, column=1)

        # Insert Guest Number Button
        self.insert_guest_num_button = tk.Button(root, text="Insert Guest Number", command=self.insert_guest_num)
        self.insert_guest_num_button.grid(row=2, column=0, columnspan=2)

        # Meal ID Entry
        self.meal_id_label = tk.Label(root, text="Meal ID:")
        self.meal_id_label.grid(row=3, column=0)
        self.meal_id_entry = tk.Entry(root)
        self.meal_id_entry.grid(row=3, column=1)

        # Number of Order Entry
        self.num_order_label = tk.Label(root, text="Number of Order:")
        self.num_order_label.grid(row=4, column=0)
        self.num_order_entry = tk.Entry(root)
        self.num_order_entry.grid(row=4, column=1)

        # Insert Guest Order Button
        self.insert_guest_order_button = tk.Button(root, text="Insert Guest Order", command=self.insert_guest_order)
        self.insert_guest_order_button.grid(row=5, column=0, columnspan=2)

        # Menu ID Entry
        self.menu_id_label = tk.Label(root, text="Menu ID:")
        self.menu_id_label.grid(row=6, column=0)
        self.menu_id_entry = tk.Entry(root)
        self.menu_id_entry.grid(row=6, column=1)

        # Price Entry
        self.price_label = tk.Label(root, text="Price:")
        self.price_label.grid(row=7, column=0)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=7, column=1)

        # Name Entry
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=8, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=8, column=1)

        # Insert Menu Button
        self.insert_menu_button = tk.Button(root, text="Insert Menu", command=self.insert_menu)
        self.insert_menu_button.grid(row=9, column=0, columnspan=2)

        # Class Entry
        self.class_label = tk.Label(root, text="Class:")
        self.class_label.grid(row=10, column=0)
        self.class_entry = tk.Entry(root)
        self.class_entry.grid(row=10, column=1)

        # State Entry
        self.state_label = tk.Label(root, text="State:")
        self.state_label.grid(row=11, column=0)
        self.state_entry = tk.Entry(root)
        self.state_entry.grid(row=11, column=1)

        # Insert Room Button
        self.insert_room_button = tk.Button(root, text="Insert Room", command=self.insert_room)
        self.insert_room_button.grid(row=12, column=0, columnspan=2)

    def insert_guest_num(self):
        pass

    def insert_guest_order(self):
        pass

    def insert_menu(self):
        pass

    def insert_room(self):
        pass

root = tk.Tk()
app = DatabaseGUI(root)
root.mainloop()
