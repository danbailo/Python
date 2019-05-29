from sys import argv

def mysql_connect(**kwargs):
    # print(kwargs)
    user=kwargs.get("user",None)
    assert user!=None,"Preciso de user"

    password=kwargs.get("password",None)
    if password==None:raise RuntimeError("Preciso de passowrd")
    
    host=kwargs.get("host",None)
    if host==None:raise Exception("Preciso de host")
import json
mysql_connect(user="root",password="lenny face",host="localhost")
mysql_connect(**json.load(open(argv[1])))