import customtkinter
import frames
import errorWindow
import NPCDataHandler
        

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Fabula Ultima NPC Generator")
        self.geometry("450x550")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0,1,2,3), weight=1)
        self.minsize(450, 550)

        self.toplevel_window = None
        self.firstPage()

    def firstPage(self):

        frames.clearFrame(self)
        #First Page
        self.name_frame = frames.MyTextBoxFrame(self, "NPC Name", values=["Bertrum Lorefinder"])
        self.name_frame.grid(row=0, column=0, columnspan = 2, padx=10, pady=10, sticky="new")
        
        self.identity_frame = frames.MyTextBoxFrame(self, "Identity", values=["Four recommended"])
        self.identity_frame.grid(row=1, column=0, columnspan = 2, padx=10, pady=10, sticky="news")

        #self.checkbox_frame = frames.MyCheckboxFrame(self, "Values", values=["Option 1","Option 2","Option 3"])
        #self.checkbox_frame.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="news")
        self.level_frame = frames.MyTextBoxFrame(self, "Level", values=["5-60"])
        self.level_frame.grid(row=2, column=0, padx=10, pady=10, sticky="new")
        
        self.stat_frame = frames.MyRadiobuttonFrame(self, "Stat Array",
        values=["Jack of All Trades: d8, d8, d8, d8", "Standard: d10, d8, d8, d6",
                "Specialized: d10, d10, d6, d6", "Super Specialized: d12, d8, d6, d6"])
        self.stat_frame.grid(row=3, column=0, padx=(0, 10), pady=(10, 0), sticky="news")

        self.species_frame = frames.MyRadiobuttonFrame(self, "Species",
        values=["Beast", "Construct", "Demon", "Humanoid", "Monster", "Plant", "Undead"])
        self.species_frame.grid(row=2, column=1, rowspan=2, padx=(0, 10), pady=(10, 0), sticky="news")

        self.next = customtkinter.CTkButton(self, text="Next", command=self.secondPage)
        self.next.grid(row=4, column=1, padx=10, pady=10, sticky="ne")
        self.back = customtkinter.CTkButton(self, text="Back", command=self.back_button_callback)
        self.back.grid(row=4, column=0, padx=10, pady=10, sticky="nw")
    
    def secondPage(self):

        #Get data from first page before moving on
        name = self.name_frame.entry.get()
        level = self.level_frame.entry.get()
        identity = self.identity_frame.entry.get()
        stat_array = self.stat_frame.get()
        species =  self.species_frame.get()
        
        #Check that all entry tables are valid
        if not name:
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = errorWindow.nameError(self)
        elif not identity:
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = errorWindow.identityError(self)
        elif not level:
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = errorWindow.levelError(self)
        elif not level.isdigit():
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = errorWindow.levelIntError(self)
        elif not stat_array:
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = errorWindow.statError(self)
        elif not species:
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = errorWindow.speciesError(self)
        else:
            newNPC = NPCDataHandler.NPCEntry(name, identity, level, stat_array, species)
            NPCDataHandler.addNPC(newNPC)

        if self.toplevel_window:
            self.toplevel_window.after(10, self.toplevel_window.lift)
        
        #Clear frame and add new elements
        frames.clearFrame(self)

        #Page 2

        self.next = customtkinter.CTkButton(self, text="Next", command=self.next_two_button_callback)
        self.next.grid(row=4, column=1, padx=10, pady=10, sticky="ne")
        self.back = customtkinter.CTkButton(self, text="Back", command=self.firstPage())
        self.back.grid(row=4, column=0, padx=10, pady=10, sticky="nw")
    
    def back_button_callback(self):
        #Just clears the page, expand
        frames.clearFrame(self)
    
    def next_two_button_callback(self):
        print("Working")

    


app = App()
app.mainloop()