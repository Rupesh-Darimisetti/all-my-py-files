import socket
from urllib.request  import Request,urlopen
import urllib
name="Rupesh"
print(f'hello: {name} welcome to python coding')
name="applicion to delete data"
print(name)
name=input('URL:')
page=urllib.urlopen(name).read()
print (page)
del page[0:len(page)]
print(name,sys)
