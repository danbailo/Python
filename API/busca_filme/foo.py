#API - application programming interface
#interface que se comunica com outros programas
#passa parametros e ela retorna

import requests
import json

request = None

def search_by_title(title):
    baseURL = 'http://www.omdbapi.com/'
    typeof = ''
    apiKey = '3232c818'
    inputURL = baseURL+'?t='+title+'&type='+typeof+'&apikey='+apiKey
    try:
        request = requests.get(inputURL)
        dict_request = json.loads(request.text)
        return dict_request
    except Exception as err:
        print('ERROR:',err)
        return False

def show_title_details(movie):
    print('Title:',movie['Title'])
    print('Year:',movie['Year'])
    print('Actors:',movie['Actors'])
    print('imdbRating:',movie['imdbRating'])
    print('Website:',movie['Website'])
    print()        

def search_all(title):
    baseURL = 'http://www.omdbapi.com/'
    typeof = 'movie'
    apiKey = '3232c818'
    inputURL = baseURL+'?s='+title+'&type='+typeof+'&apikey='+apiKey
    try:
        request = requests.get(inputURL)
        dict_request = json.loads(request.text)
        return dict_request
    except Exception as err:
        print('ERROR:',err)
        return False

def show_all_details(movies):
    for movie in movies['Search']:
        print('Title:',movie['Title'])
        print('Year:',movie['Year'])
        print('imdbID:',movie['imdbID'])

def show_details(movies):
    if len(movies)==3:
        for movie in movies['Search']:
            print('Title:',movie['Title'])
            print('Year:',movie['Year'])
            print('imdbID:',movie['imdbID'])
            print()
    else:
        print('Title:',movies['Title'])
        print('Year:',movies['Year'])
        print('Actors:',movies['Actors'])
        print('imdbRating:',movies['imdbRating'])
        print('Website:',movies['Website'])
        print()    


if __name__ == "__main__":
    while True:
        name = str(input('Input the name of the movie or F to exit: '))
        print()

        if name.lower() == 'f':
            break
        
        movie = search_by_title(name)
        movies = search_all(name)

        if movie['Response'] == 'False':
            print('Movie not found!')
            print()
        elif movies['Response'] == 'False':
            print('Movie not found!')
            print()
        else:
            # show_all_details(movies)
            show_details(movie)
            show_details(movies)