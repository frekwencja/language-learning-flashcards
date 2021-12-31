import requests
from typing import Dict

DEFAULT_URL = 'https://github.com/frekwencja/most-common-words-multilingual/releases/download/0.1.0/all.json'

"""Return object of english words as key and `language: translation` as value. Check the link to know the schema. Shortcodes are in ISO-639-1 standard."""
def get_multilingual_wordpairs(url: str = DEFAULT_URL) -> Dict[str, Dict[str, str]]:
  return requests.get(url).json()


dataset = get_multilingual_wordpairs()
