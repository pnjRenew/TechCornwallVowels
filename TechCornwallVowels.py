import pyphen
import nltk
from nltk.tokenize import SyllableTokenizer
from nltk.tokenize import LegalitySyllableTokenizer
#from nltk.util import word_tokenize
from nltk.corpus import words
import re   # reluctantly use regex (boo!)

from VowelCounting import VowelCounter

'''
initialisation
'''
#
# vowel_occurrences_count = [0] * 5
# #ordinary_vowels = ['a', 'e', 'i', 'o', 'u']
# ordinary_vowels = "aeiou"
# y_vowel_occurrences = [0]       # https://stackoverflow.com/q/74412503
strTechCornwall = "Tech Cornwall Career Pathways"
# nltk_ok = True

'''
Natural Language ToolKit corpus d'require a download
'''

#
# try:
#     nltk.download('punkt')
#     SSP = SyllableTokenizer()
#     split = SSP.tokenize(strTechCornwall)
# except:
#     print("Could not download punkt")
#     nltk_ok = False
#     # punkt not yet actually needed in this code
#     # (alternative syllable splitting method)
#
#
#
# try:
#     nltk.download('words')  # try downloading corpus
#     # might crash if 'words' not downloaded
#     words_split = nltk.word_tokenize(strTechCornwall, language='english')
#     # get the individual words
#     LP = LegalitySyllableTokenizer(words.words())
#     # ready the NLTK tokenizer using downloaded using the corpus called 'words'
#     syllables_split = [LP.tokenize(word) for word in words_split]
#     # get the individual syllables of this string
#     # https://www.nltk.org/api/nltk.tokenize.legality_principle.html
# except:
#     print("Could not download NLTK 'words'")
#     nltk_ok = False

#
# def check_for_vowel(character):
#     # if character is in list of vowels
#     vowel_index = ordinary_vowels.find(character)
#     # look for this character in string/list of ordinary vowels
#     if vowel_index != -1:
#         # if the character
#         vowel_occurrences_count[vowel_index] = vowel_occurrences_count[vowel_index] + 1
#         # increment that vowel's occurrence counter
#
#     # https://www.merriam-webster.com/grammar/why-y-is-sometimes-a-vowel-usage
#     #
#
#     # split into words
#     # split into syllables
#
# '''
# Check for presence of y-as-vowel.
# One character-at-a-time, but...
# ... submit whole words, because words and syllables are inspected.
# '''
# def check_for_y_vowel(word, index_within_word : int):
#     character = word[index_within_word]
#     if character != 'y':
#         return  # if not a 'y', don' bother
#
#     if re.search('['+ ordinary_vowels + ']', word) is False:
#         y_vowel_occurrences[0] = y_vowel_occurrences[0] + 1
#         return
#     # if this is a word but has no 'aeiou', then this 'y' must be a vowel
#     # (assuming not an acronym or something wacky)
#
#     if index_within_word == len(word)-1:
#         y_vowel_occurrences[0] = y_vowel_occurrences[0] + 1
#         return
#     # if this is a 'y' at the end of the word, this y must be a vowel
#     # (could be the end of a diphthong)
#
#     if nltk_ok is True:     # only try this if the NLTK corpus payload downloaded ok
#         if index_within_word == len(LP.onset(word)):
#             y_vowel_occurrences[0] = y_vowel_occurrences[0] + 1
#     # bit sus: 'y' in syllable nucleus can be a vowel;
#     # here saying, if first character after a word's onset
#     # (i.e. first in nucleus) is a 'y' then tis a vowel (which is sus, but nvmd)
#     # this code only working for monosyllablic words at present
#
#     # on the fence regarding y-in-a-diphthong..... (TBA)
#
#     # (i) no other vowel in syllable, (ii) at end of word, (iii) in middle/nucleus of syllable
#     # also: if in diphthong?
#
#     # (i) no vowel in syllable - tricky - need to count vowels per syllable
#     # (ii) end of word - need to compare this position with end-of-words positions
#     # (iii) in middle/nucleus of syllable - maybe check to see if not first or last character of syllable
#
#     # words_split
#     # syllables_split
#     # https://stackoverflow.com/a/18449491
#     return
#
# # from itertools import chain
# # def flatten_syllables(syllable_list):
# #     return list(chain.from_iterable(syllable_list))
#
# def print_vowel_counts(count):
#     #[print (x.to_string() + ":" + count[x.index()]) for x in count]
#     [print(ordinary_vowels[i] + ":" + str(x)) for i, x in enumerate(count)]
#     # loop through ordinary vowels (get the index as i am fond of old-fashioned indexing)
#     # for each vowel print
#     # for every vowel
#     # print the vowel followed by its occurrence count


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def main_vowel_count(strTechCornwall):


    print(strTechCornwall)
    # print the string
    user_input = input("Type in text to test, or press ENTER to count vowels in text above :")
    if user_input != "":
        strTechCornwall = user_input
    # get user's choice of string, if any

    vowel_counter = VowelCounter(strTechCornwall)

    [vowel_counter.check_for_vowel(x) for x in re.sub('[!? #@£$.]','',strTechCornwall)]
    # check every character to see if vowel (remove punctuation with regex)
    if vowel_counter.nltk_ok:
        #[check_for_y_vowel(x, i) for i, x in enumerate(re.sub('[!? #@£$.]','',strTechCornwall))]
        for word in vowel_counter.words_split:
            [vowel_counter.check_for_y_vowel(word, i) for i, x in enumerate(re.sub('[!? #@£$.]', '', word))]
    # if NLTK download was ok, check every character of every word for any y-as-vowel
    vowel_counter.print_vowel_counts(vowel_counter.vowel_occurrences_count)     # print the results
    if vowel_counter.y_vowel_occurrences[0] > 0:
        print("y:%d" % vowel_counter.y_vowel_occurrences[0])





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    main_vowel_count(strTechCornwall)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
