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
strTechCornwall = "Tech Cornwall Career Pathways"

'''
Natural Language ToolKit corpus d'require a download
'''



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

    try:
        nltk.download('punkt')
        vowel_counter.SSP = SyllableTokenizer()
        vowel_counter.split = vowel_counter.SSP.tokenize(strTechCornwall)
    except:
        print("Could not download punkt")
        vowel_counter.nltk_ok = False
        # punkt not yet actually needed in this code
        # (alternative syllable splitting method)



    try:
        nltk.download('words')  # try downloading corpus
        # might crash if 'words' not downloaded
        vowel_counter.words_split = nltk.word_tokenize(strTechCornwall, language='english')
        # get the individual words
        vowel_counter.LP = LegalitySyllableTokenizer(words.words())
        # ready the NLTK tokenizer using downloaded using the corpus called 'words'
        syllables_split = [vowel_counter.LP.tokenize(word) for word in vowel_counter.words_split]
        # get the individual syllables of this string
        # https://www.nltk.org/api/nltk.tokenize.legality_principle.html
    except:
        print("Could not download NLTK 'words'")
        vowel_counter.nltk_ok = False

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
