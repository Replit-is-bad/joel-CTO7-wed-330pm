

with open('FiveLetterWords.csv','r') as fileobj :
    
    # reads and stores it into a string
    contents = fileobj.read()

    print(contents)

    # splilt