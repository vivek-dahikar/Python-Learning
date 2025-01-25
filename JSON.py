#javascript object notation | used for trnsforming data bw the browser nd the server | import json

import json

d='{"name":"radhe","loc":"barsana","dur":"2"}' #json should b string

x=json.loads(d) #loads change json to dict
print(x)

file=open("post.json","r") #opening other file
x=file.read()

print(x)
pyobject=json.loads(x) #convert ot dict

print(pyobject)

#dumps - mainly used when we want to store and transfer objects (Python objects) into a file in the form of JSON