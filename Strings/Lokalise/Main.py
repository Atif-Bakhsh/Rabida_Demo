import tkinter as tk

# Function to load the strings from the language file
def load_strings(file_path):
    strings = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith('"') and "=" in line:
                key, value = line.split("=", 1)
                key = key.strip().strip('"')
                value = value.strip().strip('";')
                strings[key] = value
    return strings

# Function to update the labels with the selected language
def update_labels():
    selected_file = language_var.get()

    # Load the strings from the selected language file
    if selected_file == 'English':
        strings = load_strings("/Users/social/Documents/Work/Rabida_Demo/Rabida_Demo/Strings/en.lproj/Localizable.strings")
    else:
        strings = load_strings("/Users/social/Documents/Work/Rabida_Demo/Rabida_Demo/Strings/ar.lproj/Localizable.strings")

    # Update the labels with the new strings
    for label, key in zip(label_list, strings.keys()):
        label.config(text=strings[key])

# Function to handle the login button click event
def login_button_click():
    email = email_entry.get()
    password = password_entry.get()

    # Perform login validation or further processing here
    print("Email:", email)
    print("Password:", password)

# Create the main window
window = tk.Tk()
window.title("Login Form")

# Language selection dropdown menu
language_var = tk.StringVar()
language_var.set('English')
language_options = ['English', 'Arabic']
language_dropdown = tk.OptionMenu(window, language_var, *language_options, command=update_labels)
language_dropdown.pack()

# Load the initial strings from the English language file
strings = load_strings("/Users/social/Documents/Work/Rabida_Demo/Rabida_Demo/Strings/ar.lproj/Localizable.strings")

# Create labels for each key-value pair
label_list = []
for key in ["EnterEmail", "EnterPassword"]:
    label_text = strings[key]  # Initial language string
    label = tk.Label(window, text=label_text)
    label.pack()
    label_list.append(label)

# Email entry field
email_entry = tk.Entry(window)
email_entry.pack()

# Password entry field
password_entry = tk.Entry(window, show='*')
password_entry.pack()

# Login button
login_button = tk.Button(window, text=strings["SubmitButton"], command=login_button_click)
login_button.pack()

# Run the interface
window.mainloop()
