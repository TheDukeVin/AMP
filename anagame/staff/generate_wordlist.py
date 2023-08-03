'''generate_wordlist.py
'''
import json
import os

def getWordsArray(filename, maxLength):
    words = []

    f = open(filename, 'r')
    for line in f:
      word = line.strip().lower()
      if(len(word)>1 and len(word)<=maxLength and "'" not in word):
          words.append(word)

    return words

def saveWords(filename, words):
    json_object = json.dumps(words, indent=4)

    with open(filename, "w") as outfile:
        outfile.write("def get_valid_word_list():\n\treturn "+json_object)

def saveAnagramDict(filename, anagrams):
    json_object = json.dumps(anagrams, indent=4)

    with open(filename, "w") as outfile:
        outfile.write("def getAnagramPrimeHashDict():\n\treturn "+json_object)

if __name__ == "__main__":
    file_path = os.getcwd()+"\\anagame\\staff\\wordlist.txt"
    words = getWordsArray(file_path, 7)
    saveWords(os.getcwd()+"\\anagame\\staff\\valid_word_list.py", words)

    '''
    anagramDict = anagramPrimeHashDict(getWordList())
    saveAnagramDict("anagramDictHelper.py", anagramDict)
    '''
