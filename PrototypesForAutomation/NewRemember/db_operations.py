from datetime import datetime

import pandas as pd
from sqlalchemy import create_engine, text

# Create SQLite engine
engine = create_engine('sqlite:///automation.db')

def save_dataframe(df_container):
    # Transform the dictionary into a DataFrame

    df = pd.DataFrame(df_container)
    #SQLite will interpret this as a datetime.
    df['Start'] = df['Start'].dt.tz_convert(None)
    df['Start'] = df['Start'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S.%f'))

    with engine.connect() as connection:
        connection.execute(text('PRAGMA foreign_keys=ON'))

        connection.execute(text("""
                CREATE TABLE IF NOT EXISTS Blocker (
                    "Subject" TEXT,
                    "Start" TEXT PRIMARY KEY ON CONFLICT IGNORE,
                    "Duration" INTEGER,
                    "Attendees" TEXT,
                    "Reminder" TEXT,
                    "Speaker" TEXT
                )
            """))


    # Write data to sqlite table
    df.to_sql('Blocker', con=engine, if_exists='append', index=False)

def update_dataframe(start_time):
    #start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S.%f')
    with engine.connect() as connection:
        trans = connection.begin()  # start a transaction
        result = connection.execute(text("SELECT * FROM Blocker WHERE Start = :start_time AND Reminder = 'NO'"),
                                    {"start_time": start_time})
        #print('Rows matching:', [row for row in result])
        #rows = [row for row in result]
        row_data = [row for row in result]
        for row in result:  # access each row
            print('Accessing column data from select query')

        try:
            result = connection.execute(
                text("UPDATE Blocker SET Reminder = 'YES' WHERE Start = :start_time AND Reminder = 'NO'"),
                {"start_time": start_time})
            print('Rows updated:', result.rowcount)
            trans.commit()  # commit changes
        except:
            trans.rollback()  # rollback changes if exception occurred
            raise # propagate the exception
    return row_data

def get_data():
    # Write a SQL query
    query = 'SELECT * FROM Blocker'

    # Execute the query and store the result in a dataframe
    df = pd.read_sql_query(query, engine)
    #df['Start'] = df['Start'].dt.tz_convert(None)
    # Convert dataframe to html
    df['Reminder'] = df.apply(lambda row: f'<a href="#" onclick="updateReminder(\'{row["Start"]}\')">{row["Reminder"]}</a>',axis=1)
    html_table = df.to_html(escape=False)
    #print(html_table)
    return html_table

"""
        # Fetch rows matching the criteria.
        result = connection.execute(text("SELECT * FROM Blocker WHERE Start = :start_time"),
                                    {"start_time": start_time})
        print('Rows matching:', [row for row in result])

        #   Now Update
        result = connection.execute(text("UPDATE Blocker SET Reminder = 'yes' WHERE Start = :start_time AND Reminder = 'NO'"),
                           {"start_time": start_time})
        print(result.rowcount)
        # Explicitly commit the transaction
        connection.execute(text("COMMIT"))
 """