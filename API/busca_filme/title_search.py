#API - application programming interface
#interface que se comunica com outros programas
#passa parametros e ela retorna

import requests
import socket
import json

print(socket.gethostbyname('www.omdbapi.com'))

request = None

def search(title):
    baseURL = 'http://www.omdbapi.com/'
    typeof = ''
    apiKey = '3232c818'
    inputURL = baseURL+'?t='+title+'&type='+typeof+'&apikey='+apiKey
    print(inputURL)
    try:
        request = requests.get(inputURL)
        dict_request = json.loads(request.text)
        return dict_request
    except Exception as err:
        print('ERROR:',err)
        return False

def show(movie):
    print('Title:',movie['Title'])
    print('Year:',movie['Year'])
    print('Actors:',movie['Actors'])
    print('imdbRating:',movie['imdbRating'])
    print('Website:',movie['Website'])
    print()        

if __name__ == "__main__":
    while True:
        name = str(input('Input the name of the movie or F to exit: '))
        print()

        if name.lower() == 'f':
            break
        
        movie = search(name)

        if movie['Response'] == 'False':
            print('Movie not found!')
            print()
        else:
            try:
                show(movie)
            except KeyError as err:
                print("don't have {}".format(err).replace("'",''))
                print()
