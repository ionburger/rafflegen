

# Create the main window
window = tk.Tk()
window.title("File Selection")

# Create a function that will be called when the user clicks the button
def select_file():
    # Use the filedialog module to create a file selection dialog box
    selected_file = filedialog.askopenfilename()
    # Print the path to the selected file
    print(selected_file)

# Create a button that will open the file selection dialog when clicked
file_button = tk.Button(window, text="Select File", command=select_file)
file_button.pack()

# Start the main event loop to display the window and wait for user input
window.mainloop()
