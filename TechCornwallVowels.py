import pyphen
import nltk
from nltk.tokenize import SyllableTokenizer
from nltk.tokenize import LegalitySyllableTokenizer
#from nltk.util import word_tokenize
from nltk.corpus import words
import re   # reluctantly use regex (boo!)


vowel_occurrences_count = [0] * 5
#ordinary_vowels = ['a', 'e', 'i', 'o', 'u']
ordinary_vowels = "aeiou"
strTechCornwall = "Tech Cornwall Career Pathways"
try:
    nltk.download('punkt')
except:
    print("Could not download punkt")
SSP = SyllableTokenizer()
split = SSP.tokenize(strTechCornwall)

try:
    nltk.download('words')  # try downloading corpus
except:
    print("Could not download NLTK 'words'")
# might crash if 'words' not downloaded
words_split = nltk.word_tokenize(strTechCornwall, language='english')
# get the individual words
LP = LegalitySyllableTokenizer(words.words())
# ready the NLTK tokenizer using downloaded using the corpus called 'words'
syllables_split = [LP.tokenize(word) for word in words_split]
# get the individual syllables of this string
# https://www.nltk.org/api/nltk.tokenize.legality_principle.html


def check_for_vowel(character):
    # if character is in list of vowels
    vowel_index = ordinary_vowels.find(character)
    # look for this character in string/list of ordinary vowels
    if vowel_index != -1:
        # if the character
        vowel_occurrences_count[vowel_index] = vowel_occurrences_count[vowel_index] + 1
        # increment that vowel's occurrence counter

    # https://www.merriam-webster.com/grammar/why-y-is-sometimes-a-vowel-usage
    #

    # split into words
    # split into syllables

def check_for_y_vowel(character, index_within_string : int):
    # find which character index this is
    # look at syllable split

    # (i) no other vowel in syllable, (ii) at end of word, (iii) in middle/nucleus of syllable
    # also: if in diphthong?

    # (i) no vowel in syllable - tricky - need to count vowels per syllable
    # (ii) end of word - need to compare this position with end-of-words positions
    # (iii) in middle/nucleus of syllable - maybe check to see if not first or last character of syllable


    # for every word in string (consider a space after every non-last word)
    # for every syllable in word
    words_split
    syllables_split
    # https://stackoverflow.com/a/18449491
    return

# from itertools import chain
# def flatten_syllables(syllable_list):
#     return list(chain.from_iterable(syllable_list))

def print_vowel_counts(count):
    #[print (x.to_string() + ":" + count[x.index()]) for x in count]
    [print(ordinary_vowels[i] + ":" + str(x)) for i, x in enumerate(count)]
    # loop through ordinary vowels (get the index as i am fond of old-fashioned indexing)
    # for each vowel print
    # for every vowel
    # print the vowel followed by its occurrence count


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def main_vowel_count():
    print(strTechCornwall)                          # print the string
    [check_for_vowel(x) for x in re.sub('[!? #@£$.]','',strTechCornwall)]  # check every character to see if vowel
    [check_for_y_vowel(x, i) for i, x in enumerate(re.sub('[!? #@£$.]','',strTechCornwall))]
    print_vowel_counts(vowel_occurrences_count)     # print the results





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main_vowel_count()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
