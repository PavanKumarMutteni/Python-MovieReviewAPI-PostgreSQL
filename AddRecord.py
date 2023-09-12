import dbsetup as DB
import app 
from flask import Flask, request

connection = DB.setupDB()
cursor = connection.cursor()

def addMovie(data):
    try:
        cursor.execute("insert into movies(entryno, moviename,reviewscore,synopsis,director,yearofrelease) values(%s,%s,%s,%s,%s,%s)", (data['entryno'],data['moviename'],data['reviewscore'],data['synopsis'],data['director'],data['yearofrelease'],))
        connection.commit()
        return {"Message": "Sucessfully Inserted Record"}
    except:
        return {"ErrorMessage": "Something went wrong while inserting record"}