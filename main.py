import xml.etree.ElementTree as ET


def main():
    if raw_input() == "CREATE":
        tree = ET.parse('note0.xml')
        root = tree.getroot()


while __name__ == "__main__":
    main()
