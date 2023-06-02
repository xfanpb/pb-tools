import re

import docx

def countWordWord(filename):
    doc = docx.Document(filename)
    newparatextlist = []
    for paratext in doc.paragraphs:
        newparatextlist.append(paratext.text)
    totalWords = len(re.findall(r'\w+', '\n'.join(newparatextlist)))
    print(totalWords, "words for file", filename)
    return totalWords

