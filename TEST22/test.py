from lxml import etree
import csv

root = etree.Element('data')
reader = csv.reader(open('cell.csv', 'r'))
header = next(reader)
test = ""
for row in reader:

    for i in row:
        test = i.replace("|",",")

        eg = etree.SubElement(root, "eg")
        for h,v in zip(header, test):
            etree.SubElement(eg, h).text = v


    f = open(r"cell.xml","wb")
    f.write(etree.tostring(root))
    f.close