import requests
from typing import Dict
import genanki

__version__ = '0.1.0'
__dataset__ = 'Most Common Words'

MAX_WORDS = 1000
DEFAULT_URL = 'https://github.com/frekwencja/most-common-words-multilingual/releases/download/0.1.0/all.json'
MODEL = genanki.Model(
  2000000000,
  'Frekwencja Basic Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
    {'name': 'Pronunciation'}
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}} {{Pronunciation}}',
      'afmt': '{{Answer}}',
    },
  ])

"""Return object of english words as key and `language: translation` as value. Check the link to know the schema. Shortcodes are in ISO-639-1 standard."""
def get_multilingual_wordpairs(url: str = DEFAULT_URL) -> Dict[str, Dict[str, str]]:
  return requests.get(url).json()


wordpairs = get_multilingual_wordpairs('http://localhost:2137/all.json')