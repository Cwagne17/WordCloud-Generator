#                                   Word Cloud
#   
#   This script recieves a text input of any length, strips it of the punctuation, 
# and transforms the words into a random word cloud based on the frequency of the word 
# count in the text.
#
#   To try it - on ln20 change the .txt file to the path which youd like to use. ENJOY!


import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


#open the .txt file you want to make a word cloud for then run
text_file = open("pg63281.txt", "r")
file_contents = text_file.read()

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    word_count = {}
    text_file = ""

    #Removes punctuation
    for char in file_contents:
        if char.isalpha():
            text_file+=char
        else:
            text_file+=" "
                
    text_set = text_file.split()
    
    #Frequency Ctr
    for word in text_set:
        if not word.lower() in uninteresting_words:
            if word in word_count:
                word_count[word.lower()]+=1
            else:
                word_count[word.lower()]=1

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_count)
    return cloud.to_array()

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()