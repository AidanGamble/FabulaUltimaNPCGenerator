import customtkinter

class nameError(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x150")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.attributes("-topmost",True)

        self.label = customtkinter.CTkLabel(self, text="Name cannot be blank!", font=("Arial", 15))
        self.label.grid(row=0, sticky="news")

        self.close = customtkinter.CTkButton(self, text="Close", command=self.button_callback)
        self.close.grid(row=1, pady=10)

    def button_callback(self):
            self.destroy()

class levelError(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x150")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.attributes("-topmost",True)

        self.label = customtkinter.CTkLabel(self, text="Level cannot be blank!", font=("Arial", 15))
        self.label.grid(row=0, sticky="news")

        self.close = customtkinter.CTkButton(self, text="Close", command=self.button_callback)
        self.close.grid(row=1, pady=10)

    def button_callback(self):
            self.destroy()

class levelIntError(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x150")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.attributes("-topmost",True)

        self.label = customtkinter.CTkLabel(self, text="Level must be an integer!", font=("Arial", 15))
        self.label.grid(row=0, sticky="news")

        self.close = customtkinter.CTkButton(self, text="Close", command=self.button_callback)
        self.close.grid(row=1, pady=10)

    def button_callback(self):
            self.destroy()

class levelRangeError(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x150")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.attributes("-topmost",True)

        self.label = customtkinter.CTkLabel(self, text="Level must be within 5 - 60!", font=("Arial", 15))
        self.label.grid(row=0, sticky="news")

        self.close = customtkinter.CTkButton(self, text="Close", command=self.button_callback)
        self.close.grid(row=1, pady=10)

    def button_callback(self):
            self.destroy()

class identityError(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x150")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.attributes("-topmost",True)

        self.label = customtkinter.CTkLabel(self, text="Identity cannot be blank!", font=("Arial", 15))
        self.label.grid(row=0, sticky="news")

        self.close = customtkinter.CTkButton(self, text="Close", command=self.button_callback)
        self.close.grid(row=1, pady=10)

    def button_callback(self):
            self.destroy()

class statError(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x150")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.attributes("-topmost",True)

        self.label = customtkinter.CTkLabel(self, text="Select a stat array!", font=("Arial", 15))
        self.label.grid(row=0, sticky="news")

        self.close = customtkinter.CTkButton(self, text="Close", command=self.button_callback)
        self.close.grid(row=1, pady=10)

    def button_callback(self):
            self.destroy()

class speciesError(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x150")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.attributes("-topmost",True)

        self.label = customtkinter.CTkLabel(self, text="Select a species!", font=("Arial", 15))
        self.label.grid(row=0, sticky="news")

        self.close = customtkinter.CTkButton(self, text="Close", command=self.button_callback)
        self.close.grid(row=1, pady=10)

    def button_callback(self):
            self.destroy()