# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:55:30 2016

@author: cristian.munoz
"""
from unicodedata import normalize
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import re

tknzr = TweetTokenizer()

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')
    
def Customizado(x):
    return  x[:5]!='https' and \
            x[0]!='@' and \
            x[:3]!='rt' and \
            x!='co'
    
def review_to_words(raw_review , lang):
    
    if lang=="pt":
        #Limpa dados em portugues
        # Remove . , " : () ...
        raw_review1 = re.sub(r'[-./?!,":;()\']',' ',raw_review)
        # Remove números
        letters_only = re.sub('[-|0-9]',' ',raw_review1)
        # Cria a lista de palavras
        words = remover_acentos(letters_only).replace("'","").lower().split()                             
        #  Em Python, procurar um conjunto é muito melhor que por uma lista
        # por isso convertimos os stopwords para conjunto
        stops = set(stopwords.words('portuguese'))  
        # Ap os stopwords
        meaningful_words = [w for w in words if not w in stops]   
        # Passa o último filtro
        return( " ".join(filter(Customizado, meaningful_words) ))
    else:
        instance  = raw_review
        instance = re.sub("[^a-zA-Z]", " ", instance).replace("'","")
        words =  tknzr.tokenize(instance.lower())                       
        # 3. In Python, searching a set is much faster than searching
        #   a list, so convert the stop words to a set
        stops = set(stopwords.words("english"))                  
        # 4. Remove stop words
        meaningful_words = [w for w in words if not w in stops]   
        # 5. Join the words back into one string separated by space, 
        # and return the result.
        return( " ".join( filter(Customizado,meaningful_words)))        