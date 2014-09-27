import xml.etree.ElementTree as ET

class Note:
    def __init__(self, xmlTree):
        self.note = {}
        self.note['tags'] = []
        root = xmlTree.getroot()
        for child in root:
            if child.tag == "tag":
                self.note['tags'].append(child.text)
            else:
                self.note[child.tag] = child.text

    def printNote(self):
        print "GUID:", self.note['guid']
        print "Created at:", self.note['created']
        if len(self.note['tags']) > 0:
            print "Tags:",
            for tag in self.note['tags']:
                print tag+',',
            print
        print "Content:"
        print self.note['content']


def main():
    if raw_input() == "CREATE":
        tree = ET.parse('note0.xml')
        note = Note(tree)
        note.printNote()


while __name__ == "__main__":
    main()
