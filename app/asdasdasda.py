from app.DbManager import DbManager as DB

dbManager = DB("localhost",2424,'root','DDECF059707C01DE7F04E07B3C5003EF22BD8C06418265CE34E2D5D9842DDBA2')
dbManager.connect('root','DDECF059707C01DE7F04E07B3C5003EF22BD8C06418265CE34E2D5D9842DDBA2')

dbManager.create("tpFallasDB")
dbManager.open("tpFallasDB")


arrayFile = [ { "animal": 'dog',
    "legsQuantity": '4',
    "locomotion": 'quadruped',
    "class": 'mammal',
    "skin": 'hair' },
  { "animal": 'spider',
    "legsQuantity": '8',
    "locomotion": 'octoped',
    "class": 'insect',
    "skin": 'chitin' } ]

#get vertexes
vertexes = {x.title() : [] for x in arrayFile[0].keys()}

#get vertexes values
for data in arrayFile:
    for key in data.keys():
        vertexes[key.title()].append(data[key])

for vertex, values in vertexes:
    ### Create Vertex
    dbManager.executecommand("create class " + vertex + " extends V")
    for value in values:
        ### Insert a new value
        dbManager.executecommand("insert into " + vertex + " set name = '" + value + "'")


### query the values
#client.query("select * from Animal")


### Create the edge for the RELATED action
dbManager.executecommand('create class Related extends E')

### Relate all with all in the dictionary
for data in arrayFile:
    auxKeys = data.keys()
    for key in data.keys():
        auxKeys.remove(key)
        for relatedKey in auxKeys:
            dbManager.executecommand(
                "create edge Related from ("
                "select from " + key.title() + " where name = '" + data[key] + "'"
                ") to ("
                "select from " + relatedKey.title() + " where name = '" + data[relatedKey] + "'"
                ")"
            )

pea_eaters = dbManager.getcommand("select expand( in( Related )) from Animal")
for animal in pea_eaters:
    print(animal.name)