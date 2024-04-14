Name: Shawnia Noel
ID: 101207361
Group 164 - 1 Member

Application app script is: project.py
The ddl statements used are in the folder SQL
The first batch of dml statements used are the dml.sql file in sql folder
The second batch of ddl statements used are the dml2.swl file in the sql folder

This application is written in python,
It makes use of library psycopg2 which is a python wrapper for libpq, the official library in C to connect to postgresql server.
library psycopg2 has to pip installed prior to runnning the application.
python version newer than 3.6 is required
More details can be found here: https://www.psycopg.org/docs/news.html#news


Prior to running the application, make sure that:
    1. psycopg2 was pip installed
    2. python version is no older than python 3.7
    3. launch and log into pgAdmin4
    4. Create an empty database "FitnessClub"
    5. in project.py and replace arguments (if necessary);
            1)user with the username that owns the database, most likely postgres
            2)password with the password of that user [ NECESSARY]
            3) port with whichever port your localhost is running on, by default it should be 5432


To run the application just run the same way used for  any python program.
