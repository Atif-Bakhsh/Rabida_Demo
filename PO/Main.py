# import gettext
# import tkinter as tk

# def set_language(lang):
#     translation = gettext.translation('Rabida_Demo', languages=[lang])
#     translation.install()

# def create_gui():
#     window = tk.Tk()
#     window.title(_("Login Page"))

#     email_label = tk.Label(window, text=_("Enter your Email"))
#     email_label.pack()

#     email_entry = tk.Entry(window)
#     email_entry.pack()

#     password_label = tk.Label(window, text=_("Enter your password"))
#     password_label.pack()

#     password_entry = tk.Entry(window)
#     password_entry.pack()

#     submit_button = tk.Button(window, text=_("Send"))
#     submit_button.pack()

#     window.mainloop()

# if __name__ == '__main__':
#     set_language('en')  # Set the desired language ('en' for English)

#     _ = gettext.gettext  # Create a shortcut function for translations

#     create_gui()
