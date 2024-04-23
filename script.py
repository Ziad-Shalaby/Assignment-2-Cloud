import os # TO read the file
from collections import Counter # TO count the number of stop words
import nltk # TO filtter the stop words from the file
nltk.download('punkt')

# To take the path of the file 
script_dir = os.path.dirname(os.path.abspath(__file__)) 
file_path = os.path.join(script_dir,"paragraphs.txt")
# To set the language as english 
stop_words = set(nltk.corpus.stopwords.words('english'))

# To read the file and put it in text variable
with open(file_path, 'r') as file:
    text = file.read()

# To delete the stop words from the file
words = nltk.word_tokenize(text)
filttered_words = [word for word in words if word.lower() not in stop_words]
filttered_text = ' '.join(filttered_words)

# To count the frequency of the stop words we deleted
words_counter = Counter(filttered_words)
for word, count in words_counter.items():
    print(f"{word}",{count})