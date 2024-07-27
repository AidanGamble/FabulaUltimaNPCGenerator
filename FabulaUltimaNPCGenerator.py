import customtkinter
import frames


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Fabula Ultima NPC Generator")
        self.geometry("450x600")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.minsize(450, 600)

        self.name_frame = frames.MyTextBoxFrame(self, "NPC Name", values=["Bertrum Lorefinder"])
        self.name_frame.grid(row=0, column=0, columnspan = 2, padx=10, pady=10, sticky="new")
        
        self.identity_frame = frames.MyTextBoxFrame(self, "Identity", values=["Four recommended"])
        self.identity_frame.grid(row=1, column=0, columnspan = 2, padx=10, pady=10, sticky="news")

        #self.checkbox_frame = frames.MyCheckboxFrame(self, "Values", values=["Option 1","Option 2","Option 3"])
        #self.checkbox_frame.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="news")
        self.stat_frame = frames.MyRadiobuttonFrame(self, "Stat Array",
        values=["Jack of All Trades: d8, d8, d8, d8", "Standard: d10, d8, d8, d6",
                "Specialized: d10, d10, d6, d6", "Super Specialized: d12, d8, d6, d6"])
        self.stat_frame.grid(row=2, column=0, padx=(0, 10), pady=(10, 0), sticky="news")
        self.species_frame = frames.MyRadiobuttonFrame(self, "Species",
        values=["Beast", "Construct", "Demon", "Humanoid", "Monster", "Plant", "Undead"])
        self.species_frame.grid(row=2, column=1, padx=(0, 10), pady=(10, 0), sticky="news")

        self.next = customtkinter.CTkButton(self, text="Next", command=self.button_callback)
        self.next.grid(row=3, column=1, padx=10, pady=10, sticky="new")
        self.back = customtkinter.CTkButton(self, text="Back", command=self.button_callback)
        self.back.grid(row=3, column=0, padx=10, pady=10, sticky="new")

    def button_callback(self):
        print("Name:", self.name_frame.entry.get())
        print("Identity:", self.identity_frame.entry.get())
        print("Stat Array:", self.stat_frame.get())
        print("Identity:", self.species_frame.get())

app = App()
app.mainloop()