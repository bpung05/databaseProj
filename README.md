
# Database Project Pung
## Where to Start
    1. Begin by observing the different directories that I include
        a. database_input_scripts -> Holds scripts to insert data into your database. Includes the .sql file to create a database. The paths to the lahman csvs will be relative so as long as you have the files in same main folder you will be good. Ensure that you have already created a user: web , password : mypass like in the instructions within your own mariadb. The instructions to set up the database will follow.

        b. lahman_csvs -> holds the csv files that will be read in by the scripts to the database. This is the actual data that is in the database

        c. database_dump -> holds the dump sql for the newly created database and information within it. 

        d. flask_application -> holds the flask application

### Start by setting up your database