# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk
# import gettext

# def set_language(lang):
#     translation = gettext.translation('Rabida_Demo', languages=[lang], localedir='.')
#     translation.install()
#     root.title(_("Login Page"))
#     email_label.configure(text=_("Enter your Email"))
#     password_label.configure(text=_("Enter your password"))
#     submit_button.configure(text=_("Send"))

# def toggle_language():
#     current_lang = gettext.translation().info()['language']
#     new_lang = 'ar' if current_lang == 'en' else 'en'
#     set_language(new_lang)

# root = tk.Tk()
# root.geometry("300x200")
# root.title("Login Page")

# # Language Toggle Button
# toggle_button = ttk.Button(root, text="Toggle Language", command=toggle_language)
# toggle_button.pack(pady=20)

# # Email Label and Entry
# email_label = ttk.Label(root, text="Enter your Email")
# email_label.pack(pady=10)
# email_entry = ttk.Entry(root)
# email_entry.pack()

# # Password Label and Entry
# password_label = ttk.Label(root, text="Enter your password")
# password_label.pack(pady=10)
# password_entry = ttk.Entry(root, show="*")
# password_entry.pack()

# Submit Button
# submit_button = ttk.Button(root, text="Send", command=lambda: messagebox.showinfo("Message", "Form submitted!"))
# submit_button.pack(pady=20)

# # Set initial language to English
# set_language('en')

# root.mainloop()
