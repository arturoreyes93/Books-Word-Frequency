#  File: Books.py

#  Description: compares the frequency of words in two books

#  Student Name: Arturo Reyes Munoz

#  Student UT EID: ar48836

#  Partner Name: no partner

#  Partner UT EID: n/a

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 04/28

#  Date Last Modified: 04/28

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

def total(dictionary):

  total_words = 0

  for freq in dictionary:

    total_words += dictionary[freq]

  return total_words
# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):

  set1 = set(freq1)
  set2 = set(freq2)

  diff1 = set1 - set2
  diff2 = set2 - set1

  len1 = len(diff1)
  len2 = len(diff2)

  ratio_freq1 = 0
  ratio_freq2 = 0

  for word in diff1:

    ratio_freq1 += freq1[word]

  for word in diff2:

    ratio_freq2 += freq2[word]

  total_1 = total(freq1)
  total_2 = total(freq2)

  print(str(author1))
  print('Total distinct words = '+str(len(freq1)))
  print("Total words (including duplicates) = "+str(total_1))
  print('Ratio (% of total distinct words to total words) = '+str((len(freq1)/total_1)*100))
  print()

  print(str(author2))
  print('Total distinct words = '+str(len(freq2)))
  print("Total words (including duplicates) = "+str(total_2))
  print('Ratio (% of total distinct words to total words) = '+str((len(freq2)/total_2)*100))
  print()

  print(str(author1)+' used '+str(len1)+' that '+str(author2)+' did not use.')
  print('Relative frequency of words used by '+str(author1)+' not in common with '+str(author2)+' = '+str((ratio_freq1/total_1)*100))
  print()

  print(str(author2)+' used '+str(len2)+' that '+str(author1)+' did not use.')
  print('Relative frequency of words used by '+str(author2)+' not in common with '+str(author1)+' = '+str((ratio_freq2/total_2)*100))

def main():
  # Create word dictionary from comprehensive word list
  create_word_dict()

  # Enter names of the two books in electronic form
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")
  print()

  # Enter names of the two authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  print() 

  book1 = open(str(book1),'r')
  book2 = open(str(book2),'r')

  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)

  wordFreq1 = remove_capitals(wordFreq1)
  wordFreq2 = remove_capitals(wordFreq2)

  book1.close()
  book2.close()
  # Compare the relative frequency of uncommon words used
  # by the two authors
  wordComparison (author1, wordFreq1, author2, wordFreq2)

main()
