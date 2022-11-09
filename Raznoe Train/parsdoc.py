import re
import xml.dom.minidom as md

def main():
    file = md.parse("document.xml")
    names = file.getElementsByTagName("w:t")
    listdoc = []
    for name in names:
        listdoc.append(name.firstChild.nodeValue)


    allstr = (''.join(listdoc))
    # print(allstr)
    delbreaks = re.sub(r'(?:\(.*?\).)|(?:\[.*?\].)|(?: [IV]{,3} )', '', allstr)
    # (?:\(.*\))|(?:\b[IV]{,4})
    # print(delbreaks)
    regex = re.split(r'(?=\b.?[ABRIMQVLDZPRAJIŠIKMÏČUSÏyUÏQZYHKUN]{2,}\b)',
                     delbreaks.replace('1', '').replace('.', '').replace(
                         '6', 'б').strip())

    for i in regex:
        Match = re.match(r'\b.?[ABRIMVQLDZPRAJIŠIKMÏČUSÏyUÏYHKUN]{2,}.*:',
                       i)
        if Match == None:
            continue
        else:
            print(Match.group(0), '\n')
        # print(i.strip())

if __name__ == "__main__":
    main()


# import json module and xmltodict
# module provided by python
# import json
# import xmltodict
#
# # open the input xml file and read
# # data in form of python dictionary
# # using xmltodict module
# with open("documdict.xml", 'rb') as xml_file:
#     data_dict = xmltodict.parse(xml_file.read())
#     # xml_file.close()
#
#     # generate the object using json.dumps()
#     # corresponding to json data
#
#     json_data = json.dumps(data_dict, indent=4, ensure_ascii=False)
#
#     # Write the json data to output
#     # json file
#     with open("doc_xml_to_json.json", "w", encoding='utf-8') as json_file:
#         json_file.write(json_data)
#         # json_file.close()
