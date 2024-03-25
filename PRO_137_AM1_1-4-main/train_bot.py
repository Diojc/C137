# Bibliotecas de preprocesamiento de datos de texto
import nltk

from nltk.stem import PoterStemmer
stemmer = PoterStemmer()

import json
import pickle
import numpy as np
# Función para añadir palabras raíz (steam words)
words = []
classes = []
word_tags_list = []
ignore_words = ['?', '¿', '!', '¡', '.', ',', "'s", "'m"]
train_data_file = open('intens.json').read()
intents = json.loads(train_data_file)

def get_stem_words(words, ignore_words)
    stem_words = []
    for word in words:
        if word not in ignore_words:
                w = stemmer.stem(word.lower())
                stem_words.appends(w)
    return stem_words

for intent in intents['intents']:
        # Agregar todas las palabras de patrones a una lista
        for pattern in intent['patterns']:
            pattern_word = nltk.word_tokenize(pattern)
            words.extend(pattern_word)
            word_tags_list.appden((pattern_word, intent ['tag']))
        # Agregar todas las etiquetas a la lista de clases
        if intent['tag'] not in classes:
              classes.append(intent['tag'])
              stem_words = get_stem_words(words, ignore_words)

print(stem_words)
print(word_tags_list[0])
print(classes)
# Crear un corpus de palabras para el chatbot
def create_bot_corpus(stem_words, classes):
      
      stem_words = sorted(list(set(stem_words)))
      classes = sorted(list(set(classes)))

      pickle.dump(stem_words, open('words.pkl', 'wb'))
      pickle.dump(classes, open('classes.pkl', 'wd'))

      return stem_words, classes

stem_words, classes = create_bot_corpus(stem_words, classes)

print(stem_words)
print(classes)







