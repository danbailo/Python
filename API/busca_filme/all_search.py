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
                details.append('Total Result: '+dict_request['totalResults'])
            else: return details
        except Exception as err:
            print('REQUEST ERROR:',err)
            return False
        i += 1

if __name__ == "__main__":
    while True:
        name = str(input('Input the NAME or F to exit: '))
        if name.lower() == 'f': break
        typeof  = str(input('Input the TYPE or "*" for all, F to exit: '))
        if typeof.lower() == 'f': break
        print('Fetching...')
        print()

        fetch = search(name,typeof)

        if len(fetch) == 0:
            print('Movie not found!')
            print()
        else:
            # print(search(name,typeof))
            # print(fetch[::])
            for i in fetch:
                print(i)
