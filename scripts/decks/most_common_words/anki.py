import utils

from main import __version__, __dataset__

"""Return static id for a deck. It gives ability to update deck in Anki.
All below doesn't really matter, it just makes decks updatable.

It take languages indexes, zerofill them to 3 (so they have same amount of characters).
Every id has to have 10 characters, so it's zerofill it again. If word_index is added, it means that the id is for note.
Every id starts with 1 to prevent trimming zeros.
- 1 de (32) pl (128) -> 1 032 128 000
- 1 de (32) pl (128) das, ten (1) -> 1 032 128 001
"""
def get_specific_id(questions_language, answers_language, word_index = 0):
  GREATEST_SHORTCODE_INDEX_LENGTH = 3
  REQUIRED_DECK_ID_LENGTH = 10
  FILL_WITH = '0'

  question_language_id = str(utils.LANGUAGES_SHORTCODES.index(questions_language)).zfill(GREATEST_SHORTCODE_INDEX_LENGTH)
  answers_language_id = str(utils.LANGUAGES_SHORTCODES.index(answers_language)).zfill(GREATEST_SHORTCODE_INDEX_LENGTH)
  word_index = str(word_index).zfill(GREATEST_SHORTCODE_INDEX_LENGTH)

  return int((f'1{question_language_id}{answers_language_id}{word_index}').ljust(REQUIRED_DECK_ID_LENGTH, FILL_WITH))


def get_package_name(question_language, answers_language):
  return f'frekwencja: {__dataset__} v{__version__} {question_language} - {answers_language}'
