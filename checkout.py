import tkinter as tk

def print_list_of_strings(strings):
    # Create a new window
    window = tk.Tk()
    window.geometry(f"{450}x{450}")
    window.title("Checkout")
    # Create a text widget to display the list of strings
    text_widget = tk.Text(window)
    text_widget.pack(expand=True, fill="both")


    # Insert the first line with a larger font size
    text_widget.insert(tk.END, "Bill" + '\n', "big")
    text_widget.tag_configure("big", font=("Arial", 30), justify="center")
    text_widget.tag_configure("normal", font=("Arial", 15))
    text_widget.tag_configure("fnormal", font=("Arial", 17))
    # Insert each string from the list into the text widget with a smaller font size
    cnt = 0
    for i in range(len(strings)-1):
        if cnt == 0:
            text_widget.insert(tk.END, "Guest:\n", "fnormal")
        elif cnt == 1:
            text_widget.insert(tk.END, "\nRoom:\n", "fnormal")
        elif cnt == 2:
            text_widget.insert(tk.END, "\nOrders:\n", "fnormal")

        text_widget.insert(tk.END, '\t' + strings[i] + '\n', "normal")
        cnt += 1
    text_widget.insert(tk.END, "\nTotal\n", "fnormal")
    text_widget.insert(tk.END, '\t' + strings[-1] + ' $\n', "normal")


    # Configure the text widget background
    text_widget.config(background='#F7DCB9')

    # Start the main event loop
    window.mainloop()

# Example list of strings
my_list = ['Bill', 'Hello', 'World', 'GitHub', 'Copilot']

# Call the function to print the list in a new window
#print_list_of_strings(my_list)
