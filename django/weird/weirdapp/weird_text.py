import re
import random
from collections import Counter


string = 'This is a long looong test sentence,\n' \
         'with some big (biiiiig) words!'


class Weird:
    # indicator = '\n-weird-\n' # I know...
    indicator = '-weird-'
    max_string_size = 200

    @staticmethod
    def same_letters(word):
        for it in range(2,len(word)-1):
            if word[1] != word[it]:
                return False
        return True

    @staticmethod
    def find_words(orginal_string):
        pattern = r'(\w+)'
        return re.findall(pattern, orginal_string)

    @classmethod
    def check_words(cls, list_words):
        words_to_encode = []
        for word in list_words:
            if len(word) > 3 and not cls.same_letters(word): # leave words that have less than 3 letters
                words_to_encode.append(word)                   # and check if letters in word is the same
        return words_to_encode

    @classmethod
    def find_words_for_change(cls, string):
        all_words = cls.find_words(string)
        return cls.check_words(all_words)

    @staticmethod
    def replace_words(string_to_change, words_to_change, changed_words):
        for word,shuffled in zip(words_to_change,changed_words):
            string_to_change = string_to_change.replace(word, shuffled)
        return string_to_change


class Encoder(Weird):
    def __init__(self, orginal_string):
        self.string = orginal_string

    @staticmethod
    def check_lenght(string):
        if len(string) > Weird.max_string_size:
            raise ValueError

    @staticmethod
    def shift_letters(word):
        word = list(word)
        if len(word) == 4: # for change letters in every case in short words
            word[1], word[2] = word[2], word[1]
            return "".join(word)
        else:
            while True:
                inside_letters = word[1:-1] # slice first and last letter
                random.shuffle(inside_letters) # shuffle inside letters
                inside_letters.insert(0,word[0]) # add beginning letter
                inside_letters.append(word[-1]) # add last letter
                if inside_letters != word: # check if new word is different
                    break

            return "".join(inside_letters)

    @classmethod
    def change_words(cls, list_words):
        changed_words = []
        for word in list_words:
            changed_words.append(cls.shift_letters(word))
        return changed_words

    def encode_string(self):
        Encoder.check_lenght(self.string)
        proper_words = Weird.find_words_for_change(self.string)
        shuffled_words = Encoder.change_words(proper_words)

        self.string = Weird.replace_words(self.string, proper_words, shuffled_words)

        proper_words.sort()

        return Weird.indicator + \
               self.string + \
               Weird.indicator + \
               " ".join(proper_words)



class Decoder(Weird):

    def __init__(self, string):
        self.string = string
        self.weird_text = []
        self.weird_words = []
        self.proper_words = []
        self.recognise_weird(string)

    def recognise_weird(self, string):
        pattern = r'('+Weird.indicator+')(.*(\n.*)*)('+Weird.indicator+')(.*)'
        # pattern = r'(\n-weird-\n)([\0-\377[:nonascii:]*)(\n-weird-\n)(.*)'
        tokenize_re = re.compile(pattern)
        matched_groups = tokenize_re.match(string)
        if matched_groups:
            self.weird_text = str(matched_groups.group(2))
            self.proper_words = str(matched_groups.group(5))
        else:
            raise ValueError

    @staticmethod
    def remove_indicator(string):
        return string[len(Weird.indicator):]

    @staticmethod
    def find_words(orginal_string):
        pattern = r'(\w+)'
        return re.findall(pattern, orginal_string)

    @staticmethod
    def sort_list(weird_list, proper_words):
        proper_order=[]
        for word in weird_list:
            for proper_word in proper_words:
                if Counter(filter(str.isalnum, word)) == Counter(filter(str.isalnum, proper_word)):
                    proper_order.append(proper_word)

        return proper_order

    def decode_string(self):
        proper_weird_words = Weird.find_words_for_change(self.weird_text)
        proper_words = Weird.find_words(self.proper_words)
        ordered_proper_words = Decoder.sort_list(proper_weird_words, proper_words)

        self.weird_text = Weird.replace_words(self.weird_text, proper_weird_words, ordered_proper_words)

        return self.weird_text


# executing:
# e=Encoder(string)
# encoded_string = e.encode_string()
#
# d=Decoder(encoded_string)
# decoded_string = d.decode_string()
#
# print(encoded_string)
# print(decoded_string)
