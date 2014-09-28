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
        if xmlDom.getElementsByTagName('tag'):
            self.tags = self.getData(xmlDom.getElementsByTagName('tag')[0].childNodes, True)
        else:
            self.tags = []
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
        line = line.replace('&', '&amp;')
        xmlDom += line
    return xml.dom.minidom.parseString(xmlDom)

def create():
    dom = createXML()
    note = Note(dom)
    searchableNotes.append(note)

def update():
    dom = createXML()
    note = Note(dom)
    for index, n in enumerate(searchableNotes):
        if n.guid == note.guid:
            del searchableNotes[index]
            break
    searchableNotes.append(note)

def delete(key):
    for index, n in enumerate(searchableNotes):
        if n.guid == key:
            del searchableNotes[index]

def search(query):
    queries = query.split(' ')
    results = []
    for note in searchableNotes:
        queriesFound = {}
        for q in queries:
            regex = compileRegex(q)
            queriesFound[q] = False
            if "tag:" in q:
                if len(note.tags) > 0:
                    for tag in note.tags:
                        if re.search(regex, tag):
                            queriesFound[q] = True
            elif "created:" in q:
                date = regex
                if note.created >= date:
                    queriesFound[q] = True
            else:
                if re.search(regex, note.content):
                    queriesFound[q] = True
        if all(val==True for val in queriesFound.values()):
            results.append(note.guid)
    return results

def compileRegex(query):
    if "created:" not in query:
        if "tag:" in query:
            r = ''.join(filter(None,query.split('tag:')))
        else:
            r = query
        if "*" in r:
            r = r.replace("*", ".*")
        regex = re.compile(r'\b%s\b' % r, re.IGNORECASE)
    else:
        date = ''.join(filter(None,query.split('created:')))
        regex = datetime.datetime.strptime(date, '%Y%m%d')
    return regex

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
                else:
                    print
            searchableNotes.sort(key=lambda note: note.created)
        except(EOFError):
            return

if __name__ == "__main__":
    main()