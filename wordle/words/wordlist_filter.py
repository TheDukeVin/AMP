'''wordlist_filter.py
'''
import json

def getWordsArray(filename, maxLength):
    words = []

    f = open(filename, 'r')
    for line in f:
      word = line.strip().lower()
      if(len(word)>1 and len(word)<=maxLength and "'" not in word):
          words.append(word.upper())

    return words

def saveWords(filename, words):
    json_object = json.dumps(words, indent=4)

    with open(filename, "w") as outfile:
        outfile.write("def getWordList():\n\treturn "+json_object)

if __name__ == "__main__":
    words = getWordsArray("wordle_words.txt", 5)
    saveWords("wordle_wordlist.py", words)
