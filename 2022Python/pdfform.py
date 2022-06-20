from PyPDF2 import PdfFileReader
import json
import os

directory = os.fsencode('/mnt/c/Users/ELCOT/Documents/PythonWork/2022Python')
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".pdf"): 
        # print(filename)

        pdf_reader = PdfFileReader(open(filename, "rb"))

        dictionary = pdf_reader.getFormTextFields() 
        json_data=json.dumps(dictionary) 
        # print(json_data, filename)
        outfile = filename.split('.pdf')
        with open(outfile[0] + '.json', "w") as outfile:
            outfile.write(json_data)
        if  not json_data:
            print(filename)
    
    