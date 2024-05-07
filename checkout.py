import tkinter as tk

def print_list_of_strings(strings):
    # Create a new window
    window = tk.Tk()

    # Create a text widget to display the l
    # ist of strings
    text_widget = tk.Text(window)
    text_widget.pack()

    # Insert each string from the list into the text widget
    for string in strings:
        text_widget.insert(tk.END, string + '\n')
        text_widget.config(font=("Arial", 15), background='#F7DCB9')

    # Start the main event loop
    window.mainloop()

# Example list of strings
my_list = ['Hello', 'World', 'GitHub', 'Copilot']

# Call the function to print the list in a new window
#print_list_of_strings(my_list)