from medcat.cat import CAT
from medcat.utils.vocab import Vocab
from medcat.cdb import CDB 
import pandas as pd
import medcat
import numpy as np

# Create and load the CDB (Concept Database)
cdb = CDB()
cdb.load_dict(u"cdb-medmen.dat")

# Create and load the Vocabulary
vocab = Vocab()
vocab.load_dict(u"vocab.dat")

# Create CAT - the main class from medcat used for concept annotation
cat = CAT(cdb=cdb, vocab=vocab)

# Set a couple of parameters, they are usually set via environments, but
#here we will do it explicitly. You can read more about each option in the 
#medcat repository: https://github.com/CogStack/MedCAT
cat.spacy_cat.PREFER_FREQUENT = True
cat.spacy_cat.PREFER_ICD10 = False
cat.spacy_cat.WEIGHTED_AVG = True
cat.spacy_cat.MIN_CONCEPT_LENGTH = 3 # Ignore concepts (diseases) <= 3 characters
cat.spacy_cat.MIN_ACC = 0.2 # Confidence cut-off, everything bellow will not be displayed 

# Read the dataset
datasetInPandasDatFrame = pd.read_csv("Logistic_Notes.csv")

datasetInPandasDatFrame['Entities'] = np.nan

# Access Logistic notes
dfWithNotes = datasetInPandasDatFrame["Notes/Questions"].fillna('u')

listOfNotes = dfWithNotes.tolist()
print(listOfNotes)

# Generate medical entities
count = 0
for note in listOfNotes:
  text = note
  doc = cat(text)
  datasetInPandasDatFrame.iloc[count,15]= str(doc.ents)
  count += 1

print(datasetInPandasDatFrame)

# Save the entities in a csv file
datasetInPandasDatFrame.to_csv('Logistic_Notes_Entities.csv')
