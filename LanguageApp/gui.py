import tkinter as tk

from firebase_admin.exceptions import FirebaseError
from LanguageApp.window import Window
from LanguageApp.vocab_window import Vocab_window
from LanguageApp.books import Books
import LanguageApp.CONSTANTS as design
from firebase_admin import auth
from PIL import ImageTk, Image
import os
from random import randint

class GUI:
    """
    Controls the main Window in the GUI

    Stereotype:
        Controller
    
    Atrributes:
        _app (Tkinter): Initalize the gui
        books (Books): initalize the Books class
        target_language (string) = Target language of user
        naitive_language (string) = Naitive language of user
    """
    def __init__(self, root, db, auth):
        """Initailize the gui

        Args:
            self (GUI): An instance of gui
            root (Tkinter): An instance of Tkinter
        """
        self._app = root
        self.db = db
        self.auth = auth
        self.books = Books()
        self.target_language = design.spanish
        self.native_language = design.english
        self.main()


    
    def open_window(self):
        """Opens Window Class which stores the reading
        see also the read button

        Args:
            self (GUI): An instance of gui
        """
        self.dropdown_command()
        self.readWindow = tk.Toplevel(self._app)
        self.read = Window(self.readWindow, self.db, self.name)
        self.read.set_text(self.target_text, self.naitive_text)
        self.read.set_target(self.target_language)
        self.read.titles()
    
    def open_vocab(self):
        """Opens vocabWinow Class which stores the flashcards
        see also the study button

        Args:
            self (GUI): An instance of gui
        """
        self.vocabWindow = tk.Toplevel(self._app)
        self.vocab = Vocab_window(self.vocabWindow, self.db, self.name)
        self.vocab.vocab_word()
        self.vocab.vocab_scentence()

    def main(self):
        """Structure of the window

        Args:
            self (GUI): An instance of gui
        """
        self.root = self._app
        self.root_and_frame()
        self.background()
        self.authentication()
        # self.title()
        
    def authentication(self):
        """Structure of the authentication window

        Args:
            self (GUI): An instance of gui
        """
        self.username_label()
        #username label
        #password label

        self.create_account_button()
        self.login()
        #create account button
        #login button
    
    def username_label(self):
        """Gui elements for the username and password

        Args:
            self (GUI): An instance of gui
        """
        self.login_form = []

        self.username_text = tk.Label(self.root, text = "username: ", font = design.label_font_size)
        self.username_text.pack(side = "top", pady = 12, padx = 12)
        self.login_form.append(self.username_text)

        self.username_instert = tk.Entry(self.root)
        self.username_instert.pack(side = "top", pady = 12, padx = 12)
        self.login_form.append(self.username_instert)

        self.password_text = tk.Label(self.root, text = "password: ", font = design.label_font_size)
        self.password_text.pack(side = "top", pady = 12, padx = 12)
        self.login_form.append(self.password_text)

        self.password_insert = tk.Entry(self.root)
        self.password_insert.pack(side = "top", pady = 12, padx = 12)
        self.login_form.append(self.password_insert)

    def create_account_button(self):
        """Create account button

        Args:
            self (GUI): An instance of gui
        """
        text = "Create Account"
        font = design.button_font
        self.account_button = tk.Button(self.root, text = text,font = font,  height= design.button_big_height, 
        width= design.button_big_width, bg = design.button_background)
        self.account_button.pack(side = "top", pady = 12, padx = 12)
        self.account_button.config(command = lambda: self.transition_manager_new())
        self.login_form.append(self.account_button)
    
    def login(self):
        """Login button

        Args:
            self (GUI): An instance of gui
        """
        text = "Login"
        font = design.button_font
        self.login_button = tk.Button(self.root, text = text,font = font,  height= design.button_big_height, 
        width= design.button_big_width, bg = design.button_background)
        self.login_button.pack(side = "top", pady = 12, padx = 12)
        self.login_button.config(command = lambda: self.transition_manager_main())
        self.login_form.append(self.login_button)


    def transition_manager_new(self):
        """Transitions to the new account menu

        Args:
            self (GUI): An instance of gui
        """
        for item in self.login_form:
            item.destroy()
        self.new_account()
    
    def new_account_form(self):
        """Gui elements for the new account window

        Args:
            self (GUI): An instance of gui
        """
        self.form_list = []
        self.username_new = tk.Label(self.root, text = "username: ", font = design.label_font_size)
        self.username_new.pack(side = "top", pady =6, padx = 12)
        self.form_list.append(self.username_new)

        self.username_new_insert = tk.Entry(self.root)
        self.username_new_insert.pack(side = "top", pady = 6, padx = 12)
        self.form_list.append(self.username_new_insert)

        self.email = tk.Label(self.root, text = "email: ", font = design.label_font_size)
        self.email.pack(side = "top", pady = 6, padx = 12)
        self.form_list.append(self.email)

        self.email_insert = tk.Entry(self.root)
        self.email_insert.pack(side = "top", pady = 6, padx = 12)
        self.form_list.append(self.email_insert)

        self.password_new = tk.Label(self.root, text = "new password: ", font = design.label_font_size)
        self.password_new.pack(side = "top", pady = 6, padx = 12)
        self.form_list.append(self.password_new)

        self.password_new_insert = tk.Entry(self.root)
        self.password_new_insert.pack(side = "top", pady = 6, padx = 12)
        self.form_list.append(self.password_new_insert)

        self.password_new_confirm = tk.Label(self.root, text = " confirm new password: ", font = design.label_font_size)
        self.password_new_confirm.pack(side = "top", pady = 6, padx = 12)
        self.form_list.append(self.password_new_confirm)

        self.password_new_confirm_insert = tk.Entry(self.root)
        self.password_new_confirm_insert.pack(side = "top", pady = 6, padx = 12)
        self.form_list.append(self.password_new_confirm_insert)
    
    def create_new_account_button(self):
        """Create new account button 

        Args:
            self (GUI): An instance of gui
        """
        text = "Create New Account"
        font = design.button_font
        self.account_button_new = tk.Button(self.root, text = text,font = font,  height= design.button_big_height, 
        width= design.button_big_width, bg = design.button_background)
        self.account_button_new.pack(side = "top", pady = 6, padx = 12)
        self.account_button_new.config(command = lambda: self.transition_manager_login())
        self.form_list.append(self.account_button_new)

    def new_account(self):
        """Structure of the create account window

        Args:
            self (GUI): An instance of gui
        """
        self.new_account_form()
        self.create_new_account_button()
        self.root.title(design.create_title)
        

    def check_password(self):
        """Checks that the password is the same as the confirm password

        Args:
            self (GUI): An instance of gui
        """
        password = self.password_new_insert.get()
        password_confirm = self.password_new_confirm_insert.get()
        if password == password_confirm:
            return True
        else:
            return False


    def google_authentification(self):
        """Creates a user in the firebase databases

        Args:
            self (GUI): An instance of gui
        """
        username = self.username_new_insert.get()
        password = self.password_new_confirm_insert.get()
        email = self.email_insert.get()
        auth.create_user(display_name = username, email = email, password = password, uid = username)
        # self.db.child("Users").child(self.name)

    def google_login_auth(self):
        """authenticates a users login

        Args:
            self (GUI): An instance of gui
        """
        username = self.username_instert.get()
        try:
            user = auth.get_user(username)
        except auth.UserNotFoundError or FirebaseError or ValueError:
            self.popup_window("No user by that name")
        print(user.uid)
        print(user.email)
        try:
            self.current_user = self.auth.sign_in_with_email_and_password(user.email, self.password_insert.get())
        except:
            self.popup_window("Invalid Passwrod")
        self.name = self.auth.get_account_info(self.current_user['idToken'])
        print(self.name)
        self.name = self.name['users'][0]['displayName']
        print(self.name)


    def transition_manager_login(self):
        """Transition to the login if the account creates

        Args:
            self (GUI): An instance of gui
        """
        confirmed = self.check_password()
        if confirmed is True:
            self.google_authentification()
            for item in self.form_list:
                item.destroy()
            self.authentication()
            self.root.title(design.login_title)
        else:
            self.popup_window("Password does not match")
            

    def popup_window(self, text):
        """Simple pop up window

        Args:
            self (GUI): An instance of gui
        """
        popup = tk.Toplevel(self._app)
        popup.title(design.app_title)
        popup_geo = design.geometry_translate_popup
        popup_geo = popup_geo.split('x')
        popup.minsize(width= popup_geo[0], height= popup_geo[1])

        popup_label = tk.Label(popup, text = text)
        popup_label.grid(row = 0, column = 0)

        popup_button = tk.Button(popup, text = "Okay", command=popup.destroy)
        popup_button.grid(row = 1, column=0)


    def transition_manager_main(self):
        """Transition to main app

        Args:
            self (GUI): An instance of gui
        """
        self.google_login_auth()
        for item in self.login_form:
            item.destroy()
        self.switch_main()

    def switch_main(self):
        """Structure of the main window

        Args:
            self (GUI): An instance of gui
        """
        self.root.title(self.name + '-' + design.app_title)
        self.set_text()
        self.initialize_langue_dropdown()
        self.language_dropdown()
        self.set_language_current()
        self.button_read()
        self.button_study()
        

    def root_and_frame(self):
        """Controls the frame and root variables
        -Title 
        -Geometry

        Args:
            self (GUI): An instance of gui
        """
        self.root.title(design.login_title)
        self.root.geometry(design.geometry)

    def button_read(self):
        """Button to open Read window

        Args:
            self (GUI): An instance of gui
        """
        text = "Read"
        font = design.button_font
        read = tk.Button(self.root, text = text,font = font,  height= design.button_big_height, 
        width= design.button_big_width, bg = design.button_background)
        read.pack(side = "top", pady = 12, padx = 12)
        read.config(command = lambda: self.open_window())
    
    def initialize_langue_dropdown(self):
        """initalize the logic and text behind the drop down 

        Args:
            self (GUI): An instance of gui
        """
        self.i = randint(0,design.foriegn_all_length - 1)
        self.LANGUAGES = design.foriegn_all
        self.target_language = self.LANGUAGES[self.i]

    def language_dropdown(self):
        """Format the drop down

        Args:
            self (GUI): An instance of gui
        """
        self.variable = tk.StringVar(self.root)
        self.variable.set(self.LANGUAGES[self.i])
        self.dropdown = tk.OptionMenu(self.root, self.variable, *self.LANGUAGES)
        self.dropdown.pack(side = 'top', pady=40)
        # self.dropdown['command'] = lambda: self.main()

    def button_study(self):
        """Button to open Study window

        Args:
            self (GUI): An instance of gui
        """
        text = "Study"
        font = design.button_font
        read = tk.Button(self.root, text = text,font = font,  height= design.button_big_height, 
        width= design.button_big_width, bg = design.button_background)
        read.pack(side = "top", pady = 12, padx = 12)
        read.config(command = lambda: self.open_vocab())
    
    def set_language_current(self):
        """Sets target language

        Args:
            self (GUI): An instance of gui
        """
        self.target_language = self.variable.get()

    def set_text(self):
        """Sets text based on language

        Args:
            self (GUI): An instance of gui
        """
        self.books.set_naitive_language(self.native_language)
        self.books.set_foriegn_language(self.target_language)
        self.target_text = self.books.get_foriegn_language()
        self.naitive_text = self.books.get_naitive_language()

    def dropdown_command(self):
        """Method to change languagge when someone changes dropdown

        Args:
            self (GUI): An instance of gui
        """
        self.set_language_current()
        self.set_text()

    def background(self):
        """Manages background photos

        Args:
            self (GUI): An instance of gui
        """
        cwd = os.getcwd()
        language = self.target_language
        i = randint(1,4)
        image = Image.open(f'{cwd}/LanguageApp/{language}/photo{i}.jpg')

        #grab window gemoetry from constants as (###x###) 
        #split it and make it an int
        
        window_geo = design.geometry
        geo = window_geo.split("x")
        image = image.resize((int(geo[0]),int(geo[1])), Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(image)
        bg_label = tk.Label(self.root, image = bg)
        bg_label.place(x=0,y=0, relwidth =1, relheight = 1)
        bg_label.image = bg
