# Enter your code here. Read input from STDIN. Print output to STDOUT
import xml.dom.minidom

searchableNotes = []

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

def main():
    if raw_input() == "CREATE":
        line = ''
        xmlDom = ''
        while line != "</note>":
            line = raw_input()
            xmlDom += line
        dom = xml.dom.minidom.parseString(xmlDom)
        note = Note(dom)
        note.printNote()


#while __name__ == "__main__":
main()
