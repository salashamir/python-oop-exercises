"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """Class to read random words from a file/dictionary
    
    >>> wordfinder = WordFinder("words3.txt")
    4 words read

    >>> wordfinder.random() in ['aberrator','aberrometer','aberroscope','aberuncator']
    True

    >>> wordfinder.random() in ['aberrator','aberrometer','aberroscope','aberuncator']
    True

    >>> wordfinder.random() in ['aberrator','aberrometer','aberroscope','aberuncator']
    True
    """

    def __init__(self, path_to_file):
        """Reads file and prints out number of words read"""
        self.file_path = path_to_file
        self.word_list = self.__read_from_file__(self.file_path)
        self.__print_num_words_read__()

    def __read_from_file__(self, path_to_file):
        """Parse the file into a list of words"""
        list_of_words = []
        with open(path_to_file, 'r') as f:
            for word in f:
                list_of_words.append(word.strip())
        return list_of_words

    def __print_num_words_read__(self):
        """Helper function to print out how many words read"""
        print(f'{len(self.word_list)} words read')

    def random(self):
        """Return a random word from the word_list attribute"""
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """Subclass inherits from WordFinder, meant to discard comment lines and blacnk lines whenr eading file
    
    Parse file into list of words, skipping over blank lines and comments starting with #
        
    >>> swf = SpecialWordFinder('words2.txt')
    4 words read

    >>> swf.random() in ['kale','parsnips','apple','mango']
    True

    >>> swf.random() in ['kale','parsnips','apple','mango']
    True

    >>> swf.random() in ['kale','parsnips','apple','mango']
    True

    >>> swf.random() in ['kale','parsnips','apple','mango']
    True
    """
    def __read_from_file__(self, path_to_file):
        """Parse words from file filtering out blank lines and comments"""
        list_of_words = []
        with open(path_to_file, 'r') as f:
            for word in f:
                if word.strip() and not word.startswith('#'):
                    list_of_words.append(word.strip())
        return list_of_words
