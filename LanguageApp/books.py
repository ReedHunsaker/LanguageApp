class Books:
    """Class to get the right text file to display to the user"""
    def __init__(self):
        self._naitive_text = ""
        self._foriegn_text = ""
    
    def set_naitive_language(self, language):
        """Set the naitive language text

        args:
            Self (Books): An instance of Books
            language (string): the langauge file desiered
        """
        book = f'LanguageApp/Languages/{language}.txt'
        with open(book, 'r') as read_book:
            lines = read_book.read()
            self._naitive_text = lines

    def get_naitive_language(self):
        """return the contents of the text file

        args:
            Self (Books): An instance of Books
        """
        return self._naitive_text

    def set_foriegn_language(self, language):
        """Set the foriegn language text

        args:
            Self (Books): An instance of Books
            language (string): the langauge file desiered
        """
        book = f'LanguageApp/Languages/{language}.txt'
        with open(book, 'r') as read_book:
            lines = read_book.read()
            self._foriegn_text = lines

    def get_foriegn_language(self):
        """return the contents of the foriegn language text file

        args:
            Self (Books): An instance of Books
        """
        return self._foriegn_text

# book = Books()
# book.set_foriegn_language('spanish')
# print(book.get_foriegn_language())