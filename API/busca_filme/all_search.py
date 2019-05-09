#API - application programming interface
#interface que se comunica com outros programas
#passa parametros e ela retorna

import requests
import json

request = None

def search(title, typeof=None):
    if typeof is None or typeof == '*': typeof = ''
    all_pages = []
    baseURL = 'http://www.omdbapi.com/'
    apiKey = '3232c818'
    i = 1
    while i<=100:
        inputURL = baseURL+'?s='+title+'&page='+str(i)+'&type'+typeof+'&apikey='+apiKey
        # print(inputURL)
        try:
            request = requests.get(inputURL)
            dict_request = json.loads(request.text)
            # print(len(dict_request))
            # if len(dict_request) == 2: return False
            if dict_request['Response'] == 'False': return all_pages
            all_pages.append(dict_request)
        except Exception as err:
            print('REQUEST ERROR:',err)
            return False
        i += 1

# print(len(search('aaaaaaaaaaaaaaaaaaa')))
# print(len((search('matrix')))) #retorna a qtd de paginas de busca
# print((search('matrix')[1]['Search']))

def show(movies):
    if len(movies) == 0: return False
    for movie in movies:
        # print(len(movie))
        if len(movie) == 3:
            for details in movie['Search']:
                # print(movie['Search'])
                print('Title:',details['Title'])
                print('Year:',details['Year'])
                print('imdbID:',details['imdbID'])
                print('Type:',details['Type'])
                print('Poster:',details['Poster'])
                print()  
        else: return False #se entrou aqui, é pq nao encontrou nenhum filme com o nome digitado

# print(show(search('asdasd')))

if __name__ == "__main__":
    while True:
        name = str(input('Input the NAME or F to exit: '))
        if name.lower() == 'f': break
        typeof  = str(input('Input the TYPE or "*" for all, F to exit: '))
        if typeof.lower() == 'f': break
        print('Fetching...')
        print()

        fetch = search(name, typeof)
        try:
            if len(fetch) == 0:
                print('Movie not found!')
                print()
            else:
                show(fetch)          
        except TypeError as err:
            print('MAIN ERROR:',err)
            