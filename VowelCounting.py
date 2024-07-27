'''
A class to count the vowels in a string
P Jenkin 27/7/24
'''

import pyphen
import nltk
from nltk.tokenize import SyllableTokenizer
from nltk.tokenize import LegalitySyllableTokenizer
#from nltk.util import word_tokenize
from nltk.corpus import words
import re   # reluctantly use regex (boo!)

class VowelCounter:
    def __init__(self, input_string):
        self.vowel_occurrences_count = [0] * 5
        # ordinary_vowels = ['a', 'e', 'i', 'o', 'u']
        self.ordinary_vowels = "aeiou"
        self.y_vowel_occurrences = [0]  # https://stackoverflow.com/q/74412503
        self.strTechCornwall = input_string
        self.nltk_ok = True

        '''
        Natural Language ToolKit corpus d'require a download
        '''

        try:
            nltk.download('punkt')
            self.SSP = SyllableTokenizer()
            self.split = SSP.tokenize(strTechCornwall)
        except:
            print("Could not download punkt")
            self.nltk_ok = False
            # punkt not yet actually needed in this code
            # (alternative syllable splitting method)

        try:
            nltk.download('words')  # try downloading corpus
            # might crash if 'words' not downloaded
            self.words_split = nltk.word_tokenize(strTechCornwall, language='english')
            # get the individual words
            self.LP = LegalitySyllableTokenizer(words.words())
            # ready the NLTK tokenizer using downloaded using the corpus called 'words'
            syllables_split = [self.LP.tokenize(word) for word in self.words_split]
            # get the individual syllables of this string
            # https://www.nltk.org/api/nltk.tokenize.legality_principle.html
        except:
            print("Could not download NLTK 'words'")
            nltk_ok = False

    # check character for a vowel
    # returns 0 for no vowel, -1 for a vowel
    def check_for_vowel(self, character):
        # if character is in list of vowels
        vowel_index = self.ordinary_vowels.find(character)
        # look for this character in string/list of ordinary vowels
        if vowel_index != -1:
            # if the character
            self.vowel_occurrences_count[vowel_index] = self.vowel_occurrences_count[vowel_index] + 1
            # increment that vowel's occurrence counter
            return -1
        return 0

        # https://www.merriam-webster.com/grammar/why-y-is-sometimes-a-vowel-usage
        #

        # split into words
        # split into syllables
    '''
    Check for presence of y-as-vowel.
    One character-at-a-time, but...
    ... submit whole words, because words and syllables are inspected.
    Returns 0 for no y, -1 for a y vowel, -2 for a y but not a vowel
    '''
    def check_for_y_vowel(self, word, index_within_word : int):
        character = word[index_within_word]
        if character != 'y':
            return 0 # if not a 'y', don't bother

        if re.search('['+ self.ordinary_vowels + ']', word) is False:
            self.y_vowel_occurrences[0] = self.y_vowel_occurrences[0] + 1
            return -1
        # if this is a word but has no 'aeiou', then this 'y' must be a vowel
        # (assuming not an acronym or something wacky)

        if index_within_word == len(word)-1:
            self.y_vowel_occurrences[0] = self.y_vowel_occurrences[0] + 1
            return -1
        # if this is a 'y' at the end of the word, this y must be a vowel
        # (could be the end of a diphthong)

        if self.nltk_ok is True:     # only try this if the NLTK corpus payload downloaded ok
            if index_within_word == len(self.LP.onset(word)):
                self.y_vowel_occurrences[0] = self.y_vowel_occurrences[0] + 1
                return -1

        # bit sus: 'y' in syllable nucleus can be a vowel;
        # here saying, if first character after a word's onset
        # (i.e. first in nucleus) is a 'y' then tis a vowel (which is sus, but nvmd)
        # this code only working for monosyllablic words at present
        return -2
        # on the fence regarding y-in-a-diphthong..... (TBA)

        # (i) no other vowel in syllable, (ii) at end of word, (iii) in middle/nucleus of syllable
        # also: if in diphthong?

        # (i) no vowel in syllable - tricky - need to count vowels per syllable
        # (ii) end of word - need to compare this position with end-of-words positions
        # (iii) in middle/nucleus of syllable - maybe check to see if not first or last character of syllable

        # words_split
        # syllables_split
        # https://stackoverflow.com/a/18449491


    # from itertools import chain
    # def flatten_syllables(syllable_list):
    #     return list(chain.from_iterable(syllable_list))

    def print_vowel_counts(self, count):
        #[print (x.to_string() + ":" + count[x.index()]) for x in count]
        [print(self.ordinary_vowels[i] + ":" + str(x)) for i, x in enumerate(count)]
        # loop through ordinary vowels (get the index as i am fond of old-fashioned indexing)
        # for each vowel print
        # for every vowel
        # print the vowel followed by its occurrence count

