Name: Shawnia Noel
ID: 101207361


This application is written in python,
It makes use of library psycopg2 which is a python wrapper for libpq, the official library in C to connect to postgresql server.
library psycopg2 has to pip installed prior to runnning the application.
python version newer than 3.6 is required
More details can be found here: https://www.psycopg.org/docs/news.html#news


Prior to running the application, make sure that:
    1. psycopg2 was pip installed
    2. python version is no older than python 3.7
    3. launch and log into pgAdmin4
    4. Create an empty database "Fitness Club"
    5. open the source code, project.py and replace arguments;
                          :user with the username that owns the database, most likely postgres
                          :password with the password of that user
                          :port with whichever port your localhost is running on, by default it should be 5432


To run the application just run the same way used for  any python program.
.