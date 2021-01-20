import os
# note_path='/Volumes/Kindle/documents/My Clippings.txt'
# f=open(note_path,'r+')

def countWords(txt):
    if txt != None:
        arr = txt.split()
    return len(arr)

def getRowFromNote(f):
    onenote=[]
    for i in range(0,5):
        line=f.readline()
        if not line:
            return
        else:
            onenote.append(line)
    return onenote[3]

# Divide words/phrases and sentences 
def note(f):
    words = []
    sentences = []
    while True: 
        row = getRowFromNote(f)
        if row == None:
            break
        print(row)  # For test
        length = countWords(row)
        if length ==1 | (length>1&length<5):
            words.append(row)
        else :
            sentences.append(row)
    
    
    print("Note Get Success")   # For test
    return words,sentences

# [words,sentences] = note(f)







