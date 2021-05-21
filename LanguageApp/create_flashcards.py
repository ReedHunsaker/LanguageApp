import os
import csv
class Create_flascards:
    """
        Creates/reads flash cards to/from the folder flashcards

        Stereotype:
            Service Provider
        
        Atrributes:
             cwd (os): gets current workind directory
            db (Pyrebase): an instence of pyrebase database
            name (string): A string with the user name of the current user
    """
    def __init__(self, db, name):
        """Creates the flash card save file

        Args:
            self (Create_flashcards): An instance of Create_flashcards
        """

        self.cwd = os.getcwd()
        self.db = db
        self.name = name
    
    def create_card(self, target_word, target_scentence, naitive_word, naitive_scentence):
        """Creates the flash card save file

        Args:
            self (Create_flashcards): An instance of Create_flashcards
            target_word(string): Word the user wants to learn
            target_scentence(string): Context scentence
            naitive_word (string): Word in naitive language
            naitive_scenetence (string): Contex scentence in native language
            index_number (integer): Vocab card number
        """
        file_count = self.get_file_list()
        file_count += 1
        index_number = file_count
        card = f"""{target_word},{target_scentence},{naitive_word},{naitive_scentence}"""
        file_write = open(f"vocab_card{index_number}.csv", "a")
        file_write.write(card)
        file_write.close()

        os.rename(f'{self.cwd}/vocab_card{index_number}.csv', f'{self.cwd}/LanguageApp/flashcards/vocab_card{index_number}.csv')

    def call_card(self, index_number):
        """Call the card and make it into a list

        Args:
        self (Create_flashcards): An instance of Create_flashcards
        index_number (integer): Vocab card number
        """
        card = f'LanguageApp/flashcards/vocab_card{index_number}.csv'
        card_list = []
        with open(card, 'r') as read_card:
            lines = csv.reader(read_card, delimiter = ",")
            for line in lines:
                for entry in line:
                    card_list.append(entry)
        return card_list

    def get_file_list(self):
        """gets number of entries in flashcard file

        Args:
            self (Create_flashcards): An instance of Create_flashcards
        """
        file_list = []
        for root, dirs, files in os.walk(f'{self.cwd}/LanguageApp/flashcards/'):
            for filed in files:
                file_list.append(filed)
        return len(file_list) -1
