#purpose: to find and collect all entities that commenter could be attacking

from __future__ import unicode_literals
from spacy.matcher import PhraseMatcher
from spacy.lang.en import English
import spacy

# model of english
nlp = spacy.load('en')

# sample documents
#example of ad homien
doc = nlp("Tony wants us to believe that the origin of life was an “accident”.  Tony is a godless SOB who has spent more time in jail than in church, so the only information we should consider from him is the best way to make license plates.")
# txt file
doc2 = nlp(open("nlp_ex.txt").read().decode('utf8'))


# returns all entities in a doc
def getEnities(d):
    entities = []
    # iterates through every entity in doc
    for item in d.ents:
            listofnouns.append(item)
    return entities

# returns all instances of a specific word or phrase
# params: doc, phrase that exists in doc
def getRepeats(d, phrase):
    repeats = []
    for item in d:
        if (item == phrase):
            repeats.append(item)
    return repeats

# matches all last name, with a person
# example: Donald, Trump and Trump refers to the same individual
def matchNames(d, firstName, lastName):
    fullName = firstName + " " + lastName
    matcher = Matcher(nlp.vocab)
    matcher.add(lastName, None, nlp(firstName))
    matcher.add(lastName, None, nlp(lastName))
    matcher.add(lastName, None, nlp(fullName))
    return matcher(d)
