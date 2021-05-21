from translate import Translator

class Translate_word:
    """
    Translates words and keeps track of target and naitive language

    Stereotype:
        Service Provider
    
    Atrributes:
        _target_language (string): The language the user will translate to
        _naitive_language (string): The language the user will translate from
        _text (string): word and/or text to be translated

    """
    def __init__(self):
        """The class constructor.

        Args:
            self (Translate_word): An instance of translate word.
        """
        self._target_language = ""
        self._naitive_language = ""
        self._text = ""

    def set_text(self, text):
        """Set the text value

        Args:
            self (Translate_word): An instance of translate word.
            text (string): text and/or word value
        """
        self._text = text
    
    def get_text(self):
        """Get the text from the class

        Args:
            self (Translate_word): An instance of translate word.
        """
        return self._text
    
    def set_target_language(self, target_language):
        """Set the target language to the current use

        Args:
            self (Translate_word): An instance of translate word.
            target_language (string): The target language Ex:(Spanish, Tagalog, Chinese)
        """
        self._target_language = target_language
    
    def get_target_language(self):
        """Return the target language

        Args:
            self (Translate_word): An instance of translate word.
        """
        return self._target_language
    
    def set_naitive_language(self, naitive_language):
        """Set the naitive language

        Args:
            self (Translate_word): An instance of translate word.
            naitive_language (string): The langugae naitive to translate from Ex: (English, Spanish, French)
        """
        self._naitive_language = naitive_language
    
    def get_naitive_language(self):
        """Return naitive language

        Args:
            self (Translate_word): An instance of translate word.
        """
        return self._naitive_language
    
    def translation(self):
        """Translate the word

        Args:
            self (Translate_word): An instance of translate word.
        """
        translator = Translator(to_lang=self._naitive_language, 
        from_lang = self._target_language)
        original = self._text
        try:
            result = translator.translate(original)
        except:
            result = "Error 404: Page not found"
        return result


# new = Translate_word()
# new.set_text('Hello')
# new.set_naitive_language('English')
# new.set_target_language('Spanish')
# new_word = new.translation()
# print(new_word)