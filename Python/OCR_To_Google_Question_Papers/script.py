from PIL import Image
import pytesseract
import nltk.data
import re
from newspaper import Article
from googlesearch import search


def google_search(query):    # function to google querys
    return list(search(query, tld='com',num= 1, start= 1, stop= 1))

def scrape(url):            # function to web scrape
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    text = article.text

    return text

img = Image.open("test-imgs/test-1.png")    # provide path of your image that you want to give as input.

text = pytesseract.image_to_string(img, lang="eng")   # image converted to string


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

#print('\n-----\n'.join(tokenizer.tokenize(text)))
tokenized_text = '\n \n'.join(tokenizer.tokenize(text))   # text seperated into sentences.
print(tokenized_text)

print('\nDoes the text is recognized correctly ? \n')
print('\nIf the text is not recognized correctly try using a better quality image. \n')
print('\nDo you want to proceed with this text?(y\\n) \n')

sentences = tokenized_text.split('\n \n')
questions = []
if input()=='y':
    # for loop to seperate questions
    for sentence in sentences:
        if (
            sentence.endswith('?')
            or sentence.startswith("What")
            or sentence.startswith("When")
            or sentence.startswith("How")
            or sentence.startswith("Why")
            or sentence.startswith("Describe")
            or sentence.startswith("Explain")
        ):
            questions.append(sentence)
            print(sentence)

else:
    # for loop to seperate questions
    for sentence_ in sentences:
        if (
            sentence_.endswith('?')
            or sentence_.startswith("What")
            or sentence_.startswith("When")
            or sentence_.startswith("How")
            or sentence_.startswith("Why")
            or sentence_.startswith("Describe")
            or sentence_.startswith("Explain")
        ):
            questions.append(sentence_)
            print(sentence_)

print('\nDo you want to proceed with these recognized questions?(y\\n) \n')
search_querys = []
solutions = {}
if input()=='y':
    print('\nPlease wait while your questions are being searched! \n')
else:
    print('\nPlease wait while your questions are being searched! \n')
        # for loop to get URLs of answers
for question in questions:
    query = question
    output = google_search(query)
    search_querys.append(output)

# for loop to scrape answers from URLs
for i in range(len(search_querys)):
    keys = questions[i]
    try:
        answers = scrape(search_querys[i][0])
    except Exception as e:
        values = e
    values = answers
    solutions[keys] = values

# for loopp to display
for x,y in solutions.items():
    print('\n******************\n')
    print(x)
    print('\n answer = \n')
    print(y)
    print('\n******************\n')

print('\nAll questions have been answered! \n')

print('\nDo you want the URLs of the answers?(y\\n)\n')
if (input()=='y' or 'Y'):
            # for loop to display URLs
    for search_query in search_querys:
        print(search_query[0])

print('Thank You!')
        
    

   