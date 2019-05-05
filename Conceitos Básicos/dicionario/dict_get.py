#get
#https://docs.quantifiedcode.com/python-anti-patterns/correctness/not_using_get_to_return_a_default_value_from_a_dictionary.html
#https://docs.python.org/3/library/stdtypes.html#dict.get

#get(key[, default])
#Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.


dictionary = {"message": "Hello, World!"}

if "message" in dictionary:
    data = dictionary["message"]

print(data)  # Hello, World!

del dictionary
del data

dictionary = {"message": "Hello, World!"}

#data = dictionary.get("message","")
data = dictionary.get("message")

print(data)  # Hello, World!