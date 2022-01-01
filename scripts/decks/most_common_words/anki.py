import genanki

import main
import utils

"""Return static id for a deck. It gives ability to update deck in Anki.
All below doesn't really matter, it just makes decks updatable.

It take languages indexes, zerofill them to 3 (so they have same amount of characters).
Every id has to have 10 characters, so it's zerofill it again. If word_index is added, it means that the id is for note.
Every id starts with 1 to prevent trimming zeros.
- 1 de (32) pl (128) -> 1 032 128 000
- 1 de (32) pl (128) das, ten (1) -> 1 032 128 001
"""
def get_specific_id(questions_language: str, answers_language: str, word_index: int = 0):
  GREATEST_SHORTCODE_INDEX_LENGTH = 3
  REQUIRED_DECK_ID_LENGTH = 10
  FILL_WITH = '0'

  question_language_id = str(utils.LANGUAGES_SHORTCODES.index(questions_language)).zfill(GREATEST_SHORTCODE_INDEX_LENGTH)
  answers_language_id = str(utils.LANGUAGES_SHORTCODES.index(answers_language)).zfill(GREATEST_SHORTCODE_INDEX_LENGTH)
  word_index = str(word_index).zfill(GREATEST_SHORTCODE_INDEX_LENGTH)

  return int((f'1{question_language_id}{answers_language_id}{word_index}').ljust(REQUIRED_DECK_ID_LENGTH, FILL_WITH))


def get_package_name(question_language, answers_language):
  return f'frekwencja: {main.__dataset__} v{main.__version__} {question_language} - {answers_language}.apkg'


def get_audio_path(language: str, word: str):
  return f'data/pronunciation/{language}/frekwencja_{language}_{word}.mp3'


def get_deck(question_language, answer_language):
  deck = genanki.Deck(get_specific_id(question_language, answer_language), get_package_name(question_language, answer_language))
  media_files = []

  for i, word in enumerate(main.wordpairs):
    question = main.wordpairs[word][question_language]
    answer = main.wordpairs[word][answer_language]

    path = get_audio_path(answer_language, answer)

    filename = path.split('/')[-1]
    media_files.append(path)

    note = genanki.Note(main.MODEL, fields=[question, answer, f'[sound:{filename}]'])

    deck.add_note(note)

    if i + 1 == main.MAX_WORDS:
      break

  print(media_files)
  return genanki.Package(deck, media_files)


get_deck('pl', 'de').write_to_file(get_package_name('pl', 'de'))
