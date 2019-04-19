import pytest

class WeirdFixtures:
    @pytest.fixture
    def example_text(self):
        string = 'This is a long looong test sentence,\n' \
                 'with some big (biiiiig) words!'
        return string

    @pytest.fixture
    def my_text(self):
        string = 'Czesc,\n'\
                 'jestem Dominik\n'\
                 'test: jeden, oko, dwa, drzewa, ,slowo. ?!% t%!?s 121d%dsc^&cds? 123 432423 ++++\n'\
                 '___ --- -wdkas- ::dfs:: .:hejka:. .... weird   ,      , {}{} {sdsd}'\
                 'milego dnia'
        return string

    @pytest.fixture
    def short_word(self):
        return 'taak'

    @pytest.fixture
    def same_letters_word(self):
        return 'tiiiik'

    @pytest.fixture
    def proper_word(self):
        return 'task'

    @pytest.fixture
    def longer_proper_word(self):
        return 'weird'

    @pytest.fixture
    def weird_word(self):
        return '121d%dsc^&cds?'

    @pytest.fixture
    def simple_text(self):
        string = 'tiiis this tis'
        return string

    @pytest.fixture
    def weird_text(self):
        string = '%^&* t%!?s 321'
        return string

    @pytest.fixture
    def proper_word_list(self):
        return ['string', 'weird']

    @pytest.fixture
    def output1(self):
        string = '\n—weird—\n'\
                 'Tihs is a lnog loonog tset sntceene,\n'\
                 'wtih smoe big (biiiiig) wdros!'\
                 '\n—weird—\n'\
                 'long looong sentence some test This with words'
        return string

    @pytest.fixture
    def output2(self):
        string = '\n—weird—\n'\
                 'Ceszc,\n'\
                 'jtseem Dmniiok\n'\
                 'tset: jdeen, oko, dwa, dzrewa, ,solwo. ?!% t%!?s 112d%dsc^&cds? 123 423243 ++++\n'\
                 '___ --- -wkdas- ::dfs:: .:hjkea:. .... wried   ,      , {}{} {ssdd}mglieo dina'\
                 '\n—weird—\n'\
                 '121d 432423 Czesc Dominik dnia drzewa hejka jeden jestem milego sdsd slowo test wdkas weird'
        return string
