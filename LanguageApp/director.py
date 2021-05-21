import LanguageApp.secret.api_key as secret
from LanguageApp.window import Window
import LanguageApp.CONSTANTS as design
import firebase_admin
import pyrebase
from firebase_admin import credentials
from firebase_admin import firestore
from LanguageApp.gui import GUI
import tkinter as tk
import os

class Director:
    """Class to initalize the GUI and Database"""
    def __init__(self):
        self._app = tk.Tk()
        cwd = os.getcwd()
        icon = tk.PhotoImage(file = f'LanguageApp/icon.png')
        self._app.iconphoto(True,icon)

    def initialize_gui_menu(self):
        """Initalize the gui menu

        Args:
            self (Director): An instance of Director
        """
        init_db = self.initalize_database()
        self.db = init_db[0]
        self.auth = init_db[1]
        gui = GUI(self._app, self.db, self.auth)
        self._app.mainloop()

    def initalize_database(self):
        """Initalize the cloud database

        Args:
            self (Director): An instance of Director
        
        return:
            db (Pyrebase): Pyrebase database object
            auth (Pyrebase): Pyrebase authentication object
        """
        # Use the application default credentials
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = design.database
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {
        'projectId': 'language-app-8e630',
        })

        

        config = {
            "apiKey": secret.api_key,
            "authDomain": "language-app-8e630.firebaseapp.com",
            "databaseURL": "https://language-app-8e630-default-rtdb.firebaseio.com",
            "projectId": "language-app-8e630",
            "storageBucket": "language-app-8e630.appspot.com",
            "messagingSenderId": "1021961728179",
            "appId": "1:1021961728179:web:570475c6ccd22529f600c6",
            "measurementId": "G-W4BYKWPGB1",
            "serviceAccount" : design.database
        }
        firebase = pyrebase.initialize_app(config)
        def noquote(s):
            return s
        pyrebase.pyrebase.quote = noquote

        auth = firebase.auth()
        db = firebase.database()
        return (db, auth)
