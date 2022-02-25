from itertools import product
#from nltk.corpus import words
from string import ascii_lowercase
# from english_words import english_words_set

def screw_wordle(yellows, greys, greens, all_allowed_content, all_words_content):
  """
  all are strings
  """
  #make all inputs lowercase
  yellows = yellows.lower()
  greys = greys.lower()
  greens = greens.lower()
  #setofwords = set(words.words())

  #y = [''.join(i) for i in product(ascii_lowercase, repeat = 5)]


  letters = list(ascii_lowercase)
  for letter in greys:
    if letter in letters:
      letters.remove(letter)
  final_string = ''.join(letters)
  y = [''.join(i) for i in product(final_string, repeat = 5)]


  # helper function that checks if a 5 letter word fits the [greens] mask
  def mask(word, greens):
    for i in range(0, 5):
      if greens[i] != '*' and greens[i] != word[i]:
        return False
    return True

  #filter
  def custom_filter(word):
    # for letter in greys:
    #   if letter in word:
    #     return False    
    for letter in yellows:
      if letter not in word:
        return False    
    if mask(word, greens) == False:
      return False
    # if (word in all_allowed_content) or (word in all_words_content) :
    #   return True
    if word in all_words_content:
      return True 
    else:
      return False
    


  #filter
  filtered = filter(custom_filter, y)
  ans = []
  for s in filtered:
    ans.append(s)
  return ans
