import pandas as pd
import pymysql
import sys 
import os
#I use a relative path to csi5302 file. I want to put this file in my flask app and dont want you to have to change 2 spots.

sys.path.append(os.path.abspath('..'))
import flask_app.csi5302 as cfg

# Define the database connection details
config = {
    "host": cfg.mysql['location'],
    "user": cfg.mysql['user'],
    "password": cfg.mysql['password'],
    "database": cfg.mysql['database']
}

csvs_to_insert = ['AllstarFull', 'Appearances' , 'AwardsPlayers', 'AwardsManagers', 'AwardsShareManagers', 'AwardsSharePlayers','Batting', 'BattingPost', 'CollegePlaying', 
                  'Fielding', 'FieldingOF', 'FieldingOFsplit', 'FieldingPost', 'HallOfFame', 'HomeGames', 'Managers', 'ManagersHalf', 'Parks', 'People', 'Pitching',
                  'PitchingPost', 'Salaries', 'Schools', 'SeriesPost', 'Teams', 'TeamsFranchises', 'TeamsHalf']

csvs_no_id = ['People', 'Schools', 'TeamsFranchises']

for csv in csvs_to_insert:
    # Define the CSV file path. Ensure that it is relative. Use the os python library to join the path.
    csv_file = os.path.join('..', 'lahman_csvs', csv + '.csv')

    # Read the CSV file using pandas
    data_frame = pd.read_csv(csv_file)
    data_frame = data_frame.where(pd.notnull(data_frame), 'NULL')
    # Get the column headers

    column_headers = list(data_frame.columns)
    # Connect to the MariaDB database
    conn = pymysql.connect(**config)
    cursor = conn.cursor()




    #headers = ", ".join([str(header) for header in column_headers]) -> dont need as of (7/20)

    # Insert the values into the new table
    for i, row in data_frame.iterrows():
        val_string = []
        #add the auto increment if possible
        if csv not in csvs_no_id:
            val_string.append('NULL')

        for val in row.values:
            if val == 'NULL':
                val_string.append(val)
            elif("'" in str(val)):
                quoted = str(val).replace("'", "''")
                val_string.append(f"'{quoted}'")
            else:
                
                val_string.append(str(f"'{val}'"))

        values = ", ".join(val_string)
        insert_query = f"INSERT INTO {str(csv).lower()} VALUES ({values});"
        
        
        
        cursor.execute(insert_query)
  
    # Commit the changes and close the database connection
    

    conn.commit()

    conn.close()