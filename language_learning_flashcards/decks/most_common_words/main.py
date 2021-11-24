import pandas as pd
import pprint

DOWNLOAD_URL = 'https://www.wordfrequency.info/samples/wordFrequency.xlsx'
SELECTED_SHEET_NAME = '1 lemmas'
SELECTED_COLUMNS = ['lemma', 'PoS']
LIMIT = 1000

df = pd.read_excel(DOWNLOAD_URL, SELECTED_SHEET_NAME)

df = df[SELECTED_COLUMNS].head(LIMIT)

words = []

for index, row in df.iterrows():
  word, part_of_speech = row

  words.append({ 'key': word })

pprint.pprint(words)

