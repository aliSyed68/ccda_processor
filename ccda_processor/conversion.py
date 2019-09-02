import xmltodict
import re, gzip


class CCDA():

    def __init__(self, pathToInputArtifact, outputDirectory):
        self.pathToInputArtifact = pathToInputArtifact
        self.outputDirectory = outputDirectory

    def convert(self):
        with gzip.open(self.pathToInputArtifact, 'rt') as f:
            count = 0
            input = f.read()
            low = input.find('<?xml')
            # print(low)
            high = input.rfind('</ClinicalDocument>')
            # print("high : {}".format(high))
            relevantString = input[low:high + 19]
            res = re.sub(r'(?<=</ClinicalDocument>).*?(?=<\?xml)', '', relevantString)

            listofxml = re.findall(r'(?<=type="text/xsl"\?>).*?(?=<\?xml)', res)

            for x in listofxml:
                out = xmltodict.parse(x)
                fam = str(out['ClinicalDocument']['recordTarget']['patientRole']['patient']['name']['family'])
                other = out['ClinicalDocument']['recordTarget']['patientRole']['patient']['name']['given']
                if type(other) == list:
                    first = ""
                    for i in other:
                        first += " " + i
                else:
                    first = other
                    assert type(first) == str
                if fam is not None and first is not None:
                    name = fam + ' ' + first
                elif fam is not None:
                    name = fam
                elif first is not None:
                    name = first
                else:
                    name = 'unlabelled'
                html = """<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>""" \
                       + name + """"</title>\n</head>\n<body>""" \
                       + x + """</body>\n</html>"""

                with open('{}/{}.html'.format(self.outputDirectory, name), 'w+') as h:
                    h.write(html)
                count += 1
                print("document number: {}".format(count + 1))
                print("other names: {}".format(other))
                print("first name: {}".format(first))
            print("total count of patient records: {}".format(count))


def main():
    convertor = CCDA('../resources/ecwimage', '../medical_records')
    convertor.convert()


if __name__ == "__main__":
    main()
