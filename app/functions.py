from app.DbManager import DbManager as DB
import json
from pprint import pprint

def queryToVertex(vertex):
    output = "Vertex: " + vertex + "\n"
    dbManager = getDbManager();
    if canOpenDB(dbManager):
        dbManager.open("tpFallasDB")
        eaters = dbManager.getcommand("select expand( in( Related )) from " + vertex)
        for aux in eaters:
            output += aux.name + "\n"

    return output

def queryToVertexName(vertex,name):
    output = "Vertex: " + vertex + " where name: " + name + "\n"
    dbManager = getDbManager();
    if canOpenDB(dbManager):
        dbManager.open("tpFallasDB")
        eaters = dbManager.getcommand("select expand( in( Related )) from " + vertex + " where name = '" + name + "'")
        for aux in eaters:
            output += aux.name + "\n"

    return output

def getDbManager():
    dbManager = DB("localhost",2424,'root','DDECF059707C01DE7F04E07B3C5003EF22BD8C06418265CE34E2D5D9842DDBA2')
    dbManager.connect('root','DDECF059707C01DE7F04E07B3C5003EF22BD8C06418265CE34E2D5D9842DDBA2')
    return dbManager


def canOpenDB(dbManager):
    if (dbManager.checkDbExists("tpFallasDB") == False):
        print("DB not exist")
        return False
    return True


def trainDBwith(fileName):
    dbManager = getDbManager()
    if (canOpenDB(dbManager)):
        dbManager.drop("tpFallasDB")

    dbManager.create("tpFallasDB")
    dbManager.open("tpFallasDB")

    with open(fileName) as data_file:    
        arrayFile = json.load(data_file)

    #get vertexes
    vertexes = {x.title() : [] for x in arrayFile[0].keys()}

    #get vertexes values
    for data in arrayFile:
        for key in data.keys():
            vertexes[key.title()].append(data[key])

    for vertex in vertexes:
        ### Create Vertex
        dbManager.executecommand("create class " + vertex + " extends V")
        for value in vertexes[vertex]:
            ### Insert a new value
            dbManager.executecommand("insert into " + vertex + " set name = '" + value + "'")

    ### Create the edge for the RELATED action
    dbManager.executecommand('create class Related extends E')

    ### Relate all with all in the dictionary
    for data in arrayFile:
        for key in data.keys():
            auxKeys = data.keys()
            auxKeys.remove(key)
            for relatedKey in auxKeys:
                dbManager.executecommand(
                    "create edge Related from ("
                    "select from " + key.title() + " where name = '" + data[key] + "'"
                    ") to ("
                    "select from " + relatedKey.title() + " where name = '" + data[relatedKey] + "'"
                    ")"
                )