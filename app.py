from flask import Flask, request
import FetchingRecords as fr
import AddRecord as ar
import DeleteRecord as dr
import UpdateRecord as ur

app = Flask(__name__)

@app.post("/addMovie")
def addMovie():
    data = request.get_json()
    return ar.addMovie(data)

@app.get("/getAllMovies")
def getRecords():
   return fr.getAllRecords()
   
@app.get("/getMovieByName/<string:name>")
def getMovieByName(name):
    return fr.getMovieByMovieName(str(name))

@app.get("/getMovieById/<string:id>")
def getMovieById(id):
    return fr.getMovieById(str(id))

@app.delete("/deleteMovieById/<string:id>")
def deleteMovieById(id):
    print("I am running")
    return dr.deleteMovieById(str(id))
    
@app.patch("/updateReviewScore/<string:id>/<string:score>")
def updateReviewScore(id, score):
    return ur.updateReviewScore(str(id), str(score))

if __name__ == '__main__':
   app.run(port=5000)
