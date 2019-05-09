import requests
import json

request = None

def search(title, typeof=None):
    if typeof is None or typeof == '*': typeof = ''
    details = []
    baseURL = 'http://www.omdbapi.com/'
    apiKey = '3232c818'
    i = 1
    while i<=100:
        inputURL = baseURL+'?s='+title+'&page='+str(i)+'&type='+typeof+'&apikey='+apiKey
        try:
            request = requests.get(inputURL)
            dict_request = json.loads(request.text)
            if dict_request['Response'] == 'True': 
                for k in dict_request['Search']:
                    details.append(
                        'Title: '+k['Title']+'\n'+
                        'Year: '+k['Year']+'\n'+
                       'imdbID: '+k['imdbID']+'\n'+
                       'Type: '+k['Type']+'\n'+
                        'Poster: '+k['Poster']+'\n'
                    )
            else: return details
        except Exception as err:
            print('REQUEST ERROR:',err)
            return False
        i += 1

if __name__ == "__main__":
    while True:
        name = str(input('Input the NAME or F to exit: '))
        if name.lower() == 'f': exit()
        typeof  = str(input('Input the TYPE or "*" for all, F to exit: '))
        if typeof.lower() == 'f': exit()
        print('Fetching...')
        print()

        fetch = search(name,typeof)

        try:
            if len(fetch) == 0:
                print('Movie not found!')
                print()
            else:
                for i in fetch:
                    print(i)
                print('Total of Results:',len(fetch))
                print()
        except TypeError as err:
            print('URL INVALID!:',err)
            print('Please, get the correct url and try again!')
            print()