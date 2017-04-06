
# remove punctuation marks and digits from a string
def filter_string (st):
  s = ''
  for ch in st:
    if (ch >= 'a') and (ch <= 'z'):
      s += ch
    else:
      s += ' '
  return s

def main():
  # open the book
  book = open ("hard_times.txt", "r")

  # create an empty set for unique words
  word_set = set()

  # create a dictionary for the word frequency
  word_dict = {}

  # track the total number of words
  total_words = 0

  # read the book
  for line in book:
    line = line.strip()
    line = line.lower()
    line = filter_string (line)

    word_list = line.split()

    # add words to the set and to the dictionary
    for word in word_list:
      word_set.add (word)
      total_words += 1

      # add word to the frequency dictionary
      if word in word_dict:
        word_dict [word] = word_dict[word] + 1
      else:
        word_dict[word] = 1

  # close the file
  book.close()

  print ('Total words used = ', total_words)

  num_unique_words = len (word_set)
  word_ratio = num_unique_words / total_words

  print ('Number of unique words = ', num_unique_words)
  print ('Word ratio = ', word_ratio)

  # print the word frequency
  all_words = list (word_dict.keys())
  all_words.sort()
  for word in all_words:
    print (word + " : " + str(word_dict[word]))

  # get distribution according to frequency
  freq_dict = {}

  for word in word_dict:
    freq = word_dict[word]
    if freq in freq_dict:
      (freq_dict[freq]).append (word)
    else:
      new_list = []
      new_list.append (word)
      freq_dict[freq] = new_list

  # print according to frequency
  all_freq = list (freq_dict.keys())
  all_freq.sort()
  all_freq.reverse()

  for freq in all_freq:
    print (str(freq) + " : " + str (freq_dict[freq]))


main()