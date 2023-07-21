
# Database Project Pung
## Where to Start
    1. Begin by observing the different directories that I include
        a. database_input_scripts -> Holds scripts to insert data into your database. Includes the .sql file to create a database. The paths to the lahman csvs will be relative so as long as you have the files in same main folder you will be good. Ensure that you have already created a user: web , password : mypass like in the instructions within your own mariadb. The instructions to set up the database will follow.


        b. lahman_csvs -> holds the csv files that will be read in by the scripts to the database. This is the actual data that is in the database

        c. database_dump -> holds the dump sql for the newly created database and information within it. 

        d. flask_application -> holds the flask application itself. You will call this directory in your python command prompt to run the dev server

        The directory overview:
            -lahman_csvs
            -database_dump
            -flask_application
            -database_input_scripts


    2. Run your installations (pip install...) 

    3. Set up your database as shown in the second section

    4. set up your localhost

    5. run your application

### Start by setting up your database

    1. Ensure you have MariaDb instance installed
    
    2. Login with your root permisions and create a new user using the script in database_input_scripts 'create_Mariadb_setup' to ensure that you have created the web user and mypass password. Note this may fail if you already have that user created.

        Note that you may have already created the web user so you may not need to do this step.

    3. login with your new user: 

        1. Open a new command line and find the directory for your mariadb installation
        2. Change directory to path of .\mariadb (cd <path>)
        3. Now type in 'bin\mysql -u web -p' and input your password. This command calls the bin directory and mysql commandlet function calling your user and letting you type in your password.
        
        example eventual full path in new command line: 'C:\Pung\Baylor\Databases\MariaDB\bin\mysql' -u web -p

    4. Create a new database
        The new database will be created in the next step. I create and use my database all in one because I thought it might be easier for you to just run 1 or 2 scripts if you need.


    5. Create tables and insert data into tables 

        a. Use my 'create_tables.sql' script found in the 'database_input_scripts' directory to create your tables.
        This script createss the database, uses the pung database, and then also creates all the tables. You can run this .sql script and it will just create the instances of all the talbes you need. You should be able to describe and show the tables... but there will be no data yet.


        Your database should have flipped to pung after running create_tables.sql. If it was not working ensure you have mariadb running.

        try: (assume you are working in pung) :  "show tables" ....

        from there you should see 27 tables created.


        b. use the python script 'insert_data.py' to insert all your data.
        -please note that I have included the mariadb config file in two places: one of which is the database_input_scripts to allow my scripts to connect to the database. You may need to change this if you are using a different user than is defined in the instrcutions and previous setup. The config file has the web, mypass user in it.

        *****ENSURE THAT YOU ARE WORKING IN THE DATABASE_INPUT_SCRIPTS DIRECTORY WHEN RUNNING THIS*******

        Please change cd to the database_input_scripts directory. This is because I use relative paths in my insert_data.py script.

        your command to run part b should look like:

        c:///path to /database_input_scripts>python insert_data.py

        3. At this point please verify if you have :
            a. The pung database.
            b. 27 tables.
            c. data in all 27 tables from my csvs.
    