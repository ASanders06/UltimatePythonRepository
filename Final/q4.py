word_list = []
pts = 0
def scrabble_score(word): #unfinished, sorry.
    if "a" or "e" or "i" or "u" or "l" or "n" or "s" or "t" or "r" in word == True: 
        pts += 1
        term = word.find("a")
        split1 = word[0:term]
        split2 = word[term:]
        print(split1, split2)
scrabble_score("hat")
