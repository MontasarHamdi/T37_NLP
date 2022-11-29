import spacy  # Import spacy
nlp = spacy.load('en_core_web_sm')

# Create 5 sentences. Lord of the rings quotes.
sentence_1 = nlp("A wizard is never late, Frodo Baggins. Nor is he early. He arrives precisely when he means to.")
sentence_2 = nlp("He that breaks a thing to find out what it is, has left the path of wisdom.")
sentence_3 = nlp("You shall not pass!")
sentence_4 = nlp("One does not simply walk into Mordor.")
sentence_5 = nlp('''one ring to rule them all, one ring to find them, One ring to bring them all, 
                 and in the darkness bind them; In the Land of Mordor where the shadows lie.''')
# Add sentences to list
garden_path_sentences = [sentence_1, sentence_2, sentence_3, sentence_4, sentence_5]

for sentence in garden_path_sentences:  # for loop iterating through list of sentences
    for i in nlp(sentence).ents:  # tokenizing the sentences
        print("Text : {}, Entity : {}".format(i.text, i.label_))  # print the text and their respective entities

# ====== OUTPUT ====== #
# Write comment about two unusual entities. Answer below.
# The two unusual entities are GPE and ORG.
print("\n\tExplaining Unusual Entities!")
print("Entity GPE 'Mordor': ", spacy.explain("GPE"))
print("Entity ORG 'the land of mordor': ", spacy.explain("ORG"))
# Use print statements for spacy.explain to understanding definition of entities.
# Learned about spacy.explain() function here >>> https://spacy.io/api/top-level
# GPE stands for countries, cities or states and in the fictional world of LOTR, Mordor could fit into that category.
# ORG stands for companies, agencies or institutions. 'the land of mordor' falls under this category.
# I did not expect this.
##########
# Regarding dockerfile - Dockerfile was not mentioned PDF lecture documents. I tried to research it but
# I don't understand it. Apologies if I am wrong but this was not taught.
