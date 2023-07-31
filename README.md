
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


## Installs 
    pip install flask-wtf
    pip install flask
    pip install 
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
        
    6. Add in your user tables.

        a. You can run the script to create user tables and insert admin username/password

        This should add 2 tables.

        The file is in database_input_scripts. The file is called 'create_insert_users'.

        Please ensure that you are currently using the Pung table.
        

### Next is to run your app



### Extra credit things
    1I took extra attention to use ORM's. This took me a while to implement but I felt like it was worth it in the end. I know other students probably wont do this part because the SQL queries are more in line with what we had done on previous assignments.

    I felt like the ORM was harder, complex, and showed I could implement things that other web frameworks use like django (uses ORMs heavily)

    2. I added a 'add user' functionality. This was not anywhere requested by the user requriements but I added it anyway. Took a little while but handles some errors like the user already being in the database or the password/username being way too long or having spaces. Overall cool functionality only accessible to the admin via restrictions. Im sure other students wont have that so I think its a +.

    3. I took some time to format things nicely in the dashboards (in my opinion) by formatting the output tables, adding links in accessible spots, and feel like my quality-of-life will be higher than others. Maybe not a large plus but I do think the quality of life features like links in good spots, dashboards for users/admins, and table borders for mine will be better than others.


    4. Added the CSRF protections via WTF forms. I think my security in inputs and within the abstraction from the database is pretty good. I think that if you looked through my URLS and front end you be pleased with how I , to the best of young ability, tried to avoid user injection attacks and protect CSRF or other things.