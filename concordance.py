import nltk
from nltk.tokenize import RegexpTokenizer
from sys import argv

# run script and file name
script, filename = argv

# strips away punctuation
tokenizer = RegexpTokenizer(r'\w+')

# open the given file
with open(filename) as f:
    read_data = f.read()
read_data = read_data.replace('\n', ' ')

# tokenize the paragraph and save it in a list of sentences
full_txt = nltk.sent_tokenize(read_data)

# list of all the lines split by sentence
lines = [tokenizer.tokenize(line) for line in full_txt]

# set a dictionary to return
counts = {}
line_counts = {}

# current line number and word count
line_num = 0
word_count = 0

# set the dictionary up with the current word count of the words
for line in lines:
    for word in line:
        word = word.lower()
        counts[word] = counts.get(word, word_count) + 1
        line_counts.setdefault(word, set()).add(line_num)
    line_num += 1

# reset the current counts dictionary to include line_counts
for key, val in sorted(line_counts.iteritems()):
    counts[key] = (counts.get(key), list(val))
    print "%s: %s" % (key, counts[key])