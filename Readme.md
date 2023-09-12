# Please config below properties to run this API in your Local Envirnoment
# You must install the postgresql in your local Envirnoment
# Then run the below script in your psql server (For creating the movies table)
# create table movies(entryno int PRIMARY KEY NOT NULL, moviename varchar(50) NOT NULL, reviewscore float(4) NOT    NULL, synopsis varchar(256) NOT NULL, director varchar(50) NOT NULL, yearofrelease int NOT NULL)
# Modify the database parameters in dbsetup.py file (database, user, password, host and port parameters)

#  API Supported End Points

     1. Add Movie -> This end point will add/insert new movie record
              URL -> 
     2. Delete Movie By EntryNo -> This end point will delete the movie record by entryno field
              URL ->
     3. Update ReviewScore by EntryNo -> This end point will update the reviewscore of the movie based on entry no
              URL ->
     4. Get All Movie Records -> This end point will fetch all movies records
              URL ->
     5. Get Movie by Movie Name -> This end point will fetch movie record based on movie name
              URL ->  
     6. Get Movie by Entry No -> This end point will fetch movie record based on entry no
              URL -> 