import fitz

doc = fitz.open('FromEx.pdf')

for page in doc:
    for field in page.widgets():
        print(field)