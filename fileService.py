#Missing error handling
def openArchive():
        archive = open('text.txt', 'r')
        text = archive.read()
        archive.close()
        return text