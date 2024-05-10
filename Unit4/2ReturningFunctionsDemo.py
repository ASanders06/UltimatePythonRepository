# ========== 4.2.1 ==========
def greatest_number(a, b, c): 
    if a > b: 
        if a > c: 
            return a
    if b > a: 
        if b > c: 
            return b
    if c > a: 
        if c > b: 
            return c
print(greatest_number(2, 3, 4))

# ========== 4.2.2 ==========
def same_chars(sting, one, two):
    uno = sting[one]
    dos = sting[two]
    if uno == dos: 
        return True
    else: 
        return False

print(same_chars("programmer", 6, 1))

# ========== 4.2.3 ==========
sentence = "It was a dark and stormy Python"


def first_word(sentence): 
    if (" " in sentence) == True: 
        last = sentence.find(" ")
        sentence = sentence[0:last]
        return sentence
    
def second_word(sentence):
    
  space = " "
  if (" " in sentence) == True: 
        first = (sentence.find(space))
        sentence2 = sentence[(first+1): ]
        last =  ((sentence2.find(space)) + first)
        sentence = sentence[(first):(last+1)]
        return sentence
def last_word(sentence): 
    while (" " in sentence) == True: 
        last = sentence.find(" ")
        sentence= sentence[(last+1): ]
    return sentence
        

print(first_word(sentence))
print(second_word(sentence))
print(last_word(sentence)) 


