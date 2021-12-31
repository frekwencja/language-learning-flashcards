import subprocess

from main import get_multilingual_wordpairs

WORDS_COUNT = 1000
LANGUAGES = ['pl', 'de', 'en']

"""Batch download audio files with word pronunciation, using Forvo."""
def batch_download_audios(language):
  wordpairs = get_multilingual_wordpairs()

  for i, word in enumerate(wordpairs):
    # In .json english word is a key instead of value, that's why we have to check it.
    if language == 'en':
      download_audio(word, language)
    else:
      translated_word = wordpairs[word][language]
      download_audio(translated_word, language)

    if i >= WORDS_COUNT:
      break


def download_audio(word, language):
  subprocess.call(['sh', './forvo_scraper.sh', word, language])


for lang in LANGUAGES:
  batch_download_audios(lang)
