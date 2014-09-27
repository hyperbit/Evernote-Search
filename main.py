# Enter your code here. Read input from STDIN. Print output to STDOUT
import xml.dom.minidom

searchableNotes = {}

class Note:
    def __init__(self, xmlDom):
        self.note = {}
        self.note['guid'] = self.getData(xmlDom.getElementsByTagName('guid')[0].childNodes)
        self.note['created'] = self.getData(xmlDom.getElementsByTagName('created')[0].childNodes)
        self.note['tags'] = self.getData(xmlDom.getElementsByTagName('tag')[0].childNodes, True)
        self.note['content'] = self.getData(xmlDom.getElementsByTagName('content')[0].childNodes)

    def getData(self, nodelist, tags=False):
        rc = []
        for node in nodelist:
            #if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
        if tags:
            return rc
        return ''.join(rc)
        

    def printNote(self):
        for key in self.note.keys():
            print key, self.note[key]


def createXML():
    line = ''
    xmlDom = ''
    while line != "</note>":
        line = raw_input()
        xmlDom += line
    return xml.dom.minidom.parseString(xmlDom)

def create():
    dom = createXML()
    note = Note(dom)
    searchableNotes[note.note['guid']] = note
    note.printNote()

def update():
    dom = createXML()
    note = Note(dom)
    if note.note['guid'] not in searchableNotes:
        print "Note not found"
        return -1
    else:
        searchableNotes[note.note['guid']] = note



def main():
    while True:
        try:
            line = raw_input()
            if line == "CREATE":
                create()
            elif line == "UPDATE":
                update()
        except(EOFError):
            return

if __name__ == "__main__":
    main()
