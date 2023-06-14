import os

import PyPDF2
import textract, re

def countPDFWord(pdfFile):
    try:
        if os.path.exists(pdfFile):
            print("file found:", pdfFile)
    except OSError as err:
        print(err.reason)
        exit(1)

    totalWords = 0
    pdfFileObj = open(pdfFile, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    pages = pdfReader.pages
    for page in pages:
        data = page.extract_text()
        totalWords += len(data.split())
    print(totalWords, "words for file", pdfFile)
    return totalWords


