from bs4 import BeautifulSoup, Comment
import lxml
from lxml import html
import requests
import random
global driver
global soup
spanresults = []
divresults = []
atagresults = []
anyelementresults = []

translationlist = []

print('Welcome to bulk-word-definer. This application finds definitions of a list of words and provides it to you!')
filename = input('Enter a unique name for the session: ')
print('For one sentence definition press enter (recommended). Type ! if you want definitions with example sentences.')
sessionmode = input('')
dictionaryfile = input('Enter the fullname of the wordlist file: ')
words = []

#read the file
#for each line
f = open(dictionaryfile, "r", encoding='utf8')
for line in f:
    linefx = line.replace('\n','')

    words.append(linefx)
    #add scrapeurl here. line18
    linefx = linefx.replace(' ','20%')
    scrapeurl =  'http://www.google.com/search?q=' + linefx + '%20definition'
    spaninput =  ''
    divinput =  'BNeawe s3v9rd AP7Wnd'
    classinput =  ''
    r = requests.get(scrapeurl)
    soup = BeautifulSoup(r.content, 'lxml')



    #add divinput here. line33
    alldivresults = soup.find_all('div', class_ = divinput)

    for result in alldivresults:
        #it shows definition until the first dot
        if sessionmode != '!':
            resultfx = result.getText()
            positionofdot = resultfx.find('.')
            divresults.append(resultfx[0:positionofdot + 1])

        elif sessionmode == '!':
            resultfx = result.getText()
            divresults.append(resultfx)






    if len(divresults) > 0:
        translationlist.append(str(divresults[0]))
    else:
        translationlist.append('**No translation found**')

    alldivresults = []
    divresults = []
    print('Progress..  (line number ' + str(len(translationlist)) + ' was translated.)' )

f.close()


#print(str(divresults[0]))






#write to a file
randomint = random.randint(0,500000)
randomint = str(randomint)
filenameforsaving = filename + '-session-results-id' + randomint + ".txt"
f = open(filenameforsaving, "w", encoding='utf8')
for translatedword in translationlist:
    index = translationlist.index(translatedword)
    wordnr = str(index + 1)
    f.write(wordnr + '.' + words[index] + ': ' + '\n')
    f.write(translatedword + '\n' + '\n')
f.close()

print('All of the words were translated')
print('The results are stored in:  ' +  filenameforsaving)
