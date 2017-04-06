# Create word dictionary from the comprehensive word list 
word_dict = {}
def create_word_dict ():

  file = open('words.txt','r')

  for line in file:

    word_dict[line] = 1

  file.close()

# Removes punctuation marks from a string
def parseString (st):

  st = st.replace('-',' ')
  s1 = ''
  s2 = ''

  for ch in st:
    if ch.isalpha() or ch.isspace() or ch=="'":
      s1 += ch
    
    else:
      s1 += ' '

  for i in range(len(s1)):

    if (i == (len(s1)-2)) and (s1[i] == "'") and (s1[i+1] == 's'):

      s2 += ' '

    elif (i == (len(s1)-1)) and (s1[i] == "s") and (s1[i-1] == "'"):

      s2 += ' '

    elif (i==0) and (s1[i-1] == "'"):

      s2 += ' '

    else:

      s2 += s1[i]

  return s2.strip()

# Returns a dictionary of words and their frequencies
def getWordFreq (file):

  word_list = []

  for line in file:

    for word in line.split():

    	if len(word)>0:

    		word_list.append(parseString(word))

  freq_dict = {}

  for word in word_list:

    if word in freq_dict:
      freq_dict[word] = freq_dict[word] + 1

    else:
      freq_dict[word] = 1

  return freq_dict

def remove_capitals(dictionary):

  capital_list = []

  for word in dictionary:

    if len(word)> 0 and word[0].isupper():

      capital_list.append(word)

  for word in capital_list:

    if word.lower() in dictionary:

      dictionary[word.lower()] = dictionary[word.lower()] + dictionary[word]

    else:

      if word.lower() in word_dict:

        dictionary[word.lower()] = 1

    del dictionary[word]

  return dictionary


def main():
  # Create word dictionary from comprehensive word list
  create_word_dict()

  # Enter names of the two books in electronic form
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")
  print()


  book1 = open(str(book1),'r')
  book2 = open(str(book2),'r')

  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)

  wordFreq1 = remove_capitals(wordFreq1)
  wordFreq2 = remove_capitals(wordFreq2)

  print(wordFreq2)

  file1.close()
  file2.close()


main()

