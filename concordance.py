import nltk
from nltk.tokenize import RegexpTokenizer
from sys import argv

file_output = open("answer.txt","w")

# run script and file name
script, filename = argv

# regex pattern to pass to the rexeg tokenizer to strip punctuation
pattern = r'''(?x)          # flag to allowing verbose regexps
        (?:[A-Z]\.)+        # uppercase abbreviations,
      | (?:[a-z]\.)+        # abbreviations, e.g.
      | \w+(?:-\w+)*        # words with optional internal hyphens
      | \$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
      | r'\w+'              # match words
    '''

# strips away punctuation
tokenizer = RegexpTokenizer(pattern)

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


# write output to the output file
for key, val in sorted(line_counts.iteritems()):
    s=" "
    if int(counts[key]) > 1:
        s = "s "
    file_output.write('"%s" occured %s time%son line%s%s \n' % (key, counts[key], s, s,list(val)))
file_output.close()
