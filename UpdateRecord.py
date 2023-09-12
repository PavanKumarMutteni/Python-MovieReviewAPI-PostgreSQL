import dbsetup as DB
import app 
from flask import Flask, request

connection = DB.setupDB()
cursor = connection.cursor()

def updateReviewScore(id,score):
    try:
        cursor.execute("select * from movies where entryno = %s", (id,))
        row = cursor.fetchone()
        if row == None:
            return {"ErrorMessage": "No Movie record found with the provided entryno/id to update"}
        cursor.execute("update movies set reviewscore = %s where entryno = %s", (score,id,))
        connection.commit()
        return {"Message": "Updated Sucessfully !!!"}
    except:
        return {"ErrorMessage": "Something went wrong while updating the movie record"}
   
