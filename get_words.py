def get_words(sentence):
    words=[]
    sow_index=0
    for i in range (0,len(sentence)):
        if (sentence[i]==' ' or sentence[i]=='.' or sentence[i]==','):
            words.append(sentence[sow_index:i])
            sow_index=i+1
        if (sentence[i]=='\n'):
            words.append(sentence[sow_index:i])
            words.append('\n')
            sow_index=i+1
        if (i==len(sentence)-1):
            words.append(sentence[sow_index:i+1])
            sow_index=i+1
    return words

def reverse(words):
    reversed_sentence=''
    for i in range (len(words)-1,0,-1):
        reversed_sentence+=words[i]+' '
    reversed_sentence+=words[0]+'.'
    return reversed_sentence

def remove_sc(words):
    scs=['.','!','?',',']
    for word in words:
        for sc in scs:
            if word==sc:
                words.remove(word)
    return words
