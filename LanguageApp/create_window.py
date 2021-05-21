from LanguageApp.create_flashcards import Create_flascards
from LanguageApp.cloud_cards import Cloud_cards
import tkinter as tk
from tkinter import ttk
import LanguageApp.CONSTANTS as design

#grid geometry manager

class Create:
    """Window used to create the flash cards"""
    def __init__(self, root, db, name):
        """Initalize the create class


        Arguments:
            self (Create): An instance of the create class
            root (Tkinter): An instance of the Tkinter class
            db (Pyrebase): an instence of pyrebase database
            name (string): A string with the user name of the current user
        """

        self.name = name
        self.db = db
        self.root = root
        self.access = "online"
        self.access_cards()
        self.root_and_frame()
        self.column_zero()
        self.column_one()
        self.button_cancel()
        self.button_create()
        self._target_word = ""
        self._target_scentence = ""
        self._naitive_word = ""
        self._naitive_scentence = ""

    def access_cards(self):
        """choose to use either local cards or cloud cards

        Args:
            self (Create): An instance of Window
        """
        if self.access == "online":
            self.card_creation = Cloud_cards(self.db, self.name)
        else:
            self.card_creation = Create_flascards(self.db, self.name)

    def root_and_frame(self):
        """Controls the frame and root variables
        -Title 
        -Geometry

        Args:
            self (Create): An instance of Window
        """
        self.root.title(design.app_title)
        self.root.geometry(design.geometry_create)
        self.frame1 = tk.Frame(self.root)
    
    def column_zero(self):
        """Gui elements in column 0

        Args:
            self (Create): An instance of Window
        """
        title_label = tk.Label(self.root, text = "Add Vocabulary Card", font = 16)
        title_label.grid(row = 0, columnspan = 2)
        target_word_label = tk.Label(self.root, text = "Target Word: ")
        target_word_label.grid(row = 1, column = 0)
        target_scentence_label = tk.Label(self.root, text = "Target Scentence: ")
        target_scentence_label.grid(row = 2, column = 0)
        naitive_word_label = tk.Label(self.root, text = "Naitive Word: ")
        naitive_word_label.grid(row = 3, column = 0)
        naitive_scentence_label = tk.Label(self.root, text = "Naitive Scentence: ")
        naitive_scentence_label.grid(row = 4, column = 0)

    def column_one(self):
        """GUI elements in column 1

        Args:
            self (Create): An instance of Window
        """
        self.target_word_entry = tk.Entry(self.root)
        self.target_word_entry.grid(row = 1, column = 1)
        self.target_scentence_entry = tk.Entry(self.root)
        self.target_scentence_entry.grid(row = 2, column = 1)
        self.naitive_word_entry = tk.Entry(self.root)
        self.naitive_word_entry.grid(row = 3, column = 1)
        self.naitive_scentence_entry = tk.Entry(self.root)
        self.naitive_scentence_entry.grid(row = 4, column = 1)

    def button_create(self):
        """GUI Button create

        Args:
            self (Create): An instance of Window
        """
        text = "Create"
        font = design.button_font
        read = tk.Button(self.root, text = text,font = font)
        read.grid(row = 5, column = 0)
        read.config(command = lambda: self.run_creation())
    
    def button_cancel(self):
        """GUI button cancel

        Args:
            self (Create): An instance of Window
        """
        text = "Close"
        font = design.button_font
        read = tk.Button(self.root, text = text,font = font)
        read.grid(row = 5, column = 1)
        read.config(command = lambda: self.close_window())
    
    def close_window(self):
        """close the current window

        Args:
            self (Create): An instance of Window
        """
        self.root.destroy()

    def set_target_word(self, word):
        """set the target word 

        Args:
            self (Create): An instance of Window
        """
        self._target_word = word
    
    def set_naitive_word(self, word):
        """set the naitive word

        Args:
            self (Create): An instance of Window
        """
        self._naitive_word = word

    def set_entry_target(self):
        """updates the target word insert to have the data highlighted from Read window

        Args:
            self (Create): An instance of Window
        """
        self.target_word_entry.delete(0, "end")
        self.target_word_entry.insert(0, self._target_word)
    
    def set_entry_naitive(self):
        """updates the naitive word insert to have the data highlighted from Read window

        Args:
            self (Create): An instance of Window
        """
        self.naitive_word_entry.delete(0, "end")
        self.naitive_word_entry.insert(0, self._naitive_word)
    
    def run_creation(self):
        """Passes the user input into the create_card funciton

        Args:
            self (Create): An instance of Window
        """
        self._target_word = self.target_word_entry.get()
        self._target_scentence = self.target_scentence_entry.get()
        self._naitive_word = self.naitive_word_entry.get()
        self._naitive_scentence = self.naitive_scentence_entry.get()
        self.card_creation.create_card(self._target_word, self._target_scentence,
        self._naitive_word, self._naitive_scentence)
        self.close_window()
        