# Please config below properties to run this API in your Local Envirnoment
# You must install the postgresql in your local Envirnoment
# Then run the below script in your psql server (For creating the movies table)
# create table movies(entryno int PRIMARY KEY NOT NULL, moviename varchar(50) NOT NULL, reviewscore float(4) NOT    NULL, synopsis varchar(256) NOT NULL, director varchar(50) NOT NULL, yearofrelease int NOT NULL)
# Modify the database parameters in dbsetup.py file (database, user, password, host and port parameters)

#  API Supported End Points

     1. Add Movie -> This end point will add/insert new movie record
              URL -> http://127.0.0.1:5000/addMovie
     2. Delete Movie By EntryNo -> This end point will delete the movie record by entryno field
              URL -> http://127.0.0.1:5000/deleteMovieById/2
     3. Update ReviewScore by EntryNo -> This end point will update the reviewscore of the movie based on entry no
              URL -> http://127.0.0.1:5000/updateReviewScore/21/9.8
     4. Get All Movie Records -> This end point will fetch all movies records
              URL -> http://127.0.0.1:5000/getAllMovies
     5. Get Movie by Movie Name -> This end point will fetch movie record based on movie name
              URL ->  http://127.0.0.1:5000/getMovieByName/Bahubali
     6. Get Movie by Entry No -> This end point will fetch movie record based on entry no
              URL -> http://127.0.0.1:5000/getMovieById/21
