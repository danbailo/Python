def getDomain(string):
    return string.split('@')[-1]

string = 'user@domain.com'

print(getDomain(string))