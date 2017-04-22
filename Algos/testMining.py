from textblob import TextBlob

'''
subjective sentences hold sentiments 
while objective sentences are facts and figures

'''

wiki = TextBlob("Python is a high-level, general-purpose programming language.") 
print(wiki.tags)

sentence = TextBlob("Très bonnes ambiance et les plats sont délicieux \nPour ceux qui demandent les prix... pour les plats ça vari entre 1200 et 1300 da")
print(sentence.words) 
print(sentence.tags) #Donesn't work with french
print(sentence.words[2].pluralize()) #Works
print(sentence.correct())
print(sentence.detect_language())

'''
commentProcessing is a function that we use to classify comments.
We first translate the comment (since it's in french) and then tokennize it
We then extract the polarity which is a float within the range [-1.0, 1.0]
-1 is suposed to be super bad.
'''
def commentProcessing(text):
	initBlob = TextBlob(text)
	lang = initBlob.detect_language()
	textBlob = initBlob.translate(from_lang=lang, to='en')

	return textBlob

data = commentProcessing("Très bonnes ambiance et les plats sont délicieux \nPour ceux qui demandent les prix... pour les plats ça vari entre 1200 et 1300 da")
for sentence in data.sentences:
	print(sentence, "\n")
	print(sentence.sentiment)


data = commentProcessing("Un vrai délice n'est-ce pas Sofiane Iddir ??  à refaire nchallah .  Sauf problème de stationnement biensur")
for sentence in data.sentences:
	print(sentence)
	print(sentence.sentiment, "\n")