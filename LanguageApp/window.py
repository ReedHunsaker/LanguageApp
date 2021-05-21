import tkinter as tk
from LanguageApp.translate_word import Translate_word
from LanguageApp.create_window import Create
import LanguageApp.CONSTANTS as design
class Window:
    """
    Controls the main Window in the GUI

    Stereotype:
        GUI
    
    Atrributes:
        root (GUI): Initalize the GUI
        root_and_frame (method): Controls title and dimensions of the frame of GUI
        translator (Translate_word): Initallizes the Translate word class inside of Window
        menu (Method): Calls the menu method that controls the right click menu
        edit_text1 (method): Calls the method that edits the left side of the text
        edit_text2 (method): Calls the method that edits the right side of the text
        right_click (method): Calls the method that holds the commands to right click
    """
    def __init__(self, root, db, name):
        """Initalize the Window class

        Args:
            self (Window): An instance of Window
            root(tkinter): initalizes the GUI framework
        """
        self.root = root
        self.db = db
        self.name = name
        self.root_and_frame()
        self.translator = Translate_word()
        self.menu()
        self.edit_text1()
        self.edit_text2()
        self.right_click()
        self.naitive_language = design.english
        self.target_language = design.spanish

    def root_and_frame(self):
        """Controls the frame and root variables
        -Title 
        -Geometry

        Args:
            self (Window): An instance of Window
        """
        self.root.title('LanguageApp')
        self.root.geometry(design.geometry_read)
        self.frame1 = tk.Frame(self.root)

    def right_click(self):
        """Controls the commnads to right click
        
        Args:
            self (Window): An instance of Window
        """
        
        #Windows friendly commands

        self.text.bind("<Button-3>", self.popup)
        self.text2.bind("<Button-3>", self.popup)

        #Mac friendly commands

        self.text.bind("<Button-2>", self.popup)
        self.text2.bind("<Button-2>", self.popup)
        self.text2.bind("<Control-Button-1>", self.popup)
        self.text.bind("<Control-Button-1>", self.popup)


    def set_text(self, text, text2):
        """Input the text to be displayed

        Args:
            self (Window): An instance of Window
            text (string): The text on the left
            text2 (string): The text on the right
        """
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, text)
        self.text2.delete("1.0", tk.END)
        self.text2.insert(tk.END, text2)

    def edit_text1(self):
        """Controls the style of the left text

        Args:
            self (Window): An instance of Window
        """
        self.text = tk.Text(self.root, width =40, borderwidth=1)
        self.text.pack(fill = tk.BOTH, expand =1, side ='left', padx= 40, pady=40)
        self.text['font'] = design.text_font
        self.text['borderwidth'] = 0
        self.text['highlightthickness'] = 0

    def edit_text2(self):
        """Controls the style of the right text

        Args:
            self (Window): An instance of Window
        """
        self.text2 = tk.Text(self.root, width = 40, borderwidth=1)
        self.text2.pack(fill = tk.BOTH, expand = 1, side = 'right', padx= 40, pady=40)
        self.text2['font'] = design.text_font
        # self.text2['bg'] = "darkgreen"
        self.text2['borderwidth'] = 0
        self.text2['highlightthickness'] = 0

    def translate(self):
        """The translate command

        Args:
            self (Window): An instance of Window
        """

        #pop up intialize

        popup = tk.Tk()
        popup.wm_title("Translation")
        geo = design.geometry_translate_popup
        geo = geo.split('x')
        popup.minsize(int(geo[0]),int(geo[1]))

        #get selected text

        text_selected = ""
        text_selected = self.text.get('sel.first', 'sel.last')
        self.translator.set_text(text_selected)

        self.translator.set_naitive_language(design.english)
        self.translator.set_target_language(self.target_language)

        #Get translated text & languages

        translated_text = self.translator.translation()

        #display text

        text_selected = f"{text_selected}: {translated_text}"

        #formatting for the popup

        label = tk.Label(popup, text = text_selected, font= design.text_font)
        label.pack(side ="top", fill='x', pady = 10)
        Bl = tk.Button(popup, text="Okay", command = popup.destroy)
        Bl.pack()
        popup.mainloop()

        #reset selected text to avoid confusion
        text_selected = ""

    def menu(self):
        """Right click menu

        Args:
            self (Window): An instance of Window
        """
        self.m = tk.Menu(self.root, tearoff = False)
        self.m.add_command(label = 'Dark Mode', command = lambda: self.change_appearnce(design.fg_darkmode, design.bg_darkmode))
        self.m.add_command(label = 'Light Mode', command = lambda: self.change_appearnce(design.fg_default, design.bg_default))
        self.m.add_separator()
        self.m.add_command(label = 'Translate', command = lambda : self.translate())
        self.m.add_command(label = 'Add Flash Card', command = lambda: self.command_create_flashcard())
    
    def command_create_flashcard(self):
        """Command to create a new flash cared

        Args:
            self (Window): An instance of Window
        """
        level = tk.Toplevel(self.root)
        create = Create(level, self.db, self.name)
        create.set_target_word(self.return_selected_text())
        create.set_naitive_word(self.return_translated_word())
        create.set_entry_target()
        create.set_entry_naitive()
        level.mainloop()

    def return_selected_text(self):
        """Gets selected text

        Args:
            self (Window): An instance of Window
        """
        text_selected = ""
        text_selected = self.text.get('sel.first', 'sel.last')
        return text_selected

    def return_translated_word(self):
        """returns translated word

        Args:
            self (Window): An instance of Window
        """
        word = self.return_selected_text()
        self.translator.set_text(word)
        translated_text = self.translator.translation()
        return translated_text

    def popup(self, event):
        """Right click pop up at cursor location

        Args:
            self (Window): An instance of Window
            event (event): Grabs events from the computer input
        """
        try:
            self.m.tk_popup(event.x_root, event.y_root)
        finally:
            self.m.grab_release()
        
    
    def titles(self):
        """format for the title of the page

        Args:
            self (Window): An instance of Window
        """
        self.book_title = "1 Nephi 1"
        text = f'{self.target_language}     {self.book_title}     {self.naitive_language}'
        self.title1 = tk.Label(self.root, text = text, anchor = 'w')
        self.title1.pack(side = 'left', anchor = 'n')
    
    def set_target(self, language):
        """sets the target language

        Args:
            self (Window): An instance of Window
            language (string): target language
        """
        self.target_language = language

    def change_appearnce(self, fg, bg):
        """change colors on the screen

        Args:
            self (Window): An instance of Window
            fg (string): hexcode for foreground colors
            bg (string): hexcode for background colors
        """
        self.root['bg'] = bg
        self.text2['bg'] = bg
        self.text2['fg']= fg
        self.text['fg']= fg
        self.text['bg'] = bg
        self.title1['bg'] = bg
        self.title1['fg'] = fg