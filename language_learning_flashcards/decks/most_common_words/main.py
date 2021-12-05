import pandas as pd
from pprint import pprint
import deep_translator
import time

# DOWNLOAD_URL = 'https://www.wordfrequency.info/samples/wordFrequency.xlsx'
DOWNLOAD_URL = 'http://localhost:2137/wordFrequency.xlsx'
SELECTED_SHEET_NAME = '1 lemmas'
SELECTED_COLUMNS = ['lemma', 'PoS']
LIMIT = 1000

def get_words():
  df = pd.read_excel(DOWNLOAD_URL, SELECTED_SHEET_NAME)
  df = df.head(LIMIT)

  # Some words are recognized as bool, so we should convert them to string.
  return [str(row.lemma) for row in df.itertuples()]

def get_joined_words(words) -> str:
  # When separated by endline, translator seems to treat it as a separate word.
  return '\n '.join(words)

def translate_words(lang: str, words: list):
  # en_list -> en_lists -> en_list[string] -> translated_list[string] -> translated_lists -> translate_list
  # We want to translate words in bulk to not be rate limited. We will join the list into two halfs, because Google Translate limits to 5000 characters.
  words_lists = [words[:500], words[500:1000]]
  words_strings = [get_joined_words(list) for list in words_lists]

  translated_strings = deep_translator.GoogleTranslator(source='en', target=lang).translate_batch(words_strings)
  translated_lists = translated_strings[0].split('\n')

  return translated_lists


words = get_words()
translated_words = translate_words('pl', words)

# for translated_word, word in zip(translated_words, words):
#   print(translated_word, word)