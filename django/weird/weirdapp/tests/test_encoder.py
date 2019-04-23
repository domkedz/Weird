import pytest
import re
from weirdapp.fixtures import fixtures
from collections import Counter
from weirdapp.weird_text import Weird, Encoder, Decoder


class TestWeird(fixtures.WeirdFixtures):
    def test_same_letters(self, short_word, same_letters_word, proper_word,
                          longer_proper_word, weird_word):
        assert Encoder.same_letters(short_word) == True
        assert Encoder.same_letters(same_letters_word) == True
        assert Encoder.same_letters(proper_word) == False
        assert Encoder.same_letters(longer_proper_word) == False
        assert Encoder.same_letters(weird_word) == False

    def test_finding_words_for_change(self, simple_text, weird_text):
        assert Weird.find_words_for_change(simple_text) == ['this']
        assert Weird.find_words_for_change(weird_text) == []

    def test_changing_word_in_string(self, simple_text,proper_word):
        assert Weird.replace_words(simple_text, ['this'], ['task']) == 'tiiis '+'task'+' tis'


class TestEncoder(fixtures.WeirdFixtures):
    def test_shuffle(self, proper_word, longer_proper_word):
        shuffled = Encoder.shift_letters(proper_word)
        assert shuffled[0] == proper_word[0]
        assert shuffled[-1] == proper_word[-1]
        assert Encoder.shift_letters(proper_word) != proper_word
        shuffled = Encoder.shift_letters(longer_proper_word)
        assert shuffled[0] == longer_proper_word[0]
        assert shuffled[-1] == longer_proper_word[-1]
        assert Encoder.shift_letters(longer_proper_word) != longer_proper_word

    def test_change_words_in_list(self, proper_word_list):
        weird_word_list = Encoder.change_words(proper_word_list)
        assert len(proper_word_list) == len(weird_word_list)
        assert weird_word_list[0] != proper_word_list[0]
        assert Counter(filter(str.isalnum, proper_word_list[0])) == Counter(filter(str.isalnum, weird_word_list[0]))
        assert Counter(filter(str.isalnum, proper_word_list[1])) == Counter(filter(str.isalnum, weird_word_list[1]))

    def test_output_encoder(self, example_text):
        pattern = r'('+Weird.indicator+')(.*(\n.*)*)('+Weird.indicator+')(.*)'
        e = Encoder(example_text)
        encoded_string = e.encode_string()
        tokenize_re = re.compile(pattern)
        matched_groups = tokenize_re.match(encoded_string)
        assert matched_groups != None

    def test_output2_encoder(self, my_text):
        pattern = r'('+Weird.indicator+')(.*(\n.*)*)('+Weird.indicator+')(.*)'
        e = Encoder(my_text)
        encoded_string = e.encode_string()
        tokenize_re = re.compile(pattern)
        matched_groups = tokenize_re.match(encoded_string)
        print(matched_groups)
        assert matched_groups != None

