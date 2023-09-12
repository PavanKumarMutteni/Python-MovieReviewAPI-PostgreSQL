import dbsetup as DB
import app 
from flask import Flask, request

connection = DB.setupDB()
cursor = connection.cursor()

def deleteMovieById(id):
    try:
        cursor.execute("select * from movies where entryno = %s", (id,))
        row = cursor.fetchone()
        if row == None:
            return {"ErrorMessage": "No Movie record found with the provided entryno/id to delete"}
        cursor.execute("delete from movies where entryno = %s", (id,))
        connection.commit()
        return {"Message": "Successfully movie record deleted !!!"}
    except:
        return {"ErrorMessage": "Something went wrong while deleting movie record"}
   
