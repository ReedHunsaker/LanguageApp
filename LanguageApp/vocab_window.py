import tkinter as tk
from tkinter import ttk
from LanguageApp.create_flashcards import Create_flascards
from LanguageApp.cloud_cards import Cloud_cards
from LanguageApp.create_window import Create
import LanguageApp.CONSTANTS as design


class Vocab_window:
    """Class controls the vocab card window"""
    def __init__(self, root, db, name):
        self.root = root
        self.db = db
        self.name = name
        self.access = "Online"
        self.get_access()
        self.current_index = 1
        self.flip = 1
        self.target = True
        self._indexes = self.cards.get_file_list()
        self._word = ''
        self._scentence = ''
        self.create_screen()

    def create_screen(self):
        """Build the flashcard screen

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        self.root_and_frame()
        self.edit_word()
        self.edit_scentence()
        self.button_flip()
        self.button_next()
        self.button_modify()
        self.button_delete()
        self.display_card_number()
        self.rewrite_card_number()
        self.get_vocab()
        self.set_target(True)
        self.vocab_word()
        self.vocab_scentence()
        self.word_label()
        self.scentence_label()
        self.menu()
        self.right_click()
        # self.button_back()
    
    def get_access(self):
        """sets the access to either cloud cards or file cards

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        if self.access == "Online":
            self.cards = Cloud_cards(self.db, self.name)
        else:
            self.cards = Create_flascards(self.db, self.name)

    def root_and_frame(self):
        """format the window

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        self.root.title('Vocab Cards')
        self.root.geometry(design.geometry)
        self.frame = tk.Frame(self.root)
    
    def vocab_word(self):
        """sets vocab word

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        self.word.delete("1.0", tk.END)
        self.word.insert(tk.END, self._word)
    
    def vocab_scentence(self):
        """sets vocab scentence

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        self.scentence.delete("1.0", tk.END)
        self.scentence.insert(tk.END, self._scentence)

    def edit_word(self):
        """GUI element for vocab word

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        self.word = tk.Text(self.root, height = 4, width = 30)
        self.word.grid(row = 0, column = 1, padx = 15, pady =15)
        self.word['font'] = ('Helvetica', 20)
        # self.word['bg'] = 'darkgreen'
        self.word['fg'] = 'black'
        self.word['borderwidth'] = 0
        self.word['highlightthickness'] = 0


    def edit_scentence(self):
        """GUI element for vocab scentence

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        self.scentence = tk.Text(self.root, height = 4, width = 30, wrap = 'word')
        self.scentence.grid(row = 1, column = 1, padx = 15, pady =15)
        self.scentence['font'] = ('Helvetica', 20)
        # self.scentence['bg'] = 'darkgreen'
        self.scentence['fg'] = 'black'
        self.scentence['borderwidth'] = 0
        self.scentence['highlightthickness'] = 0

    def button_flip(self):
        """GUI flip button

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        text = "Flip"
        font = design.button_font
        read = tk.Button(self.root, text = text, font = font, height=2, width=20)
        read.grid(row = 3, column = 0, pady = 5, padx = 2)
        read.config(command = lambda: self.refresh_flip())

    def refresh_flip(self):
        """command to flip the card to the other side

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        self.flip += 1
        if self.flip % 2 == 0:
            self.target = True
        else:
            self.target = False
        self.set_target(self.target)
        self.vocab_word()
        self.vocab_scentence()
    
    def button_next(self):
        """GUI next button

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        text = "Next"
        font = design.button_font
        read = tk.Button(self.root, text = text, font = font, height=2, width=20)
        read.grid(row = 3, column = 1, pady = 5, padx = 2, sticky = 'w')
        read.config(command = lambda: self.refresh_next())
    
    def button_modify(self):
        """GUI modify button

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        text = "Modify"
        font = design.button_font
        read = tk.Button(self.root, text = text, font = font, height=1, width=20)
        read.grid(row = 4, column = 0, pady = 5, padx = 2, sticky = 'w')
        read.config(command = lambda: self.init_mod())
    
    def button_delete(self):
        """GUI delete button

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        text = "Delete"
        font = design.button_font
        read = tk.Button(self.root, text = text, font = font, height=1, width=20)
        read.grid(row = 4, column = 1, pady = 5, padx = 2, sticky = 'w')
        read.config(command = lambda: self.delete_card())
    
    def delete_card(self):
        """Run the command to delete the current card

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        self.cards.delete_card(self.current_index)
    
    def init_mod(self):
        """Initalize the modifcation window

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        mod_window = tk.Toplevel(self.root)
        mod = Modify_window(mod_window, self.db, self.name, self.current_index)
    
    # def button_back(self):
    #     text = "Back"
    #     font = "Helvetica"
    #     read = tk.Button(self.root, text = text, font = font, height=2, width=20)
    #     read.grid(row = 3, column = 0, pady = 5, padx = 2)
    #     read.config(command = lambda: self.refresh_back())
    
    def refresh_next(self):
        """Build gui

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        self.get_next_card()
        self.get_vocab()
        self.set_target(self.target)
        self.vocab_word()
        self.rewrite_card_number()
        self.vocab_scentence()
    
    # def refresh_back(self):
    #     self.get_last_card()
    #     self.get_vocab()
    #     self.set_target(self.target)
    #     self.vocab_word()
    #     self.rewrite_card_number()
    #     self.vocab_scentence()

    def get_vocab(self):
        """Get the vocab words and scentences

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        card_list = self.cards.call_card(self.current_index)
        print(card_list)
        self.target_word = card_list["target_word"]
        self.target_scentence = card_list["target_scentence"]
        self.naitive_word = card_list["naitive_word"]
        self.naitive_scentence = card_list["naitive_scentence"]
    
    def get_next_card(self):
        """Advance to the next card

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        if self.current_index < self._indexes:
            self.current_index += 1
        else:
            self.current_index = 1
    
    # def get_last_card(self):
    #     if self.current_index > self._indexes:
    #         self.current_index -= 1
    #     else:
    #         self.current_index = 1
    
    def set_target(self, target):
        """show either the target or naitive vocab word

        Args:
            self (Vocab_window): An instance of Vocab_window
            target (bool): True is the target word, False is the native word
        """
        if target == True:
            self._word = self.target_word
            self._scentence = self.target_scentence
        elif target == False:
            self._word = self.naitive_word
            self._scentence = self.naitive_scentence

    def display_card_number(self):
        """Gets the current card number

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        self.card_number = tk.Text(self.root, width = 20, height = 4)
        self.card_number.grid(row = 2, column = 1, sticky = 'w')
        self.card_number['font'] = ('Helvetica', 18)
        self.card_number['borderwidth'] = 0
        self.card_number['highlightthickness'] = 0

    def rewrite_card_number(self):
        """Refreshes the flash card

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        card_number = f'Card Number: {self.current_index}'
        self.card_number.delete("1.0", tk.END)
        self.card_number.insert(tk.END, card_number)
    
    def word_label(self):
        """Label vocab word part of flashcard

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        text = 'Vocabulary\n word: '
        self.wl = tk.Label(self.root, text = text)
        self.wl.grid(column = 0, row = 0, sticky = 'n', pady = 10)
        self.wl.config(font =('Helvetica', 20))
        self.wl['borderwidth'] = 0
        self.wl['highlightthickness'] = 0

    def scentence_label(self):
        """label the example scentence part of flashcard

        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        text = 'Example\n Scentence: '
        self.sl = tk.Label(self.root, text = text)
        self.sl.grid(column =0, row = 1, sticky = 'n', pady = 10)
        self.sl.config(font =('Helvetica', 20))
        self.sl['borderwidth'] = 0
        self.sl['highlightthickness'] = 0


    def menu(self):
        """right click menu

        Args:
            self (Vocab_window): An instance of Vocab_window
            event (event): Grabs events from the computer input
        """
        self.m = tk.Menu(self.root, tearoff = False)
        self.m.add_command(label = 'Dark Mode', command = lambda: self.change_apperance(design.fg_darkmode, design.bg_darkmode ))
        self.m.add_command(label = 'Light Mode', command = lambda: self.change_apperance(design.fg_default, design.bg_default))

    def popup(self, event):
        """Right click pop up at cursor location

        Args:
            self (Vocab_window): An instance of Vocab_window
            event (event): Grabs events from the computer input
        """
        try:
            self.m.tk_popup(event.x_root, event.y_root)
        finally:
            self.m.grab_release()

    def change_apperance(self, fg, bg):
        """Change the apperance to either darkmode or lightmode

        Args:
            self (Vocab_window): an instance of Vocab_window
            fg (string): string containing the foreground hexcode
            bg (string): string contating the background gexcode 
        """
        self.root['bg'] = bg
        self.scentence['bg'] = bg
        self.scentence['fg']= fg
        self.word['fg']= fg
        self.word['bg'] = bg
        self.card_number['bg'] = bg
        self.card_number['fg'] = fg
        self.sl['bg'] = bg
        self.sl['fg'] = fg
        self.wl['bg'] = bg
        self.wl['fg'] = fg


    def right_click(self):
        """Controls the commnads to right click
        
        Args:
            self (Vocab_window): An instance of Vocab_window
        """
        
        #Windows friendly commands

        self.word.bind("<Button-3>", self.popup)
        self.scentence.bind("<Button-3>", self.popup)

        #Mac friendly commands

        self.word.bind("<Button-2>", self.popup)
        self.scentence.bind("<Button-2>", self.popup)
        self.scentence.bind("<Control-Button-1>", self.popup)
        self.word.bind("<Control-Button-1>", self.popup)
    
class Modify_window(Create):
    def __init__(self, root, db, name, current_index):
        super().__init__(root, db, name)
        self.current_index =  current_index
    
    def column_zero(self):
        """Gui elements in column 0

        Args:
            self (Modify_window): An instance of Modify_window
        """
        title_label = tk.Label(self.root, text = "Update Vocabulary Card", font = 16)
        title_label.grid(row = 0, columnspan = 2)
        target_word_label = tk.Label(self.root, text = "Target Word: ")
        target_word_label.grid(row = 1, column = 0)
        target_scentence_label = tk.Label(self.root, text = "Target Scentence: ")
        target_scentence_label.grid(row = 2, column = 0)
        naitive_word_label = tk.Label(self.root, text = "Naitive Word: ")
        naitive_word_label.grid(row = 3, column = 0)
        naitive_scentence_label = tk.Label(self.root, text = "Naitive Scentence: ")
        naitive_scentence_label.grid(row = 4, column = 0)

    def button_create(self):
        """Changes the create button to an update button

        Args:
            self (Modify_window): An instance of Modify_window
        """
        text = "update"
        font = design.button_font
        read = tk.Button(self.root, text = text,font = font)
        read.grid(row = 5, column = 0)
        read.config(command = lambda: self.run_modify())
    
    def run_modify(self):
        """runs the modify function with the user inputed data

        Args:
            self (Modify_window): An instance of Modify_window
        """
        self._target_word = self.target_word_entry.get()
        self._target_scentence = self.target_scentence_entry.get()
        self._naitive_word = self.naitive_word_entry.get()
        self._naitive_scentence = self.naitive_scentence_entry.get()
        data = {"target_word": self._target_word,
                "target_scentence": self._target_scentence,
                "naitive_word": self._naitive_word,
                "naitive_scentence": self._naitive_scentence,
                "card_number": self.current_index,
                "User_name": self.name}
        self.card_creation.modify(self.current_index, data)
        self.close_window()