from LanguageApp.director import Director

class LanguageApp():
    def __init__(self):
        pass
    def run_app(self):
        """ Run the Language App

        self (LanguageApp): an instance of Language App
        """
        app = Director()
        app.initialize_gui_menu()


def main():
    language_app = LanguageApp()
    language_app.run_app()

if __name__ == "__main__":
    main()