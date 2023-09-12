import dbsetup as DB
import app 
from flask import Flask, request

connection = DB.setupDB()
cursor = connection.cursor()

def getAllRecords():
    try:
        cursor.execute("select * from movies")
        row = cursor.fetchone()
        if row == None:
            return {"ErrorMessage": "No movies data available to fetch"}
        rows = cursor.fetchall()
        return {"movies": rows}
    except:
        return {"ErrorMessage": "Something went wrong while fetching the data"}

def getMovieByMovieName(movieName):
    try:
        cursor.execute("select * from movies where moviename = %s", (movieName,))
        row = cursor.fetchone()
        if row != None:
            return {"movieData": row}
        return {"ErrorMessage": "No Movie data found with the provided movie name"}
    except:
        return {"ErrorMessage": "Something went wrong while fetching the data"}

def getMovieById(id):
    try:
        cursor.execute("select * from movies where entryno = %s", (id,))
        row = cursor.fetchone()
        if row != None:
            return {"movieData": row}
        return {"ErrorMessage": "No Movie data found with the provided movie Id"}
    except:
        return {"ErrorMessage": "Something went wrong while fetching the data"}