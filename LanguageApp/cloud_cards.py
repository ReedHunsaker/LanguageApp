class Cloud_cards:
    """Logic for implementing the cloud database with the flashcards"""
    def __init__(self, db, name):
        """Creates the flash card save file

        Args:
            self (Cloud_flashcards): An instance of Cloud_flashcards
            db (Pyrebase): an instence of pyrebase database
            name (string): A string with the user name of the current user
        """

        self.db = db
        self.name = name
    
    def create_card(self, target_word, target_scentence, naitive_word, naitive_scentence):
        """Creates the flash card save file

        Args:
            self (Cloud_flashcards): An instance of Cloud_flashcards
            target_word(string): Word the user wants to learn
            target_scentence(string): Context scentence
            naitive_word (string): Word in naitive language
            naitive_scenetence (string): Contex scentence in native language
        """
        index_length = self.get_file_list()
        card_number = index_length + 1
        data = {"target_word": target_word,
                "target_scentence": target_scentence,
                "naitive_word": naitive_word,
                "naitive_scentence": naitive_scentence,
                "card_number": card_number,
                "User_name": self.name}
        self.db.child("Users").push(data)
    
    def call_card(self, current_index):
        """Call the card and make it into a dictionary

        Args:
        self (Cloud_flashcards): An instance of Cloud_flashcards
        index_number (integer): Vocab card number
        """
        card_data = self.db.child("Users").order_by_child("User_name").equal_to(self.name).get()
        for values in card_data.each():
            card = values.val()
            if card["card_number"] == current_index:
                return card
    
    def get_file_list(self):
        """Get the number of flash cards in the database under the current user

        Args:
        self (Cloud_flashcards): An instance of Cloud_flashcards
        """
        count_me = []
        card_number_data = self.db.child("Users").order_by_child("User_name").equal_to(self.name).get()
        for item in card_number_data.each():
            print(item.val()["card_number"])
            count_me.append(item.val())
        return len(count_me)
    
    def modify(self, current_index, data):
        """Update the current flash card with new data

        Args:
        self (Cloud_flashcards): An instance of Cloud_flashcards
        current_index (int): flash card number
        data (dict): dicitonary including the data to be updated
        """
        card_data = self.db.child("Users").order_by_child("User_name").equal_to(self.name).get()
        for values in card_data.each():
            card = values.val()
            if card["card_number"] == current_index:
                mod_card = values.key()
        new_data = {f"Users/{mod_card}" : data}
        self.db.update(new_data)

    def delete_card(self, current_index):
        """Delete a flash card from the cloud database

        Args:
        self (Cloud_flashcards): An instance of Cloud_flashcards
        current_index (int): flash card number that will be deleted
        """
        card_data = self.db.child("Users").order_by_child("User_name").equal_to(self.name).get()
        for values in card_data.each():
            card = values.val()
            if card["card_number"] == current_index:
                mod_card = values.key()
        
        self.db.child("Users").child(mod_card).remove()