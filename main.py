# Enter your code here. Read input from STDIN. Print output to STDOUT
import xml.dom.minidom
import datetime
import re

searchableNotes = []

class Note:
    def __init__(self, xmlDom):
        self.guid = self.getData(xmlDom.getElementsByTagName('guid')[0].childNodes)
        created = self.getData(xmlDom.getElementsByTagName('created')[0].childNodes)
        self.created = datetime.datetime.strptime(created, '%Y-%m-%dT%H:%M:%SZ')
        self.tags = self.getData(xmlDom.getElementsByTagName('tag')[0].childNodes, True)
        self.content = self.getData(xmlDom.getElementsByTagName('content')[0].childNodes)

    def getData(self, nodelist, tags=False):
        rc = []
        for node in nodelist:
            #if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
        if tags:
            return rc
        return ''.join(rc)
        

    def printNote(self):
        print "guid:", self.guid
        print "created at:", self.created
        if len(self.tags) > 0:
            print "tags:",
            for tag in self.tags:
                print tag,
            print
        print "content:"
        print self.content
        print


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
    searchableNotes.append(note)
    #note.printNote()
    #print

def update():
    dom = createXML()
    note = Note(dom)
    #if note.note['guid'] not in searchableNotes:
    #    print "Note not found"
    #    return -1
    #else:
    #    searchableNotes[note.note['guid']] = note

def delete(key):
    del searchableNotes[key]

def search(query):
    queries = query.split(' ')
    results = []
    for q in queries:
        for note in searchableNotes:
            #parseQuery(q)
            if re.search(q, note.content, re.IGNORECASE):
                results.append(note.guid)
    return results

def parseQuery(query):
    return None

def main():
    while True:
        try:
            line = raw_input()
            if line == "CREATE":
                create()
            elif line == "UPDATE":
                update()
            elif line == "DELETE":
                key = raw_input()
                delete(key)
            elif line == "SEARCH":
                query = raw_input()
                results = search(query)
                if len(results) > 0:
                    print ','.join(results)
        except(EOFError):
            return

if __name__ == "__main__":
    main()
