import tkinter as tk
import plistlib

# English and Arabic .plist file paths
english_plist_path = '/Users/social/Documents/Work/Rabida_Demo/Rabida_Demo/Apple/Plist/en.plist'
arabic_plist_path = '/Users/social/Documents/Work/Rabida_Demo/Rabida_Demo/Apple/Plist/ar.plist'

# Current selected language
current_language = 'English'

# Initialize label text
enter_email = "Enter your Email"
enter_password = "Enter your password"
login_title = "Login Page"
submit_button = "Send"

def toggle_language():
    global current_language, enter_email, enter_password, login_title, submit_button

    # Toggle the language
    if current_language == 'English':
        current_language = 'Arabic'
        plist_path = arabic_plist_path
    else:
        current_language = 'English'
        plist_path = english_plist_path

    # Read the .plist file and retrieve the key-value pairs
    with open(plist_path, 'rb') as plist_file:
        plist_data = plistlib.load(plist_file)

    enter_email = plist_data.get('EnterEmail')
    enter_password = plist_data.get('EnterPassword')
    login_title = plist_data.get('LoginTitle')
    submit_button = plist_data.get('SubmitButton')

    # Update the labels and button text
    label_email.config(text=enter_email)
    label_password.config(text=enter_password)
    window.title(login_title)
    button_submit.config(text=submit_button)

def login():
    input_email = entry_email.get()
    input_password = entry_password.get()

    # Perform login validation here
    # ...

    # Clear the input fields
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title(login_title)

# Create labels, entry fields, and button
label_email = tk.Label(window, text=enter_email)
label_email.pack()

entry_email = tk.Entry(window)
entry_email.pack()

label_password = tk.Label(window, text=enter_password)
label_password.pack()

entry_password = tk.Entry(window, show="*")
entry_password.pack()

button_toggle = tk.Button(window, text="Toggle Language", command=toggle_language)
button_toggle.pack()

button_submit = tk.Button(window, text=submit_button, command=login)
button_submit.pack()

# Run the main event loop
window.mainloop()
